class Auto:
    def getInfo(self):
        return (f"{self.registration}, {self.type}, {self.km}")
    def __init__(self, registration, type, km, free=True):
        self.registration = registration
        self.type = type
        self.km = km
        self.free = free

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253, True)

print(peugeot.getInfo())



