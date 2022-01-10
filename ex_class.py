import math

class Particle:
    def __init__(self,name,mass,charge, momentum=0.):
        self.name=name
        self.mass=mass #in Gev/c
        self.charge=charge #in e
        self.momentum=momentum #in Mev

    def energy(self):
        return math.sqrt(self.momentum**2. + self.mass**2.)

    def push(self):
        self.momentum+=1

class alpha(Particle):
    def __init__(self, momentum=0.):
        Particle.__init__(self, "Alpha", 3.7, 2, momentum)

class proton(Particle):
    def __init__(self, momentum=0.):
        Particle.__init__(self, "Proton", 1., 1, momentum)


measure_1=alpha()
measure_1.push()
print(f'The energy of {measure_1.name} is {measure_1.energy()} Gev/c^2')
measure_1.push()
measure_1.push()

print(f'The energy of {measure_1.name} is {measure_1.energy()} Gev/c^2')



measure_2=proton()

print(f'The energy of {measure_2.name} is {measure_2.energy()} Gev/c^2')