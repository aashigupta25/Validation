from matplotlib.font_manager import json_dump
import requests
import json

URL = "http://127.0.0.1:8000/person-api/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL, data= json_data)
    data = r.json()
    print(data)
# get_data()

def post_data():
    data = {
        'first_name': 'Rohan',
        'last_name': 'Cute',
        'age': 30,
    }
    json_data = json.dumps(data)
    r = requests.post(url= URL, data= json_data)
    data = r.json()
    print(data)
post_data()


def update_data():
    data = {
        'id': 9,
        'first_name': 'Aashi',
        'last_name': 'Bharagava',
        'age': 230
    }
    json_data = json.dumps(data)
    r = requests.put(url= URL, data= json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {'id': 1}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, data= json_data)
    data = r.json()
    print(data)
# delete_data()

