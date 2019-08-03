import requests
import re
import json

# url
url = 'https://lol.qq.com/biz/hero/champion.js'
image_url = 'https://ossweb-img.qq.com/images/lol/img/champion/'
# 请求
response = requests.get(url).text
# print(response)

str_hero_list = re.search('("keys"):(.*),"data"',
                          response).group(2)  # 如果填 1 则 输出 "keys"
# print(str_hero_list)

dict__hero_list = json.loads(str_hero_list)

for hero_id, hero_name in dict__hero_list.items():
    # print(hero_id, hero_name)
    image_result = image_url + hero_name + '.png'
    print(image_result)
    image = requests.get(image_result).content

    with open(f'./image2/{hero_name}.png','wb') as file:
        file.write(image)