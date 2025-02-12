from pprint import pprint

def cookBookToShopList(input):
    shopList = {}
    for i in input:
        ingredient_name = i.pop('ingredient_name')
        shopList.update({ingredient_name: i})
    return shopList

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        shlt = cookBookToShopList(cook_book[i])
        for j in shlt:
            if shop_list.get(j) is None:
                shop_list.update({j : shlt[j]})
            else:
                shop_list[j]['quantity'] = int(shop_list[j]['quantity']) + int(shlt[j]['quantity'])
    return(shop_list)           

cook_book = {}

with open('input.txt') as f:
    data = f.read()

for i in data.split('\n\n'):
    recipe = i.split('\n')
    ingredients = []
    tags = ['ingredient_name', 'quantity', 'measure']
    for i in range(2, 2 + int(recipe[1])):
        ingredients.append(dict(zip(tags, recipe[i].strip().replace(' ', '').split('|'))))
    cook_book.update({recipe[0] : ingredients})
    
pprint(cook_book)
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))