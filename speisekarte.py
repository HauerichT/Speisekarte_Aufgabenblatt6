# Aufgabenblatt 6
# Aufgabe: 3
# Name: Timo Haverich

# importiert das Modul os um den relativen Pfad ermitteln zu können
from os import path

# Deklaration der Speisekarte als dictionary
speisekarte = {}
kategorien = ["Vorspeisen", "Hauptspeisen", "Nachspeisen", "Getränke"]

# Speicherung des Dateipfades der Speisekarte
ordnerPfad = path.dirname(__file__)
dateiPfad = ordnerPfad + '/speisekarte.txt'


# Methode um die Speisekarte anzuzeigen
def printSpeisekarte(karte):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(karte) > 0:

        print("\n----- Speisekarte -----")
        countGerichte = 1
        for kat in kategorien:
            # gibt den Namen der Kategorie aus
            print(kat + ": ")
            # gibt die Elemente passend zur Kategorie aus
            for gericht, (preis, kategorie) in karte.items():
                if kategorie == kat:
                    print(str(countGerichte) + ": " + gericht + ", " + preis + "ct")
                    countGerichte += 1

    else:
        print("\nDie Speisekarte ist leer!")


# Methode um ein Gericht zur Speisekarte hinzuzufügen
def addGericht(karte):
    neuesGerichtName = ""
    neuesGerichtPreis = ""
    neuesGerichtKategorie = ""

    print("\n----- Neues Gericht hinzufügen -----")

    # get name of new product
    runGetName = True
    while runGetName:
        neuesGerichtName = input("Name: ")
        if neuesGerichtName == "":
            return karte

        for gericht, (preis, kategorie) in karte.items():
            if neuesGerichtName == gericht:
                print("Gericht mit gleichem Namen gibt es bereits!")
                return karte

        runGetName = False

    # get price of new product
    runGetPrice = True
    while runGetPrice:
        neuesGerichtPreis = input("Preis: ")
        if neuesGerichtPreis == "":
            return karte

        if not neuesGerichtPreis.isnumeric():
            print("Preis muss eine Zahl sein!")
        else:
            runGetPrice = False

    # get category of new product
    runGetCategory = True
    while runGetCategory:
        print("1: Vorspeisen\n2: Hauptspeisen\n3: Nachspeisen\n4: Getränke")

        neuesGerichtKategorie = input("Nummer der Kategorie: ")

        # prüft, ob Eingabe leer ist
        if neuesGerichtKategorie == "":
            return karte

        # prüft, ob Eingabe zu Kategorie passt
        if neuesGerichtKategorie == "1":
            neuesGerichtKategorie = kategorien[0]
            runGetCategory = False
        elif neuesGerichtKategorie == "2":
            neuesGerichtKategorie = kategorien[1]
            runGetCategory = False
        elif neuesGerichtKategorie == "3":
            neuesGerichtKategorie = kategorien[2]
            runGetCategory = False
        elif neuesGerichtKategorie == "4":
            neuesGerichtKategorie = kategorien[3]
            runGetCategory = False
        else:
            print("Keine bestehende Kategorie gewählt!")

    # add new data
    karte[neuesGerichtName] = (neuesGerichtPreis, neuesGerichtKategorie)
    print(neuesGerichtName + " hinzugefügt!")
    return karte


# Methode um ein Gericht aus der Speisekarte zu löschen
def removeGericht(karte):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(karte) > 0:

        runGetDeleteNumber = True
        while runGetDeleteNumber:

            printSpeisekarte(karte)

            # Abfrage des zu löschenden Elements
            inputRemove = input("\nNummer des zu löschenden Elements eingeben: ")

            # prüft, ob Eingabe leer ist
            if inputRemove == "":
                return karte

            if inputRemove.isnumeric() and len(karte) >= int(inputRemove) > 0:
                counter = 1
                for gericht, (preis, kategorie) in karte.items():
                    if int(inputRemove) == counter:
                        del karte[gericht]
                        print(gericht + " gelöscht!")
                        return karte
                    counter += 1
            else:
                print("Falsche Eingabe!")

    else:
        print("\nDie Speisekarte ist leer!")


# Methode um die aktualisierten Daten zurück in die Datei zu schreiben
def writeDatei(karte, pfad):
    # versucht datei zum Schreiben öffnen
    try:
        datei = open(pfad, mode="w")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datei in " + pfad + " konnte nicht gefunden werden!")
    # wenn datei geöffnet werden kann, wird die aktualisierte Speisekarte in die Textdatei geschrieben
    else:
        for gericht, (preis, kategorie) in karte.items():
            datei.write(gericht + ", " + preis + ", " + kategorie + "\n")
        # schließt datei und beendet die while-Schleife (beendet das Programm)
        datei.close()


# Methode um die Daten aus der Datei zu lesen
def readDatei(karte, pfad):
    # versucht datei zum Lesen zu öffnen
    try:
        datei = open(pfad, mode="r")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datei in " + pfad + "konnte nicht gefunden werden!")
    # wenn datei geöffnet werden kann, wird das Programm weiter ausgeführt
    else:
        for i in datei:
            # formatiert den Inhalt der Datei
            if not i.isspace():
                # entfernt \n am Ende einer Zeile
                i = i.rstrip()
                try:
                    # teilt jede Zeile in gericht und preis, wo ein "," ist
                    (gericht, preis, kategorie) = i.split(",")
                # wirft Fehler, wenn Zeilen nicht valide sind
                except:
                    print(i + " = nicht valide Zeile! Diese wird nicht berücksichtigt")

                # entfernt das Leerzeichen nach dem Komma
                preis = preis[1:]
                kategorie = kategorie[1:]

                # speichert die Speisekarte im dictionary speisekarte
                karte[gericht] = (preis, kategorie)


# ruft die Methode readDatei auf, um die Datei einzulesen
readDatei(speisekarte, dateiPfad)

# Variabel zur Prüfung, ob Programm weiter ausgeführt werden soll
run = True

# wird ausgeführt, solange das programm nicht beendet wird
while run:
    # gibt das Hauptmenü auf der Konsole aus
    print(
        "\nHauptmenü:" + "\na = Speisekarte anzeigen" + "\nn = neues Gericht hinzufügen" + "\nl = Gericht löschen" + "\ne = Programmende" + "\n(Mit Enter können Sie jedes Menü wieder verlassen!)")

    # fragt Eingabe des gewünschten Menüs ab
    eingabe = input("\nBuchstaben eingeben um Menüpunkt zu wählen: ")

    # prüft, welches Menü gewählt wurde und führt die jeweilige Methode/Aktion aus
    if eingabe == "a":
        printSpeisekarte(speisekarte)
    elif eingabe == "n":
        speisekarte = addGericht(speisekarte)
    elif eingabe == "l":
        speisekarte = removeGericht(speisekarte)
    elif eingabe == "e":
        writeDatei(speisekarte, dateiPfad)
        run = False
    else:
        print("\nEingabe ungültig!")
