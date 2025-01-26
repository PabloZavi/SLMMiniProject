from lmStructuredOutputs import LMSession
from collections import Counter

def contar_ocurrencias(lista):
    # Convierte listas en tuplas para que sean hashables y cuenta las ocurrencias
    array_tuplas = [tuple(sub_array) for sub_array in lista]
    return Counter(array_tuplas)

def obtener_elemento_mas_repetido(contador):
    # Encuentra la frecuencia máxima y los elementos con esa frecuencia
    max_frecuencia = max(contador.values())
    elementos = [list(elemento) for elemento, cantidad in contador.items() if cantidad == max_frecuencia]
    return elementos[0] if len(elementos) == 1 else elementos

def realizar_pruebas(slm, prompt, correct_response, num_iteraciones=10):
    counter_correct_resp_individual = 0
    final_results = []
    aciertos_por_iteracion = []

    for _ in range(num_iteraciones):
        responses = [(slm.execute(prompt, format="plain")) for _ in range(10)]
        print("Respuestas en la iteración actual:", responses)
        correctos_individuales = sum(1 for resp in responses if resp == correct_response)
        counter_correct_resp_individual += correctos_individuales
        contador = contar_ocurrencias(responses)
        elemento_mas_repetido = obtener_elemento_mas_repetido(contador)
        print("Elemento(s) más repetido(s) en la iteración actual:", elemento_mas_repetido)
        final_results.append(elemento_mas_repetido)
        aciertos_por_iteracion.append(correctos_individuales / 10 * 100)

    return counter_correct_resp_individual, final_results, aciertos_por_iteracion

def imprimir_resultados(contador):
    for elemento, cantidad in contador.items():
        print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")

def main():
    slm = LMSession()
    prompt = """
    Tengo la siguiente lista de números:
    [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
    Quiero que me digas cuál es el mayor. La respuesta tiene que ser un solo número.
    """
    #!Poner cuál sería la respuesta correcta!
    correct_response = [20]

    counter_correct_resp_individual, final_results, aciertos_por_iteracion = realizar_pruebas(slm, prompt, correct_response)
    contador_final = contar_ocurrencias(final_results)
    elemento_mas_repetido_final = obtener_elemento_mas_repetido(contador_final)

    imprimir_resultados(contador_final)
    print("\nElemento(s) más repetido(s) entre los más repetidos:", elemento_mas_repetido_final)
    
    if elemento_mas_repetido_final == correct_response:
        print("El resultado final es la Respuesta correcta!!\n")

    print("Respuestas correctas de forma individual (de un total de 100): ", counter_correct_resp_individual)
    print("Porcentaje de respuestas correctas de forma individual: ", round((counter_correct_resp_individual / 100) * 100, 2), "%")

    print("\nPorcentaje de aciertos por iteración:")
    for i, porcentaje in enumerate(aciertos_por_iteracion, 1):
        print(f"Iteración {i}: {porcentaje}%")
    
if __name__ == "__main__":
    main()
    
    
#! Prompt para ordenar de menor a mayor
""" 
Tengo la siguiente lista de números:
[1,1,1,1,1,1,1,1,1,1,1,1]
Quiero que la ordenes de menor a mayor
"""
# Respuesta correcta: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Otra lista de números para pruebas:
# [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]

#! Prompt para encontrar el número más alto
"""
Tengo la siguiente lista de números:
[17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
Quiero que me digas cuál es el mayor. 
La respuesta tiene que ser un solo número.
"""
# Respuesta correcta: [20]

#! Prompt para el promedio
"""
Tengo la siguiente lista de números:
[5, -12.3, 19, 8, -7.5, 14, 2.6, -1, 20, 9, -3.2, 15, -11, 18.4, -6, 4.5, -10, 12, -4.7, 16]
Quiero saber cuál es el promedio. 
La respuesta tiene que ser un solo número.
"""
# Respuesta correcta: [5.525]
