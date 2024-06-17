from flask import Flask, jsonify
import json

app = Flask(__name__)

from Users import Users

@app.route("/")
def root():
    return "Hbnb"

@app.route("/Users")
def get_all_Users():
    return jsonify(Users)






if __name__ == '__main__':
    app.run(debug=True, port=4000)