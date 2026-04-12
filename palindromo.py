frase = "ciao mondo"

# 1️⃣ Invertire l'ordine delle parole
parole = frase.split(" ")
parole_invertite = parole[::-1]
frase_invertita = " ".join(parole_invertite)

print("Parole invertite:", frase_invertita)

# 2️⃣ Controllo palindromo 
frase_pulita = frase.lower().replace(" ", "")
frase_al_contrario = frase_pulita[::-1]

if frase_pulita == frase_al_contrario:
    print("La frase è un palindromo")
else:
    print("La frase NON è un palindromo")
