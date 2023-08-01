#Program: Implementing concepts of inheritance
#This is Multilevel inheritance:
class Subparticles:
    pass
class Atoms(Subparticles):
    pass
class Molecules(Atoms):
    pass
class Allotropes(Molecules):
    pass

#Objects of class Subparticles:
electron= Subparticles()
proton= Subparticles()
neutron= Subparticles()

#Objects of class Atoms:
Oxygen= Atoms()
Nitrogen= Atoms()
Carbon= Atoms()

#Objects of class Molecules:
O3= Molecules()
N2= Molecules()
C60= Molecules()

#Objects of class Allotropes:
Ozone= Allotropes()
NitrogenGas= Allotropes()
BuckminsterFullerene= Allotropes()
