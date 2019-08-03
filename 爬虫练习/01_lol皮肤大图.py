import requests
import re
import json

# url
url = 'https://lol.qq.com/biz/hero/champion.js'
image_url = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
# 请求
response = requests.get(url).text
# print(response)
# 筛选数据(xpath  正则:使用特殊的符号代替特殊的意义 .
# 表示通配  * 表示所有 ()表示组group,group括号内的数字代表第几个括号的内容
str_id = re.search('("keys"):(.*),"data"', response).group(2)  # 如果填 1 则 输出 "keys"
# print(str_id)
# print(type(str_id))

dict_id = json.loads(str_id)
# print(dict_id)
# print(type(dict_id))

for i, name in dict_id.items():
    # print(i, name)

    # 获取英雄的所有皮肤图片
    for num in range(30):
        # 依次添加不同的后缀
        image_result = image_url + i + '%03d' % num + '.jpg'

        # 判断图片页面是否存在
        if requests.get(image_result).status_code == 200:
            print(image_result)
            image = requests.get(image_result).content

            # save 将图片以二进制的形式写入文件夹
            with open(f'./image1/{name}.jpg', 'wb') as file:
                file.write(image)
