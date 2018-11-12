#__init__ file for WITv1

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from tdService import views
