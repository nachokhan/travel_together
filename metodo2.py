import math


def metodo_2(personas):
    
    vehiculos_seleccionados = seleccionar_vehiculos_por_tamaño(personas)

    con_v, sin_v = dividir_personas(personas, vehiculos_seleccionados)

    grupos = agrupar_personas(con_v, sin_v)

    for g in grupos:
        for p in g:
            g[0].vehiculo.agregar_persona(p)

    vehiculos_seleccionados = [p.vehiculo for p in con_v]

    return vehiculos_seleccionados


def agrupar_personas(con_v, sin_v):
    grupos_asignados = []

    personas = len(con_v) + len(sin_v)
    lista_capacidades = [p.vehiculo.capacidad_personas for p in con_v]
    maximos = distribuir_personas_en_vehiculos(personas, lista_capacidades)

    index = 0

    for dueño in con_v:
        vehiculo = dueño.vehiculo
        capacidad = maximos[index] if vehiculo.capacidad_personas >= maximos[index] else vehiculo.capacidad_personas
        capacidad -= 1 # lugar para el dueño

        # Encontrar las N personas más cercanas geográficamente en sin_v
        sin_v_cercanas = sorted(sin_v, key=lambda p: calcular_distancia(dueño.ubicacion[0], dueño.ubicacion[1], p.ubicacion[0], p.ubicacion[1]))[:capacidad]

        # Crear un grupo con la persona dueña y las personas asignadas
        grupo_asignado = [dueño] + sin_v_cercanas

        # Agregar el grupo a la lista de grupos asignados
        grupos_asignados.append(grupo_asignado)

        # Remover las personas asignadas de sin_v
        sin_v = [p for p in sin_v if p not in sin_v_cercanas]
        index += 1

    return grupos_asignados


def distribuir_personas_en_vehiculos(M, capacidades_vehiculos):
    # Verificar que haya suficiente capacidad total en los vehículos
    capacidad_total = sum(capacidades_vehiculos)
    if capacidad_total < M:
        raise ValueError("La capacidad total de los vehículos no es suficiente para alojar a todas las personas.")

    # Calcular la cantidad máxima de personas que se pueden asignar equitativamente a cada vehículo
    max_personas_equitativas = M // len(capacidades_vehiculos)

    # Inicializar la lista que contendrá la cantidad de personas asignadas a cada vehículo
    asignaciones_vehiculos = [max_personas_equitativas] * len(capacidades_vehiculos)

    # Calcular el número restante de personas por asignar
    personas_restantes = M % len(capacidades_vehiculos)

    # Distribuir las personas restantes de manera equitativa entre los vehículos
    for i in range(personas_restantes):
        asignaciones_vehiculos[i] += 1

    return asignaciones_vehiculos




def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula de Haversine para calcular la distancia entre dos puntos geográficos
    R = 6371  # Radio de la Tierra en kilómetros

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distancia = R * c
    return distancia


def dividir_personas(personas, lista_vehiculos):
    # Inicializar listas para los dos grupos de personas
    personas_dueñas = []
    otras_personas = []

    personas_dueñas = [p for p in personas if p.vehiculo in lista_vehiculos]
    otras_personas = [p for p in personas if p.vehiculo not in lista_vehiculos]

    return personas_dueñas, otras_personas




def seleccionar_vehiculos_por_tamaño(personas):
    vehiculos_seleccionados = []

    vehiculos = sorted([p.vehiculo for p in personas if p.vehiculo is not None], key=lambda v: v.capacidad_personas, reverse=True)
    num_personas = len(personas)
    num_vehiculos = len(vehiculos)
    capac_vehiculos = sum([v.capacidad_personas for v in vehiculos])

    v_index = 0
    while num_personas > 0:
        if vehiculos[v_index].capacidad_personas <= num_personas:
            vehiculos_seleccionados.append(vehiculos[v_index])
            capac_vehiculos -= vehiculos[v_index].capacidad_personas
            num_personas -= vehiculos[v_index].capacidad_personas
            vehiculos.remove(vehiculos[v_index])
        else:
            vehiculos_seleccionados.append(vehiculos[v_index])
            break

    return vehiculos_seleccionados