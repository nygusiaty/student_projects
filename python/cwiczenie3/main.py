tablica = []

for i in range(1, 4):
	liczba = int(input("Podaj " + str(i) + " liczbe:"))
	tablica.append(liczba)
suma = 0
for element in tablica:
	suma += element

print("wynik: " + str(suma))

if suma <= 0:
	print("Tablica jest pusta")

if suma % 2 == 0:
	print("Liczba jest parzysta")
