# Aufgabenblatt 5
# Aufgabe: 2. Die zweite Speisekarte
# Name: Timo Haverich

# importiert das Modul os um den relativen Pfad ermitteln zu können
from os import path

# Deklaration der Speisekarte als dictionary
speisekarte = {}

# Speicherung des Dateipfades der Speisekarte
ordnerPfad = path.dirname(__file__)
dateiPfad = ordnerPfad + '/speisekarte.txt'


# Methode um die Speisekarte anzuzeigen
def speisekarteAnzeigen(karte):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(karte) > 0:

        print("\n----- Speisekarte -----")

        # printet die Vorspeisen
        print("Vorspeisen:")
        vorspeiseExists = False
        for id, info in karte.items():
            for key in info:
                if key == "kategorie" and info[key] == "Vorspeise":
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    vorspeiseExists = True
        if not vorspeiseExists:
            print("Noch keine Vorspeise hinzugefügt.")

        print()

        # printet die Hauptspeisen
        print("Hauptspeisen:")
        hauptspeiseExists = False
        for id, info in karte.items():
            for key in info:
                if key == "kategorie" and info[key] == "Hauptspeise":
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    hauptspeiseExists = True
        if not hauptspeiseExists:
            print("Noch keine Hauptspeise hinzugefügt.\n")

        print()

        # printet die Nachspeisen
        print("Nachspeisen:")
        nachspeiseExists = False
        for id, info in karte.items():
            for key in info:
                if key == "kategorie" and info[key] == "Nachspeise":
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    nachspeiseExists = True
        if not nachspeiseExists:
            print("Noch keine Nachspeise hinzugefügt.\n")

        print()

        # printet die Getränke
        print("Getränke:")
        getraenkExists = False
        for id, info in karte.items():
            for key in info:
                if key == "kategorie" and info[key] == "Getränk":
                    print(str(id) + ": " + info["gericht"] + ", " + info["preis"] + "ct")
                    getraenkExists = True
        if not getraenkExists:
            print("Noch kein Getränk hinzugefügt.\n")

    else:
        print("\nDie Speisekarte ist leer!")


def kategorieCheck(karte):
    # Abfrage des Preises
    print("1: Vorspeise\n2: Hauptspeise\n3: Nachspeise\n4: Getränk")
    inputKategorie = input("Nummer der Kategorie: ")

    if inputKategorie == "":
        return ""

    if inputKategorie == "1" or inputKategorie == "2" or inputKategorie == "3" or inputKategorie == "4":
        return inputKategorie
    else:
        print("Keine bestehende Kategorie gewählt!\n")
        kategorieCheck(karte)


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
            neuesGerichtKategorie = kategorieCheck(karte)
            if neuesGerichtKategorie == "":
                pass
            else:
                print("super")
    return karte


# Methode um ein Gericht aus der Speisekarte zu löschen
def gerichtLoeschen(karte):
    if len(karte) > 0:
        speisekarteAnzeigen(karte)
        # fragt das zu löschende Gericht ab
        eingabeNummer = input("\nNummer des zu löschenden Elements eingeben: ")

        for id, info in karte.items():
            if id == int(eingabeNummer):
                del karte[id]
                print("Gericht gelöscht!")
                return karte

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
        for speise, preis in karte.items():
            datei.write(str(speise) + ", " + str(preis) + "\n")
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
                # teilt jede Zeile in gericht und preis wo ein "," ist
                (gericht, preis, kategorie) = i.split(",")
                # entfernt das Leerzeichen nach dem Komma
                preis = preis[1:]
                kategorie = kategorie[1:]
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
