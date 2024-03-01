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

@app.route('/adduser_todb', methods=['POST'])
def adduser_todb():
    cur = conn.reconnect()

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    
    sql = "INSERT INTO memo(firstname, lastname, email)"
    sql += " VALUES(%s,%s,%s)"
    data = (firstname,lastname,email)

    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect('https://localhost:5001/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)