import requests
import csv

# Construye la URL
url = 'https://apidatos.ree.es/es/datos/demanda/evolucion?start_date=2023-01-01T00:00&end_date=2023-12-31T00:00&time_trunc=day'

# Encabezados requeridos por la API
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Realiza la solicitud GET
response = requests.get(url, headers=headers)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Convierte la respuesta a formato JSON
    data = response.json()

 # Abre un archivo CSV para escribir los datos
    with open('Tarea/demanda_electrica2023.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Escribe los encabezados del CSV
        writer.writerow(['Fecha', 'Demanda'])
        
        # Navega por la estructura del JSON para extraer los datos de interés
        for item in data['included'][0]['attributes']['values']:
            # Extrae la fecha y la demanda de cada registro
            fecha = item['datetime']
            demanda = item['value']
            
            # Escribe la fila en el archivo CSV
            writer.writerow([fecha, demanda])
            
    print("Datos guardados en Tarea/demanda_electrica2024.csv")
else:
    print("Error en la solicitud:", response.status_code)