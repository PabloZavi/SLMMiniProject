from lmStructuredOutputs import LMSession
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def execute_with_timeout(slm, prompt, timeout):
    """Executes the prompt with a timeout. Returns an empty array if it exceeds the time limit."""
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(slm.execute, prompt, format="plain")
        try:
            return future.result(timeout=timeout)
        except TimeoutError:
            print("Timeout reached! Returning an empty array for this response.")
            return []
        finally:
            # Ensures resources are released immediately
            executor.shutdown(wait=False)


def get_response_accuracy(slm, prompt, correct_response, iterations, timeout):
    """Execute the prompt multiple times and calculate accuracy."""
    results = []
    for _ in range(iterations):
        response = execute_with_timeout(slm, prompt, timeout=timeout)
        print(f"Response: {response}")
        results.append(response)
    correct_count = sum(1 for r in results if r == correct_response)
    return results, correct_count


def find_most_frequent_responses(results):
    """Find the most frequent responses from a list of results."""
    response_tuples = [tuple(r) for r in results]
    frequency_count = Counter(response_tuples)
    max_frequency = max(frequency_count.values())
    most_frequent = [list(k)
                     for k, v in frequency_count.items() if v == max_frequency]
    return most_frequent, frequency_count


def display_frequency_analysis(frequency_count):
    """Display the frequency analysis in the desired format."""
    for response_tuple, count in frequency_count.items():
        response_list = list(response_tuple)
        print(f"Cantidad: {count}, Elemento: {response_list}")


def main():
    # Initial setup
    slm = LMSession()
    # TODO Used prompt
    prompt = """
    Tengo la siguiente lista de números:
    [1,1,1,1,1,1,1,1,1,2,1,1]
    Quiero que la ordenes de menor a mayor
    Muestrame como respuesta sólo la lista con el resultado final con los números ordenados de
    menor a mayor, no comentarios tuyos o repetición de lo que te pedí. Tampoco sugerencias.
    """
    # TODO Put Correct answer
    correct_response = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    # TODO Put the number of iterations
    external_iterations = 10
    internal_iterations = 10
    # TODO Put Timeout
    timeout = 10

    # Track performance
    individual_correct_count = 0
    loop_correct_count = 0
    final_results = []

    for i in range(external_iterations):
        print(f"\nIteration {i + 1}/{external_iterations}:")
        # Get individual responses and their accuracy
        results, correct_count = get_response_accuracy(
            slm, prompt, correct_response, internal_iterations, timeout)
        individual_correct_count += correct_count

        # Find the most frequent result
        most_frequent, frequency_count = find_most_frequent_responses(results)
        final_results.append(most_frequent)

        # Display frequency analysis
        print("\nFrequency Analysis:")
        display_frequency_analysis(frequency_count)

        # Check if the most frequent result matches the correct response
        if correct_response in most_frequent:
            loop_correct_count += 1
        print(f"\nElemento/s más repetido/s: {most_frequent}")

    # Analyze the final aggregated results
    flattened_results = [tuple(sublist)
                         for sublist in final_results for sublist in sublist]
    final_most_frequent, final_frequency_count = find_most_frequent_responses(
        flattened_results)

    # Display final results
    print("\nFinal Analysis:")
    print(f"Correct individual responses: {
          individual_correct_count}/{external_iterations * internal_iterations}")
    print(f"Loops with correct results: {
          loop_correct_count}/{external_iterations}")
    print("\nMost frequent response across all loops:", final_most_frequent[0])
    if final_most_frequent[0] == correct_response:
        print("The final result is correct! :)")
    else:
        print("The final result is incorrect :(")


if __name__ == "__main__":
    main()


#! Prompt para ordenar de menor a mayor una lista con los mismos números
""" 
Tengo la siguiente lista de números:
[1,1,1,1,1,1,1,1,1,1,1,1]
Quiero que la ordenes de menor a mayor
"""
# Respuesta correcta: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


#! Prompt para ordenar de menor a mayor una lista con diferentes números
""" 
Tengo la siguiente lista de números:
[17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2]
Quiero que la ordenes de menor a mayor
"""
# Respuesta correcta: [-12.1, -11, -10, -7.2, -6, -3.5, -1, 2, 4, 5, 8, 9.3, 13.7, 14.8, 15.5, 17, 18, 19, 20]


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
Solo muestrame el resultado, no los calculos
"""
# Respuesta correcta: [4.39]
