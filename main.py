import folium

from metodo1 import metodo_1
from metodo2 import metodo_2

from mapa import mostrar_personas_en_mapa
from mapa import calcular_ruta

from datos_prueba import personas
from utils import clear_screen


def ver_situacion_inicial(personas):
    print("------------INIT -----------------")
    for persona in personas:
        if persona.vehiculo:
            print(f"{persona.nombre}, tiene AUTO ({persona.vehiculo.capacidad_personas} personas")
        else:
            print(f"{persona.nombre}")
    print("----------------------------------\n\n")


def mostrar_asignacion_vehiculos(vehiculos):
    print("\n\n------------  ASI QUEDA -----------------")
    for vehiculo in vehiculos:
        print(f"Vehículo de {vehiculo.personas[0].nombre}")
        print("-" * 20) 
        for persona in vehiculo.personas:
            print(persona.nombre)
        print()
    print("----------------------------------")


def chequear_capacidad_total(personas):
    capacidad_total_personas = sum([p.vehiculo.capacidad_personas for p in personas if p.vehiculo is not None])
    capacidad_total_bicicletas = sum([p.vehiculo.capacidad_bicicletas for p in personas if p.vehiculo is not None])

    total_personas = len(personas)

    if capacidad_total_personas >= total_personas:
        return True
    else:
        return False


if __name__ == "__main__":
    clear_screen()
    ver_situacion_inicial(personas)
    
    if not chequear_capacidad_total(personas):
        print("No hay suficientes lugares para la natidad de personas")
        exit()

    vehiculos_metodo_2 = metodo_2(personas)
    mostrar_personas_en_mapa(personas, vehiculos_metodo_2)

    calcular_ruta(vehiculos_metodo_2[0].personas[0], vehiculos_metodo_2[0].personas[1])

    mostrar_asignacion_vehiculos(vehiculos_metodo_2)
    
