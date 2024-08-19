from flask import Flask
from flask import render_template
from flask import request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route('/todolist', methods=['GET', 'POST'])
def todolist():
      mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="todo-list"
    )
      mycursor = mydb.cursor()
      date = str(request.form['date'])
      sql1 = "SELECT MAX(id) FROM todolist"
      mycursor.execute(sql1)
      myresult = str(mycursor.fetchall())
      new_result = myresult.replace("(", "")
      new_result = new_result.replace(",)", "")
      new_result = new_result.replace("[", "")
      new_result = int(new_result.replace("]", ""))
      print(new_result)
      sql = "INSERT INTO todolist (id, date, text) VALUES ("+str((new_result)+1)+", '"+date+"', '0')"
      print(date)
      mycursor.execute(sql)
      mydb.commit()
      return render_template('todo-list.html',date=date)