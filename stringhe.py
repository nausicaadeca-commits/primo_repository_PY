#esercizio 1
#Estrarre Primo e Ultimo Carattere:
testo = "python"

print("primo carattere" , testo[0])
print("ultimo carattere" , testo[-1])

#esercizio 2
#Convertire in Maiuscolo e Minuscolo:

testo = "giOcAttOlo"

print(testo.upper())
print(testo.lower())

#esercizio 3
# Contare Occorrenze di una Lettera:

testo = "anatra"

lettera = "a"
conteggio = testo.count(lettera)
print(f"la lettera '{lettera}' viene ripetuta {conteggio}")

#esercizio 4
# Verificare Inizio e Fine di una Parola:

testo = "favola"

print(testo.startswith("f"))
print(testo.endswith("a"))

#esercizio 5
# Invertire una Stringa:

parola1 = "cielo"

print(parola1 [::-1])

#esercizio 6
# Rimuovere Spazi Iniziali e Finali:

testo1 = "       ciao        "

print(testo1.strip())

#esercizio 7
# Ripetere le Prime Tre Lettere:

parola = "mondo"
print(parola [:3]*3)
