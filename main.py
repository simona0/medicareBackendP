"""glavna"""
import os
import sys
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE
import json
from flask import Flask, request, render_template
#import routes, os
from flask import Flask, render_template, Response, jsonify, request, redirect, url_for
from datetime import datetime
from domain import Korisnici

from flask import Flask, Response, jsonify, request, render_template, json
from datetime import datetime
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID


app = Flask(__name__)
"""
@app.route("/index", methods=["GET", "POST"])
def pocetna():
    return render_template('index.html')

@app.route("/s", methods=["GET", "POST"])
def pocetna():
    return render_template('layout.html')

"""
@app.route("/", methods=["GET", "POST"])
def layout():
    return render_template('prelayout.html')

@app.route("/izbornik", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/pocetna", methods=["GET", "POST"])
def pocetna():
    return render_template('layout.html')

@app.route("/log&sign", methods=["GET", "POST"])
def logisign():
    return render_template('loginsign.html')

@app.route("/about", methods=["GET", "POST"])
def izbornik():
    return render_template('about.html')

@app.route("/kontakti", methods=["GET", "POST"])
def kontakti():
    return render_template('contact.html')

@app.route("/savjeti", methods=["GET", "POST"])
def savjeti():
    return render_template('savjeti.html')

@app.route("/mojiPodaci", methods=["GET", "POST"])
def mojiPodaci():
    return render_template('mojiPodaci.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/signup", methods=["GET", "POST"])
def handleSignUp():
    status, errors = Korisnici.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(errors)
        return r

    

@app.route("/hello", methods=["GET"])
def handle_korisnici():
    korisnici = Korisnici.listaj()
    return jsonify({"data":korisnici})


@app.route("/hello", methods=["POST"])
def handle_input_korisnici():
    status, greske = Korisnici.dodaj(request.get_json())
    if status:
        return Response(status = 201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r





if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", "8000")