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
from domain import Korisnici, Pitanja, Specijalizacije, SavijetiList
from flask_cors import CORS
from flask import Flask, Response, jsonify, request, render_template, json
from datetime import datetime
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID



app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
def error(status=500, text="An error happened"):
    return jsonify({"error": text}), status


@app.route("/upit", methods=["POST"])
def handleNewPost():
    status, errors = Pitanja.dodajUpit(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(errors)
        return r

@app.route("/upit", methods = ["GET"])
def handlePosts():
    postovi = Pitanja.listajP()
    return jsonify({"data": postovi})

@app.route("/upit/<upit_id>", methods = ["PUT"])
def handleUpit(upit_id):
    data = request.get_json()
    if data is None or "id" not in data:
        return error(404, "non matching id")
    response = Pitanja.update(data)
    if response is None:
        return error()
    return Response(status=202)


@app.route("/sign-up", methods=[ "POST"])
def handleSignUp():
    status, errors = Korisnici.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(errors)
        return r

@app.route("/sign-up", methods=["GET"])
def handleUsers():
    users = Korisnici.listaj()
    return jsonify({"data": users})

@app.route("/login/<email>/<lozinka>", methods=["GET"])
def handleLogin(email, lozinka):
    email = str(email)
    lozinka = str(lozinka)
    login = Korisnici.prijava(email, lozinka)
    return jsonify(login)

@app.route("/kategorija", methods=["GET"])
def handleKat():
    kategorije = Specijalizacije.listajS()
    return jsonify({"data": kategorije})

@app.route("/kategorija/<kat_id>", methods=['GET'])
def odaberiKategoriju(kat_id):
    id_kat = str(kat_id)
    res = Specijalizacije.filter_spec(id_kat).to_dict
    return jsonify(res)

@app.route("/savjeti", methods=['GET'])
def handleSavjeti():
    savjeti = SavijetiList.listajSavjete()
    return jsonify({"data": savjeti})    



if __name__ == "__main__":
    app.debug = True
    app.run()