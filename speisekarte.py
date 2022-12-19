"""
Aufgabe: Speisekarte
Name: Timo Haverich
"""

from os import path

# Dateipfad
folderPath = path.dirname(__file__)
filePath = folderPath + '/speisekarte.txt'

# Speisekarte
menu = []


# Methode gibt die aktuelle Speisekarte auf der Konsole aus
def printMenu(_menu, _heading="Speisekarte"):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(_menu) > 0:
        print("\n----- " + _heading + " -----")

        # gibt die Elemente der Kategorie "Vorspeisen" aus
        print("Vorspeisen:")
        for i in range(len(_menu)):
            for j in range(len(_menu[i])):
                if _menu[i][j] == "Vorspeisen":
                    print(str(_menu.index(_menu[i])) + ": " + _menu[i][0] + ", " + _menu[i][1] + "ct")

        # gibt die Elemente der Kategorie "Hauptspeisen" aus
        print("Hauptspeisen:")
        for i in range(len(_menu)):
            for j in range(len(_menu[i])):
                if _menu[i][j] == "Hauptspeisen":
                    print(str(_menu.index(_menu[i])) + ": " + _menu[i][0] + ", " + _menu[i][1] + "ct")

        # gibt die Elemente der Kategorie "Nachspeisen" aus
        print("Nachspeisen:")
        for i in range(len(_menu)):
            for j in range(len(_menu[i])):
                if _menu[i][j] == "Nachspeisen":
                    print(str(_menu.index(_menu[i])) + ": " + _menu[i][0] + ", " + _menu[i][1] + "ct")

        # gibt die Elemente der Kategorie "Getränke" aus
        print("Getränke:")
        for i in range(len(_menu)):
            for j in range(len(_menu[i])):
                if _menu[i][j] == "Getränke":
                    print(str(_menu.index(_menu[i])) + ": " + _menu[i][0] + ", " + _menu[i][1] + "ct")

    else:
        print("\nDie Speisekarte ist leer!")


# Methode ändert Attribute eines Elementes der Speisekarte
def changeElement(_menu):
    # gibt zunächst die Speisekarte aus
    printMenu(_menu, _heading="Gericht ändern")

    # speichert das zu ändernde Element
    changingElement = None
    # speichert das zu ändernde Attribut
    changingAttribute = None

    # fragt das zu ändernde Element ab
    runGetElement = True
    while runGetElement:
        inputChange = input("\nNummer der Speise: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if inputChange == "":
            return _menu
        # prüft, ob die Eingabe valide ist
        if inputChange.isnumeric() and len(_menu) > int(inputChange) >= 0:
            changingElement = int(inputChange)
            runGetElement = False
        else:
            print("Nummer gibt es nicht!")

    # fragt das zu ändernde Attribut ab
    runGetAttribute = True
    while runGetAttribute:
        print(_menu[changingElement][0] + " wird bearbeitet.\n\n1: Name\n2: Preis\n3: Kategorie")
        inputAttribute = input("Nummer des zu ändernden Attributs: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if inputAttribute == "":
            return _menu
        # prüft, ob die Eingabe valide ist
        if inputAttribute.isnumeric() and 3 >= int(inputAttribute) > 0:
            changingAttribute = int(inputAttribute)
            runGetAttribute = False
        else:
            print("Attribut gibt es nicht!")

    # ändert den Namen
    if changingAttribute == 1:
        # fragt den neuen Namen ab
        newName = input("Umbenennen in: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if newName == "":
            return _menu
        # setzt den neuen Namen
        _menu[changingElement][0] = newName
        print("Name von " + _menu[changingElement][0] + " geändert.")
        return _menu

    # ändert den Preis
    if changingAttribute == 2:
        while True:
            # fragt den neuen Preis ab
            newPrice = input("Neuer Preis: ")
            # prüft, ob in das Hauptmenü zurückgekehrt werden soll
            if newPrice == "":
                return _menu
            # prüft, ob Eingabe eine Zahl ist und setzt ggf. den neuen Preis
            if newPrice.isnumeric():
                _menu[changingElement][1] = newPrice
                print("Preis von " + _menu[changingElement][0] + " geändert.")
                return _menu
            else:
                print("Preis muss eine Zahl sein!")

    # ändert die Kategorie
    if changingAttribute == 3:
        while True:
            print("\n1: Vorspeisen\n2: Hauptspeisen\n3: Nachspeisen\n4: Getränke")
            # fragt die neue Kategorie ab
            newCategory = input("Neue Kategorie: ")
            # prüft, ob in das Hauptmenü zurückgekehrt werden soll
            if newCategory == "":
                return _menu
            # ändert die Kategorie je nach Eingabe
            if newCategory == "1":
                _menu[changingElement][2] = "Vorspeisen"
                print("Kategorie von " + _menu[changingElement][0] + " geändert.")
                return _menu
            elif newCategory == "2":
                _menu[changingElement][2] = "Hauptspeisen"
                print("Kategorie von " + _menu[changingElement][0] + " geändert.")
                return _menu
            elif newCategory == "3":
                _menu[changingElement][2] = "Nachspeisen"
                print("Kategorie von " + _menu[changingElement][0] + " geändert.")
                return _menu
            elif newCategory == "4":
                _menu[changingElement][2] = "Getränke"
                print("Kategorie von " + _menu[changingElement][0] + " geändert.")
                return _menu
            else:
                print("Eingabe ungültig!")


# Methode fügt ein Element zur Speisekarte hinzu
def addElement(_menu):

    newElementName = None
    newElementPrice = None
    newElementCategory = None

    print("\n----- Neues Gericht hinzufügen -----")

    # fragt den Namen des neuen Elementes ab
    runGetName = True
    while runGetName:
        # fragt Namen ab
        newElementName = input("Name: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if newElementName == "":
            return _menu
        # prüft, ob es bereits ein Element mit den gleichen Namen gibt
        for i in range(len(_menu)):
            for j in range(len(_menu[i])):
                if newElementName == _menu[i][0]:
                    print("Gericht mit gleichem Namen gibt es bereits!")
        runGetName = False

    # fragt den Preis des neuen Elementes ab
    runGetPrice = True
    while runGetPrice:
        # fragt Preis ab
        newElementPrice = input("Preis: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if newElementPrice == "":
            return _menu
            # prüft, ob Preis eine Zahl ist
        if not newElementPrice.isnumeric():
            print("Preis muss eine Zahl sein!")
        else:
            runGetPrice = False

    # fragt die Kategorie des neuen Elementes ab
    runGetCategory = True
    while runGetCategory:
        # gibt die verfügbaren Kategorien aus
        print("1: Vorspeisen\n2: Hauptspeisen\n3: Nachspeisen\n4: Getränke")
        # fragt die Kategorie ab
        newElementCategory = input("Nummer der Kategorie: ")
        # prüft, ob in das Hauptmenü zurückgekehrt werden soll
        if newElementCategory == "":
            return _menu
            # prüft, ob Eingabe zu Kategorie passt
        if newElementCategory == "1":
            newElementCategory = "Vorspeisen"
            runGetCategory = False
        elif newElementCategory == "2":
            newElementCategory = "Hauptspeisen"
            runGetCategory = False
        elif newElementCategory == "3":
            newElementCategory = "Nachspeisen"
            runGetCategory = False
        elif newElementCategory == "4":
            newElementCategory = "Getränke"
            runGetCategory = False
        else:
            print("Keine bestehende Kategorie gewählt!\n")

    # add new data
    _menu.append([newElementName, newElementPrice, newElementCategory])
    print(newElementName + " hinzugefügt!")
    return _menu


# Methode löscht ein Element von der Speisekarte
def removeElement(_menu):
    # prüft, ob die Speisekarte Inhalt besitzt
    if len(_menu) > 0:
        while True:
            # gibt die Speisekarte aus
            printMenu(_menu, _heading="Gericht löschen")
            # fragt das zu löschende Element ab
            inputRemove = input("\nNummer des zu löschenden Elements eingeben: ")
            # prüft, ob in das Hauptmenü zurückgekehrt werden soll
            if inputRemove == "":
                return _menu
                # prüft, ob die Eingabe valide ist und löscht das Element
            if inputRemove.isnumeric() and len(_menu) > int(inputRemove) >= 0:
                index = int(_menu.index(_menu[int(inputRemove)]))
                print(_menu[index][0] + " gelöscht!")
                del _menu[index]
                return _menu
            else:
                print("Falsche Eingabe!")

    else:
        print("\nDie Speisekarte ist leer!")


# Methode schreibt die Speisekarte in die Datei zurück
def writeFile(_menu, _path):
    # versucht Datei zum Schreiben zu öffnen
    try:
        file = open(_path, mode="w")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datei in " + _path + " konnte nicht gefunden werden!")
    # wenn datei geöffnet werden kann, wird die aktualisierte Speisekarte in die Textdatei geschrieben
    else:
        for i in range(len(_menu)):
            file.write(_menu[i][0] + ", " + _menu[i][1] + ", " + _menu[i][2] + "\n")
        # schließt Datei
        file.close()


# Methode liest Daten aus Speisekartendatei aus
def readFile(_menu, _path):
    # versucht Datei zum Lesen zu öffnen
    try:
        file = open(_path, mode="r")
    # wirft Fehler, wenn Datei nicht geöffnet werden kann
    except FileNotFoundError:
        print("Die Datei in " + _path + "konnte nicht gefunden werden!")
    # wenn Datei geöffnet werden kann, wird das Programm weiter ausgeführt
    else:
        for i in file:
            # formatiert den Inhalt der Datei
            if not i.isspace():
                # entfernt \n am Ende einer Zeile
                i = i.rstrip()
                try:
                    # teilt jede Zeile in gericht und preis, wo ein "," ist
                    (name, price, category) = i.split(",")
                # wirft Fehler, wenn Zeilen nicht valide sind
                except:
                    print(i + " = nicht valide Zeile! Diese wird nicht berücksichtigt")

                # entfernt das Leerzeichen nach dem Komma
                price = price[1:]
                category = category[1:]

                # speichert die Speisekarte im dictionary speisekarte
                _menu.append([name, price, category])
    return _menu


# ruft die Methode readDatei auf, um die Datei einzulesen
menu = readFile(menu, filePath)
# Variabel zur Prüfung, ob Programm weiter ausgeführt werden soll
run = True
# wird ausgeführt, solange das programm nicht beendet wird
while run:
    # gibt das Hauptmenü auf der Konsole aus
    print("\n----- Hauptmenü -----")
    print("a = Speisekarte anzeigen" + "\nn = neues Gericht hinzufügen" + "\nl = Gericht löschen" + "\nc = Gericht ändern" + "\ne = Programmende")
    # fragt Eingabe des gewünschten Menüs ab
    inputMenu = input("\nBuchstaben eingeben um Menüpunkt zu wählen: ")
    # prüft, welches Menü gewählt wurde und führt die jeweilige Methode/Aktion aus
    if inputMenu == "a":
        printMenu(menu)
    elif inputMenu == "n":
        menu = addElement(menu)
    elif inputMenu == "l":
        menu = removeElement(menu)
    elif inputMenu == "c":
        menu = changeElement(menu)
    elif inputMenu == "e":
        writeFile(menu, filePath)
        run = False
    else:
        print("\nEingabe ungültig!")
