from tinydb import TinyDB, Query
from datetime import datetime

import json
import math
db = TinyDB('db.json')
User = Query()

Inventar = {'Banane': '2', 'Mere': '6', 'Struguri': '5', 'Portocale': '7'}
Comanda = {'Comanda1': {'data' : '2020-12-25T00:05:23','fruct' : 'Banane','cantitate' : 20},
           'Comanda2': {'data' : '2020-12-25T00:05:23','fruct' : 'Struguri','cantitate' : 30},
           'Comanda3': {'data' : '2020-12-18T00:05:23','fruct' : 'Mere','cantitate' : 50},
           'Comanda4': {'data' : '2020-12-24T00:05:23','fruct' : 'Portocale','cantitate' : 27},
           'Comanda5': {'data' : '2020-12-27T00:05:23','fruct' : 'Banane','cantitate' : 45},
           'Comanda6': {'data' : '2020-12-27T00:05:23','fruct' : 'Banana2','cantitate' : 4}
           }

db.insert(Inventar)
db.insert(Comanda)
Valori = db.all()

def numar_marfa(Valori, TimeStamp, Zile):

    perioada = datetime.now() - TimeStamp
    elemente = []

    for element in Valori[1]:
        for ala in Valori[1][element]:
            if (ala == 'fruct' and Comanda[element][ala] not in elemente):
                elemente.append(Comanda[element][ala])

    valoriMaxime = [None] * len(elemente)

    for element in Comanda:
        for ala in Comanda[element]:
            if (ala == 'fruct'):
                nume = Comanda[element][ala]
        for fructul in range(0, len(elemente)):
            if (nume == elemente[fructul] and  TimeStamp < datetime.fromisoformat(Comanda[element]['data'])):
                print(fructul)
                if (valoriMaxime[fructul] == None):
                    valoriMaxime[fructul] = Comanda[element]['cantitate']
                else:
                    valoriMaxime[fructul] += Comanda[element]['cantitate']

    print(valoriMaxime)
    print (perioada)

    print("\n")
    for iterator in range (0,len(valoriMaxime)):
        print(str(elemente[iterator]) + " " + str(valoriMaxime[iterator]))

    for iterator in range(0, len(valoriMaxime)):
        if(valoriMaxime[iterator] == None):
            valoriMaxime[iterator] = 0

    for iterator in range (0,len(valoriMaxime)):
        valoriMaxime[iterator] = math.ceil(valoriMaxime[iterator] / perioada.days) *Zile
        print(valoriMaxime[iterator])

    print("\n")

    for iterator in range(0, len(valoriMaxime)):
        if(valoriMaxime[iterator] == 0):
            valoriMaxime[iterator] = 0
        else:
            if(elemente[iterator]  not in Inventar):
                Inventar[elemente[iterator]] = 0
            if(valoriMaxime[iterator] - int(Inventar[elemente[iterator]]) < 0):
                valoriMaxime[iterator] = 0
            else:
                valoriMaxime[iterator]-= int(Inventar[elemente[iterator]])

    print("comanda pentru urmatoarea perioada este:")
    for iterator in range (0,len(valoriMaxime)):
        print(str(elemente[iterator]) + " " + str(valoriMaxime[iterator]))


def main():
    luna = 100
    zile = 100
    ora = 100
    minut = 100
    nrZile = 0
    an = 0
    while(nrZile < 1):
        nrZile = int(input("introdu numarul de zile "))
    while(an < 1):
        an = int(input("introdu anul pentru timestamp "))
    while(luna > 12 or luna <= 0):
        luna = int(input("introdu luna pentru timestamp "))
    while(zile > 31 or zile <= 0):
        zile = int(input("introdu ziua pentru timestamp "))
    while(ora > 24 or ora < 0):
        ora = int(input("introdu ora pentru timestamp "))
    while(minut < 0 or minut > 60):
        minut = int(input("introdu minutele pentru timestamp "))
    print(datetime(an, luna, zile, ora, minut, 0, 0 ))
    timp = datetime(an, luna, zile, ora, minut, 0, 0 )
    numar_marfa(Valori, timp ,int(nrZile))
    aux =open('db.json','w')
    aux.write('{}')
if __name__ == "__main__":
    main()

