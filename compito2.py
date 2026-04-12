class Animali:
    pass

lista = ["Cane", "Gatto", "pesce"]
lista[1] = "anatra"
lista.insert(1, 50)
lista.remove("Cane")

tupla = tuple(lista)

lista.remove("pesce")

for l in lista:
    print(l)
    print(tupla)

#print(lista)