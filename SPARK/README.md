# Primera clase

- Spark -> procesamiento de datos
- HDFS --> sistema distruibuido de ficheros.

## Apache spark

Claves de spark:

- Es muy rápido, se almacena la infromación en los workers. No escribimos en disco cada vez.
- Es muy acesible. Permite muchos lenguajes de programación.
- Tiene un shell iteractiva. Permite hacer pruebas más rápidas.
- Mejora de productividad. Nos centramos más en la lógica que en el código.

¿Cuándo utilizamos spark?

- Para procesar datasets gigantes.
- Querys iteractivas.
- Maching learning.
- `End to end` de diversas fuentes de datos.

## RDD

---

Estructura básica de datos de spark

- Son inmutables.
- Esta particionado
- Acciones
- Transformaciones: nos dan otro RDD pero no implica que nos devuelva nada. Spark recuerda toda la linea de transformaciones que vamos haciendo.
