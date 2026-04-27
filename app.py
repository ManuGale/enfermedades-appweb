from flask import Flask, request, jsonify, render_template
from expert_system import evaluar_sintomas
from db import guardar_evaluacion, obtener_sintomas, guardar_paciente

app = Flask(__name__)

# HOME
@app.route('/')
def index():
    sintomas = obtener_sintomas()
    return render_template('index.html', sintomas=sintomas)

# SISTEMA EXPERTO
@app.route('/evaluar', methods=['POST'])
def evaluar():
    data = request.get_json()
    sintomas = data.get("sintomas", [])

    resultado = evaluar_sintomas(sintomas)

    guardar_evaluacion(sintomas, resultado["riesgo"])

    return jsonify(resultado)

# GUARDAR PACIENTE
@app.route('/guardar_paciente', methods=['POST'])
def guardar():
    data = request.get_json()

    print("GUARDANDO:", data)  # debug

    guardar_paciente(
        data["nombre"],
        data["edad"],
        data["sistolica"],
        data["diastolica"]
    )

    return jsonify({"msg": "ok"})

# SIEMPRE AL FINAL
if __name__ == '__main__':
    app.run(debug=True)