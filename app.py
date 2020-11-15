from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient



app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.easyDur


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/index.html')
def backtomain():
    return render_template('index.html')



@app.route('/dur.html')
def dur():
    return render_template('dur.html')



@app.route('/adr_search.html')
def adr():
    return render_template('adr_search.html')



@app.route('/interaction_search.html')
def interaction():
    return render_template('interaction_search.html')




# API
@app.route('/adr', methods=['GET'])
def showAdr():
    drug = request.args.get('drug_name')
    adrs = list(db.adrList.find({'name': str(drug)}, {'_id': False}))
    #print(adrs)
    return jsonify(
        {
            'result': 'success',
            'adr': adrs
        }
    )



@app.route('/interaction', methods=['GET'])
def showInteraction():
    drugA = request.args.get('drug_name_01')
    drugB = request.args.get('drug_name_02')
    interactions_01 = list(db.interactionList.find({'drug_01': str(drugA),'drug_02': str(drugB)}, {'_id': False}))
    interactions_02 = list(db.interactionList.find({'drug_01': str(drugB),'drug_02': str(drugA)}, {'_id': False}))
    # print('-------1:', interactions_01)
    # print('-------2:', interactions_02)
    interactions = interactions_01 + interactions_02
    #print(interactions)

    boolean = False
    content = ''

    if interactions:  # not empty -> 병용금기 있음
        boolean = True
        content = interactions[0]['prohbt_content']


    return jsonify(
        {
            'result': 'success',
            'interaction': boolean,
            'prohbt_content': content
        }
    )


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)