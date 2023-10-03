from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='testing', host='0.0.0.0', port='3306', password='testing', database='test')

@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route('/api/getMonths', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_months():
    db = getMysqlConnection()
    print(db)
    try:
        sqlstr = "SELECT * from users"
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return jsonify(results=output_json)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')