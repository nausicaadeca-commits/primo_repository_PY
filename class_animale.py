class Animale:
    pass

class Cane(Animale):
    pass

# crea l'oggetto
mio_cane = Cane()

# controlli isinstance
print(isinstance(mio_cane, Cane))      # True
print(isinstance(mio_cane, Animale))   # True
print(isinstance(mio_cane, str))       # False