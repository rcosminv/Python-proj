from tinydb import TinyDB, Query
from datetime import datetime

import json
import math
db = TinyDB('db.json')
User = Query()

Inventar = {'Banane': '2', 'Mere': '6', 'Struguri': '5', 'Portocale': '7'}
Comanda = {'Comanda1': {'data' : '2020-12-25T00:05:23','fruct' : 'Banane','cantitate' : 20},
           'Comanda2': {'data' : '2020-12-24T00:05:23','fruct' : 'Struguri','cantitate' : 30},
           'Comanda3': {'data' : '2020-12-18T00:05:23','fruct' : 'Mere','cantitate' : 50},
           'Comanda4': {'data' : '2020-12-24T00:05:23','fruct' : 'Portocale','cantitate' : 27},
           'Comanda5': {'data' : '2020-12-27T00:05:23','fruct' : 'Banane','cantitate' : 45}
           }

db.insert(Inventar)
db.insert(Comanda)
Valori = db.all()

def numar_marfa(Valori, TimeStamp, Zile):
    BList = []
    MList = []
    SList = []
    PList = []
    MaxBanane = 0
    MaxMere = 0
    MaxStruguri = 0
    MaxPortocale = 0
    Inventarul = []

    TimeStamp = datetime.fromisoformat(TimeStamp)
    perioada = datetime.now() - TimeStamp

    for key in Valori[0]:
        Inventarul.append(Valori[0][key])
    for element in Valori[1]:
        for el in Valori[1][element]:
            if (el == 'fruct' and Comanda[element][el] == 'Banane' and  TimeStamp < datetime.fromisoformat(Comanda[element]['data'])):
                BList.append(Valori[1][element]['cantitate'])
            if (el == 'fruct' and Comanda[element][el] == 'Mere' and  TimeStamp < datetime.fromisoformat(Comanda[element]['data'])):
                MList.append(Valori[1][element]['cantitate'])
            if (el == 'fruct' and Comanda[element][el] == 'Struguri' and  TimeStamp < datetime.fromisoformat(Comanda[element]['data'])):
                SList.append(Valori[1][element]['cantitate'])
            if (el == 'fruct' and Comanda[element][el] == 'Portocale' and  TimeStamp < datetime.fromisoformat(Comanda[element]['data'])):
                PList.append(Valori[1][element]['cantitate'])
    print("BList" + str(BList))
    print("MList" + str(MList))
    print("SList" + str(SList))
    print("PList" + str(PList))
    print(Inventarul)
    print (perioada)
    for element in MList:
        MaxMere = MaxMere + element

    for element in BList:
        MaxBanane = MaxBanane + element

    for element in SList:
        MaxStruguri = MaxStruguri + element

    for element in PList:
        MaxPortocale = MaxPortocale + element

    print("\n")
    print("nr de mere maxim " + str(MaxMere))
    print("nr de Banane maxim " + str(MaxBanane))
    print("nr de struguri maxim " + str(MaxStruguri))
    print("nr de portocale maxim " + str(MaxPortocale))
    print("\n")

    print( math.ceil(MaxBanane / perioada.days))
    print( math.ceil(MaxMere / perioada.days))
    print( math.ceil(MaxStruguri / perioada.days))
    print( math.ceil(MaxPortocale / perioada.days))

    MaxBanane = math.ceil(MaxBanane / perioada.days ) * Zile
    MaxMere = math.ceil(MaxMere / perioada.days ) * Zile
    MaxStruguri = math.ceil(MaxStruguri / perioada.days ) * Zile
    MaxPortocale = math.ceil(MaxPortocale / perioada.days ) * Zile

    print("nr de mere maxim " + str(MaxMere))
    print("nr de Banane maxim " + str(MaxBanane))
    print("nr de struguri maxim " + str(MaxStruguri))
    print("nr de portocale maxim " + str(MaxPortocale))
    print("\n")

    if(MaxMere == 0):
        CMere = 0
    else:
        CMere = MaxMere - int(Inventarul[1])

    if(MaxBanane == 0):
        CBanane = 0
    else:
        CBanane = MaxBanane - int(Inventarul[0])

    if(MaxStruguri == 0):
        CStruguri = 0
    else:
        CStruguri = MaxStruguri - int(Inventarul[2])

    if(MaxPortocale == 0):
        CPortocale = 0
    else:
        CPortocale = MaxPortocale - int(Inventarul[3])

    print("comanda pentru urmatoarele " + str(Zile) + " zile este: \n" +  str(CBanane) + " Banane \n" +
          str(CMere) + " Mere\n" + str(CStruguri) + " Struguri\n" + str(CPortocale) + " Portocale")

def main():
    numar_marfa(Valori,'2020-12-26T00:05:23',6)
    aux =open('db.json','w')
    aux.write('{}')
if __name__ == "__main__":
    main()