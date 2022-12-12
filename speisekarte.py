# Aufgabenblatt 5
# Aufgabe: 2. Die zweite Speisekarte
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
def speisekarteAnzeigen(karte):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(karte) > 0:

        print("\n----- Speisekarte -----")
        print(len(karte))
        foundKat = False
        for kat in kategorien:
            print(kat + ": ")
            for id, info in karte.items():
                if info["kategorie"] == kat:
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    foundKat = True
            if not foundKat:
                print("Noch kein Gericht in dieser Kategorie.")

    else:
        print("\nDie Speisekarte ist leer!")


# Methode um ein Gericht zur Speisekarte hinzuzufügen
def gerichtHinzufuegen(karte):
    # Abfrage des Namens
    neuesGericht = input("\nName des neuen Gerichts: ")
    # prüft, ob Eingabe leer ist
    if neuesGericht == "":
        pass
    else:
        # Abfrage des Preises
        neuesGerichtPreis = input("Preis des neuen Gerichts: ")
        # prüft, ob Eingabe leer ist
        if neuesGerichtPreis == "":
            pass
        else:
            while True:
                print("1: Vorspeisen\n2: Hauptspeisen\n3: Nachspeisen\n4: Getränke")
                neuesGerichtKategorie = input("Nummer der Kategorie: ")

                if neuesGerichtKategorie == "":
                    return karte

                if neuesGerichtKategorie != "1" and neuesGerichtKategorie != "2" and neuesGerichtKategorie != "3" and neuesGerichtKategorie != "4":
                    print("Keine bestehende Kategorie gewählt!\n")
                else:
                    lastKey = next(reversed(karte.keys()))
                    newItemKey = lastKey + 1
                    karte[newItemKey] = {}
                    karte[newItemKey]["gericht"] = neuesGericht
                    karte[newItemKey]["preis"] = neuesGerichtPreis
                    karte[newItemKey]["kategorie"] = kategorien[int(neuesGerichtKategorie) - 1]
                    return karte


# Methode um ein Gericht aus der Speisekarte zu löschen
def gerichtLoeschen(karte):
    if len(karte) > 0:

        while True:
            speisekarteAnzeigen(karte)
            deletInput = input("\nNummer des zu löschenden Elements eingeben: ")

            if deletInput == "":
                return karte

            for id, info in karte.items():
                if str(id) == deletInput:
                    del karte[id]
                    print(info["gericht"] + " erfolgreich gelöscht!")
                    return karte
            print("Kein Gericht mit der eingegebenen Nummer gefunden!")

    else:
        print("\nDie Speisekarte ist leer!")


# Methode um die aktualisierten Daten zurück in die Datei zu schreiben
def dateiSchreiben(karte, pfad):
    # versucht datei zum schreiben öffnen
    try:
        datei = open(pfad, mode="w")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datein in " + pfad + " konnte nicht gefunden werden!")
    # wenn datei geöffnet werden kann, wird die aktualisierte Speisekarte in die Textdatei geschrieben
    else:
        for id, info in karte.items():
            datei.write(info["gericht"] + ", " + info["preis"] + ", " + info["kategorie"] + "\n")
        # schließt datei und beendet die while-Schleife (beendet das Programm)
        datei.close()


# Methode um die Daten aus der Datei zu lesen
def dateiLesen(karte, pfad):
    # versucht datei zum lesen öffnen
    try:
        datei = open(pfad, mode="r")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datein in " + pfad + "konnte nicht gefunden werden!")
    # wenn datei geöffnet werden kann, wird das Programm weiter ausgeführt
    else:
        # formatiert den Inhalt der Datei
        counter = 1
        for i in datei:
            if not i.isspace():
                # entfernt \n am Ende einer Zeile
                i = i.rstrip()
                try:
                    # teilt jede Zeile in gericht und preis, wo ein "," ist
                    (gericht, preis, kategorie) = i.split(",")
                except:
                    print("Es wurden nicht valide Zeilen gefunden, welche nicht berücksichtigt werden!")
                # entfernt das Leerzeichen nach dem Komma
                preis = preis[1:]
                kategorie = kategorie[1:]

                kategorieValide = False
                for kat in kategorien:
                    if kategorie == kat:
                        kategorieValide = True

                if not kategorieValide:
                    print(gericht + " hat leider keine valide Kategorie und wird somit nicht berücksichtigt!")
                else:
                    # speichert die Speisekarte im dictionary speisekarte
                    karte[counter] = {}
                    karte[counter]["gericht"] = gericht
                    karte[counter]["preis"] = preis
                    karte[counter]["kategorie"] = kategorie
                    counter += 1


# ruft die Methode dateiLesen auf
dateiLesen(speisekarte, dateiPfad)

# Variabel zur Prüfung, ob Programm weiter ausgeführt werden soll
programmAusfuehren = True

# wird ausgeführt, solange das programm nicht beendet wird
while programmAusfuehren:
    # gibt das Hauptmenü auf der Konsole aus
    print(
        "\nHauptmenü:" + "\na = Speisekarte anzeigen" + "\nn = neues Gericht hinzufügen" + "\nl = Gericht löschen" + "\ne = Programmende" + "\n(Mit Enter können Sie jedes Menü wieder verlassen!)")
    # fragt Eingabe des gewünschten Menüs ab
    eingabe = input("\nBuchstaben eingeben um Menüpunkt zu wählen: ")

    # prüft, welches Menü gewählt wurde und führt die jeweilige Methode/Aktion aus
    if eingabe == "a":
        speisekarteAnzeigen(speisekarte)
    elif eingabe == "n":
        speisekarte = gerichtHinzufuegen(speisekarte)
    elif eingabe == "l":
        speisekarte = gerichtLoeschen(speisekarte)
    elif eingabe == "e":
        dateiSchreiben(speisekarte, dateiPfad)
        programmAusfuehren = False
    else:
        print("\nEingabe ungültig!")
