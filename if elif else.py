# es. 1 Verifica se un numero è multiplo di 3 utilizzando l'operatore modulo.
n = 3
n2 = 10

if n2 % n == 0:
    print("il numero è multiplo di 3")
else: 
    print ("il numero non è multiplo di 3")

#es2 Controllo se il voto inserito è sufficiente (>= 18).

numero = 10

if numero >= 18:
    print("il voto è sufficente")
else:
    print("il voto è insufficente")

#es.3 Distingui se un carattere è una vocale o consonante tramite le strutture condizionali.

lettera = "a"

if lettera in ("a", "e", "i", "o", "u"):
    print("è una vocale")
else:
    print("è una consonante")

#es.4 Determina se un numero è positivo, negativo o zero.

n3 = -8

if n3 > 0:
    print("il numero è positivo")
elif n3 == 0:
    print("il numero è zero")
else:
    print("il numero è negativo")

#es.5 Trova il numero maggiore tra tre variabili.

c = 5
n = 9
t = 3

if c > n and c > t:
    print(f"il numero maggiore è {c}")
elif n > c and n > t:
    print(f"il numero maggiore è {n}")
else:
    print(f"il numero maggiore è {t}")

#es.6 Calcola il prezzo del biglietto in base all'età:

eta = 16

if eta < 12:
    print("il prezzo del biglietto è 5 euro")
elif eta <= 64:
    print("il prezzo del biglietto è 10 euro")
else:
    print("il prezzo del biglietto è 7 euro")

#es.7 Identifica se un triangolo è equilatero, isoscele, o scaleno basandoti sulle lunghezze dei suoi lati

l1 = 5
l2 = 5
l3 = 5

if l1 == l2 and l2 == l3:
    print("il triangolo è equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("il triangolo è isoscele")
else:
    print("il triangolo è scaleno")