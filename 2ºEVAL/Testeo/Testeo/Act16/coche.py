class Coche:
    def __init__(self, marca, modelo, tipo):
        if type(marca) != str:
            raise Exception("Tipo de dato incorrecto para la marca")
        self.marca = marca
        if type(modelo) != str:
            raise Exception("Tipo de dato incorrecto para el modelo")
        self.modelo = modelo
        if type(tipo) != str:
            raise Exception("Tipo de dato incorrecto para el tipo")
        self.tipo = tipo
        self.tamanyo_tanque_gasolina = 70
        self.nivel_gasolina = 0
        self.maximos_ocupantes = 0
        self.ocupantes_actuales = 0
        self.numero_ruedas = 4
        self.numero_ruedas_correctas = 4
        self._matricula = ""

    def llena_deposito(self):
        self.nivel_gasolina = self.tamanyo_tanque_gasolina
        print('El depósito de gasolina ahora está lleno.')

    def actualiza_combustible(self, nuevo_nivel):
        if nuevo_nivel < 0:
            raise Exception('Depósito vacío.')
        if nuevo_nivel <= self.tamanyo_tanque_gasolina:
            self.nivel_gasolina = nuevo_nivel
        else:
            raise Exception('Capacidad excedida.')

    def obtener_combustible(self, cantidad):
        if self.nivel_gasolina + cantidad <= self.tamanyo_tanque_gasolina:
            self.nivel_gasolina += cantidad
            print('Repostado combustible.')
        else:
            raise Exception('No es posible llenar tanto el depósito.')

    def conducir(self):
        if self.get_matricula() == "":
            raise Exception('No es posible conducir sin matrícula.')
        if self.ocupantes_actuales == 0:
            raise Exception('Debe de haber al menos un ocupante para conducir el coche.')
        print(f'El {self.modelo} está ahora en marcha.')
        self.actualiza_combustible(self.nivel_gasolina - 1)

    def subir_ocupante(self):
        self.ocupantes_actuales += 1
        if self.ocupantes_actuales > self.maximos_ocupantes:
            raise Exception('No es posible llevar tantos ocupantes en el coche.')

    def bajar_ocupante(self):
        self.ocupantes_actuales -= 1
        if self.ocupantes_actuales < 0:
            raise Exception('No es posible.')

    def pinchazo(self):
        self.numero_ruedas_correctas -= 1
        if self.numero_ruedas_correctas < 0:
            raise Exception('No es posible pinchar tantas ruedas.')

    def reparar_pinchazo(self):
        self.numero_ruedas_correctas += 1
        if self.numero_ruedas_correctas > self.numero_ruedas:
            raise Exception('No es posible reparar tantas ruedas.')

    def set_matricula(self, nmatricula):
        numeros = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        letras = (
            "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
        if type(nmatricula) != str:
            raise Exception("Tipo de dato incorrecto para la matrícula")
        if len(nmatricula) != 7:
            raise Exception("Longitud incorrecta de matrícula")
        if nmatricula[0] not in numeros:
            raise Exception("Formato incorrecto en el primer digito de la matrícula")
        if nmatricula[1] not in numeros:
            raise Exception("Formato incorrecto en el segundo digito de la matrícula")
        if nmatricula[2] not in numeros:
            raise Exception("Formato incorrecto en el tercer digito de la matrícula")
        if nmatricula[3] not in numeros:
            raise Exception("Formato incorrecto en el cuarto digito de la matrícula")
        if nmatricula[4] not in letras:
            raise Exception("Formato incorrecto en la primera letra de la matrícula")
        if nmatricula[5] not in letras:
            raise Exception("Formato incorrecto en la segunda letra de la matrícula")
        if nmatricula[6] not in letras:
            raise Exception("Formato incorrecto en la tercera letra de la matrícula")

        self._matricula = nmatricula

    def get_matricula(self):
        return self._matricula
