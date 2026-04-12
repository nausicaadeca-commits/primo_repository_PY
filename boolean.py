eta_testo = input("Quanti anni hai? ")
eta = int(eta_testo)

patente_testo = input("Hai la patente? (si/no) ")

puo_guidare = (eta >= 18) and (patente_testo == "si")

print(puo_guidare)
