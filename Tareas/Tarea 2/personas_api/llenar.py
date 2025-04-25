# script_personas_aleatorias.py
import requests
import random
from faker import Faker
from datetime import datetime
import json

# Configurar Faker para generar datos en español
fake = Faker('es_ES')

# URL de la API
API_URL = "http://localhost:8000/api/personas/"

# Lista de profesiones comunes
profesiones = [
    "Ingeniero de Software", "Médico", "Abogado", "Contador", 
    "Arquitecto", "Profesor", "Diseñador Gráfico", "Enfermero", 
    "Psicólogo", "Chef", "Economista", "Periodista", "Farmacéutico"
]

def generar_carnet():
    """Genera un número de carnet aleatorio con formato"""
    return f"{random.randint(1000000, 9999999)}-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"

def generar_persona_aleatoria():
    """Genera datos aleatorios para una persona"""
    # Determinar sexo para usar el nombre correcto
    sexo = random.choice(['M', 'F'])
    
    if sexo == 'M':
        nombre = fake.first_name_male()
        apellido = f"{fake.last_name()} {fake.last_name()}"
    else:
        nombre = fake.first_name_female()
        apellido = f"{fake.last_name()} {fake.last_name()}"
    
    # Fecha de nacimiento en formato ISO (YYYY-MM-DD)
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
    
    return {
        "carnet": generar_carnet(),
        "nombres": nombre,
        "apellidos": apellido,
        "sexo": sexo,
        "fecha_nacimiento": fecha_nacimiento,
        "profesion": random.choice(profesiones),
        "celular": fake.phone_number().replace(' ', '')[0:8],
        "direccion": fake.address().replace('\n', ', ')
    }

def crear_personas_aleatorias(cantidad=10):
    """Crea y envía a la API el número especificado de personas aleatorias"""
    personas_creadas = 0
    personas_fallidas = 0
    
    print(f"Generando {cantidad} personas aleatorias...")
    
    for i in range(cantidad):
        persona = generar_persona_aleatoria()
        
        try:
            response = requests.post(
                API_URL,
                data=json.dumps(persona),
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 201:
                personas_creadas += 1
                print(f"✅ Persona {i+1}/{cantidad} creada: {persona['nombres']} {persona['apellidos']}")
            else:
                personas_fallidas += 1
                print(f"❌ Error al crear persona {i+1}: {response.status_code} - {response.text}")
        except Exception as e:
            personas_fallidas += 1
            print(f"❌ Excepción al crear persona {i+1}: {str(e)}")
    
    print(f"\nResumen:")
    print(f"- Personas creadas exitosamente: {personas_creadas}")
    print(f"- Personas con errores: {personas_fallidas}")
    print(f"- Total intentado: {cantidad}")

if __name__ == "__main__":
    # Asegúrate de que el servidor Django esté corriendo antes de ejecutar este script
    print("Asegúrate de que tu servidor Django esté corriendo en http://localhost:8000")
    input("Presiona Enter para continuar...")
    
    crear_personas_aleatorias(10)