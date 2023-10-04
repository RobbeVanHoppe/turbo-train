import os

from flask import Flask, request, jsonify, Response
import mysql.connector

app = Flask(__name__)


def get_mysql_connection():
    host = os.environ.get('MYSQL_HOST', 'localhost')
    port = os.environ.get('MYSQL_PORT', '3306')
    user = os.environ.get('MYSQL_USER', 'devUser')
    password = os.environ.get('MYSQL_PASSWORD', 'Dev')
    database = os.environ.get('MYSQL_DATABASE', 'turbo_train')
    return mysql.connector.connect(user=user, host=host, port=port, password=password, database=database)


def sql_command_select_x_from_y_where_z(amount: str, table: str, condition=''):
    sqlstr = f"SELECT {amount} FROM {table} "
    if condition != '':
        sqlstr = sqlstr + f"WHERE {condition};"
    return sql_base_command(sqlstr)


def sql_command_insert_into_x_y_values_z(table: str, values: str, columns=''):
    sqlstr = f"INSERT INTO {table} "
    if columns != '':
        sqlstr = sqlstr + f"({columns}) "
    sqlstr = sqlstr + f"VALUES ({values});"
    return sql_base_command(sqlstr, insert=True)


def sql_base_command(sqlstr: str, insert=False):
    db = get_mysql_connection()
    try:
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        if insert:
            db.commit()
            return "Insert succesful"
        else:
            output_json = cur.fetchall()
            return output_json

    except Exception as e:
        return "Error in SQL: \n", e
    finally:
        db.close()


@app.route("/")
def hello():
    return "Flask inside Docker!!"


@app.route('/api/getUsers', methods=['GET'])
def get_users():
    data = sql_command_select_x_from_y_where_z('*', 'users')
    return jsonify(data)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user_data = sql_command_select_x_from_y_where_z("*", 'users', f"username = '{username}' AND password = '{password}'")
    return jsonify(user_data)


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user = {
        "username": data['username'],
        "password": data['password'],
        "email": data['email']
    }

    resp = sql_command_insert_into_x_y_values_z('users',
                                                f"'{user['username']}', '{user['password']}', '{user['email']}'",
                                                'username, password, email')
    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')