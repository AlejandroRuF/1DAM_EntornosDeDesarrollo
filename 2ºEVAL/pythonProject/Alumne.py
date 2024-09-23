import re
from datetime import datetime


class Alumno:
    __num_Alumnos = 0
    __fecha_nacimiento=""
    __anyos=0
    __nota_media=""

    def __init__(self, nom, apellido, fecha_nacimiento, curso, nota_media):
        Alumno.__num_Alumnos += 1
        self.__nom = nom
        self.__apellido = apellido
        self.set_fecha_nacimiento(fecha_nacimiento)
        self.__curso = curso
        self.set_notamedia(nota_media)
        self.set_anyos(fecha_nacimiento)
        self.__num_Alumnos = Alumno.__num_Alumnos

    def validar_fecha(self, fecha):
        patron = (
            r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1][/]0[1-9]|1[1-2][/][0-9]{4}])")  # me he ayudado de IA aunque he aprendido a hacerlo mas menos
        if re.match(patron, fecha):  # aunque se que es un comprobador no se como funciona re
            return True
        else:
            return False
    def set_fecha_nacimiento(self, fecha_nacimiento):
        if self.validar_fecha(fecha_nacimiento):
            self.__fecha_nacimiento = fecha_nacimiento
        else:
            raise Exception("La fecha debe ser valida en formato DD/MM/AAAA")
    def get_Fecha(self):
        return self.__fecha_nacimiento



    def validar_nota(self, nota_media):
        patron_nota = (r"^\d{1,2}([.,]\d{1,2})?$")#he necesitado bastante ayuda y eso que era sencillo cuando lo he visto ...
        if re.match(patron_nota, nota_media):
            return True
        else:
            return False
    def set_notamedia(self, nota_media):
        if self.validar_nota(nota_media):
            self.__nota_media = nota_media
        else:
            raise Exception("La nota media debe seguir el formato correcto")
    def get_notamedia(self):
        return self.__nota_media




    def set_anyos(self,fecha_nacimiento):
        partes_fecha = fecha_nacimiento.split("/")
        if len(partes_fecha) == 3:
            anyo_actual = datetime.now().year
            anyo_nacimiento = int(partes_fecha[2])
            self.__anyos = anyo_actual - anyo_nacimiento
        else:
            raise Exception("La fecha de nacimiento debe estar en formato DD/MM/AAAA")
    def get_anyos(self):
        return self.__anyos



    def get_nombre(self):
        return self.__nom
    def set_nombre(self,nombre):
        self.__nom=nombre



    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido=apellido



    def get_curso(self):
        return self.__curso
    def set_curso(self,curso):
        self.__curso=curso

    def __str__(self):
        return (f"El nombre del alumno es {self.get_nombre()} {self.get_apellido()} nació en {self.get_Fecha()} tiene "
                f"{self.get_anyos()} años una nota media de {self.get_notamedia()} y cursa {self.get_curso()}")

    def certificado(self):
        print(f"L’alumne {self.get_nombre()} nascut el {self.get_Fecha()} ha cursat {self.get_curso()} i ha obtés una "
              f"nota mitjana de {self.get_notamedia()}")


alumnos = []
while True:
    error = False
    nom = input("Introduce el Nombre del alumno: \n")
    apellido = input("Introduce el apellido del alumno: \n")
    fecha_nacimiento = input("Introduce la fecha de nacimiento de alumno en formato DD/MM/AAAA: \n")
    curso = input("Introduce el curso del alumno:\n")
    nota_medi = input("Introduce la nota media del alumno máximo 2 decimales:\n")
    try:
        alumno = Alumno(nom, apellido, fecha_nacimiento, curso, nota_medi)
    except Exception as e:
        print(f"{e}")
        error = True

    if not error:
        alumnos.append(alumno)

        while True:
            crear = False
            nuevo_a = input("Quieres introducir otro alumno S/N\n").upper()
            if nuevo_a == "N":
                break
            elif nuevo_a:
                crear = True
                break
            else:
                print("Introduce la opcion correctamente")

        if not crear:
            break

for i in range(len(alumnos)):
    print(alumnos[i])