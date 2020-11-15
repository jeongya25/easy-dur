import requests
from pymongo import MongoClient
import xmltodict
import json


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.easyDur



def insert_adr(json: dict):
    db.adrList.drop()  #기존 db 삭제
    items = json['response']['body']['items']['item']    # [{}, {}, {}, ...]

    for item in items:
        name = item['COL_001']
        adr = item['COL_005']

        doc = {
                'name': name,
                'adr': adr
               }

        db.adrList.insert_one(doc)
        print('완료', name)



# 부작용 API json으로 변환
#url_adr
req_adr = requests.get(url_adr)
xpars_adr = xmltodict.parse(req_adr.text)
jsonDump_adr = json.dumps(xpars_adr)
jsonBody_adr = json.loads(jsonDump_adr)
# print(type(jsonBody_adr))



# 실행
insert_adr(jsonBody_adr)


