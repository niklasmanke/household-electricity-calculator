# 1. Bibliotheken importieren
import csv
import matplotlib.pyplot as plt #Bibliothek für die Diagramme
# 2. Funktionen definieren
def stromverbrauch(leistung,stunden,tage):
    Emonat = ((leistung*stunden*tage)/1000)
    return Emonat
def kosten(verbrauch,preis):
    stromkosten=verbrauch*preis
    return stromkosten
def berechne_gesamtverbrauch(geraete):
    gesamtverbrauch=0
    for geraet in geraete:
        gesamtverbrauch += geraet["verbrauch"]
    return gesamtverbrauch
def finde_maximum(geraete):
    peak=0
    peak_name=""
    for geraet in geraete:
        if geraet["verbrauch"]>peak:
            peak=geraet["verbrauch"]
            peak_name=geraet["name"]
    return peak_name,peak
def finde_minimum(geraete):
    minimum=geraete[0]["verbrauch"]
    minimum_name=geraete[0]["name"]#Müssen wir hier so machen weil geraet noch gar nicht definiert ist
    for geraet in geraete:
        if geraet["verbrauch"]<minimum:
            minimum=geraet["verbrauch"]
            minimum_name=geraet["name"]
    return minimum_name,minimum
def zeige_auswertung(geraete,preis_kwh):
    if len(geraete)<1:
        print("Keine Geräte vorhanden.")
        return
    gesamtverbrauch = berechne_gesamtverbrauch(geraete)
    maximum_name, maximum = finde_maximum(geraete)
    minimum_name, minimum = finde_minimum(geraete)
    #Jetzt werden die Ergebnisse präsentiert
    print("--- Stromverbrauchsauswertung ---")
    print(f"Gesamtverbrauch: {gesamtverbrauch:.2f} kWh")
    if gesamtverbrauch == 0:
        print("Der Gesamtverbrauch begträgt 0 kWh.")
    else:
        for geraet in geraete:
            anteil=(geraet["verbrauch"]/gesamtverbrauch)*100
            print(f"Das Gerät {geraet["name"]} verbraucht {anteil:.2f} % des Gesamtverbrauches.")
    for geraet in geraete:
        print("Gerät:",geraet["name"])
        print(f'Verbrauch: {geraet["verbrauch"]:.2f} kWh')
        print(f'Kosten: {kosten(geraet["verbrauch"],preis_kwh):.2f} €')
    print(f"Größter Stromverbraucher: {maximum_name} mit {maximum:.2f} kWh")
    print(f"Kleinster Stromverbraucher: {minimum_name} mit {minimum:.2f} kWh")
    monatskosten=kosten(gesamtverbrauch,preis_kwh)
    print(f"Die monatlichen Kosten betragen:{monatskosten:.2f}€")
def zeige_diagramm(geraete):
    namen=[]
    verbraeuche=[]
    for geraet in geraete:
        namen.append(geraet["name"])
        verbraeuche.append(geraet["verbrauch"])
    #erstes Balkendiagramm
    plt.figure(figsize=(10,5))#die ersten beiden müssen am anfang sein weil sie das Diagramm kreieren
    plt.bar(namen,verbraeuche)#erstes Argument x-Achse, zweites y-Achse
    plt.title("Stromverbauch nach Gerät")
    plt.xlabel("Gerät")
    plt.ylabel("Verbrauch in kWh")
    plt.show()

def speichere_geraete(geraete,preis_kwh):
        with open("stromverbrauch.csv", "w", newline="", encoding="utf-8") as datei:
            writer = csv.writer(datei)
            writer.writerow(["Gerät","Verbrauch","Kosten"])
            for geraet in geraete:
                writer.writerow([geraet["name"],geraet["verbrauch"],round(kosten(geraet["verbrauch"],preis_kwh)),2])

def einlesen_geraete():
    geraete=[]
    #Jetzt lesen wir die Zeilen aus der CSV-Datei aus
    try:
        with open("stromverbrauch.csv", "r", encoding="utf-8") as datei:
            reader = csv.reader(datei)
            next(reader) #Überspringt die Überschriften

            for zeile in reader:
                geraet = {"name":zeile[0],"verbrauch":float(zeile[1])}
                geraete.append(geraet)
    except FileNotFoundError: #Sodass in der ersten Iteration kein Fehler hochkommt weil noch keine CSV-Datei existiert
        print("Noch keine gespeicherten Geräte vorhanden.")
    return geraete

def geraet_hinzufuegen(geraete):
    try:#Jetzt fragen wir die Geräte und dessen Leistung und Nutzungsdauer ab
            name=input("Name des Geräts:")
            leistung=float(input("Leistung in Watt:"))
            stunden=float(input("Nutzungsdauer pro Tag in Stunden:"))
            tage=float(input("Anzahl der Tage:"))
    except ValueError:
        print("Bitte eine Zahl eingeben:")
        return
    if leistung<0 or stunden<0 or tage<0:
        print("Bitte positive Werte eingeben:")
        return

    monatsverbrauch=stromverbrauch(leistung,stunden,tage)
    geraet= {"name":name,"verbrauch":monatsverbrauch}
    geraete.append(geraet)
def geraet_loeschen(geraete):
    anzahl_vorher = len(geraete)
    loeschen = input("Welches Gerät möchtest du löschen?")
    neue_liste=[]
    for geraet in geraete:
        if geraet["name"] != loeschen:
            neue_liste.append(geraet)
    if anzahl_vorher == len(neue_liste):
        print("Gerät nicht gefunden.")
    else:
        print("Gerät wurde entfernt.")
    return neue_liste

verbrauchswerte=[]
gesamtverbrauch=0
# 3. Hauptprogramm
def main():
    preis_kwh=0.35
    geraete = einlesen_geraete()
    while True:
        print("--- STROMVERBRAUCHSRECHNER ---")#Programm benutzerfreundlich machen
        print("1 - Neues Gerät hinzufügen")
        print("2 - Verbrauchsauswertung anzeigen")
        print("3 - Diagramm anzeigen")
        print("4 - Programm beenden")
        print("5 - Gerät löschen")
        antwort=input("Meine Auswahl:")
        if antwort == "1":
            geraet_hinzufuegen(geraete)
        elif antwort=="2":
            zeige_auswertung(geraete,preis_kwh)
        elif antwort=="3":
            zeige_diagramm(geraete)
        elif antwort=="4":#Alle Geräte dauerhaft in der CSV-Datei speichern
            speichere_geraete(geraete,preis_kwh)
            break
        elif antwort == "5":
            geraete = geraet_loeschen(geraete)
        else:
            print("Die Eingabe muss eine Zahl von 1 bis 5 sein.")

if __name__ == "__main__":
    main()