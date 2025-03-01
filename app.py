import requests
import os

# Configurações
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')  # Chave da API obtida das variáveis de ambiente
CITY = 'Valencia'
OUTPUT_FILE = 'index.html'

# Função para buscar dados da API
def get_weather():

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":CITY,"days":"1"}

    headers = {
	    "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    return data

# Função para gerar o HTML
def generate_html(data):
    temperature = data['current']['temp_c']
    description = data['location']['tz_id']
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tempo em {CITY}</title>
    </head>
    <body>
        <h1>Tempo em {CITY}</h1>
        <p>Temperatura: {temperature}°C</p>
        <p>Condição: {description}</p>
    </body>
    </html>
    """
    with open(OUTPUT_FILE, 'w') as file:
        file.write(html)

# Executar o script
if __name__ == '__main__':
    weather_data = get_weather()
    generate_html(weather_data)
    print(f"Arquivo {OUTPUT_FILE} gerado com sucesso!")
