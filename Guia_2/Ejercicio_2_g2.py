from unicodedata import name


class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.name = nombre
        self.ap = apellido
        self.nota = nota

    def printer(self):
        print(self.name, self.ap, self.nota)

    def regularizado(self):
        if self.nota < 6:
            print("el alumno no esta aprobado")
        elif self.nota >= 6:
            print("el alumno esta aprobado")


a1 = Alumno("Juan", "Rodriguez", 6)
a2 = Alumno("Maria", "Paredes", 3)

a1.printer()
a2.printer()

a1.regularizado()
a2.regularizado()
