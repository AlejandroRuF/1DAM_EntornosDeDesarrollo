diasemana = int(input("Pon un numero del 1 al 7 dependiendo del dia de la semana en que estemos\n"))

if diasemana == 1:
    print(f"Estamos a Lunes")
elif diasemana == 2:
    print(f"Estamos a Martes")
elif diasemana == 3:
    print(f"Estamos a Miercoles")
elif diasemana == 4:
    print(f"Estamos a Jueves")
elif diasemana == 5:
    print(f"Estamos a Viernes")
elif diasemana == 6:
    print(f"Estamos a Sabado")
elif diasemana == 7:
    print(f"Estamos a Domingo")
else:
    print(f"El numero {diasemana} no es un numero entre el 1 y el 7")
