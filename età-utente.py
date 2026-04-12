def chat():  # FUNZIONE principale della chat
    print("Ciao! Scrivi la tua età e ti dirò il doppio😊")
    
    eta_testo = input("età: ")
    eta_numero = int(eta_testo)
    
    doppio = eta_numero * 2
    
    print(f"il doppio della tua età è {doppio}")

chat()
