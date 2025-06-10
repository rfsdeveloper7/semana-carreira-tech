import requests 
 
cidade = input("Digite o nome da cidade: ") 
 
api_key = "P3CseKEnCuGS804GKtsGcw==hO9RY4TaiHnmNN9d" 
 
url = f"https://api.api-ninjas.com/v1/airquality?city={cidade}" 
headers = {"X-Api-Key": api_key} 
 
resposta = requests.get(url, headers=headers) 
 
if resposta.status_code == 200: 
    dados = resposta.json() 
 
    print(f"\nQualidade do ar em {cidade.capitalize()}:") 
    print(f" - Índice Geral (AQI): {dados['overall_aqi']}") 
    print(f" - Partículas PM2.5: {dados['PM2.5']}") 
    print(f" - Dióxido de Nitrogênio (NO2): {dados['NO2']}") 
    print(f" - Ozônio (O3): {dados['O3']}") 
else: 
    print("  Não foi possível obter os dados. Verifique a cidade ou sua chave de API.") 