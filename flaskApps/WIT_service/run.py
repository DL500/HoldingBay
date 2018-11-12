# run app file for WITv1

from tdService import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=True)
