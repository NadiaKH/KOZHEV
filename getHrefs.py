from parsePage import getIngredients
import urllib.request
from bs4 import BeautifulSoup
import pprint


url = 'https://www.bbcgoodfood.com/recipes'


def hrefList(url, prefix, tag_name, tag_kwargs):
    """
    ...
    """

    tags, next_page = getTagsFromPage(url, tag_name, tag_kwargs)
    for tag in tags:
        yield tag['href']

    while next_page:
        tags, next_page = getTagsFromPage(prefix + next_page['href'], tag_name, tag_kwargs)

        for tag in tags:
            yield tag['href']


def getTagsFromPage(url, tag_name, tag_kwargs):
    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    res = soup.findAll(tag_name, tag_kwargs)

    next_page = soup.find('a', {'aria-label': 'Next Page'})

    return res, next_page


if __name__ == '__main__':

    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    by_category = soup.find('div', {'data-id' : '8c7bf23'}).find('div', {'class' : 'row row-cards'})

    categories = set(tag['href'] for tag in by_category.findAll('a', recursive=True))

    prefix = 'https://www.bbcgoodfood.com'
    tag_name = 'a'
    tag_kwargs = {'class': 'standard-card-new__article-title qa-card-link'}

    collections = set()

    for url in categories:
        for href in hrefList(url, prefix, tag_name, tag_kwargs):
            collections.add(href)

    prefix = 'https://www.bbcgoodfood.com'
    tag_name = 'a'
    tag_kwargs = {'class': 'standard-card-new__article-title qa-card-link'}

    recepie_refs = set()

    for i, url in enumerate(collections):
        print(i, end=' ')
        for href in hrefList(url, prefix, tag_name, tag_kwargs):
            recepie_refs.add(href)

    with open('recepiehrefs.txt', 'w') as f:
        for href in recepie_refs:
            print(href, file=f)


