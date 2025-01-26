import requests
import random
import ollama
from utils import extract_numbers

class LMSession:

    def __init__(self, endpoint="http://localhost:11434/api/chat", model="llama3.2"):
        self.model = model
        self.url = endpoint
        self.history = []  

    def get_num_tokens(self, text: str) -> int:
        tokenized_text = self.llm.tokenize(text.encode("utf-8"))
        return len(tokenized_text)
    
    def execute(self, prompt, temperature=-1, format="json"):
        self.history.append({"role": "user", "content": prompt})
        if temperature == -1:
            data = {
                "model": self.model,
                "stream": False,
                "messages": self.history,
                "format": format,
                "options": {
                    "seed": random.randint(1, 1000)
                }
            }
        else:
            data = {
                "model": self.model,
                "stream": False,
                "messages": self.history,
                "format": format,
                "options": {
                    "temperature": temperature,
                    "main_gpu": 1,
                    "seed": random.randint(1, 1000)
                },
            }
        try:
            response = ollama.chat(self.model, messages=self.history)
        except requests.Timeout:
            print("La solicitud ha excedido el tiempo límite de espera.")
            response = None
        except requests.ConnectionError:
            print("Error de conexión. Verifica la URL o tu conexión a internet.")
            response = None
        except requests.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
            response = None
        except requests.RequestException as req_err:
            print(f"Error en la solicitud: {req_err}")
            response = None
        
        else:
            if response:
                # Convertimos el contenido del mensaje a string
                response_content = response['message']['content']
                # Extraemos los números del contenido
                numeros_extraidos = extract_numbers(response_content)
                return numeros_extraidos
            else:
                print("La respuesta está vacía")
                return None

        self.remove_history()
        return None

    def print_history(self):
        print(self.history)
    def remove_history(self):
        self.history = self.history[:-1]
    def add_history(self, response_llm):
        self.history.append({"role": "assistant", "content": response_llm })
    def reset_session(self):
        self.history = []