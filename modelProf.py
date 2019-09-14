from pony.orm import *
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
    specijalnost = Required(str)
    pitanja = Set("Pitanje")
    # Veza na više, pišemo kao string jer je definirano tek niže
   # specijalizacija = Set("Specijalizacija")



class Specijalizacija(db.Entity):
    id = PrimaryKey(str)
    naziv = Required(str)  


class Pitanje(db.Entity):
    id = PrimaryKey(str)
    naslov = Required(str)
    text = Required(str)
    kategorija = Required(str)
    odgovor = Optional(str)
    kategorija_id = Required(str)
    created_odgovor = Optional(datetime, sql_default='CURRENT_TIMESTAMP')
    created = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    doktor = Optional(str)
    user = Optional(Korisnik)
   # specijalizacija = Required("Specijalizacija")
    #odgovor = Set("Odgovor")

class Savjeti(db.Entity):
    id = PrimaryKey(str)
    naslov = Required(str)
    text = Required(str)


db.generate_mapping(check_tables=True, create_tables=True)



with db_session() as s:
    spec1 = Specijalizacija(id="1",naziv="Uho,grlo,nos")
    spec2 = Specijalizacija(id="2",naziv="Mozak i živćani sustav")
    spec3 = Specijalizacija(id="3",naziv="Kosti i mišićni sustav")
    spec4 = Specijalizacija(id="4",naziv="Probavni sustav")
    spec5 = Specijalizacija(id="5",naziv="Pluća i dišni sustav")
    spec6 = Specijalizacija(id="6",naziv="Mokraćni i spolni organi")
    spec7 = Specijalizacija(id="7",naziv="Srce i krvožilni sustav")
    spec8 = Specijalizacija(id="8",naziv="Alergije")
    savjet1 = Savjeti(id="1",naslov="Sezonske alergije", text="Što je alergija i kako nastaje alergijska reakcija? Alergiju uzrokuju alergeni koje udišemo iz okoliša, unosimo hranom ili se javljaju kao posljedica uzimanja lijekova ili uboda insekata. Alergijska reakcija je odgovor našeg imunološkog sustava odnosno reakcija preosjetljivosti na alergene iz okoliša.U jednom trenutku tijelo počinje prepoznavati alergene kao stvarajući antitijela protiv njih. Pri sljedećem susretu s alergenom se oslobađa histamin koji uzrokuje neugodne simptome alergije. Alergijska reakcija se može dogoditi odmah ili par sati nakon kontakta s nekim alergenom. Nekada se simptomi alergije mogu javiti jako brzo i ozbiljno ugroziti život bolesnika. Alergijske bolesti mogu biti nasljedne ali se mogu i razviti uslijed dugotrajne izloženosti nekom alergenu ili infekciji.")
    savjet2 = Savjeti(id="2", naslov="Sunčanica", text="Sunčanica je termoregulacijski poremećaj koji nastaje nakon intenzivnog izlaganja glave i zatiljka sunčevim zrakama. Sunčanica se svrstava u stanja povišene tjelesne temperature, izazvane vanjskim čimbenicima,  odnosno visokom temperaturom okoline. Osobito su podložne osobe svijetle puti, osobe bez kose, te djeca i starije osobe koje se i  inače slabije prilagođavaju naglim promjenama temperature.PrevencijaUgroženi su sve osobe koje se dugotrajno izlažu sunčevim zrakama.  Nije preporučljivo izlaganje suncu u vremenu od 11,00-17,00 sati. Osobe koje su zbog posla direktno izložene sunčevim zraka u preventivne svrhe trebaju zaštiti glavu pokrivalom ,dobro je pokrivalo držati mokrim kako bi se glava i zatiljak što više rashlađivao, preporučljivo je obilno konzumiranje tekućine izuzev alkohola i kave. Rashlađivanje tijela kontinuirano može pomoći u prevenciji .")
    savjet3 = Savjeti(id="3", naslov="Kako se zaštititi od gripe?", text="Iako se trenutno ispituju brojni protuvirusni lijekovi koji bi mogli pomoći u liječenju gripe, liječenje se danas svodi na ublažavanje simptoma i liječenje eventualnih komplikacija.Gripa je onesposobljavajuća i neugodna bolest s mnogo potencijalnih komplikacija, te je najbolje u potpunosti je izbjeći. Iako niti jedno cjepivo ne može garantirati 100%-tnu učinkovitost, cijepljenje protiv gripe preporučljivo je svima, a pogotovo osobama starijim od 65 godina, kroničnim bolesnicima, zdravstvenim djelatnicima, djelatnicima u vrtićima, školama i sličnim ustanovama te imunokompromitiranima (osobe koje su splenektomirane, HIV-pozitivne, primaju kemoterapiju i slično). Kontraindikacije za cijepljenje su preosjetljivost na sastojke cjepiva, posebice na proteine jajeta, te akutna bolest u trenutku namjere cijepljenja. Cijepljenje je potrebno ponoviti svake godine jer virus vrlo često mutira te je potrebno redovito imunološki sustav. Ne smije se zaboraviti da je potrebno nekoliko tjedana da bi se stvorila protutijela na virus protiv kojega smo se cijepljenjem zaštitili, stoga je potrebno cijepljenje obaviti već sredinom studenoga. Iako se trenutno ispituju brojni protuvirusni lijekovi koji bi mogli pomoći u liječenju gripe, liječenje se danas svodi na ublažavanje simptoma i liječenje eventualnih komplikacija. Budući da gripa toliko dugo odolijeva svim naporima čovječanstva da je iskorijeni, mogla bi još dugo vremena biti podsjetnik svima, a pogotovo mladim i zdravim ljudima, na to kako je biti bolestan.Kako razlikovati gripu od prehladeza razliku od prehlade, gripa je redovito praćena povišenom tjelesnom temperaturom (i do 40°C!) u trajanju najmanje 3-4 danagripu prate i glavobolja, bolovi u mišićima i zglobovima te dugotrajni umor i osjećaj slabosti i iscrpljenostidok su glavna obilježja prehlade hunjavica, kihanje i grlobolja, moguće je preboljeti gripu i bez pojave tih simptomaKako liječiti gripu? odmarajte se izbjegavajte nepotrebni kontakt s drugim ljudima, kako ih ne biste zarazili redovito provjetravajte prostorije u kojima boravite ne jedite iz zajedničkih posuda niti dijelite zajedničke ručnike s ostatkom ukućana jedite svježe voće - agrumi su ukusni, pomoći će u rehidraciji i sadrže velike količine vitamina C pijte mnogo tekućine, najbolje u obliku toplog čaja vitamin C prestaje biti aktivan na visokim temperaturama, stoga nemojte stavljati limun u vrući čaj ako time planirate unijeti vitamin C u svoj organizam pomoći će vam i brojni komercijalni pripravci za ublažavanje simptoma gripe (dostupni i bez liječničkog recepta) u obliku kombinacije najčešće paracetamola, vitamina C, dekongestiva nosne sluznice i sličnih aktivnih tvari nemojte na svoju ruku uzimati antibiotike: gripa je virusna bolest te je ne možemo liječiti antibioticima, koji, kao i svaki lijek, mogu biti štetni za organizam naravno, antibiotike uzimajte ako je vaš liječnik zaključio da se bolest zakomplicirala bakterijskom infekcijom javite se liječniku ako vam se javi žuti, gnojavi sekret iz nosa, ako teško gutate ili počnete znatno jače iskašljavati sluz te ako bolest traje dulje od 10 dana djeca mlađa od 15 godina nipošto ne bi smjela uzimati acetilsalicilnu kiselinu zbog opasnosti od pojave Reyeva sindroma; njima se kao adekvatna zamjena preporuča paracetamol nemojte gripu bespotrebno ponovno proživljavati: sljedeće se godine na vrijeme cijepite i dajte gripi do znanja da je ona za vas persona non grata")




# zgodno za testiranje, ne poziva se kad se uključi ovaj file kao modul

        

