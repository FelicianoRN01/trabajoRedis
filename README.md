# Enunciado de lo trabajo de Redis

# Trabajo: Aplicación en Python con Redis

## Descripción
Debemos desarrollar una aplicación en Python que utilice Redis para implementar diversas funcionalidades relacionadas con la gestión de datos. La aplicación debe estar vinculada con la empresa de negocio del tema 1 y debe cumplir con los siguientes requisitos:

---

## Requisitos y Funcionalidades

1. **Crear registros clave-valor**  
   *Puntuación*: 0.5 puntos  
   Desarrollar una funcionalidad que permita insertar registros en Redis utilizando claves y valores.

2. **Obtener y mostrar el número de claves registradas**  
   *Puntuación*: 0.5 puntos  
   Contar todas las claves almacenadas en Redis y mostrar el resultado.

3. **Obtener y mostrar un registro en base a una clave**  
   *Puntuación*: 0.5 puntos  
   Recuperar el valor asociado a una clave específica.

4. **Actualizar el valor de una clave y mostrar el nuevo valor**  
   *Puntuación*: 0.5 puntos  
   Modificar el valor de una clave existente y mostrar el nuevo contenido.

5. **Eliminar una clave-valor y mostrar la clave y el valor eliminado**  
   *Puntuación*: 0.5 puntos  
   Eliminar un registro de Redis y mostrar la clave y el valor eliminados.

6. **Obtener y mostrar todas las claves guardadas**  
   *Puntuación*: 0.5 puntos  
   Listar todas las claves almacenadas en Redis.

7. **Obtener y mostrar todos los valores guardados**  
   *Puntuación*: 0.5 puntos  
   Listar todos los valores almacenados en Redis.

8. **Obtener y mostrar varios registros con una clave con un patrón en común usando `*`**  
   *Puntuación*: 0.5 puntos  
   Filtrar y recuperar claves que coincidan con un patrón utilizando el wildcard `*`.

9. **Obtener y mostrar varios registros con una clave con un patrón en común usando `[]`**  
   *Puntuación*: 0.5 puntos  
   Recuperar registros que coincidan con un patrón definido por `[]`.

10. **Obtener y mostrar varios registros con una clave con un patrón en común usando `?`**  
    *Puntuación*: 0.5 puntos  
    Filtrar y recuperar claves que coincidan con un patrón utilizando el wildcard `?`.

11. **Obtener y mostrar varios registros y filtrarlos por un valor en concreto**  
    *Puntuación*: 0.5 puntos  
    Filtrar claves en Redis según un valor específico.

12. **Actualizar una serie de registros en base a un filtro**  
    *Puntuación*: 0.5 puntos  
    Modificar múltiples registros que coincidan con un filtro. Ejemplo: aumentar un valor numérico en 1.

13. **Eliminar una serie de registros en base a un filtro**  
    *Puntuación*: 0.5 puntos  
    Borrar varios registros según un filtro específico.

14. **Crear una estructura en JSON de array de los datos que vayáis a almacenar**  
    *Puntuación*: 0.5 puntos  
    Definir una estructura en formato JSON y almacenarla en Redis.

15. **Realizar un filtro por cada atributo de la estructura JSON anterior**  
    *Puntuación*: 0.5 puntos  
    Aplicar filtros sobre los atributos del JSON almacenado.

16. **Crear una lista en Redis**  
    *Puntuación*: 0.5 puntos  
    Crear una lista en Redis con múltiples elementos.

17. **Obtener elementos de una lista con un filtro en concreto**  
    *Puntuación*: 0.5 puntos  
    Filtrar elementos de una lista según un criterio específico.

18. **Explorar otras formas de almacenar datos en Redis**  
    *Puntuación*: 1.5 puntos  
    Seleccionar dos tipos de estructuras avanzadas de Redis (Set, Hashes, SortedSet, Streams, Geospatial, Bitmaps, Bitfields, Probabilistic, Time Series) y:  
    - Crear una función que permita guardar datos en estas estructuras.  
    - Crear otra función que recupere estos datos.

---

## Requisitos del Entregable

1. **Archivo Python**:  
   - Debe implementar todas las funcionalidades descritas.  
   - Cada funcionalidad debe estar claramente identificada, explicando qué hace y mostrando los resultados obtenidos.  
   - El código no debe generar errores.

2. **Repositorio en Git**:  
   - Subir el proyecto a un repositorio en Git.  
   - Proporcionar el enlace al repositorio.
