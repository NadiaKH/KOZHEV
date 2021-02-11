Описание файлов в репозитории
========
* **parsePage** - ответ на задание, скрипт который парсит страничку и печатает результат 
* **getHrefs** - скрипт, который собирает ссылки на все рецепты в **recepiehrefs.txt**, всего их ~2000
* **getRecepies.py** - скрипт, который печатает все рецепты в файл **ingredients.txt**, используя ссылки из  **recepiehrefs.txt**

Комментарий
===========
Изначально я хотела сохранить каждый рецепт в такую структуру:

```json
{ recepie : [
    {
      quantity   : <...>,
      name       : <...>,
      description: <...>
    }
        ...
    ]
}
     
```

Но я не знаю как распарсить строку в рецепте.
Например:
  * couple of handfuls fresh cherries , pitted, plus extra to serve
      - как понять где обозначено количество 
  
  
  * lime wedges, lime zest and mint leaves, to decorate
      - как понять, что тут сразу несколько продуктов 
  
  
  * 50g grated chocolate or 100g curls, to decorate
      - или то, или другое 
  
  
  * tropical fruit of your choice, sliced, then each slice cut into triangles or the shapes required for your design (we used mangoes, kiwis, pineapple and dragon fruit)
      - проблема определить количество  

Задание
=======

1.Изучить структуру html страницы: https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli 

2.Придумать структуру в которой хранить данные про рецепт

3.Написать парсер, который:
* На вход принимает url рецепта
* На выходе в формате json отдает структурированный рецепт :)

