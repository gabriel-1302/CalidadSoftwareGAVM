import csv
import random
from faker import Faker

fake = Faker('es_MX')  # Para nombres en español
output_file = 'personas.csv'

# Opciones para sexo y profesiones
sexos = ['M', 'F']
profesiones = [
    'Ingeniero', 'Doctor', 'Profesor', 'Abogado', 'Arquitecto',
    'Contador', 'Enfermero', 'Programador', 'Diseñador', 'Electricista'
]

def generar_direccion_corta():
    """Genera una dirección más corta sin comillas"""
    direccion = f"{fake.street_name()} {random.randint(100, 999)}"
    # Eliminar cualquier comilla que pudiera aparecer
    return direccion.replace('"', '').replace("'", "")

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Encabezado
    writer.writerow([
        'carnet', 'nombres', 'apellidos', 'sexo',
        'fecha_nacimiento', 'profesion', 'celular', 'direccion'
    ])

    for i in range(500):
        sexo = random.choice(sexos)
        nombres = fake.first_name_male() if sexo == 'M' else fake.first_name_female()
        apellidos = fake.last_name() + ' ' + fake.last_name()
        carnet = f"{random.randint(100000, 999999)}-{i}"
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat()
        profesion = random.choice(profesiones)
        celular = fake.phone_number()
        direccion = generar_direccion_corta()

        writer.writerow([
            carnet, nombres, apellidos, sexo,
            fecha_nacimiento, profesion, celular, direccion
        ])

print(f"CSV generado exitosamente con 500 registros en '{output_file}'")