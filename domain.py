from modelProf import Korisnik, Specijalizacija, Pitanje, Savjeti
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID
import datetime as dt
from flask import Flask, Response, jsonify, request, render_template, json
import logging


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

    @db_session()
    def prijava(email, lozinka):
        korisnik = Korisnik.get(email=email)
        if korisnik:
            korisnik = korisnik.to_dict()
            if korisnik["lozinka"] == lozinka:
                return korisnik
            else:
                return "Pogrešna lozinka"
        else:
            return "Korisnik s tim podacima ne postoji!"


class Specijalizacije:
    @db_session()
    def listajS():
        q = select(s for s in Specijalizacija)
        data = [x.to_dict() for x in q]
        return data

    @db_session()
    def filter_spec(spec_id):
        spec = Specijalizacija.get(id=spec_id)
        return spec


class Pitanja:
    @db_session()
    def listajP():
        q = select(p for p in Pitanje)
        data = [x.to_dict() for x in q]
        return data

    @db_session()
    def dodajUpit(p):
        try:
            p["id"] = str(gid())
            p = Pitanje(**p)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session()
    def update(data):
        try:
            data["created_odgovor"] = dt.datetime.now()
            pitanje = Pitanje[data["id"]]
            pitanje.set(**data)
            return True
        except Exception as e:
            logging.exception("Error saving data")


class SavijetiList:
    @db_session()
    def listajSavjete():
        q = select(s for s in Savjeti)
        data = [x.to_dict() for x in q]
        return data
