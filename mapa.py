import folium
import requests

from api_keys import OPEN_STREET_MAP_API


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

    # Agregar marcadores para cada persona y colorearlas según el vehículo utilizado
    for persona in personas:
        color = 'blue' if persona.vehiculo in vehiculos_utilizados else 'orange'
        icono_persona = folium.Icon(icon='user', prefix='fa', color=color)
        folium.Marker([persona.latitud, persona.longitud], icon=icono_persona, popup=persona.nombre).add_to(mapa)

    # Ajustar el tamaño del mapa para que abarque todas las personas
    mapa.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])

    # Mostrar el mapa en un archivo HTML
    mapa.save('_data/mapa_personas.html')



def calcular_ruta(persona1, persona2):
    # Obtener las coordenadas de inicio y destino
    lat1, lon1 = persona1.latitud, persona1.longitud
    lat2, lon2 = persona2.latitud, persona2.longitud

    # Crear un mapa centrado en la ubicación de la primera persona
    mapa = folium.Map(location=[lat1, lon1], zoom_start=12)

    # Crear marcadores para las ubicaciones de inicio y destino
    folium.Marker([lat1, lon1], icon=folium.Icon(color='green'), popup=persona1.nombre).add_to(mapa)
    folium.Marker([lat2, lon2], icon=folium.Icon(color='red'), popup=persona2.nombre).add_to(mapa)

    # Realizar una solicitud a la API de enrutamiento (puedes usar una API como OpenRouteService)
    # Reemplaza 'YOUR_API_KEY' con tu clave de API válida
    api_key = OPEN_STREET_MAP_API
    url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={lon1},{lat1}&end={lon2},{lat2}'
    response = requests.get(url)

    if response.status_code == 200:
        # Decodificar la respuesta JSON
        data = response.json()

        # Extraer la geometría de la ruta
        geometry = data['features'][0]['geometry']

        # Agregar la ruta al mapa
        folium.PolyLine(locations=[list(reversed(coord)) for coord in geometry['coordinates']], color='blue').add_to(mapa)

        # Mostrar el mapa con la ruta
        mapa.save(f'_data/ruta_entre_{persona1.nombre}_y_{persona2.nombre}.html')
    else:
        print('Error al calcular la ruta.')