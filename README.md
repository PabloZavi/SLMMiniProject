# SMLs

## Breve Introducción

Los Small Language Models (SMLs) se pueden ejecutar localmente sin necesidad de tener conexión a internet, ocupando menos recursos. Esta es una ventaja importante, aunque la desventaja es que, al ocupar poco espacio (para poder ser descargados y ejecutados localmente), tienen menos parámetros que un LLM, lo cual resulta en menor capacidad y precisión.

### **Actualización Importante**

En diciembre de 2024, a partir de la versión 0.5.0, Ollama incorporó los "structured outputs" para recibir las respuestas en un JSON con un formato específico configurado por nosotros. 

- **Antes**: La información se recibía en formato de texto libre y había que procesar las respuestas con funciones propias para extraer los datos necesarios. Esto requería lidiar con respuestas inconsistentes.
- **Ahora**: Con los "structured outputs" podemos recibir respuestas según un esquema que definamos, permitiendo que los datos sean consistentes y fácilmente parseables. Esto aumenta la consistencia de las respuestas. Aunque, si las respuestas no se adhieren al esquema, se puede devolver un objeto vacío, lo cual puede no ser conveniente en algunos casos.

_Podemos usar tanto el enfoque anterior como el nuevo enfoque al utilizar Ollama._

### **Recomendaciones según la Documentación**

Para un uso fiable de los "structured outputs", considera lo siguiente:

- Usa **Pydantic** para definir el esquema de la respuesta (Pydantic es para la validación de datos).
- Añade "return as JSON" al prompt para ayudar al modelo a entender la solicitud.
- Establece la temperatura en 0 para obtener salidas más determinísticas.

## Resumen: Ventajas y Desventajas de un SML

### Ventajas

- **Privacidad**: Se ejecuta en local.
- **Sin costo**: No es necesario pagar por un servicio externo.
- **Independencia de la conexión a internet**.

### Desventajas

- **Menos parámetros que un LLM**, lo cual resulta en...
- **Resultados menos precisos**.

## Resumen de la Investigación

### Modelo Usado

Herramienta de modelos --> Ollama versión 0.5.7.
Modelo utilizado --> llama3.2

### Ejercicios Numéricos para Probar el Modelo

- Ordenamiento de listas de números.
- Encontrar el mayor número de un array.
- Calcular el promedio de un array.

### Restricciones

- Los números pueden ser enteros o decimales.
- Pueden ser tanto positivos como negativos.
- Pueden estar repetidos.

### Objetivos

- Descubrir cuán bueno es un SML para resolver ciertos problemas algorítmicos.
- Si no tienen buen desempeño, ver cómo mejorar los resultados.

### Pasos para Ejecutar Ollama en un Ordenador

1. Descargar Ollama en [Ollama](https://ollama.com/). Con esta herramienta podremos descargar modelos y consultarlos localmente, como se detalla en los puntos siguientes.
2. En la misma página, buscar el modelo deseado para descargar (en este caso, el modelo llama 3.2).
3. Copiar el comando para instalar el modelo en nuestra computadora (en nuestro caso 'ollama run llama3.2').
4. Abrir una terminal en nuestra computadora y ejecutar el comando copiado.
   - Se instalará el modelo y ya podrá ser consultado en local.
   - Si queremos, podemos usar el modelo en la terminal, ejecutando el mismo comando del punto 4.
5. En nuestro caso, usaremos los archivos que están en este proyecto, principalmente el `main.py`, el cual será usado para experimentar, cambiando las instrucciones, los parámetros, añadiendo funcionalidades, etc. Todo esto con el objetivo de probar el modelo y mejorarlo, según lo que se detalló en los ejercicios y restricciones.
6. Instalar la librería Ollama con `pip install -U ollama`.
7. Ejecutar el archivo deseado (`python main01.py` o `python main02.py`).

### Metodología

Se podrán ver dos archivos principales:

- `main01.py`: Este fue el archivo inicial donde se empezaron a probar diferentes cosas en bruto, primando el enfoque de prueba/error más que la limpieza del código.
- `main02.py`: En este archivo se mejoró el código modularizándolo, quitando duplicaciones y haciéndolo más claro. Inclusive se agrega la opción de Timeout para continuar con la ejecución si una respuesta demora mucho.

La metodología aplicada fue:

1. Se hace un ciclo de 10 iteraciones, donde cada iteración da una respuesta numérica.
   - Se compara la respuesta de cada iteración con la respuesta correcta.
   - Si la respuesta de la iteración coincide con la respuesta correcta, se contabiliza.
2. Del conjunto de 10 respuestas del ciclo, se elige la respuesta que más se repite.
   - Se compara la respuesta más elegida del ciclo con la respuesta correcta.
   - Si la respuesta más elegida del ciclo coincide con la respuesta correcta, se contabiliza.
3. Este proceso se repite a su vez 10 veces.
4. De cada ciclo se elige una respuesta (la más repetida), al haber 10 ciclos, son 10 respuestas. La respuesta más repetida (sería como la respuesta más repetida entre las respuestas más repetidas) se elige como respuesta final.
5. Se compara dicha respuesta final con la respuesta correcta. Si coincide, se informa el acierto.
6. Además, se brindan los siguientes cálculos:
   - La cantidad de respuestas totales correctas y su porcentaje (sin importar a qué ciclos pertenecen).
   - La cantidad de respuestas correctas por ciclo y su porcentaje.

### Resultados

#### Mayor Número

**Prompt:** Tengo la siguiente lista de números: [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2] Quiero que me digas cuál es el mayor. La respuesta tiene que ser un solo número.

| Iteración | Resp Ind Correctas | Loops c/ resp correctas | Res Final Correcto? |
|-----------|--------------------|-------------------------|---------------------|
| 1         | 81/100             | 10/10                   | Sí                  |
| 2         | 80/100             | 10/10                   | Sí                  |
| 3         | 77/100             | 10/10                   | Sí                  |
| 4         | 77/100             | 10/10                   | Sí                  |
| 5         | 81/100             | 10/10                   | Sí                  |
| 6         | 77/100             | 10/10                   | Sí                  |
| 7         | 81/100             | 10/10                   | Sí                  |
| 8         | 77/100             | 10/10                   | Sí                  |
| 9         | 80/100             | 10/10                   | Sí                  |
| 10        | 69/100             | 10/10                   | Sí                  |

#### Ordenamiento de Lista de Números Iguales

**Prompt:** Tengo la siguiente lista de números: [1,1,1,1,1,1,1,1,1,1,1,1] Quiero que la ordenes de menor a mayor

| Iteración | Resp Ind Correctas | Loops c/ resp correctas | Res Final Correcto? |
|-----------|--------------------|-------------------------|---------------------|
| 1         | 19/100             | 5/10                    | Sí                  |
| 2         | 16/100             | 4/10                    | Sí                  |
| 3         | 20/100             | 5/10                    | Sí                  |
| 4         | 19/100             | 5/10                    | Sí                  |
| 5         | 22/100             | 6/10                    | Sí                  |
| 6         | 4/100              | 0/10                    | No                  |
| 7         | 16/100             | 5/10                    | Sí                  |
| 8         | 14/100             | 5/10                    | No                  |
| 9         | 26/100             | 7/10                    | Sí                  |
| 10        | 14/100             | 8/10                    | Sí                  |

#### Ordenamiento de Lista de Números Mixtos

**Prompt:** Tengo la siguiente lista de números: [17, -3.5, 19, 8, -12.1, 5, 14.8, -1, 20, 9.3, -6, 15.5, 2, -11, 18, 13.7, -10, 4, -7.2] Quiero que la ordenes de menor a mayor

| Iteración | Resp Ind Correctas | Loops c/ resp correctas | Res Final Correcto? |
|-----------|--------------------|-------------------------|---------------------|
| 1         | 5/100              | 1/10                    | No                  |
| 2         | 5/100              | 2/10                    | Sí                  |
| 3         | 7/100              | 1/10                    | Sí                  |
| 4         | 2/100              | 0/10                    | No                  |
| 5         | 6/100              | 2/10                    | No                  |
| 6         | 8/100              | 4/10                    | Sí                  |
| 7         | 6/100              | 2/10                    | No                  |
| 8         | 6/100              | 4/10                    | Sí                  |
| 9         | 7/100              | 5/10                    | Sí                  |
| 10        | 4/100              | 1/10                    | Sí                  |

#### Cálculo del Promedio

**Prompt:**
  Tengo la siguiente lista de números:
  [5, -12.3, 19, 8, -7.5, 14, 2.6, -1, 20, 9, -3.2, 15, -11, 18.4, -6, 4.5, -10, 12, -4.7, 16]
  Quiero saber cuál es el promedio. La respuesta tiene que ser un solo número. Solo muéstrame el resultado, no los cálculos

<table>
  <tr>
    <th>Iteración</th>
    <th>Resp Ind Correctas</th>
    <th>Loops c/ resp correctas</th>
    <th>Res Final Correcto?</th>
  </tr>
  <tr>
    <td colspan="4" align="center">Todas las respuestas en todas las iteraciones fueron incorrectas</td>
  </tr>
</table>


### **Conclusiones**

- Se comprueba que el modelo no es muy bueno para trabajar con ejercicios numéricos, ya que retorna respuestas inexactas en un porcentaje bastante alto, llegando a veces a superar el 50% de respuestas equivocadas, más que todo cuando se trata de números decimales, repetidos, o mezclados entre positivos y negativos. Después se fue viendo que con otros ejercicios, el porcentaje llegaba al 0% la mayoría de las veces (ver detalle a continuación).
- En el ejercicio de ordenar una lista de 12 números iguales (todos eran 1), el desempeño fue muy malo, como se puede ver en los resultados.
- Por esto mismo se prueba también ordenar una lista de números, pero diferentes entre sí (19 números).
- Se hizo también una variación del ejercicio de ordenar 12 números 1, poniendo un 2 en alguna posición.
- Al tratar de ver el porqué de tantas respuestas incorrectas en algunos ejercicios (principalmente el de ordenar una lista con números iguales o la variante con sólo un número diferente), se le pedía lo mismo pero a través de la terminal, tratando de ver las respuestas completas, y lo que a veces sucedía es que el modelo nos contestaba con una respuesta más "conversacional", repitiendo lo que le pedimos, o dándonos sugerencias, y estas cosas se tomaban como respuestas finales, por lo que se modificó el prompt para pedirle que sólo nos diera la respuesta final, sin sugerencias ni comentarios, e igual lo que devolvía era ineficiente, incluso más que antes de las modificaciones en los prompts.
- También se notó que al pedirle al modelo que por favor revisara las respuestas, o incluso inducir que podría haberse equivocado, aunque sin darle la respuesta final, en algunos casos se daba cuenta, y cuando después se le volvía a pedir el mismo ejercicio, acertaba algunas veces más, pero después volvía al comportamiento ineficiente de vuelta. Incluso cuando se le decía que la respuesta posible estaba entre tres opciones dadas (la mayoría de las veces daba respuestas fuera de esas opciones).

### **Pasos a Seguir**

- Usando varios modelos, llevar un registro de análisis de porcentaje de respuestas correctas de forma individual y por ciclo para hacer un ranking de fiabilidad de modelos para este tipo de ejercicios numéricos.
- Ver la posibilidad de probar con modelos recientes, como el lanzado en enero de 2025 llamado "DeepSeek-R1", el cual tiene versiones desde 1.5 a 671 billones de parámetros.
- Investigar qué modelos están más orientados a problemas con números, ya que por lo general, la mayoría de los modelos, incluso los más conocidos, como ChatGPT o Copilot, tienen problemas para resolver ejercicios básicos como los que se han tratado acá.
