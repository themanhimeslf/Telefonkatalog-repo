telefonkatalog = []
import sqlite3 # imortbibl sqlite3 

conn = sqlite3.connect('telefonkatalog.db')

cursor = conn.cursor()

#cursor.execute ("DROP TABLE IF EXISTS personer")

cursor.execute('''CREATE TABLE IF NOT EXISTS personer (
                fornavn TEXT,
                etternavn TEXT,
                telefonnummer TEXT
        )''')
conn.commit()

def printMeny():
    print("-------------------  Telefonkatalog -------------------")
    print("| 1. Legg til ny person                               |")
    print("| 2. Søk opp personer eller telefonnummer             |")
    print("| 3. Vis alle personer                                |")
    print("| 4. Avslutt                                          |")
    print("-------------------------------------------------------")
    menyvalg = input("skriv inn tall for å velge fra menyen:  ")
    utfoerMenyvalg(menyvalg)


def visAllePersoner():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else:
        print("*********************************************"
              "**********************************************")
        for personer in resultater:
            print("* Fornavn: {:15s} Etternavn:  {:15s} Telefonnummer:{:8s}"
                .format(personer[0], personer[1], personer[2]))
        print("*********************************************"
              "**********************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()

def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO personer (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)",
                   (fornavn, etternavn, telefonnummer))
    conn.commit()
    
def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnmmer: ")

    legg_til_person_i_db(fornavn, etternavn, telefonnummer,)

    print("{0}  {1} er registrert met telefonnummer {2}"
          .format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1": # input retunerer string, derfor "1"
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avslutte J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            conn.close()
            exit()
    else:
        nyttForsoek = input("Ugyldig valg. Velg et tall mellom 1-4: ")
        utfoerMenyvalg(nyttForsoek)

def sokPerson():
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. TIlbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake:  ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("Fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            tlfnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", tlfnummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print("Ugyldig valg. Velg et tall mellom 1-4:")
            sokPerson()


def finnPerson(typeSok, sokeTekst):
    if typeSok == "fornavn":
        cursor.execute("SELECT * FROM personer WHERE fornavn=?", (sokeTekst,))
    elif typeSok == "etternavn":
        cursor.execute("SELECT * FROM personer WHERE etternavn=?", (sokeTekst,))
    elif typeSok == "telefonnummer":
        cursor.execute("SELECT * FROM personer WHERE Telefonnummer=?", (sokeTekst,))

        resultater = cursor.fetchall()

        if not resultater:
            print("Finner ingen personer")
        else:
            for personer in resultater:
                print("{0} {1} har telefonummer {2}"
                    .format(personer[0], personer[1], personer[2]))
                
printMeny()