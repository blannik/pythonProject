sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadej kód součástky: ")

if kod in sklad:
  pocet = int(input("Zadej požadované množství: "))
  if sklad[kod] < pocet:
    print(f'"Na skladě zbývá posledních {sklad[kod]} ks.')
    sklad.pop(kod)
  else:
    print("Zboží je skladem.")
    sklad[kod] -= pocet
else:
  print("Součástka není skladem.")