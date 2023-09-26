import random
import math

from model.Persona import Persona
from model.Vehiculo import Vehiculo

# Lista de 20 nombres
nombres_disponibles = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Luis", "Sofía", "Elena", "Diego",
                       "Marta", "José", "Julia", "Andrés", "Isabel", "Roberto", "Carmen", "Fernando", "Lucía"]


# Definir las coordenadas de Mendoza, Argentina
latitud_mendoza = -32.889458
longitud_mendoza = -68.845839


def generar_coordenadas_aleatorias(lat, lon, radio_km):
    # Convertir el radio de kilómetros a grados de latitud/longitud
    radio_grados = radio_km / 111.32

    # Generar coordenadas aleatorias dentro del círculo
    u = random.uniform(0, 1)
    v = random.uniform(0, 1)
    radio_aleatorio = radio_grados * math.sqrt(u)
    angulo_aleatorio = 2 * math.pi * v

    nueva_latitud = lat + (radio_aleatorio * math.cos(angulo_aleatorio))
    nueva_longitud = lon + (radio_aleatorio * math.sin(angulo_aleatorio))

    return nueva_latitud, nueva_longitud


# Crear un arreglo de personas con ubicaciones aleatorias en el círculo
personas = []
numero_de_personas = 13

for i in range(numero_de_personas):
    latitud, longitud = generar_coordenadas_aleatorias(latitud_mendoza, longitud_mendoza, 5)
    nombre_persona = random.choice(nombres_disponibles)  # Nombre aleatorio de la lista
    
    # Eliminar el nombre utilizado para que no se repita
    nombres_disponibles.remove(nombre_persona)
    
    # Probabilidad del 50% de que una persona tenga vehículo
    if random.random() < 0.3:
        capacidad_personas = random.randint(4, 5)  # Capacidad de personas en el vehículo
        capacidad_bicicletas = random.randint(0, 2)  # Capacidad de bicicletas en el vehículo
        vehiculo = Vehiculo(capacidad_personas, capacidad_bicicletas)
        personas.append(Persona(nombre_persona, latitud, longitud, vehiculo))
    else:
        personas.append(Persona(nombre_persona, latitud, longitud))