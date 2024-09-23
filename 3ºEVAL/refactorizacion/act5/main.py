import random
import time
import sys

FINAL = 40
while True:
    numeroCaracoles = input('¿Cuántos caracoles van a competir? Máximo: 8 \n> ')
    if numeroCaracoles.isdecimal() and 1 < int(numeroCaracoles) <= 8:
        numeroCaracoles = int(numeroCaracoles)
        break
    print('Introduce un número entre 2 y 8')

Noms = []
for caracol in range(numeroCaracoles):
    while True:
        print('Introduce el nombre del caracol' + str(caracol + 1) + " :")
        nombre = input('> ')
        if len(nombre) == 0:
            print('Por favor introduce un nombre.')
        elif nombre in Noms:
            print('Introduce un nombre que no haya sido utilizado.')
        else:
            break
    Noms.append(nombre)
pista = ('\n' * FINAL) + ('\nINICIO' + (' ' * (FINAL - len('INICIO')) + 'FIN')) + ('\n|' + (' ' * (FINAL - len('|')) +
                                                                                            '|'))
# print('\n' * FINAL)
# print('INICIO' + (' ' * (FINAL - len('INICIO')) + 'FIN'))
# print('|' + (' ' * (FINAL - len('|')) + '|'))
print(pista)
progreso = {}
for caracoles in Noms:
    print(caracoles[:20])
    print('@v')
    progreso[caracoles] = 0

time.sleep(1.5)
 
while True:
    for caracol in range(random.randint(1, numeroCaracoles // 2)):
        TurnoCaracol = random.choice(Noms)
        progreso[TurnoCaracol] += 1

        if progreso[TurnoCaracol] == FINAL:
            print(TurnoCaracol, 'ha ganado!!!')
            sys.exit()

    time.sleep(0.5)
    print(pista)
    # print('\n' * FINAL)
    # print('INICIO' + (' ' * (FINAL - len('INICIO')) + 'FIN'))
    # print('|' + (' ' * (FINAL - 1) + '|'))

    for caracoles in Noms:
        NombreParticipante = progreso[caracoles]
        print((' ' * NombreParticipante) + caracoles[:20])
        print(('.' * progreso[caracoles]) + '@v')
