class Persona:
    def id(self, name):
        self.nombre = name

    def printer(self):
        print("Nombre:", self.nombre)


p1 = Persona()
p2 = Persona()

p1.id("Juan")
p2.id("Pedro")

p1.printer()
p2.printer()
