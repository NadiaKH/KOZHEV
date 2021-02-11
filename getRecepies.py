from parsePage import getIngredients
import json


if __name__ == "__main__":
    with open('ingredients.txt', 'w') as outputf, open('recepiehrefs.txt', 'r') as inputf:

        for i, url in enumerate(inputf):
            recepie = json.loads(getIngredients(url))['recepie']

            for item in recepie:
                print(item['description'], file=outputf)

            print('', file=outputf)
            print(i, end=' ')

