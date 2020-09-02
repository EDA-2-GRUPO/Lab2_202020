from time import process_time
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
import csv
import config as cf
import sys
import os


def cmpfunctionmovies(element1, element2):
    if int(element1["id"]) == int(element2["id"]):
        return 0
    elif int(element1["id"]) < int(element2["id"]):
        return -1
    else:
        return 1


def loadCSVFile(file, tipo_lista, cmpfunction=None, sep=";"):
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
    # Usando implementacion linkedlist
    lst = lt.newList(tipo_lista, cmpfunction)
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


def operacion_iteracion(target, col_evaluacion, operacion, criterio):
    for col in col_evaluacion:
        if operacion(target[col], criterio):
            return True
    return False


def extraerColumsBycolumcriteria(lst, col_extaer="ALL", listfilter=None):
    t1 = process_time()

    cmp = lst["cmpfunction"]
    filtrada = lt.newList("ARRAY_LIST", cmp)
    array = True if lst["type"] == "ARRAY_LIST" else False
    all = True if col_extaer == "ALL" else False

    if listfilter is None:
        paso = True
    else:
        paso = False
        col_evaluacion, operacion, criterio = listfilter

    def iteracion():
        if paso or operacion_iteracion(element, col_evaluacion, operacion, criterio):
            if all:
                fila = element
            else:
                fila = {}
                for col in col_extaer:
                    fila[col] = element[col]

            lt.addLast(filtrada, fila)

    if array:
        largo = lt.size(lst) + 1
        for i in range(1, largo):
            element = lt.getElement(lst, i)
            iteracion()
    else:
        iterador = it.newIterator(lst)
        while it.hasNext(iterador):
            element = it.next(iterador)
            iteracion()

    t2 = process_time()
    print("tiempo de finalizacion f1", t2 - t1)

    return filtrada


def buscar_xmitades_list_dict_ADT_ARRAY(target, lst):
    n_top = lt.size(lst) + 1
    n_low = 1
    cmp = lst["cmpfunction"]
    encontre = False
    element = None

    while not encontre and (n_top - n_low >= 0):
        n_nuevo = (n_top + n_low) // 2
        a_mirar = lt.getElement(lst, n_nuevo)
        comparacion = cmp(target, a_mirar)
        if comparacion == 0:
            element = a_mirar
            encontre = True
        elif comparacion == -1:
            n_top = n_nuevo - 1
        else:
            n_low = n_nuevo + 1

    return element


def Join_Extract_2_list_m_filter(col_gide, lst1, lst2, extract1="ALL", extract2="ALL", listFilter1=None,
                                 listFilter2=None):
    t1_t = process_time()

    all1 = True if extract1 == "ALL" else False
    all2 = True if extract2 == "ALL" else False
    cmp = lst1["cmpfunction"]
    array2 = True if lst2["type"] == "ARRAY_LIST" else False
    filtrated = lt.newList("ARRAY_LIST", cmp)

    if listFilter2 is None:
        paso2 = True
    else:
        col_evaluacion2, operacion2, criterio2 = listFilter2
        paso2 = True

    if listFilter1 is None:
        pre_fil = lst1
    elif array2:
        pre_fil = extraerColumsBycolumcriteria(lst1, [col_gide], listFilter1)
    else:
        pre_fil = extraerColumsBycolumcriteria(lst1, "ALL", listFilter1)

    pre_array1 = True if pre_fil["type"] == "ARRAY_LIST" else False

    iterador1 = it.newIterator(pre_fil)
    iterador2 = it.newIterator(lst2)

    largo = lt.size(pre_fil) + 1

    for i in range(1, largo):
        #t3 = process_time()
        if pre_array1:
            p_el = lt.getElement(pre_fil, i)
        else:
            p_el = it.next(iterador1)

        val_guide = p_el[col_gide]
        if array2:
            possible2 = buscar_xmitades_list_dict_ADT_ARRAY(p_el, lst2)
            if possible2 is None:
                continue
            if paso2 or operacion_iteracion(possible2, col_evaluacion2, operacion2, criterio2):
                element2 = possible2
                element1 = buscar_xmitades_list_dict_ADT_ARRAY(p_el, lst1)
            else:
                continue
        else:
            coincide = False
            while it.hasNext(iterador2):
                element2 = it.next(iterador2)
                if element2[col_gide] == val_guide:
                    coincide = True
                    break
            if not coincide or (not paso2 and not operacion_iteracion(element2, col_evaluacion2, operacion2, criterio2)):
                continue
            else:
                element1 = p_el

        fila = {}
        if all1:
            fila = element1
        else:
            for col in extract1:
                fila[col] = element1[col]
        if all2:
            fila.update(element2)
        else:
            for col in extract2:
                fila[col] = element2[col]

        lt.addLast(filtrated, fila)
        #t4 = process_time()
        #print("la iteracion demoro: ", t4 - t3)

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

    freq_dato = {"director": None, "veces": 0}
    most = []
    freq_max = 0
    for dato, freq in conteo.items():
        if freq > freq_max:
            freq_dato["director"] = [dato]
            freq_max = freq
        elif freq == freq_max:
            most.append(dato)

    freq_dato["veces"] = freq_max

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
