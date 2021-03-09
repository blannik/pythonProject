cislo = input("Zadej telefonní číslo, na které chceš zaslat zprávu: ")
cislo = cislo.replace(" ", "")

if len(cislo) == 9 or len(cislo) == 13:
    format = True

else:
    format = False
    print(f"Číslo {cislo} není v platném formátu.")

zprava = input("Napiš zprávu: ")
print(len(zprava))
cena = int((1 + len(zprava)//180) * 3)

print(f"Cena zprávy je {cena} Kč.")