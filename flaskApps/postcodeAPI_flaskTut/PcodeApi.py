#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

"""I will be trying to make an API that will resolve a postcode
to the city from a client database.
Agent will ask for the postcode from a client and input this into perx.
Perx (API) will take postcode and search database for client and give back city.
For test purpose I will be using the fake data from Faker."""

"""I will be taking 4 entries from the Faker data file and using this the try and get the
desired result on my local machine before connecting to 'davidsandbox'."""

from flask import Flask, jsonify


app = Flask(__name__)

postalcodes = [
    {
        'id': 'S925XZ',
        'city': 'South Harryview',
        'postcode': 'S92 5XZ',
    },
    {
        'id': 'G89SU',
        'city': 'Rachelbury',
        'postcode': 'G8 9SU',
    },
    {
        'id': 'N665AT',
        'city': 'Smithburg',
        'postcode': 'N66 5AT',
    },
    {
        'id': 'EH711GQ',
        'city': 'South Ashleymouth',
        'postcode': 'EH71 1GQ',
    }
]

@app.route('/pcode/<string:pcode_postcode>', methods=['GET'])

def cityname(pcode_postcode):
    pcode = [pcode for pcode in postalcodes if pcode['postcode'] == pcode_postcode]
    return jsonify({'Clients City': pcode[0]})

if __name__ == '__main__':
    app.run(debug=True)
