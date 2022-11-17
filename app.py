from flask import Flask, jsonify
import sqlite3

from sqlalchemy import null

app = Flask(__name__)

@app.route('/')
def home():
    return "HOME"

@app.route("/result/<float:volH>/<float:volS>/<float:N>", methods=['GET'])
def similar_to(volH,volS,N):
    res = (volH*N*50*1000)/(volS)
    res =  jsonify(res)
    res.headers.add("Access-Control-Allow-Origin","*")
    print(res)
    return res


if  __name__ == "__main__":
    app.run(debug = True)