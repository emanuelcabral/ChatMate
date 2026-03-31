# import langchain 
# import pydantic 
# print("Prueba exitosa!") 
# print("Prueba exitosa!") 


from huggingface_hub import login
from transformers import pipeline
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener el token de Hugging Face de forma segura
token = os.getenv("HF_TOKEN")
login(token=token)

# Crear generador de texto
generator = pipeline('text-generation', model='gpt2')

# Generar texto
prompt = "What is artificial intelligence?"
response = generator(prompt, max_new_tokens=100, num_return_sequences=1)

print(response[0]['generated_text'])