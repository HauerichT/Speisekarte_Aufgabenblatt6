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

        countGerichte = 0
        for kat in kategorien:
            # gibt den Namen der Kategorie aus
            print(kat + ": ")
            # gibt die Elemente passend zur Kategorie aus
            for id, info in karte.items():
                if info["kategorie"] == kat:
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    countGerichte += 1

            # prüft ob Kategorie leer ist
            if countGerichte == 0:
                print("Keine Gerichte in dieser Kategorie!")
            else:
                countGerichte = 0

    else:
        print("\nDie Speisekarte ist leer!")


# Methode um ein Gericht zur Speisekarte hinzuzufügen
def addGericht(karte):
    # Abfrage des Namens
    neuesGerichtName = input("\nName des neuen Gerichts: ")
    # prüft, ob Eingabe leer ist
    if neuesGerichtName == "":
        pass
    else:
        # Abfrage des Preises
        neuesGerichtPreis = input("Preis des neuen Gerichts: ")
        # prüft, ob Eingabe leer ist
        if neuesGerichtPreis == "":
            pass
        else:
            # Abfrage der Kategorie, bis Methode returnt wird
            while True:
                print("1: Vorspeisen\n2: Hauptspeisen\n3: Nachspeisen\n4: Getränke")

                neuesGerichtKategorie = input("Nummer der Kategorie: ")

                # prüft, ob Eingabe leer ist
                if neuesGerichtKategorie == "":
                    return karte

                # prüft, ob Eingabe zu Kategorie passt
                if neuesGerichtKategorie != "1" and neuesGerichtKategorie != "2" and neuesGerichtKategorie != "3" and neuesGerichtKategorie != "4":
                    print("Keine bestehende Kategorie gewählt!\n")
                else:
                    # fügt neues Gericht hinzu
                    lastKey = list(karte)[-1]
                    newItemKey = lastKey + 1
                    karte[newItemKey] = {}
                    karte[newItemKey]["gericht"] = neuesGerichtName
                    karte[newItemKey]["preis"] = neuesGerichtPreis
                    karte[newItemKey]["kategorie"] = kategorien[int(neuesGerichtKategorie) - 1]
                    print(neuesGerichtName + " hinzugefügt!")
                    return karte


# Methode um ein Gericht aus der Speisekarte zu löschen
def removeGericht(karte):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(karte) > 0:

        # Abfrage des zu löschenden Gerichts, bis Methode returnt wird
        while True:
            # zeigt Speisekarte
            printSpeisekarte(karte)

            # Abfrage des zu löschenden Elements
            removeEingabe = input("\nNummer des zu löschenden Elements eingeben: ")

            # prüft, ob Eingabe leer ist
            if removeEingabe == "":
                return karte

            # sucht das zu löschende Element und entfernt es aus Karte
            for id, info in karte.items():
                if str(id) == removeEingabe:
                    del karte[id]
                    print(info["gericht"] + " erfolgreich gelöscht!")
                    return karte
            print("Kein Gericht mit der eingegebenen Nummer gefunden!")

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
        for id, info in karte.items():
            datei.write(info["gericht"] + ", " + info["preis"] + ", " + info["kategorie"] + "\n")
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
        counter = 1
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
                karte[counter] = {}
                karte[counter]["gericht"] = gericht
                karte[counter]["preis"] = preis
                karte[counter]["kategorie"] = kategorie
                counter += 1


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
