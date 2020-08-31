from time import process_time
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
import csv
import config as cf
import sys
import os


def loadCSVFile(file, tipo_lista, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep
            Separador utilizado para determinar cada objeto dentro del archivo
        tipo_lista
            Define el tipo de lista para almacenar los datos entre "ARRAY_LIST" y
            "SINGLE_LINKED"
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None
    """
    lst = lt.newList(tipo_lista)  # Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep

    try:
        with open(file, encoding="utf-8-sig") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lt.addLast(lst, row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return lst


def operacion_iteracion(target, listfilter):
    col_evaluacion, operacion, criterio = listfilter
    for col in col_evaluacion:
        if operacion(target[col], criterio):
            return True
    return False


def extraerColumsBycolumcriteria(lst, col_extaer="ALL", listfilter=None):
    t1 = process_time()
    filtrada = lt.newList("ARRAY_LIST")
    iterador = it.newIterator(lst)
    filtro = False if listfilter is None else True

    while it.hasNext(iterador):
        element = it.next(iterador)
        if not filtro or operacion_iteracion(element, listfilter):
            fila = {}
            if col_extaer == "ALL":
                fila = element
            else:
                for col in col_extaer:
                    fila[col] = element[col]

            lt.addLast(filtrada, fila)
    t2 = process_time()
    print("tiempo de finalizacion f1", t2 - t1)

    return filtrada


def buscar_xmitades_list_dict(dlist, colum, buscado: int):
    n_top = len(dlist)
    n_low = 0
    encontre = False
    element = None

    while not encontre and (n_top - n_low >= 0):
        n_nuevo = (n_top + n_low) // 2
        a_mirar = int(dlist[n_nuevo][colum])

        if a_mirar == buscado:
            element = dlist[n_nuevo]
            encontre = True
        elif a_mirar > buscado:
            n_top = n_nuevo - 1
        else:
            n_low = n_nuevo + 1

    return element


def Join_Extract_2_list_m_filter(col_gide, lst1, lst2, extract1="ALL", extract2="ALL", listFilter1=None,
                                 listFilter2=None):


    t1_t = process_time()
    all1 = True if extract1 == "ALL" else False
    all2 = True if extract2 == "ALL" else False
    filtered_1 = False if listFilter1 is None else True
    filtered_2 = False if listFilter2 is None else True

    array = True

    filtrated = lt.newList("ARRAY_LIST")

    if all1 and not filtered_1:
        pre_fil = lst1
    else:
        pre_fil = extraerColumsBycolumcriteria(lst1, extract1, listFilter1)

    iterador1 = it.newIterator(pre_fil)
    iterador2 = it.newIterator(lst2)

    while it.hasNext(iterador1):
        t3 = process_time()
        element1 = it.next(iterador1)
        val_guide = int(element1[col_gide])
        if array:
            a_recorrer = lst2["elements"]
            possible = buscar_xmitades_list_dict(a_recorrer, col_gide, val_guide)
        else:
            possible = None
            while it.hasNext(iterador2):
                element2 = it.next(iterador2)
                if element2[col_gide] == val_guide:
                    possible = element2
                    break

        if not filtered_2 or operacion_iteracion(possible, listFilter2):
            fila = element1
            if all2:
                fila.append(possible)
            else:
                for col in extract2:
                    fila[col] = possible[col]

            lt.addLast(filtrated, fila)

        t4 = process_time()
        print("la iteracion demoro: ", t4 - t3)

    t2_t = process_time()
    print("total 2 filt: ", t2_t - t1_t)
    return filtrated


def orderElementsByCriteria(function, column: str, lst, orden, n_rank):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    function:
        funcion de ordenamiento
    colum:
        nombre de la columna por la que se quiere ordenar
    lst:
        Estructura de lista que contiene los datos
    orden:
        funcion que indica la comparacion entre elementos, ej: lambda x,y: x > y
    n_rank:
        cantidad de datos a desplegar

    return:
    """

    def less_funtionnat(element1, element2):
        return orden(float(element1[column]), float(element2[column]))

    ranking_ordenado = function(lst, less_funtionnat, n_rank)

    return ranking_ordenado


def promedio_ADT(lst, column) -> float:
    largo = lt.size(lst)
    iterador = it.newIterator(lst)
    suma = 0
    prom = 0
    if largo != 0:
        while it.hasNext(iterador):
            dato = float(it.next(iterador)[column])
            suma += dato
        prom = suma / largo

    return prom


def freq_ADT(lst, colum) -> dict:
    conteo = {}
    iterador = it.newIterator(lst)
    while it.hasNext(iterador):
        muestra = it.next(iterador)[colum]
        if conteo.get(muestra) is None:
            conteo[muestra] = 1
        else:
            conteo[muestra] += 1

    freq_dato = {None: 0}
    most = []
    freq_max = 0
    for dato, freq in conteo.items():
        if freq > freq_max:
            most = [dato]
            freq_max = freq
        elif freq == freq_max:
            most.append(dato)

    if len(most) == 1:
        freq_dato = {most[0]: freq_max}
    else:
        freq_dato = {most: freq_max}

    return freq_dato


def countElementsFilteredByColumn(lst, listfilter):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada
    Args:
        lst
            Lista en la cual se realizará el conteo, debe estar inicializada

        listfilter
            Lista con la definicion del criterio y tipo de busqueda
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size'] == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            element = it.next(iterator)
            # filtrar por palabra clave
            if operacion_iteracion(element, listfilter):
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter
