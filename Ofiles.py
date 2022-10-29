# Задача 1
cook_book = {}
dish_list = []
with open('bloodo.txt', 'rt', encoding= 'utf8') as file:
  for l in file:     
      dish_name = l.strip()   
      ingredients_list = []
      dish = {dish_name: ingredients_list}      
      dish_count = file.readline() 
      for i in range(int(dish_count)):           
        dsh = file.readline().strip().split(' | ') 
        ingredients_list.append({'ingredient_name': dsh[0],
                            'quantity': int(dsh[1]),
                            'measure': dsh[2]})
        dish_list.append(dish)                
      blank_line = file.readline()
      cook_book.update(dish)              
print(cook_book)

# Задачача 2
def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for loc in cook_book[dish]:
        person_q = int(loc['quantity']) * person_count
        dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
        shop_list.update(dict_list)
    return shop_list
    
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задача 3
# import os

# lin_1 = {}
# for file in os.listdir('files'):
#   with open(os.path.join('files', file), encoding='utf-8') as f:
#     text = f.readlines()
#     text_ = "".join(text)
#     len_ = len(text)
#     lin_1[file] = (f'{len_}\n{text_}\n')
# #print(lin_1)    
# lin_2 = {} 
# for x in sorted(lin_1, key=lin_1.get):
#   lin_2[x] = lin_1[x]
# text_dict = {}                                                         
# for key, value in lin_2.items():
#   with open('all_file.txt', 'a', encoding='utf-8') as f:
#     f.writelines(f'{key}\n{value}\n')
# file.close()

