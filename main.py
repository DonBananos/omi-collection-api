from flask import Flask, Response
from flask.ext import restful
from flask.ext.restful import reqparse

import json

app = Flask(__name__)

# Run the server externally
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)
