# app/calculadora.py
""" Modulo de la calculadora donde se realizan las operaciones."""
def sumar(a, b):
    """ Funcion para sumar dos numeros. """
    return a + b


def restar(a, b):
    """ Funcion para restar dos numeros. """
    return a - b


def multiplicar(a, b):
    """ Funcion para multiplicar dos numeros. """
    return a * b


def dividir(a, b):
    """ Funcion para dividir dos numeros. """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
