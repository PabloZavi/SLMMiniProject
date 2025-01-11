from lm import LMSession
import utils
from collections import Counter

#[17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
#[1,1,1,1,1,1,1,1,1,1,1,1]
#Quiero que la ordenes de menor a mayor

slm = LMSession()

final_results = []
for i in range(10):
    
    prompt = """
    Tengo la siguiente lista de números:

    [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
    

    Quiero que me digas cuál es el mayor
    """
    results = []

    for i in range(10):
        response = slm.execute(prompt, format="plain")   
        response = utils.extract_numbers(response)
        results.append(response)
        print(i)

    """ for i in results:
        for j in i:
            print(j, end=" ")
        print() """

    #print(results)

    # Convertir listas en tuplas para que sean hashables
    array_tuplas = [tuple(sub_array) for sub_array in results]

    # Usar Counter para contar las ocurrencias
    contador = Counter(array_tuplas)

    # Encontrar la frecuencia máxima
    max_frecuencia = max(contador.values())

    # Obtener los elementos con la frecuencia máxima
    elemento_mas_repetido = [list(elemento) for elemento, cantidad in contador.items() if cantidad == max_frecuencia]
    
    # Tomar el primer elemento más repetido (en caso de empate)
    final_results.append(elemento_mas_repetido)

    # Mostrar los elementos y sus repeticiones
    for elemento, cantidad in contador.items():
        print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")
        
    print("Elemento/s más repetido/s: ", elemento_mas_repetido)

    """ super_array = []
    super_array.append(elemento_mas_repetido)
    
for i in super_array:
        for j in i:
            print(j, end=" ")
        print()
        
# Convertir listas en tuplas para que sean hashables
array_tuplas = [tuple(sub_array) for sub_array in super_array]

# Usar Counter para contar las ocurrencias
contador = Counter(array_tuplas)

# Encontrar la frecuencia máxima
max_frecuencia = max(contador.values())

# Obtener los elementos con la frecuencia máxima
elemento_mas_repetido = [list(elemento) for elemento, cantidad in contador.items() if cantidad == max_frecuencia]

# Mostrar los elementos y sus repeticiones
for elemento, cantidad in contador.items():
    print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")
    
print("Elemento más repetido: ", elemento_mas_repetido) """


print("\nResultados más repetidos de cada iteración externa:")
for i, result in enumerate(final_results, 1):
    print(f"Iteración {i}: {result}")

""" # Convertir listas en tuplas para contar ocurrencias entre los resultados externos
array_tuplas_final = [tuple(sub_array) for sub_array in final_results]

# Usar Counter para contar ocurrencias finales
contador_final = Counter(array_tuplas_final) """


# Aplanar la lista de resultados para el conteo final
resultados_aplanados = [tuple(sub_array) for sublist in final_results for sub_array in sublist]

# Usar Counter para contar ocurrencias entre los resultados aplanados
contador_final = Counter(resultados_aplanados)

# Encontrar la frecuencia máxima en los resultados finales
max_frecuencia_final = max(contador_final.values())

# Obtener los elementos con la frecuencia máxima en los resultados finales
elemento_mas_repetido_final = [list(elemento) for elemento, cantidad in contador_final.items() if cantidad == max_frecuencia_final]

# Mostrar los resultados finales
print("\nConteo final de elementos más repetidos:")
for elemento, cantidad in contador_final.items():
    print(f"Cantidad: {cantidad}, Elemento: {list(elemento)}")

print("\nElemento(s) más repetido(s) entre los más repetidos:", elemento_mas_repetido_final)