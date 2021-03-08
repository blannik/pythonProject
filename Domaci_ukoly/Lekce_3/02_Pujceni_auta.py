class Auto:
    def getInfo(self):
        return (f"{self.registration}, {self.type}, {self.km}")
    def __init__(self, registration, type, km, zapujcka=True):
        self.registration = registration
        self.type = type
        self.km = km
        self.zapujcka = zapujcka
    def pujc_auto(self):
        if self.zapujcka==True:
            return(f"Potvrzuji zapůjčení vozidla.")
            self.zapujcka = false
        else:
            return(f"Vozidlo není k dispozici.")

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253, True)

zapujcka = input("Jakou značku vozidla si přejete zapůjčit: peugeot/skoda?")

pujc_auto(self.zapujcka)


