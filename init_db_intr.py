import requests
from pymongo import MongoClient
import xmltodict
import json


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.easyDur


def insert_interaction(json: dict):
    items = json['response']['body']['items']['item']  # [{}, {}, {}, ...]

    for item in items:
        drug_01 = item['INGR_KOR_NAME']
        drug_02 = item['MIXTURE_INGR_KOR_NAME']
        content = item['PROHBT_CONTENT']

        doc = {
            'drug_01': drug_01,
            'drug_02': drug_02,
            'prohbt_content': content
        }

        db.interactionList.insert_one(doc)
        print('완료', drug_01, drug_02)


 # 기존 db 삭제
db.interactionList.drop()


# 병용금기 API json 으로 변환 -> db 저장
for i in range(1,11):
    #oepn_url_intr
    req_intr = requests.get(open_url_intr)
    xpars_intr = xmltodict.parse(req_intr.text)
    jsonDump_intr = json.dumps(xpars_intr)
    jsonBody_intr = json.loads(jsonDump_intr)
    # print(type(jsonBody_intr))
    # 실제 실행
    insert_interaction(jsonBody_intr)

















