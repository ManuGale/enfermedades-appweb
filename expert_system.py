def evaluar_sintomas(sintomas):
    reglas = {
        "infarto": {
            "sintomas": ["dolor_pecho", "falta_aire"],
            "peso": 3,
            "mensaje": "⚠️ Posible riesgo de infarto"
        },
        "arritmia": {
            "sintomas": ["latidos_irregulares", "mareos"],
            "peso": 2,
            "mensaje": "⚠️ Posible arritmia"
        },
        "insuficiencia": {
            "sintomas": ["fatiga", "hinchazon_piernas"],
            "peso": 2,
            "mensaje": "⚠️ Posible debilidad del corazón"
        }
    }

    puntaje = 0
    mensajes = []

    for enfermedad, datos in reglas.items():
        coincidencias = len(set(sintomas) & set(datos["sintomas"]))
        if coincidencias >= 2:
            puntaje += datos["peso"]
            mensajes.append(datos["mensaje"])

    if puntaje >= 4:
        riesgo = "ALTO"
        recomendacion = "⚠️ Acude inmediatamente al médico"
    elif puntaje >= 2:
        riesgo = "MEDIO"
        recomendacion = "⚠️ Consulta con un especialista"
    else:
        riesgo = "BAJO"
        recomendacion = " Mantén hábitos saludables"

    return {
        "riesgo": riesgo,
        "mensajes": mensajes,
        "recomendacion": recomendacion
    }