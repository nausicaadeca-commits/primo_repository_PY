class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni")


# Qui creo una persona e chiamo il metodo
p = Persona("Paperino", 12)
p.saluta()