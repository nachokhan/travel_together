import folium


def mostrar_personas_en_mapa(personas, vehiculos_utilizados):
    # Obtener las coordenadas extremas de las personas
    latitudes = [persona.latitud for persona in personas]
    longitudes = [persona.longitud for persona in personas]

    max_lat = max(latitudes)
    min_lat = min(latitudes)
    max_lon = max(longitudes)
    min_lon = min(longitudes)

    # Calcular el centro del mapa
    centro_lat = (max_lat + min_lat) / 2
    centro_lon = (max_lon + min_lon) / 2

    # Crear un mapa centrado en el centro calculado
    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)

    # Crear un diccionario para asignar colores a cada vehículo
    colores = {}
    for i, vehiculo in enumerate(vehiculos_utilizados):
        colores[vehiculo.personas[0].nombre] = f'C{i}'

    # Agregar marcadores para cada persona y colorearlas según el vehículo utilizado
    for persona in personas:
        color = colores.get(persona.nombre, 'blue')  # Colorear de azul si es dueño
        icono_persona = folium.Icon(icon='user', prefix='fa', color=color)
        folium.Marker([persona.latitud, persona.longitud], icon=icono_persona, popup=persona.nombre).add_to(mapa)

    # Ajustar el tamaño del mapa para que abarque todas las personas
    mapa.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    # Mostrar el mapa en un archivo HTML
    mapa.save('mapa_personas.html')



def mostrar_personas_en_mapa_1(personas):
    # Obtener las coordenadas extremas de las personas
    latitudes = [persona.latitud for persona in personas]
    longitudes = [persona.longitud for persona in personas]

    max_lat = max(latitudes)
    min_lat = min(latitudes)
    max_lon = max(longitudes)
    min_lon = min(longitudes)

    # Calcular el centro del mapa
    centro_lat = (max_lat + min_lat) / 2
    centro_lon = (max_lon + min_lon) / 2

    # Crear un mapa centrado en el centro calculado
    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)

    # Agregar marcadores para cada persona
    for persona in personas:
        icono_persona = folium.Icon(icon='user', prefix='fa', color='blue')
        folium.Marker([persona.latitud, persona.longitud], icon=icono_persona, popup=persona.nombre).add_to(mapa)

    # Ajustar el tamaño del mapa para que abarque todas las personas
    mapa.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    # Mostrar el mapa en un archivo HTML
    mapa.save('mapa_personas.html')

