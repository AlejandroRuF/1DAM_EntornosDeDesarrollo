import tkinter
import math
import time


class Reloj(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        self.longitud_de_las_manecillas = 50
        self.inicializar()

    def inicializar(self):
        self.crea_canvas()
        self.creando_fondo()
        self.crear_palitos()
        return

    # Crea el fondo con una imagen
    def creando_fondo(self):
        self.image = tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(150, 150, image=self.image)
        return

    # crear canvas
    def crea_canvas(self):
        self.canvas = tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes', fill='both')
        return

    # Crear las manecillas del reloj
    def crear_palitos(self):
        self.palitos = []

        store = self.canvas.create_line(self.x, self.y, self.x + self.longitud_de_las_manecillas,
                                        self.y + self.longitud_de_las_manecillas, width=2, fill='red')
        self.palitos.append(store)
        store = self.canvas.create_line(self.x, self.y, self.x + self.longitud_de_las_manecillas,
                                        self.y + self.longitud_de_las_manecillas, width=2, fill='red')
        self.palitos.append(store)
        store = self.canvas.create_line(self.x, self.y, self.x + self.longitud_de_las_manecillas,
                                        self.y + self.longitud_de_las_manecillas, width=2, fill='red')
        self.palitos.append(store)

        return

    # Método para actualizar la posición de las manecillas
    def actualiza(self):
        horaActual = time.localtime()
        horaActualFormato24 = time.strptime(str(horaActual.tm_hour), "%H")
        posicionManecillaHoras = int(time.strftime("%I", horaActualFormato24)) * 5
        horaActual = (posicionManecillaHoras, horaActual.tm_min, horaActual.tm_sec)

        # Cambiando las coordenadas de los palitos
        for horas, minutos in enumerate(horaActual):
            x, y = self.canvas.coords(self.palitos[horas])[0:2]
            cr = [x, y]
            cr.append(self.longitud_de_las_manecillas * math.cos(math.radians(minutos * 6) - math.radians(90)) + self.x)
            cr.append(self.longitud_de_las_manecillas * math.sin(math.radians(minutos * 6) - math.radians(90)) + self.y)
            self.canvas.coords(self.palitos[horas], tuple(cr))
        return


if __name__ == '__main__':
    a = Reloj()

    while True:
        a.update()
        a.update_idletasks()
        a.actualiza()
