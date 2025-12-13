import csv

class jegkori:
    def __init__(self, nev,orszag,technikai,komponens,levonas):
        self._nev=nev
        self._orszag=orszag
        self._technikai=technikai
        self._komponens=komponens
        self._levonas=levonas

    def __str__(self):
        return f"{self._nev} ; {self._orszag} ;{self._technikai} ; {self._komponens} ;{self._levonas}"

    
versenyzok=[]
donto=[]
osszpontszam=0

with open("rovidprogram.csv","r",encoding='utf-8') as file:
    csvreader=csv.reader(file, delimiter=';')
    next(csvreader, None)

    for row in csvreader:
        nev=row[0]
        orszag=row[1]
        technikai=row[2]
        komponens=row[3]
        levonas=row[4]

        kori=jegkori(nev,orszag,technikai,komponens,levonas)
        versenyzok.append(kori)

with open("donto.csv","r",encoding='utf-8') as f:
    csv_reader=csv.reader(f,delimiter=';')
    next(csv_reader, None)

    for r in csv_reader:
        nev=r[0]
        orszag=r[1]
        technikai=r[2]
        komponens=r[3]
        levonas=r[4]

        eredmeny=jegkori(nev,orszag,technikai,komponens,levonas)
        donto.append(eredmeny)

def main():
    for versenyzo in versenyzok:
        print(versenyzo)

    for e in donto:
        print(e)

def versenyzok_szama():
    vszama=len(versenyzok)
    print(f"2. feladat \n A rövid programban {vszama} induló volt.")

def bejutott():        
    for b in donto:
        if b._orszag=="HUN":
            print(f"3. feladat \n A magyar versenyző bejutott a kűrbe.")
        

def OsszPontszam():
    
    nev= input(f"Kérem a versenyző nevét: ")
    osszpontszam=0
    nincs=False
    for ve in versenyzok:
            if ve._nev==nev:
                    osszpontszam=(float(ve._technikai) + float(ve._komponens))-float(ve._levonas)

                    for dont in donto:
                        if dont._nev==nev:
                            osszpontszam+=((float(dont._technikai) + float(dont._komponens))-float(dont._levonas))
            
            if osszpontszam==0:
                print("Ilyen nevű induló nem volt")


    print(f"Versenyző összpontszáma: {osszpontszam}")

def tovabbjuto():
    tovabbjut_lista=[o._orszag for o in versenyzok ]
    egyedi = set(tovabbjut_lista)

    for e in egyedi:
        db=tovabbjut_lista.count(e)

        if db > 1:
            print(f"{e}: {db} versenyző")

if __name__=="__main__":
    main()
    versenyzok_szama()
    bejutott()
    # OsszPontszam()
    tovabbjuto()