import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="sistema_medico",
        user="postgres",
        password="halo3456"
    )

# OBTENER SINTOMAS
def obtener_sintomas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre FROM sintomas")

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return [d[0] for d in datos]

# GUARDAR EVALUACION
def guardar_evaluacion(sintomas, resultado):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO evaluaciones (sintomas, resultado)
        VALUES (%s, %s)
        """,
        (str(sintomas), resultado)
    )

    conn.commit()

    cursor.close()
    conn.close()

# GUARDAR PACIENTE
def guardar_paciente(nombre, edad, sistolica, diastolica):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO pacientes
        (nombre, edad, sistolica, diastolica)
        VALUES (%s,%s,%s,%s)
        """,
        (nombre, edad, sistolica, diastolica)
    )

    conn.commit()

    cursor.close()
    conn.close()

# OBTENER PACIENTES
def obtener_pacientes():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        nombre,
        edad,
        sistolica,
        diastolica
        FROM pacientes
        ORDER BY id DESC
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos

# OBTENER HISTORIAL
def obtener_historial():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        sintomas,
        resultado,
        fecha
        FROM evaluaciones
        ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos