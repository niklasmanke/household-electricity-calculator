from Stromverbrauchsrechner.stromverbrauchsrechner import stromverbrauch, berechne_gesamtverbrauch

def test_normaler_verbrauch():
    assert stromverbrauch(100, 5, 20) == 10

def test_keine_nutzung():
    assert stromverbrauch(200, 0, 30) == 0

def test_keine_leistung():
    assert stromverbrauch(0, 10, 30) == 0

def test_dezimalverbrauch():
    assert stromverbrauch(75,3,30) == 6.75

def test_gesamtverbrauch():
    geraete = [
        {"name": "Kühlschrank", "verbrauch": 30},
        {"name": "Fernseher", "verbrauch": 15},
        {"name": "Laptop", "verbrauch": 10}
    ]
    assert berechne_gesamtverbrauch(geraete) == 55

def test_leere_geraeteliste():
    assert berechne_gesamtverbrauch([]) == 0

def test_gesamtverbrauch_dezimal():
    geraete = [
        {"name": "Laptop", "verbrauch": 2.5},
        {"name": "Fernseher", "verbrauch": 3.2},
        {"name": "Kühlschrank", "verbrauch": 10.8}
    ]

    assert berechne_gesamtverbrauch(geraete) == 16.5

