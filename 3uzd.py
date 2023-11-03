"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""

class Dati:
    def __init__(self,vards,vecums,iem_summa):
        self.vards=vards
        self.vecums=vecums
        self.iem_summa=iem_summa

kkk=Dati("Pēteris", 20, 0.5)
        