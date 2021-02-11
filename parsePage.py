import urllib.request
import json

from bs4 import BeautifulSoup
import bs4
import re
import pprint


urls = ['https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli',
        'https://www.bbcgoodfood.com/recipes/vegan-kale-pesto-pasta',
        'https://www.bbcgoodfood.com/recipes/pasta-e-fagioli',
        'https://www.bbcgoodfood.com/recipes/one-pot-paneer-curry-pie',
        'https://www.bbcgoodfood.com/recipes/italian-veggie-cottage-pie'
        ]


def getRecepieContent(recepie_url):
    """
    Находит на странице html код относящийся ко списку ингредиентов
    """

    with urllib.request.urlopen(recepie_url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    recepie = soup.find('div', {'class': 'row recipe__instructions'})
    content = recepie.find('section', {'class': 'recipe__ingredients col-12 mt-md col-lg-6'})

    return content


def parseContent(content):
    """
    Парсит html код рецепта в список строк. Каждая строка соответствует строке рецепта
    (в большинстве случаев одному ингредиенту)

    """

    token_list = [tag.contents for tag in content.section.ul.findAll('li')]

    # convert tags to strings
    for item in token_list:
        for i, token in enumerate(item):
            if type(token) == bs4.element.Tag:
                token = token.contents[0]
            item[i] = str(token).strip()

    joined = [' '.join(token) for token in token_list]

    recepie = [re.sub(' +', ' ', s) for s in joined]

    return recepie


def containsNumericSymbol(string):
    numeric = set(['¼', '⅗', '½', '⅘', '¾', '⅙', '⅐', '⅚',
                   '⅑', '⅛', '⅒', '⅜', '⅓', '⅝', '⅔', '⅞', '⅕', '↉', '⅖',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    return bool(numeric.intersection(set(string)))


def toJSON(ingredients_list):
    """
    Конвертирует лист с ингредиентами в JSON

    Изначально я хотела представить каждую строку в формате:
    { quantity: <...>, name: <...>, description: <...> }

    Но дело в том, что я прошлась по всем страницам, собрала все рецепты
    и никакого алгоритма, чтобы он работал на всем не придумала.
    """

    # for i, item in enumerate(ingredients_list):
    #    quantity, name, description = processItem(item)
    #    recepie['ingredients'][i] = {'quantity' : quantity,
    #                                   'name' : name,
    #                                   'description' : description}

    recepie = {'recepie': [{'description': item} for item in ingredients_list]}
    return json.dumps(recepie)


def getIngredients(recepie_url):
    """
    Возвращает JSON с ингредиентами со страницы
    """

    content = getRecepieContent(recepie_url)
    ingredients_list = parseContent(content)

    return toJSON(ingredients_list)

if __name__ == '__main__':
    pp = pprint.PrettyPrinter()
    for url in urls:
        ilist = getIngredients(url)
        # обратно из json
        pp.pprint(json.loads(ilist))
        print('\n')