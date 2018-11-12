from flask import render_template, request, flash, redirect
from dlcarService import app
import psycopg2
import datetime


## connect to the database and share with all functions
DSN = "dbname='davidsandbox' user='dev_admin' host='10.20.0.164' password='l!3bg0tt'"
db = psycopg2.connect(DSN)
dbCur = db.cursor()

# fakeData = [{'person': 'David Lasso', 'airport': 'Heathrow', 'time': '5pm'},
# {'person': 'Nigel Smithson', 'airport': 'Heathrow', 'time': '7pm'},
# {'person': 'Cleo Cooke', 'airport': 'Gatwick', 'time': '10am'}]

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return redirect('/select')

@app.route('/res', methods=['POST'])
def booking():
    return render_template('reservations2.html')

@app.route('/bookingsData', methods=['GET'])
def data():
  connectString = 'dbname=davidsandbox user=dev_admin host=10.20.0.164 password=l!3bg0tt'
  myConn = psycopg2.connect(connectString)
  cur = myConn.cursor()
  if request.method == 'GET':
    try:
      cur.execute("""SELECT * FROM reservations""")
      myResult = cur.fetchall()
      return render_template('bookingsData.html', title='Bookings', myResult = myResult)
    except Exception as errorMsg:
      print(errorMsg)
      return render_template('bookingsData.html')

@app.route('/location', methods=['GET'])
def airports():
    connectString = 'dbname=davidsandbox user=dev_admin host=10.20.0.164 password=l!3bg0tt'
    myConn = psycopg2.connect(connectString)
    cur = myConn.cursor()
    if request.method == 'GET':
        try:
            cur.execute("""SELECT * FROM pickup_locations""")
            resultLocation = cur.fetchall()
            print(resultLocation)
            return render_template('location.html', title='Pickup Location', resultLocation = resultLocation)
        except Exception as errorMsg:
            print(errorMsg)
            return render_template('location.html')

@app.route('/bookedRes', methods=['GET', 'POST'])
def bookingconf():
  connectString = 'dbname=davidsandbox user=dev_admin host=10.20.0.164 password=l!3bg0tt'
  myConn = psycopg2.connect(connectString)
  cur = myConn.cursor()
  if request.method == 'POST':
    try:
      cur.execute("""INSERT INTO reservations VALUES (DEFAULT, DEFAULT, 'David Lasso', 1, '2018-03-01 08:00:00', 1, 8.4)""")
      myConn.commit()
      return render_template('bookedRes.html')
    except Exception as errorMsg:
      print(errorMsg)

  #elif request.method == 'GET':
    ##try:
      ##findRes = dbCur.execute("SELECT customer_name, pickup_location, pickup_datetime FROM reservations")
      ##results = findRes.fetchall()
      ###return render_template('bookedRes.html', reservations=results)
    #return render_template('bookedRes.html')
    ##except Exception as errorMsg:
      ##print(errorMsg)

# @app.route('/bookedRes', methods=['GET', 'POST'])
# def bookingconf():
#     if request.method == 'POST':
#         fakeData.append({'person': request.form['name'],
#         'airport': request.form['airport'],
#         'time': request.form['time']})
#     return render_template('bookedRes.html', airport=fakeData)

@app.route('/select', methods=['GET'])
def select_option():
    return render_template('select.html')
