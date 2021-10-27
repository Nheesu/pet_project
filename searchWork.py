import requests
from bs4 import BeautifulSoup
import random


def findCategory(num):
    request_url = "http://api.kcisa.kr/openapi/service/rest/convergence2019/getConver03"
    serviceKey = 'f058717d-f5bf-489b-b678-dcdd796a5d85'
    categories = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    random_num = random.sample(range(1, 411), num)
    for i in random_num:
        pageNo = str(i)
        url = request_url + '?serviceKey=' + serviceKey + '&pageNo=' + pageNo

        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        items = soup.select('items > item')

        if items != None:
            for item in items:
                category = item.select_one('subjectcategory')
                category_name = category.text
                if category_name not in categories:
                    categories.append(category_name)

    return categories

findCategory(10)