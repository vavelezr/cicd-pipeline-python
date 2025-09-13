# app/app.py
"""Modulo de app de la calculadora."""


from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.get("/")
def index_get():
    """Funcion principal de la app."""
    return render_template("index.html")


@app.post("/")
def index():
    """Funcion principal de la app."""
    resultado = None
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacion = request.form["operacion"]
        if operacion == "sumar":
            resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "multiplicar":
            resultado = multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación no válida"
    except ValueError:
        resultado = "Error: Introduce números válidos"
    except ZeroDivisionError:
        resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=False, port=5000, host="0.0.0.0")  # Quita debug=True para producción
