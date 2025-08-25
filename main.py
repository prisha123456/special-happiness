from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def details():
    StudentID= request.form['StudentID']
    Password= request.form['Password']
    Marks out of 100= request.form['marks out of 100']
    date= request.form['date']
    mydb = mysql.connector.connect(
        host="remotemysql:com",
        user="uL7j9FaRVB",
        password="qQvo5rGf3i",
        database="uL7j9FaRVB",)
    mycursor = mydb.cursor()
    mycursor.execute(
      "INSERT INTO customer_details VALUES ($s,$s,$s,$s,$s)",
       (StudentID,password,Marks out of 100,date)
    )
    mydb.commit()

    return render_template('index.html')

@app.route('/winner', methods=['POST', 'GET'])
def winner():
    mysql.connector.connect(
    host="remotemysql:com",
    user="uL7j9FaRVB",
    password="qQvo5rGf3i",
    database="uL7j9FaRVB",)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM customer_details WHERE date = CURRENT_DATE ORDER BY TOTAL AMOUNT DESC')

    account=mycursor.fetchone()
    print(account)
    if account:
      StudentID= account[0]
      Marks out of 100= account[1]
      return render_template('page.html', username=username, phone_number=phone_number)

    else:
      return render_template('page.html')

@app.route('/')
def index():
    return render_template('index.html')
app.run(host='0.0.0.0', port=8000
