# SMLs

## Breve introducción

Los Small Language Model (SML), se pueden ejecutar en local sin necesidad de tener conexión a internet, ocupando menos recursos, lo cual es una ventaja, aunque la desventaja es que al ocupar poco espacio (para poder ser descargado y ejecutado en local), es que tiene muchos menos parámetros que un LLM, lo cual lleva a tener menos capacidad y resultados menos precisos.

**Actualización importante! -->**
En diciembre de 2024 Ollama incorporó los "structured outputs" para recibir las respuestas en un json con un formato específico configurado por nosotros.
Antes se recibía la información en formato de texto libre y había que procesar con funciones propias las respuestas para extraer los datos que necesitábamos.
Ahora con los structured outputs podemos recibir según un esquema JSON, con la estructura que definamos en el mismo, las respuestas, permitiendo que los datos sean consistentes y fácilmente parseables pudiendo manejar la información de manera más eficiente.
*Aclaración*: Para no cambiar todo el código, se adaptó parte de la funcionalidad anterior a las nuevas formas de comunicarse con el modelo, pero se sigue usando la función dentro de 'utils' para extraer los números de las respuestas.

**Recomendaciones según la documentación**
For reliable use of structured outputs, consider to:
- Use 'Pydantic' to define the schema for the response
- Add “return as JSON” to the prompt to help the model understand the request
- Set the temperature to 0 for more deterministic outpu

**Resumen ventajas de un SML**
- Privacidad, al ejecutarse en local.
- Sin costo, al no pagar un servicio externo.
- No es necesaria la conexión a internet.

**Resumen desventajas de un SML**
- Menos parámetros que un LLM, por ende...
- Resultados menos precisos.

## Resumen investigación
#### Modelo usado:
Se trabaja en local con el SML Llama 0.5.7.

#### Ejercicios numéricos para probar el modelo
- Ordenamiento de listas de números
- Encontrar el mayor número de un array
- Calcular el promedio de un array

#### Restricciones
- Los números pueden ser enteros o decimales
- Pueden ser tanto positivos como negativos
- Pueden estar repetidos

#### Objetivos
- Descubrir cuán bueno es un SML para resolver ciertos problemas algorítmicos.
- Si no tienen buen desempeño, ver cómo mejorar los resultados.

**Pasos para ejecutar Ollama en un ordenador**
1. Descargar Ollama en [Ollama](https://ollama.com/). Con esta herramienta podremos descargar modelos y consultarlos localmente, como se detalla en los puntos siguientes.
2. En la misma página, buscar el modelo deseado para descargar (en este caso, el modelo llama 3.2)
3. Copiar el comando para instalar el modelo en nuestra computadora (en nuestro caso 'ollama run llama3.2').
4. Abrir una terminal en nuestra computadora y ejecutar el comando copiado.
   a. Se instalará el modelo y ya podrá ser consultado en local.
   b. Si queremos, podemos usar el modelo en la terminal, ejecutando el mismo comando del punto 4. 
5. En nuestro caso usaremos los archivos que están en este proyecto, principalmente el main.py, el cual será usado para experimentar, cambiando las instrucciones, los parámetros, añadiendo funcionalidades, etc. Todo esto con el objetivo de probar el modelo y mejorarlo, según lo que se detalló en los ejercicios y restricciones.
6. Instalar la librería Ollama --> pip install -U ollama
7. Ejecutar el archivo deseado (python main01.py || python main02.py)


**Metodología**
Se podrán ver dos archivos pricipales:
main01.py --> Este fue el archivo inicial donde se empezaron a probar diferentes cosas en bruto, primando lo prueba/error más que la limpieza del código.
main02.py --> En este archivo se mejoró el código modularizandoló, quitando duplicaciones y haciendoló más claro.

La metodología aplicada fue:
1. Se hace un ciclo de 10 iteraciones, donde cada iteración da una respuesta numérica.
   1.a. Se compara la respuesta de cada iteración con la respuesta correcta.
   1.b. Si la respuesta de la iteración coincide con la respuesta correcta, se contabiliza. 
2. Del conjunto de 10 respuestas del ciclo, se elige la respuesta que más se repite.
   2.a. Se compara la respuesta más elegida del ciclo con la respuesta correcta.
   2.b. Si la respuesta más elegida del ciclo coincide con la respuesta correcta, se contabiliza. 
3. Este proceso se repite a su vez 10 veces.
4. De cada ciclo se elige una respuesta (la más repetida), al haber 10 ciclos, son 10 respuestas. La respuesta más repetida (sería como la respuesta más repetida entre las respuestas más repetidas) se elige como respuesta final.
5. Se compara dicha respuesta final con la respuesta correcta. Si coincide, se informa el acierto.
6. Además se brindan los siguientes cálculos:
   6.a. La cantidad de respuestas totales correctas y su porcentaje (sin importar a qué ciclos pertenecen).
   6.b. La cantidad de respuestas correctas por ciclo y su porcentaje.

**Conclusiones**
- El código hecho en el archivo 'main02.py' es mucho más eficiente que el del archivo 'main01.py', a pesar de que se usan los mismos prompts.
- Se comprueba que el modelo no es muy bueno para trabajar con ejercicios numéricos, ya que retorna respuestas inexactas en un porcentaje bastante alto, llegando a veces a superar el 50% de respuestas equivocadas (esto termina siendo relativo, según el archivo usado de los dos que se detallaron en el punto anterior), más que todo cuando se trata de números decimales, repetidos, o mezclados entre positivos y negativos.

**A analizar**
- Usando varios modelos, llevar un registro de análisis de porcentaje de respuestas correctas de forma individual y por ciclo para hacer un ranking de fiabilidad de modelos para este tipo de ejercicios numéricos.
