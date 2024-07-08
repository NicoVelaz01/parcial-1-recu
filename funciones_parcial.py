from random import randint

def menu()-> str:
    """Imprimi un menu

    Returns:
        input: nos pide una opcion
    """
    print(f"{'Menu de Opciones':^50s}")
    print("1- Cargar archivo .CSV")
    print("2- Imprimir Lista")
    print("3- Asignar Tiempo")
    print("4- Informar ganador")
    print("5- Filtrar por tipo de bicicleta")
    print("6- Informar promedio de tiempo por tipo")
    print("7- Mostrar posiciones")
    print("8- Guardar posiciones")
    print("9- Salir")

    return input("Ingrese una opcion: ")

# 1
def get_path_actual(nombre_archivo: str)-> str:
    """Obtiene el path del nombre del archivo

    Args:
        nombre_archivo (str): archivo a obtener path

    Returns:
        str: path
    """
    import os
    direccion_actual = os.path.dirname(__file__)
    return os.path.join(direccion_actual, nombre_archivo)

def obtener_lista_bicicletas(nombre_archivo: str)-> list:
    """Obtiene una lista de un archivo scv que le pasamos 

    Args:
        nombre_archivo (str): nombre del archivo del cual queremos obtener la lista

    Returns:
        list: lista de diccionarios
    """
    with open(get_path_actual(nombre_archivo), "r", encoding = "utf-8") as archivo:
        lista = []
        archivo.readline()
        
        for linea in archivo.readlines():
            bicicleta = {}
            linea = linea.strip("\n").split(",")

            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = float(tiempo)
            lista.append(bicicleta)

        return lista

# 2
def mostrar_bicicletas(lista_bicicletas: list)-> None:
    """Muestra una lista de bicicletas

    Args:
        lista_movies (list): lista de bicicletas a mostrar
    """
    tam = len(lista_bicicletas)
    print()
    print("ID        Nombre          Tipo           Tiempo")
    print("-----------------------------------------------")
    for i in range(tam):
        mostrar_bicicletas_item(lista_bicicletas[i])
    print()

def mostrar_bicicletas_item(bicicleta: dict)-> None:
    """Muestra las key de un diccionario

    Args:
        bicicleta (dict): diccionario a mostrar
    """
    print(f"{bicicleta['id_bike']:<4}     {bicicleta['nombre']:<15}  {bicicleta['tipo']:<14}  {bicicleta['tiempo']}")
    
# 3
def asignar_tiempo(lista_bicicletas: list):
    """Recorre la lista de bicicletas asignado tiempo

    Args:
        lista_bicicletas (list): lista de diccionario a asignar tiempo
    """
    from random import randint
    for el in lista_bicicletas:
        el["tiempo"] = randint(50, 150)

def mostrar_bicicletas_y_dato(lista_bicicletas:list, dato:str)-> None:
    """Recorre la lista y muestra el nombre y el dato de cada una

    Args:
        lista_bicicletas (list): lista de peliculas a recorrer
        dato (str): dato a mostrar junto al titulo
    """
    print(f"Nombre                              {dato.capitalize()}")
    for el in lista_bicicletas:
        print(f"{el['nombre']:<15}       {el[dato]}")

# 4
def obtener_mejor_dato(lista_bicicletas: list, dato: str)-> int:
    """Recorre la lista de peliculas y obtiene la pelicula con menor dato

    Args:
        lista_bicicletas (list): lista a recorrer 
        dato (str): dato a encotrar su minimo

    Returns:
        int: menor tiempo encontrado
    """
    menor_tiempo = 0
    flag_menor_tiempo = True
    for el in lista_bicicletas:
        if flag_menor_tiempo or el[dato] < menor_tiempo:
            menor_tiempo = el[dato]
            flag_menor_tiempo = False
            
    return menor_tiempo

def mostrar_bicicleta_menor_tiempo(lista_bicicletas: list, tiempo: int)-> None:
    """Recorre la lista y busca a los competidores con el menor tiempo para mostrarlos

    Args:
        lista_bicicletas (list): lista de bicicletas a recorrer 
        tiempo (int): menor tiempo a encotrar
    """
    print("El ganador/Los ganadores son:")
    for bicicleta in lista_bicicletas:
        if bicicleta["tiempo"] == tiempo:
            print(f"Titulo: {bicicleta['nombre'].capitalize()} | Tiempo: {bicicleta['tiempo']} minutos")
            
# 5
def filtrar_bicicletas(lista_bicicletas: list, tipo: str)-> list:
    """Recibe una lista de bicicletas y devuelve una nueva con bicicletas del tipo pasado por parametro

    Args:
        lista_bicicletas (list): Lista de bicicletas a filtrar
        genero (str): tipo por el cual queremos que filtre

    Returns:
        list: Nueva lista filtrada
    """
    lista_filtrada = []
    for el in lista_bicicletas:
        if el["tipo"] == tipo:
            lista_filtrada.append(el)
    return lista_filtrada

def crear_archivo_tipo_bicicleta(lista_bicicletas: list, nombre_archivo: str):
    """Escribre la lista de bicicletas que le pasemos a un archivo scv

    Args:
        lista_bicicletas (list): Lista a escribir en el archivo scv
        nombre_archivo (str): Nombre del archivo donde vamos a escribir la lista
    """
    with open(get_path_actual(nombre_archivo), "w", encoding = "utf-8") as archivo:
        encabezado = ",".join(list(lista_bicicletas[0].keys())) + "\n"
        archivo.write(encabezado)
        
        for bicicleta in lista_bicicletas:
            values = list(bicicleta.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            
            linea = ",".join(l) + "\n"
            archivo.write(linea) 
            
# 6
def obtener_promedio_tiempo_tipo(lista_bicicletas: list, tipo:str):
    """Calcula el promedio del tipo pasado por parametro

    Args:
        lista_bicicletas (list): Lista a recorrer 
        tipo (str): campo a filtrar para calcular el promedio

    Returns:
        _type_: _description_
    """
    acumulador = 0
    contador = 0
    for bicicleta in lista_bicicletas:
        if bicicleta["tipo"] == tipo:
            acumulador = bicicleta["tiempo"]
            contador += 1
    return acumulador / contador

# 7
def swap_lista(lista: list, i:int, j:int)-> None:
    """Intercambia valores de i a j

    Args:
        lista (list): lista de los elemetos i y j
        i (int): elemento uno
        j (int): elemento dos
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_bicicletas(lista_bicicletas: list, campo: str):
    """Ordena los elementos de una lista de manera ascendente

    Args:
        lista_bicicletas (list): lista de bicicletas a recorrer y comparar sus elementos
        campo (str): campo a tener en cuenta para ordenar
    """
    tam = len(lista_bicicletas)
    for i in range(tam - 1):
        for j in range(i + 1, tam):            
            if lista_bicicletas[i][campo] > lista_bicicletas[j][campo]:
                swap_lista(lista_bicicletas, i, j)                

def ordenar_bicicletas_tiempo(lista_bicicletas: list, campo:str, campo_2:str)-> list:
    """Filtra por campo y ordena los elementos de manera ascendente

    Args:
        lista_bicicletas (list): lista a filtrar
        campo (str): campo a filtrar
        campo_2 (str): campo a ordenar 

    Returns:
        list: Nueva lista filtrada y ordenada
    """
    lista_filtrada = filtrar_bicicletas(lista_bicicletas, campo)
    ordenar_bicicletas(lista_filtrada, campo_2)
    return lista_filtrada

# 8
def crear_json(bicicleta: dict, nombre_archivo: str):
    """Escribe los datos en un archivo JSON

    Args:
        bicicleta (dict): bicicleta a escribir en el archivo JSON
        nombre_archivo (str): nombre del archivo donde vamos a escribir
    """
    import json
    with open(get_path_actual(nombre_archivo), "w", encoding = "utf-8") as archivo:
        json.dump(bicicleta, archivo, indent = 4)
        
