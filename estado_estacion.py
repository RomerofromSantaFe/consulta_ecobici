import requests


url_estado = "https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus?client_id=eed0f545737b4dcd822b2b7eb2f43bc4&client_secret=5583BfC08D304ffCA9148e6BAe5e7eDd"
url_estacion = "https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationInformation?client_id=eed0f545737b4dcd822b2b7eb2f43bc4&client_secret=5583BfC08D304ffCA9148e6BAe5e7eDd"






busqueda = input("Ingrese el ID a consultar: ")


direccion: None
bicis_disponibles = None


#obtengo direccion de la estación ingresada

response_estacion = requests.get(url_estacion)
if response_estacion.status_code == 200:
    data = response_estacion.json()
    estaciones = data['data']['stations']

    for estacion in estaciones:
        if estacion['station_id'] == busqueda:
            direccion = estacion['address']     #guardo la direccion
            break

else: 
    print("ERROR - estacion inexistente")

#obtengo bicis disponibles

response_estado = requests.get(url_estado)
if response_estado.status_code == 200:
    data_estado = response_estado.json()
    estaciones_estado = data_estado['data']['stations']

    for estacion in estaciones_estado:
        if estacion['station_id'] == busqueda:
            bicis_disponibles=estacion['num_bikes_available'] #guardo cant bicis
            break
else:
    print("ERROR - estacion inexistente")



#muestro resultados:
print("----------------")
print(f"Datos obtenidos:") 
print(f"Estacion #{busqueda}")
print(f"Direccion: {direccion}")
print(f"Bicis disponibles: {bicis_disponibles}")