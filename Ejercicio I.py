class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def texto(self):
        print (f"El cargo de {self.nombre}")

class Operativo (Persona):
    def __init__(self, nombre, salario1):
        super().__init__(nombre)
        self.salario1 = salario1

    def texto(self):
        print (f"El cargo de {self.nombre} es cargo Operativo, con un salario de {self.salario1}. ")

class Administrativo (Persona):
    def __init__(self, nombre, salario2):
        super().__init__(nombre)
        self.salario2 = salario2

    def texto(self): 
        print (f"El cargo de {self.nombre} es cargo Administrativo, con un salario de {self.salario2}. ")


operativo1 = Operativo("Juan", 1800000)
operativo2 = Operativo("Andrés", 1950000)
administrativo1 = Administrativo("Luis", 2400000)
administrativo2 = Administrativo("Felipe", 3200000)

operativo1.texto()
administrativo1.texto()
operativo2.texto()
administrativo2.texto()
