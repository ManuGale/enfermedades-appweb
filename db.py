import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="sistema_medico",
        user="postgres",
        password="halo3456"  
    )

def obtener_sintomas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM sintomas")
    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return [d[0] for d in datos]

def guardar_evaluacion(sintomas, resultado):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO evaluaciones (sintomas, resultado) VALUES (%s, %s)",
        (str(sintomas), resultado)
    )

    conn.commit()
    cursor.close()
    conn.close()

# 🔥 ESTA ES LA QUE TE FALTA
def obtener_historial():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM evaluaciones ORDER BY fecha DESC")
    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos

def guardar_paciente(nombre, edad, sistolica, diastolica):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pacientes (nombre, edad, sistolica, diastolica) VALUES (%s,%s,%s,%s)",
        (nombre, edad, sistolica, diastolica)
    )

    conn.commit()
    cursor.close()
    conn.close()