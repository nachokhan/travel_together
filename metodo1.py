

def metodo_1(personas):
    personas_con_vehiculo = [p for p in personas if p.vehiculo is not None]
    personas_sin_vehiculo = [p for p in personas if p.vehiculo is None]

    for p in personas_con_vehiculo:
        p.vehiculo.agregar_persona(p)

    vehiculos = [p.vehiculo for p in personas_con_vehiculo]


    for persona in personas_sin_vehiculo:
        vehiculos.sort(key=lambda v: len(v.personas))
        vehiculo_asignado = vehiculos[0]
        vehiculo_asignado.agregar_persona(persona)

    return vehiculos