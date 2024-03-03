from flask import Flask, request, render_template, redirect, jsonify
import os
import mysql.connector as mysql

conn = mysql.connect(
    host="localhost",
    user = "root",
    password = "12345678",
    port = 3306,
    database = "my_memo"
)

app = Flask(__name__)

@app.route('/getuser/v1/<idmemo>', methods=["GET"])
def get_user(idmemo):
    cur = conn.reconnect()

    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo WHERE idmemo=%s ORDER By firstname"
    data = (idmemo,)
    cur = conn.cursor()
    cur.execute(sql, data)
    records = cur.fetchone()
    conn.close()
    return jsonify(records)

@app.route('/getuser', methods=["GET"])
def get_user_all():
    cur = conn.reconnect()

    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo ORDER By firstname"
   
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    conn.close()
    return jsonify('/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)