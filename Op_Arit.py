#Chiede all'utente quanti euro ha. 
#Chiede il prezzo di un singolo oggetto. 
#Usa // per calcolare quante unità può comprare.
#Usa % per calcolare quanti euro restano

import math
euro_utente = input("quanti euro hai?")
euro = int(euro_utente)

prezzo_oggetto = input("quanto è il prezzo di un oggetto?")
prezzo = int(prezzo_oggetto)

unita = euro // prezzo

resti = euro % prezzo

print(f"puoi comprare {unita} oggetti")

print(f"ti restano {resti} euro")