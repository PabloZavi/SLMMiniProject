import re

# Se modifica el método original para limitar a 40 números la extracción, 
# ya que había casos en los que el modelo devolvía una cantidad muy grande de números,
# haciendo que el proceso fuera muy poco eficiente.

def extract_numbers(input_string):
    """
    Extrae, si es el caso, hasta 40 números enteros y decimales, positivos y negativos, de un string.

    Args:
        input_string (str): El texto de entrada.

    Returns:
        list: Una lista con los números extraídos (floats o ints), limitada a 40 números.
    """
    # Expresión regular para encontrar números (enteros y decimales, positivos y negativos)
    pattern = r"-?\d+\.?\d*"
    matches = re.findall(pattern, input_string)
    # Limitar los resultados a los primeros 40 números
    limited_matches = matches[:40]
    # Convertir los resultados limitados a números (int o float)
    numbers = [float(num) if '.' in num else int(num)
               for num in limited_matches]
    return numbers


def convert_chat_response_to_plain_text(chat_response):
    plain_text = ""
    plain_text += f"{chat_response}\n"
    return plain_text
