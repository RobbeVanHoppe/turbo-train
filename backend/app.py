import os

from flask import Flask, request, jsonify, Response
import mysql.connector

app = Flask(__name__)

def getMysqlConnection():
    host = os.environ.get('MYSQL_HOST', 'localhost')
    port = os.environ.get('MYSQL_PORT', '3306')
    user = os.environ.get('MYSQL_USER', 'devUser')
    password = os.environ.get('MYSQL_PASSWORD', 'Dev')
    database = os.environ.get('MYSQL_DATABASE', 'turbo_train')
    return mysql.connector.connect(user=user, host=host, port=port, password=password, database=database)

@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route('/api/getMonths', methods=['GET'])
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