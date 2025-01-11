import re

def extract_numbers(input_string):
    """
    Extrae todos los números enteros y decimales, positivos y negativos, de un string.

    Args:
        input_string (str): El texto de entrada.

    Returns:
        list: Una lista con los números extraídos (floats o ints).
    """
    # Expresión regular para encontrar números (enteros y decimales, positivos y negativos)
    pattern = r"-?\d+\.?\d*"
    matches = re.findall(pattern, input_string)
    # Convertir los resultados a números (int o float)
    numbers = [float(num) if '.' in num else int(num) for num in matches]
    return numbers