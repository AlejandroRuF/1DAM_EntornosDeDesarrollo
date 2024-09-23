def process(number):
    if type(number) != int:
        raise Exception("No es un número entero")
    if number<0:
        raise Exception("No se admiten números negativos")
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number
