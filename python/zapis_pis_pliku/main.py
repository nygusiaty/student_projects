print("Co chcesz zapisac?")
co = input()
print("podaj nazwe pliku")
nazwa_pliku = input()

def zapisz():
	with open(nazwa_pliku, "w") as plik:
		plik.write(co)

def odczytaj():
	with open(nazwa_pliku, "r") as plik:
		for linia in plik:
			print(linia.strip())

print("Zawartosc pliku:\n")
odczytaj()




