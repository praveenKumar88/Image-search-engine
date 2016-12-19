import os

from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

from image_match.signature_database_base import SignatureDatabaseBase

# create flask instance
app = Flask(__name__)

INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')


# main route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    es = Elasticsearch()
    ses = SignatureES(es)
    image = ses.search_image('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')
    print image
    return 'ok'


@app.route('/add', methods=['POST'])
def add():
    es = Elasticsearch()
    ses = SignatureES(es)
    ses.add_image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
    return 'ok'


# run!
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
