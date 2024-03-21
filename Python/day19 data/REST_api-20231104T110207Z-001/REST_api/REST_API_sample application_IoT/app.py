# app.py
from flask import Flask, request, jsonify
import pandas as pd
from json import loads, dumps

app = Flask(__name__)

def add_record(record, data_file="data.csv"):
    df=pd.read_csv(data_file)
    print("sent record", type(record), record)
    rec_df = pd.DataFrame(record.values()).T
    rec_df.columns=record.keys()
    print("record data frame", rec_df)
    try:
        df = pd.concat([df,rec_df],ignore_index=True)
        df.to_csv(data_file,index=False)
        data_json = df.to_json(orient="records")
        return data_json
    except:
        print("There was an exception in adding record", record)
        return None

def load_data_json(data_file="data.csv"):
    df=pd.read_csv(data_file)
    data_json = df.to_json(orient="records")
    # print(data_json)
    return data_json


@app.route('/sensors', methods=["GET"])
def get_sensors():
    data_json = load_data_json()
    return data_json #jsonify(data_json)



@app.route('/sensors', methods=["POST"])
def add_sensor():
    if request.is_json:
        sensor = request.get_json()
        data_json = add_record(sensor)
        if (data_json != None):
            return data_json, 201
        else:
            return {"error": "Exception in adding the record"}, 415
    return {"error": "Request must be JSON"}, 415


"""
# Setting commands

set FLASK_APP=app.py

set FLASK_ENV=development

flask run

"""