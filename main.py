from tinydb import TinyDB, Query
import json
import math
db = TinyDB('db.json')
User = Query()

Inventar = {'Banane': '2', 'Mere': '6', 'Struguri': '5', 'Portocale': '7', 'Zile': '13'}
Comanda1 = {'Banane': '40', 'Mere': '100', 'Struguri': '27', 'Portocale': '14', 'Zile': '13'}
Comanda2 = {'Banane': '12', 'Mere': '70', 'Struguri': '40', 'Portocale': '40', 'Zile': '13'}
Comanda3 = {'Banane': '0', 'Mere': '25', 'Struguri': '13', 'Portocale': '100', 'Zile': '9'}

db.insert(Inventar)
db.insert(Comanda1)
db.insert(Comanda2)
db.insert(Comanda3)
Valori = db.all()


def numar_marfa(Valori, zilele):
    BList = []
    MList = []
    SList = []
    PList = []
    ZList = []
    MaxBanane = 0
    MaxMere = 0
    MaxStruguri = 0
    MaxPortocale = 0
    Inventarul = []
    for key in Valori[0]:
        Inventarul.append(Valori[0][key])
    for i in range(0, 4):
        BList.append(Valori[i]["Banane"])
        MList.append(Valori[i]["Mere"])
        SList.append(Valori[i]["Struguri"])
        PList.append(Valori[i]["Portocale"])
        ZList.append(Valori[i]["Zile"])
    print(BList)
    print(MList)
    print(SList)
    print(PList)
    print(ZList)
    print(Inventarul)

    for i in range(0, 3):
        MaxMere = max(MaxMere, math.ceil(int(MList[i]) / int(ZList[i])))
        MaxBanane = max(MaxBanane, math.ceil(int(BList[i]) / int(ZList[i])))
        MaxStruguri = max(MaxStruguri, math.ceil(int(SList[i]) / int(ZList[i])))
        MaxPortocale = max(MaxPortocale, math.ceil(int(PList[i]) / int(ZList[i])))
    print("nr de mere maxim " + str(MaxMere))
    print("nr de Banane maxim " + str(MaxBanane))
    print("nr de struguri maxim " + str(MaxStruguri))
    print("nr de portocale maxim " + str(MaxPortocale))

    MaxBanane = MaxBanane * zilele
    MaxMere = MaxMere * zilele
    MaxStruguri = MaxStruguri * zilele
    MaxPortocale = MaxPortocale * zilele

    print("comanda pentru urmatoarele " + str(zilele) + " zile este: \n" +  str(MaxBanane-int(Inventarul[0])) + " Banane \n" +
          str(MaxMere-int(Inventarul[1])) + " Mere\n" + str(MaxStruguri-int(Inventarul[2])) + " Struguri\n" + str(MaxPortocale-int(Inventarul[3])) + " Portocale")
    # print(produse)
    # print(db.all())

def main():
    numar_marfa(Valori,6)

if __name__ == "__main__":
    main()