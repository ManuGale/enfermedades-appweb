from flask import Flask, request, jsonify, render_template

from expert_system import evaluar_sintomas

from db import (
    guardar_evaluacion,
    obtener_sintomas,
    guardar_paciente,
    obtener_pacientes,
    obtener_historial
)

app = Flask(__name__)

# HOME
@app.route('/')
def index():

    sintomas = obtener_sintomas()

    return render_template(
        'index.html',
        sintomas=sintomas
    )

# PACIENTES
@app.route('/pacientes')
def pacientes():

    pacientes = obtener_pacientes()

    return render_template(
        'pacientes.html',
        pacientes=pacientes
    )

# HISTORIAL
@app.route('/historial')
def historial():

    historial = obtener_historial()

    return render_template(
        'historial.html',
        historial=historial
    )

# CONSULTAS NECESARIAS
@app.route('/consultas')
def consultas():

    pacientes = obtener_pacientes()

    pacientes_riesgo = []

    for p in pacientes:

        sistolica = p[2]
        diastolica = p[3]

        if sistolica >= 140 or diastolica >= 90:
            pacientes_riesgo.append(p)

    return render_template(
        'consultas.html',
        pacientes=pacientes_riesgo
    )

# EVALUAR
@app.route('/evaluar', methods=['POST'])
def evaluar():

    data = request.get_json()

    sintomas = data.get("sintomas", [])

    resultado = evaluar_sintomas(sintomas)

    guardar_evaluacion(
        sintomas,
        resultado["riesgo"]
    )

    return jsonify(resultado)

# GUARDAR PACIENTE
@app.route('/guardar_paciente', methods=['POST'])
def guardar():

    data = request.get_json()

    guardar_paciente(
        data["nombre"],
        data["edad"],
        data["sistolica"],
        data["diastolica"]
    )

    return jsonify({
        "msg":"ok"
    })

if __name__ == '__main__':
    app.run(debug=True)