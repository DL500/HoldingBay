
def connectToDB():
    DBNAME = 'davidsandbox'
    USER = 'dev_admin'
    DBHOST = '10.20.0.164'
    PASSWORD = 'l!3bg0tt'
    connectionString = "dbname="+DBNAME+" user="+USER+" host="+DBHOST+" password="+PASSWORD+""
    print(connectionString)
    try:
        return psycopg2.connect(connectionString)
    except Exception as errorMsg:
        print(errorMsg)

@app.route('/pcode/<string:uk_postal_address', methods=['GET'])

def cityname(uk_postal_address):
    conn = connectToDB()
    cur = conn.cursor()
    try:
        cur.execute()
