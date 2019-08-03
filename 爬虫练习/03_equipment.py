import requests
import re

# 字符串转列表导入 ast 模块
import ast

# url
items_url = 'https://game.gtimg.cn/images/lol/act/img/js/items/items.js'
image_url = 'https://game.gtimg.cn/images/lol/act/img/item/'

# 请求
response = requests.get(items_url).text
# print(response)


"""
此处重点掌握:
    ast模块中的literal_eval() equ_info装换成list,list中其他容器(list,dict)也转换成了相应的数据类型
"""
equ_info = re.search('("items"):(.*),"version"', response).group(2)
item_list = ast.literal_eval(equ_info)

# s = open('1.md', 'w')
# i = str(item_list)
# s.write(i)
# s.close()
#
# print(type(item_list[0]['types']))

# s = open('2.md', 'a')
# for i in item_list:
#     i = str(i)
#     s.write(i + '\n')
#
# s.close()
c = 0
for i in item_list:
    id = i['itemId']
    name = i['name']

    image_equ = image_url + id + '.png'
    image = requests.get(image_equ).content
    # print(i['description'])
    with open(f'./image3/{name}.png', 'wb') as file:
        file.write(image)
        c += 1

print(c)