Se trabaja en local con el SML Llama 0.5.4.

Se lo prueba para trabajar con ejercicios numéricos:
- Ordenamiento de listas de números.
- Encontrar el mayor número de un array.
- Calcular el promedio de un array.

Se aclara que los números pueden ser enteros o decimales, estar repetidos y pueden ser tanto positivos como negativos.

Se comprueba que el modelo no es muy bueno para trabajar con ellos, ya que retorna respuestas inexactas en un porcentaje bastante alto, llegando a veces a superar el 50% de respuestas equivocadas, más que todo cuando se trata de números decimales, repetidos, o mezclados entre positivos y negativos.

Se prueba un enfoque de repetir el mismo prompt varias veces, almacenando cada resultado y después viendo cuáles respuestas fueron las más repetidas, de las cuales se termina eligiendo sólo una, la que más veces se repitió.

Este proceso se repite a su vez varias veces más pero ya sobre las que se eligieron en el bucle anterior (sería como las más elegidas de las más elegidas), ya que se comprueba que ofrece mayor fiabilidad.

Cosas a analizar:
- Usar probabilidad?
- Sacar estadística de resultados diferentes? 
- Se podría analizar la cantidad de respuestas iguales, y a menor cantidad de repeticiones, menos fiable es el modelo.

