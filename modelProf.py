from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from pony.flask import Pony
from uuid import uuid4 as gid, UUID
from datetime import datetime, date
import os


db = Database()
print("ulazak u bazu")

# ukoliko želiš da se svaki puta briše baza
# if os.path.exists("database.sqlite"):
#    os.remove("database.sqlite")

db.bind(provider='sqlite', filename='probnaabase.sqlite', create_db=True)


class Korisnik(db.Entity):
    id = PrimaryKey(str)
    ime = Required(str)
    prezime = Required(str)
    email = Required(str)
    lozinka = Required(str)
    datum = Required(datetime)
    korisnickoIme = Required(str)
    # Veza na više, pišemo kao string jer je definirano tek niže
   # specijalizacija = Set("Specijalizacija")



class Specijalizacija(db.Entity):
    id = PrimaryKey(str)
    naziv = Required(str)  
    # Veza na više, ovaj puta ne mora kao string, ali može
   # korisnici = Required("Korisnik")
    #pitanje = Set("Pitanje")


class Pitanje(db.Entity):
    id = PrimaryKey(str)
    text = Required(str)
   # specijalizacija = Required("Specijalizacija")
    #odgovor = Set("Odgovor")

class Savjeti(db.Entity):
    id = PrimaryKey(str)
    text = Required(str)

class Kontakti(db.Entity):
    id = PrimaryKey(str)
    text = Required(str)    


"""
class Odgovor(db.Entity):
    id = PrimaryKey(str)
    text = Required(str)
    pitanje = Required(Pitanje)


"""
db.generate_mapping(check_tables=True, create_tables=True)


# zgodno za testiranje, ne poziva se kad se uključi ovaj file kao modul
if __name__ == "__main__":
    with db_session() as s:
        a = Korisnik(id="1", jmbag="02", ime="Nikola")
        k = Kolegij(id="1", naziv="DWA", semestar=1, studenti=[a])
        i = Ispit(id="1", kolegij=k, datum=dt.datetime.now(), maxBodova=100.)
        si = StavkaIspita(id="1", ispit=i, brojBodova=99.5, ocjena=5, student=a)