from google import genai

def get_car_ai_bio(model, brand, year):
    client = genai.Client(api_key="AIzaSyDrIRsjlKs3yHT5CqI1kmQSXIBAFfB33aM")
    prompt = """
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas especificas desse modelo. 
    """
    prompt = prompt.format(brand, model, year)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt)

    return response.text
