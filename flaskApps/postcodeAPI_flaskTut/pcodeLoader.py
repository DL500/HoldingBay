#Loader script to add data into table in davidsandbox. Not complete.
#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

# This script is to download fake data from Faker
# The script will also do a remote call to davidsandbox and insert fake data.

from faker import Faker
import psycopg2


fake = Faker('en_GB')

myFile = open('fakePcode.tsv', 'w')

for i in range(100):
    myPostcode = fake.postcode()
    myFile.writelines(myPostcode.replace(' ', '') + '\t' + fake.city() + '\t' + myPostcode + '\n')

DBNAME = 'davidsandbox'
USER = 'dev_admin'
DBHOST = '10.20.0.164'
PASSWORD = 'l!3bg0tt'

try:
    dbConn = psycopg2.connect("dbname="+DBNAME+" user="+USER+" host="+DBHOST+" password="+PASSWORD+"")
    dbCur = dbConn.cursor()
except Exception as errorMsg:
    print(errorMsg)

dbCur.execute("""INSERT INTO uk_postal_address (id, city, postcode) VALUES (myPostcode, city, myPostcode, ...);""")
dbConn.close()
dbCur.close()

""" I have a feeling that the data has to come from the file created
'myFile = fakePcode.tsv' to be inserted into table 'uk_postal_address' and not from line 16.
Not sure how this works"""

## Cleo's Comments:
"""
There are two approaches here: you can insert the data straight from the faker output OR you can write the faker data to a file and then read it out and insert it. There are pros/cons to both strategies. If it was me, for this exercise, I would just insert from the faker libray.

In either event, the answer to your question is a "loop". A loop is basically:

for <individual item> in <set of items>:
    do one thing
    do another thing


So to set this up, the faker process should generate the "for item in set" bit and then the INSERT will be part of the "do one thing" process.

I'll leave the hint here. Please let me know if you need another nudge.
"""
