import redis
import json

# Conexión a la base de datos Redis
client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# 1 - Crear registros clave-valor(0.5 puntos)

print("1 - Crear registros clave-valor")

def crear_registro_clave_valor(clave, valor):
    """
    Esta función crea un registro clave-valor en Redis.
    
    Parámetros:
    clave (str): La clave del registro.
    valor (str): El valor del registro.
    
    Resultado:
    Devuelve un mensaje indicando que el registro ha sido creado.
    """
    client.set(clave, valor)
    return f"Registro creado: {clave} -> {valor}"

# Ejemplo de uso
clave = "usuario:1"
valor = json.dumps({
    "nombre": "Juan Perez",
    "edad": 30,
    "profesion": "Ingeniero de Software",
    "ciudad": "Sevilla"
})

resultado = crear_registro_clave_valor(clave, valor)
print(resultado)

clave2 = "usuario:2"
valor2 = json.dumps({
    "nombre": "Maria Lopez",
    "edad": 25,
    "profesion": "Diseñadora Grafica",
    "ciudad": "Madrid"
})

resultado2 = crear_registro_clave_valor(clave2, valor2)
print(resultado2)

clave3 = "usuario:3"
valor3 = json.dumps({
    "nombre": "Diego Martinez",
    "edad": 19,
    "profesion": "Ingeniero de Datos",
    "ciudad": "Sevilla"
})

resultado3 = crear_registro_clave_valor(clave3, valor3)
print(resultado3)

clave4 = "usuario:4"
valor4 = json.dumps({
    "nombre": "Ana Gomez",
    "edad": 28,
    "profesion": "Analista de Datos",
    "ciudad": "Barcelona"
})

resultado4 = crear_registro_clave_valor(clave4, valor4)
print(resultado4)

clave5 = "usuario:5"
valor5 = json.dumps({
    "nombre": "Carlos Ruiz",
    "edad": 35,
    "profesion": "Analista de Datos",
    "ciudad": "Valencia"
})

resultado5 = crear_registro_clave_valor(clave5, valor5)
print(resultado5)

print("=====================================")

# 2 - Obtener y mostrar el número de claves registradas(0.5 puntos)

print("2 - Obtener y mostrar el número de claves registradas")

def obtener_numero_de_claves():
    """
    Esta función obtiene el número de claves registradas en Redis.
    
    Resultado:
    Devuelve el número de claves registradas.
    """
    return client.dbsize()

# Ejemplo de uso
numero_de_claves = obtener_numero_de_claves()
print(f"Número de claves registradas: {numero_de_claves}")
print("=====================================")

# 3 - Obtener y mostrar un registro en base a una clave (0.5 puntos)


print("3 - Obtener y mostrar un registro en base a una clave")

def obtener_registro_por_clave(clave):
    """
    Esta función obtiene un registro en base a una clave en Redis.
    
    Parámetros:
    clave (str): La clave del registro.
    
    Resultado:
    Devuelve el valor del registro si existe, de lo contrario devuelve None.
    """
    valor = client.get(clave)
    if valor:
        return json.loads(valor)
    return None

# Ejemplo de uso
clave_a_buscar = "usuario:1"
registro = obtener_registro_por_clave(clave_a_buscar)
if registro:
    print(f"Registro encontrado para la clave '{clave_a_buscar}': {registro}")
else:
    print(f"No se encontró ningún registro para la clave '{clave_a_buscar}'")
print("=====================================")

# 4 - Actualizar el valor de una clave y mostrar el nuevo valor(0.5 puntos)

print("4 - Actualizar el valor de una clave y mostrar el nuevo valor")

def actualizar_valor_clave(clave, nuevo_valor):
    """
    Esta función actualiza el valor de una clave en Redis.
    
    Parámetros:
    clave (str): La clave del registro.
    nuevo_valor (str): El nuevo valor del registro.
    
    Resultado:
    Devuelve un mensaje indicando que el registro ha sido actualizado.
    """
    if client.exists(clave):
        client.set(clave, nuevo_valor)
        return f"Registro actualizado: {clave} -> {nuevo_valor}"
    else:
        return f"No se encontró ningún registro para la clave '{clave}'"

# Ejemplo de uso
clave_a_actualizar = "usuario:1"
nuevo_valor = json.dumps({
    "nombre": "Juan Perez",
    "edad": 42,
    "profesion": "Ingeniero de Datos",
    "ciudad": "Sevilla"
})

resultado_actualizacion = actualizar_valor_clave(clave_a_actualizar, nuevo_valor)
print(resultado_actualizacion)

# Mostrar el nuevo valor
registro_actualizado = obtener_registro_por_clave(clave_a_actualizar)
if registro_actualizado:
    print(f"Nuevo valor para la clave '{clave_a_actualizar}': {registro_actualizado}")
else:
    print(f"No se encontró ningún registro para la clave '{clave_a_actualizar}'")
print("=====================================")

# 5 - Eliminar una clave-valor y mostrar la clave y el valor eliminado(0.5 puntos)

print("5 - Eliminar una clave-valor y mostrar la clave y el valor eliminado")

def eliminar_clave_valor(clave):
    """
    Esta función elimina un registro clave-valor en Redis.
    
    Parámetros:
    clave (str): La clave del registro.
    
    Resultado:
    Devuelve el valor del registro eliminado si existe, de lo contrario devuelve None.
    """
    valor = client.get(clave)
    if valor:
        client.delete(clave)
        return f"Registro eliminado: {clave} -> {json.loads(valor)}"
    else:
        return f"No se encontró ningún registro para la clave '{clave}'"

# Ejemplo de uso
clave_a_eliminar = "usuario:2"
resultado_eliminacion = eliminar_clave_valor(clave_a_eliminar)
print(resultado_eliminacion)
print("=====================================")

# 6 - Obtener y mostrar todas las claves guardadas (0.5 puntos)

print("6 - Obtener y mostrar todas las claves guardadas")

def obtener_todas_las_claves():
    """
    Esta función obtiene todas las claves guardadas en Redis.
    
    Resultado:
    Devuelve una lista de todas las claves guardadas.
    """
    return client.keys()

# Ejemplo de uso
todas_las_claves = obtener_todas_las_claves()
print(f"Todas las claves guardadas: {todas_las_claves}")
print("=====================================")

# 7 - Obtener y mostrar todos los valores guardados(0.5 puntos)

print("7 - Obtener y mostrar todos los valores guardados")

def obtener_todos_los_valores():
    """
    Esta función obtiene todos los valores guardados en Redis.
    
    Resultado:
    Devuelve una lista de todos los valores guardados.
    """
    keys = client.keys()  # Obtener todas las claves
    valores = []
    for key in keys:
        try:
            valor = client.get(key)
            valores.append(valor)
        except redis.exceptions.ResponseError:
            # Skip keys that do not hold string values
            continue
    return valores

# Ejemplo de uso
todos_los_valores = obtener_todos_los_valores()
print(f"Todos los valores almacenados: {todos_los_valores}")
print("=====================================")
# 8 - Obtener y mostrar varios registros con una clave con un patrón en común usando * (0.5 puntos)

print("8 - Obtener y mostrar varios registros con una clave con un patrón en común usando *")

def obtener_registros_por_patron(patron):
    """
    Esta función obtiene varios registros con una clave con un patrón en común en Redis.
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    
    Resultado:
    Devuelve un diccionario con las claves y sus valores correspondientes.
    """
    claves = client.keys(patron)
    registros = {clave: json.loads(client.get(clave)) for clave in claves}
    return registros

# Ejemplo de uso
patron = "usuario:*"
registros_con_patron = obtener_registros_por_patron(patron)
print(f"Registros encontrados con el patrón '{patron}': {registros_con_patron}")
print("=====================================")

# 9 - Obtener y mostrar varios registros con una clave con un patrón en común usando [] (0.5 puntos)

print("9 - Obtener y mostrar varios registros con una clave con un patrón en común usando []")

def obtener_registros_por_patron_con_corchetes(patron):
    """
    Esta función obtiene varios registros con una clave con un patrón en común en Redis usando [].
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    
    Resultado:
    Devuelve un diccionario con las claves y sus valores correspondientes.
    """
    claves = client.keys(patron)
    registros = {clave: json.loads(client.get(clave)) for clave in claves}
    return registros

# Ejemplo de uso
patron_con_corchetes = "usuario:[1-3]"
registros_con_patron_corchetes = obtener_registros_por_patron_con_corchetes(patron_con_corchetes)
print(f"Registros encontrados con el patrón '{patron_con_corchetes}': {registros_con_patron_corchetes}")
print("=====================================")

# 10 - Obtener y mostrar varios registros con una clave con un patrón en común usando ? (0.5 puntos)

print("10 - Obtener y mostrar varios registros con una clave con un patrón en común usando ?")

def obtener_registros_por_patron_con_interrogacion(patron):
    """
    Esta función obtiene varios registros con una clave con un patrón en común en Redis usando ?.
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    
    Resultado:
    Devuelve un diccionario con las claves y sus valores correspondientes.
    """
    claves = client.keys(patron)
    registros = {clave: json.loads(client.get(clave)) for clave in claves}
    return registros

# Ejemplo de uso
patron_con_interrogacion = "usuario:?"
registros_con_patron_interrogacion = obtener_registros_por_patron_con_interrogacion(patron_con_interrogacion)
print(f"Registros encontrados con el patrón '{patron_con_interrogacion}': {registros_con_patron_interrogacion}")
print("=====================================")

# 11 - Obtener y mostrar varios registros y filtrarlos por un valor en concreto (0.5 puntos)

print("11 - Obtener y mostrar varios registros y filtrarlos por un valor en concreto")

def obtener_registros_filtrados_por_valor(patron, campo, valor):
    """
    Esta función obtiene varios registros con una clave con un patrón en común en Redis y los filtra por un valor en concreto.
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    campo (str): El campo del registro a filtrar.
    valor (str): El valor del campo a filtrar.
    
    Resultado:
    Devuelve un diccionario con las claves y sus valores correspondientes que cumplen con el filtro.
    """
    claves = client.keys(patron)
    registros_filtrados = {}
    for clave in claves:
        registro = json.loads(client.get(clave))
        if registro.get(campo) == valor:
            registros_filtrados[clave] = registro
    return registros_filtrados

# Ejemplo de uso
patron = "usuario:*"
campo_a_filtrar = "ciudad"
valor_a_filtrar = "Sevilla"
registros_filtrados = obtener_registros_filtrados_por_valor(patron, campo_a_filtrar, valor_a_filtrar)
print(f"Registros encontrados con el patrón '{patron}' y filtrados por {campo_a_filtrar}='{valor_a_filtrar}': {registros_filtrados}")
print("=====================================")

# 12 - Actualizar una serie de registros en base a un filtro (por ejemplo aumentar su valor en 1 )(0.5 puntos)

print("12 - Actualizar una serie de registros en base a un filtro")

def actualizar_registros_por_filtro(patron, campo, incremento):
    """
    Esta función actualiza una serie de registros en base a un filtro en Redis.
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    campo (str): El campo del registro a actualizar.
    incremento (int): El valor a incrementar en el campo.
    
    Resultado:
    Devuelve un diccionario con las claves y sus nuevos valores correspondientes.
    """
    claves = client.keys(patron)
    registros_actualizados = {}
    for clave in claves:
        registro = json.loads(client.get(clave))
        if campo in registro and isinstance(registro[campo], int):
            registro[campo] += incremento
            client.set(clave, json.dumps(registro))
            registros_actualizados[clave] = registro
    return registros_actualizados

# Ejemplo de uso
patron = "usuario:*"
campo_a_actualizar = "edad"
incremento = 1
registros_actualizados = actualizar_registros_por_filtro(patron, campo_a_actualizar, incremento)
print(f"Registros actualizados con el patrón '{patron}' y campo '{campo_a_actualizar}' incrementado en {incremento}: {registros_actualizados}")
print("=====================================")

# 13 - Eliminar una serie de registros en base a un filtro (0.5 puntos)

print("13 - Eliminar una serie de registros en base a un filtro")

def eliminar_registros_por_filtro(patron, campo, valor):
    """
    Esta función elimina una serie de registros en base a un filtro en Redis.
    
    Parámetros:
    patron (str): El patrón de las claves a buscar.
    campo (str): El campo del registro a filtrar.
    valor (str): El valor del campo a filtrar.
    
    Resultado:
    Devuelve un diccionario con las claves y sus valores correspondientes que fueron eliminados.
    """
    claves = client.keys(patron)
    registros_eliminados = {}
    for clave in claves:
        registro = json.loads(client.get(clave))
        if registro.get(campo) == valor:
            client.delete(clave)
            registros_eliminados[clave] = registro
    return registros_eliminados

# Ejemplo de uso
patron = "usuario:*"
campo_a_filtrar = "ciudad"
valor_a_filtrar = "Sevilla"
registros_eliminados = eliminar_registros_por_filtro(patron, campo_a_filtrar, valor_a_filtrar)
print(f"Registros eliminados con el patrón '{patron}' y filtrados por {campo_a_filtrar}='{valor_a_filtrar}': {registros_eliminados}")
print("=====================================")

# 14 - Crear una estructura en JSON de array de los datos que vayais a almacenar (0.5 puntos)

print("14 - Crear una estructura en JSON de array de los datos que vayais a almacenar")

def crear_estructura_json_array():
    """
    Esta función crea una estructura en JSON de array de los datos almacenados en Redis.
    
    Resultado:
    Devuelve una lista de diccionarios con los datos almacenados.
    """
    claves = client.keys()
    datos = [json.loads(client.get(clave)) for clave in claves]
    return json.dumps(datos, indent=4)

# Ejemplo de uso
estructura_json_array = crear_estructura_json_array()
print(f"Estructura en JSON de array de los datos almacenados: {estructura_json_array}")
print("=====================================")

# 15 - Realizar un filtro por cada atributo de la estructura JSON anterior (0.5 puntos)

print("15 - Realizar un filtro por cada atributo de la estructura JSON anterior")

def filtrar_por_atributo(atributo, valor):
    """
    Esta función filtra los datos almacenados en Redis por un atributo específico.
    
    Parámetros:
    atributo (str): El atributo por el cual filtrar.
    valor (str): El valor del atributo a filtrar.
    
    Resultado:
    Devuelve una lista de diccionarios que cumplen con el filtro.
    """
    claves = client.keys()
    datos_filtrados = []
    for clave in claves:
        registro = json.loads(client.get(clave))
        if registro.get(atributo) == valor:
            datos_filtrados.append(registro)
    return datos_filtrados

# Ejemplo de uso
atributo_a_filtrar = "profesion"
valor_a_filtrar = "Analista de Datos"
datos_filtrados = filtrar_por_atributo(atributo_a_filtrar, valor_a_filtrar)
print(f"Datos filtrados por {atributo_a_filtrar}='{valor_a_filtrar}': {datos_filtrados}")
print("=====================================")

# 16 - Crear una lista en Redis (0.5 puntos)

print("16 - Crear una lista en Redis")

def crear_lista_en_redis(nombre_lista, elementos):
    """
    Esta función crea una lista en Redis.
    
    Parámetros:
    nombre_lista (str): El nombre de la lista.
    elementos (list): Una lista de elementos a almacenar en Redis.
    
    Resultado:
    Devuelve un mensaje indicando que la lista ha sido creada.
    """
    for elemento in elementos:
        client.rpush(nombre_lista, json.dumps(elemento))
    return f"Lista '{nombre_lista}' creada con {len(elementos)} elementos."

# Ejemplo de uso
nombre_lista = "lista_usuarios"
elementos = [
    {"nombre": "Juan Perez", "edad": 30, "profesion": "Ingeniero de Software", "ciudad": "Sevilla"},
    {"nombre": "Maria Lopez", "edad": 25, "profesion": "Diseñadora Grafica", "ciudad": "Madrid"},
    {"nombre": "Diego Martinez", "edad": 19, "profesion": "Ingeniero de Datos", "ciudad": "Sevilla"},
    {"nombre": "Ana Gomez", "edad": 28, "profesion": "Analista de Datos", "ciudad": "Barcelona"},
    {"nombre": "Carlos Ruiz", "edad": 35, "profesion": "Analista de Datos", "ciudad": "Valencia"}
]

resultado_lista = crear_lista_en_redis(nombre_lista, elementos)
print(resultado_lista)
print("=====================================")

# 17 - Obtener elementos de una lista con un filtro en concreto(0.5 puntos)

print("17 - Obtener elementos de una lista con un filtro en concreto")

def obtener_elementos_de_lista_con_filtro(nombre_lista, campo, valor):
    """
    Esta función obtiene elementos de una lista en Redis con un filtro en concreto.
    
    Parámetros:
    nombre_lista (str): El nombre de la lista.
    campo (str): El campo del elemento a filtrar.
    valor (str): El valor del campo a filtrar.
    
    Resultado:
    Devuelve una lista de elementos que cumplen con el filtro.
    """
    elementos = client.lrange(nombre_lista, 0, -1)
    elementos_filtrados = []
    for elemento in elementos:
        registro = json.loads(elemento)
        if registro.get(campo) == valor:
            elementos_filtrados.append(registro)
    return elementos_filtrados

# Ejemplo de uso
campo_a_filtrar = "ciudad"
valor_a_filtrar = "Sevilla"
elementos_filtrados = obtener_elementos_de_lista_con_filtro(nombre_lista, campo_a_filtrar, valor_a_filtrar)
print(f"Elementos de la lista '{nombre_lista}' filtrados por {campo_a_filtrar}='{valor_a_filtrar}': {elementos_filtrados}")
print("=====================================")

# 18 - En Redis hay otras formas de almacenar datos: Set, Hashes, SortedSet,Streams, Geopatial, Bitmaps, Bitfields,Probabilistic y Time Series. 
# Elige dos de estos tipos, y crea una función que los guarde en la base de datos y otra que los obtenga. (1.5 puntos)

print("18A - Almacenar y obtener datos en Redis usando Hashes")

def guardar_hash(nombre_hash, datos):
    """
    Esta función guarda un hash en Redis.
    
    Parámetros:
    nombre_hash (str): El nombre del hash.
    datos (dict): Un diccionario de datos a almacenar en el hash.
    
    Resultado:
    Devuelve un mensaje indicando que el hash ha sido guardado.
    """
    client.hmset(nombre_hash, datos)
    return f"Hash '{nombre_hash}' guardado con datos: {datos}"

def obtener_hash(nombre_hash):
    """
    Esta función obtiene un hash de Redis.
    
    Parámetros:
    nombre_hash (str): El nombre del hash.
    
    Resultado:
    Devuelve un diccionario con los datos del hash.
    """
    return client.hgetall(nombre_hash)

# Ejemplo de uso
nombre_hash = "usuario:hash:1"
datos_hash = {
    "nombre": "Juan Perez",
    "edad": "30",
    "profesion": "Ingeniero de Software",
    "ciudad": "Sevilla"
}

resultado_guardar_hash = guardar_hash(nombre_hash, datos_hash)
print(resultado_guardar_hash)

datos_obtenidos_hash = obtener_hash(nombre_hash)
print(f"Datos obtenidos del hash '{nombre_hash}': {datos_obtenidos_hash}")
print("=====================================")

# Funciones para almacenar y obtener datos en Redis usando Sets

print("18B - Almacenar y obtener datos en Redis usando Sets")

def guardar_set(nombre_set, elementos):
    """
    Esta función guarda un set en Redis.
    
    Parámetros:
    nombre_set (str): El nombre del set.
    elementos (list): Una lista de elementos a almacenar en el set.
    
    Resultado:
    Devuelve un mensaje indicando que el set ha sido guardado.
    """
    client.sadd(nombre_set, *elementos)
    return f"Set '{nombre_set}' guardado con elementos: {elementos}"

def obtener_set(nombre_set):
    """
    Esta función obtiene un set de Redis.
    
    Parámetros:
    nombre_set (str): El nombre del set.
    
    Resultado:
    Devuelve una lista con los elementos del set.
    """
    return list(client.smembers(nombre_set))

# Ejemplo de uso
nombre_set = "ciudades"
elementos_set = ["Sevilla", "Madrid", "Barcelona", "Valencia", "Sevilla"]

resultado_guardar_set = guardar_set(nombre_set, elementos_set)
print(resultado_guardar_set)

elementos_obtenidos_set = obtener_set(nombre_set)
print(f"Elementos obtenidos del set '{nombre_set}': {elementos_obtenidos_set}")
print("=====================================")