'''
Created on Apr 4, 2018

@author: animesh
'''
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

PATH = os.getcwd()
app = Flask(__name__)    
CORS(app)

usernames = ["admin1", "admin2"]
password = ["pass1", "pass2"]

@app.route("/Register", methods=["GET", "POST"])
def Register():
    data = request.form.to_dict()
    print(data)
    return "hell"

@app.route("/login", methods=["GET", "POST"])
def login():
    data = request.form.to_dict()
    for i in range(0,2):
        if (data['username'] == usernames[i] and data['password'] == password[i]):
            print(usernames[i])
            print(password[i])
            result = "Login"
            break
        else:
            result = "Do not allow login"
    
    return result
    
if __name__ == "__main__":
    app.run()