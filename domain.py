from modelProf import Korisnik, Specijalizacija, Pitanje
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID
from datetime import datetime, date
from datetime import date, datetime
from flask import Flask, Response, jsonify, request, render_template, json



class Korisnici:
    @db_session()
    def listaj():
        q = select(user for user in Korisnik)
        data = [x.to_dict() for x in q]
        return data


    @db_session()
    def dodaj(user):
        try:
            user["id"] = str(gid())
            user = Korisnik(**user)
            return True, None
        except Exception as e:
            return False, str(e)



class Specijalizacije:
    @db_session()
    def listajS():
        q = select(user for user in Specijalizacija)
        data = [x.to_dict() for x in q]
        return data


    @db_session()
    def dodaj(user):
        try:
            user["id"] = str(gid())
            user = Specijalizacija(**user)
            return True, None
        except Exception as e:
            return False, str(e)

class Pitanja:
    @db_session()
    def listajS():
        q = select(user for user in Pitanje)
        data = [x.to_dict() for x in q]
        return data


    @db_session()
    def dodaj(user):
        try:
            user["id"] = str(gid())
            user = Pitanje(**user)
            return True, None
        except Exception as e:
            return False, str(e)