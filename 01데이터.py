# import gdown
# gdown.download('https://bit.ly/3eecMKZ','남산도서관 장서 대출목록 (2021년 04월).csv',quiet=False)

# import chardet
# with open('남산도서관 장서 대출목록 (2021년 04월).csv',mode='rb') as f:
#     d = f.readline()
# print(chardet.detect(d))
#
# filename = '남산도서관 장서 대출목록 (2021년 04월).csv'
# # with open(filename,encoding='EUC-KR') as f:
#     # print(f.readline())
#     # print(f.readline())
# import pandas as pd
# #자료형을 자동으로 파악하다가 데이터 타입이 달라져서 경고 발생 해결법
# # df = pd.read_csv(filename,encoding='EUC-KR',low_memory=False)
# #근본적인해결법
# df = pd.read_csv(filename,encoding='EUC-KR',dtype={'ISBN':str,'세트 ISBN':str,'주제분류번호':str})
# #저장 UTF-8로 저장
# df.to_csv('ns_202104.csv')
# with open('ns_202104.csv',encoding='EUC-KR') as f:
#     for i in range(3):
#         print(f.readline(),end='')
#

d = {"name":"혼자 공부하는 데이터 분석"}
print(d['name'])
import json
d_str = json.dumps(d,ensure_ascii=False)
print(d_str)
d2 = json.loads(d_str)
print(d2['name'])


d4_str ="""
[{"name":"혼자 공부하는 데이터 분석","author":"박해선","publisher":"길벗","price":25000,"isbn":"9791160506262","pubdate":"2020-12-30"},
    {"name":"혼자 공부하는 데이터 분석 with 파이썬","author":"박해선","publisher":"길벗","price":25000,"isbn":"9791160506279","pubdate":"2021-01-20"}]
    
"""
d4 = json.loads(d4_str)
from io import StringIO
import pandas as pd
df = pd.read_json(StringIO(d4_str))
df = pd.DataFrame(d4)
print(df)


x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <price>25000</price>
</book>
"""

import xml.etree.ElementTree as ET
book = ET.fromstring(x_str)
print(type(book))
book_childs = list(book)
print(book_childs)
name,author,year = book_childs
NAME = book.findtext('name')
print(NAME)

import requests
url = "http://data4library.kr./api/loanItemSrch?format=json&startDt=2021-04-0endDt=2021-04-30&age=20&authKey=8d2382a5f7c2fa2548c5f674128c08deaa4a107eb3ee3582dafbc3726e5762a3"
r = requests.get(url)
data = r.json()
books = []
for d in data['response']['docs']:
    books.append(d['doc'])
books_df = pd.DataFrame(books)
print(books_df)
books_df.to_json('20s_best_book.json')