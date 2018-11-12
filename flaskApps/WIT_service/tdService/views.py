#!/usr/bin/python3
# views file for WITv1

from flask import render_template, request, flash, redirect
from tdService import app
import psycopg2
import datetime

connectionString = 'dbname=davidsandbox user=dev_admin host=10.20.0.164 password=l!3bg0tt'

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return redirect('/select')

@app.route('/forex_rates', methods=['GET', 'POST'])
def exRates():
    myConn = psycopg2.connect(connectionString)
    cur = myConn.cursor()
    if request.method == 'GET':
        try:
            cur.execute("""SELECT target_currency, target_amount FROM forex_rates WHERE rate_tstamp IN (SELECT MAX(rate_tstamp) FROM forex_rates)""")
            resultForex = cur.fetchall()
            return render_template('forex_rates.html', title='ExRates', resultForex = resultForex)
        except Exception as errorMsg:
            print(errorMsg)
            return render_template('forex_rates.html')

@app.route('/agent_call', methods=['GET'])
def call():
    return render_template('agent_callStats.html', title='Call Stats')

@app.route('/agent_Salesfig', methods=['GET'])
def salesFig():
    return render_template('agent_Salesfigures.html', title='Leaderboard')

@app.route('/sales_deals', methods=['GET'])
def deals():
    return render_template('sales_deals.html', title='Special Deals')

@app.route('/select', methods=['GET'])
def select_option():
    return render_template('select.html')
