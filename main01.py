from lmStructuredOutputs import LMSession
from collections import Counter



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


slm = LMSession()

counterCorrectRespIndividual = 0
counterCorrectRespLoop = 0


final_results = []
for i in range(10):

    prompt = """
    Tengo la siguiente lista de números:

    [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
    
    Quiero que me digas cuál es el mayor. La respuesta tiene que ser un solo número.
    
    """
    #!Poner cuál sería la respuesta correcta!
    correctResponse = [20]

    results = []

    for i in range(10):
        response = slm.execute(prompt, format="plain")
        print(response)
        if response == correctResponse:
            counterCorrectRespIndividual += 1
        results.append(response)
        # print(i)

    for i in results:
        for j in i:
            print(j, end=" ")
        print()

    print(results)

    # Convertir listas en tuplas para que sean hashables
    array_tuplas = [tuple(sub_array) for sub_array in results]

    # Usar Counter para contar las ocurrencias
    contador = Counter(array_tuplas)

    # Encontrar la frecuencia máxima
    max_frecuencia = max(contador.values())

    # Obtener los elementos con la frecuencia máxima
    elemento_mas_repetido = [list(
        elemento) for elemento, cantidad in contador.items() if cantidad == max_frecuencia]
    # elemento_mas_repetido = elemento_mas_repetido[0]
    if elemento_mas_repetido == correctResponse:
        counterCorrectRespLoop += 1

    # Tomar el primer elemento más repetido (en caso de empate)
    final_results.append(elemento_mas_repetido)

    # Mostrar los elementos y sus repeticiones
    for elemento, cantidad in contador.items():
        print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")

    print("Elemento/s más repetido/s: ", elemento_mas_repetido)

    super_array = []
    super_array.append(elemento_mas_repetido)

for i in super_array:
    for j in i:
        print(j, end=" ")
    print()

# Convertir listas en tuplas para que sean hashables
array_tuplas = [tuple(tuple(sub_element) if isinstance(sub_element, list)
                      else sub_element for sub_element in sub_array) for sub_array in super_array]
# array_tuplas = [tuple(sub_array) for sub_array in super_array]

# Usar Counter para contar las ocurrencias
contador = Counter(array_tuplas)

# Encontrar la frecuencia máxima
max_frecuencia = max(contador.values())

# Obtener los elementos con la frecuencia máxima
elemento_mas_repetido = [list(
    elemento) for elemento, cantidad in contador.items() if cantidad == max_frecuencia]


# Mostrar los elementos y sus repeticiones
for elemento, cantidad in contador.items():
    print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")

print("Elemento más repetido: ", elemento_mas_repetido)


print("\nResultados más repetidos de cada iteración externa:")
for i, result in enumerate(final_results, 1):
    print(f"Iteración {i}: {result}")
    if result[0] == correctResponse:
        counterCorrectRespLoop += 1

# Convertir listas en tuplas para contar ocurrencias entre los resultados externos
# array_tuplas_final = [tuple(sub_array) for sub_array in final_results]
array_tuplas_final = [tuple(tuple(sub_element) if isinstance(
    sub_element, list) else sub_element for sub_element in sub_array) for sub_array in final_results]

# Usar Counter para contar ocurrencias finales
contador_final = Counter(array_tuplas_final)


# Aplanar la lista de resultados para el conteo final
resultados_aplanados = [tuple(sub_array)
                        for sublist in final_results for sub_array in sublist]

# Usar Counter para contar ocurrencias entre los resultados aplanados
contador_final = Counter(resultados_aplanados)

# Encontrar la frecuencia máxima en los resultados finales
max_frecuencia_final = max(contador_final.values())

# Obtener los elementos con la frecuencia máxima en los resultados finales
elemento_mas_repetido_final = [list(
    elemento) for elemento, cantidad in contador_final.items() if cantidad == max_frecuencia_final]
elemento_mas_repetido_final = elemento_mas_repetido_final[0]

# Mostrar los resultados finales
print("\nConteo final de elementos más repetidos:")
for elemento, cantidad in contador_final.items():
    print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")

print("\nElemento(s) más repetido(s) entre los más repetidos:",
      elemento_mas_repetido_final)
if elemento_mas_repetido_final == correctResponse:
    print("\nEl resultado final es la Respuesta correcta!!\n")

print("Respuestas correctas de forma individual (de un total de 100): ",
      counterCorrectRespIndividual)
print("Porcentaje de respuestas correctas de forma individual (de un total de 100): ",
      round(counterCorrectRespIndividual, 2), "%")
print("\nCantidad de loops con respuestas correctas (de un total de 10 loops): ",
      counterCorrectRespLoop)
print("Porcentaje de loops con respuestas correctas (de un total de 10 loops): ",
      round(counterCorrectRespLoop, 2)*10, "%")
