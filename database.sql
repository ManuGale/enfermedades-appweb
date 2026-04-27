-- Crear base de datos
CREATE DATABASE sistema_experto;

-- Usar la base de datos
\c sistema_experto;

-- Tabla enfermedades
CREATE TABLE enfermedades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

-- Tabla pacientes
CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    sistolica INTEGER,
    diastolica INTEGER,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla sintomas
CREATE TABLE sintomas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Tabla evaluaciones
CREATE TABLE evaluaciones (
    id SERIAL PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sintomas TEXT,
    resultado TEXT,
    paciente_id INTEGER REFERENCES pacientes(id)
);