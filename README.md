Se trabaja en local con el SML Llama 0.5.4.
Se lo prueba para trabajar con números. 
Se comprueba que el modelo no es muy bueno para trabajar con ellos, ya que retorna respuestas inexactas en un porcentaje bastante alto, llegando a veces a superar el 50% de respuestas equivocadas, más que todo cuando se trata de números decimales, repetidos, o mezclados entre positivos y negativos.
Se prueba un enfoque de repetir el mismo prompt varias veces, almacenando cada resultado y después viendo cuáles respuestas fueron las más repetidas, de las cuales se termina eligiendo sólo una, la que más veces se repitió.
Este proceso se repite a su vez varias veces más pero ya sobre las que se eligieron en el bucle anterior (sería como las más elegidas de las más elegidas), ya que se comprueba que ofrece mayor fiabilidad.

