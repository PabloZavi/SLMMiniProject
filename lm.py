import requests
import json
import random

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
            response = requests.post(self.url, json=data, timeout=240)
            response.raise_for_status()  
        except requests.Timeout:
            print("La solicitud ha excedido el tiempo límite de espera.")
        except requests.ConnectionError:
            print("Error de conexión. Verifica la URL o tu conexión a internet.")
        except requests.HTTPError as http_err:
            print(f"Error HTTP: {http_err}")
        except requests.RequestException as req_err:
            print(f"Error en la solicitud: {req_err}")
        else:
            response_data = response.json()
            if 'message' in response_data and 'content' in response_data['message']:
                return response_data['message']['content']
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

