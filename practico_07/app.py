import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida
from practico_05.ejercicio_01 import Socio

app = Flask(__name__)
negocio = NegocioSocio()


@app.route('/')
def index():
    socios = negocio.todos()
    return render_template('index.html', socios=socios)


@app.route('/alta', methods=['GET', 'POST'])
def alta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        socio = Socio()
        socio.dni = dni
        socio.nombre = nombre
        socio.apellido = apellido
        try:
            negocio.alta(socio)
            return redirect(url_for('index'))
        except LongitudInvalida:
            return "Error: Longitud inválida"
    return render_template('alta.html')


@app.route('/baja/<int:id>')
def baja(id):
    negocio.baja(id)
    return redirect(url_for('index'))


@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    socio = negocio.buscar(id)
    if not socio:
        return "Socio no encontrado"

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        socio = Socio()
        socio.id_socio = id
        socio.nombre = nombre
        socio.apellido = apellido
        socio.dni = dni
        try:
            negocio.modificacion(socio)
            return redirect(url_for('index'))
        except LongitudInvalida:
            return "Error: Longitud inválida"

    return render_template('modificar.html', socio=socio)


if __name__ == '__main__':
    app.run(debug=True)
