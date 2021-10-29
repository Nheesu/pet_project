import requests
from bs4 import BeautifulSoup
import random


def findCategory(num):
    request_url = "http://api.kcisa.kr/openapi/service/rest/convergence2019/getConver03"
    serviceKey = '서비스키 값'
    categories = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    random_num = random.sample(range(1, 411), num)  // 1~411페이지 내에서 입력받은 num값만큼 추출한다.
    for i in random_num:
        pageNo = "pageNo" +str(i)                  // 위에서 뽑아낸 값을 페이지로 입력
        url = request_url + serviceKey + '&' + pageNo

        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        items = soup.select('items > item')

        if items != None:
            for item in items:
                category = item.select_one('subjectcategory')
                category_name = category.text
                if category_name not in categories:     // categories에 해당 요소가 없으면
                    categories.append(category_name)    // categories에 category_name을 추가

    return categories

findCategory(36)
