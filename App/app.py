"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""
import config as cf
import sys
import csv

# sorting
from Sorting.insertionsort import insertionSort
from Sorting.mergesort import mergesort
from Sorting.quicksort import quickSort
from Sorting.selectionsort import selectionSort
from Sorting.shellsort import shellSort

# estructuras
from ADT import list as lt
from DataStructures import listiterator as it
from time import process_time
from DataStructures import liststructure as list_a


def loadCSVFile(file, tipo_lista, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        tipo_lista
            Define el tipo de lista para almacenar los datos entre "ARRAY_LIST" y
            "SINGLE_LINKED"
        Try:
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


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Ranking de peliculas")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
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
            if criteria.lower() in element[column].lower():  # filtrar por palabra clave
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop - t1_start, " segundos")
    return counter


def countElementsByCriteria(criteria, column, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return 0


def orderElementsByCriteria(function, column: str, lst, orden):
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
    despligue:
        cantidad de datos a desplegar

    return:
    """

    def less_funtionnat(element1, element2):
        return orden(float(element1[column]), float(element2[column]))

    function(lst, less_funtionnat)

    return lst


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_casting = lt.newList()  # se require usar lista definida
    lista_details = lt.newList()
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n')  # leer opción ingresada
        if len(inputs) > 0:

            if int(inputs[0]) == 1:  # opcion 1
                file = "../Data/Movies/SmallMoviesDetailsCleaned.csv"
                tipo_lista = input("Ingrese el tipo de lista que quiere usar, 0 linked, 1 array: ")
                if tipo_lista == "1":
                    tipo_lista = "ARRAY_LIST"
                if tipo_lista == "2":
                    tipo_lista = "SINGLE_LINKED"
                valido = False
                C1 = input("¿Que archivos desea cargar? 1: prueba, 2: completos")
                if C1 == "1":
                    file_detail = "../Data/Movies/SmallMoviesDetailsCleaned.csv"
                    file_cast = "../Data/Movies/MoviesCastingRaw-small.csv"
                    valido = True
                elif int(C1) == 2:
                    file_detail = "../Data/Movies/AllMoviesDetailsCleaned.csv"
                    file_cast = "../Data/Movies/AllMoviesCastingRaw.csv"
                    valido = True
                else:
                    print("Opcion invalida")

                if valido:
                    c1_1 = input("Datos del elenco? 0 o 1: ")
                    if c1_1 == "1":
                        print(file_cast,lista_casting)
                        # llamar funcion cargar datos
                        lista_casting = loadCSVFile(file_cast, tipo_lista)
                        print("Datos cargados, " + str(lt.size(lista_casting)) + " elementos cargados")
                        # llamar funcion cargar datos
                    c1_2 = input("Datos de la pelicula? 0 o 1: ")
                    if int(c1_2):
                        print(file_detail, lista_details)
                        lista_details = loadCSVFile(file_detail, tipo_lista)
                        print("Datos cargados, " + str(lt.size(lista_details)) + " elementos cargados")

            elif int(inputs[0]) == 2:  # opcion 2
                """
                if ==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
                """
            elif int(inputs[0]) == 3:  # opcion 3
                if lista_casting == None or lista_casting['size'] == 0:  # obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    column = input('ingrese el nombre de la columna')
                    counter = countElementsFilteredByColumn(criteria, column,
                                                            lista_casting)  # filtrar una columna por criterio
                    print("Coinciden ", counter, " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                """
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")

                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
                """
            elif int(inputs[0]) == 5:  # opcion 5
                # obtener la longitud de la lista
                if lista_details == None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    dict_ord = {"1": selectionSort, "2": insertionSort,
                                "3": shellSort, "4": quickSort, "5": mergesort}
                    col_orden = input("Desea ordenar por COUNT: 1 o por AVERAGE: 2")
                    orden_str = input("Ingrese, si desea las mayores: 1 si desea las menores: 0 : ")
                    funcion_str = input("ingrese el tipo dde ordenamiento que quiere hacer \n"
                                        "select:1, Insert:2, Shell:3\n quick:4, merge: 5 :")
                    n_rank = int(input("ingrese el numero de peliculas que quiere ver"))
                    t1 = process_time()
                    funcion_orden = dict_ord[funcion_str]
                    if orden_str == "0":
                        def orden(x, y):
                            return x < y
                    else:
                        def orden(x, y):
                            return x > y

                    if col_orden == "1":
                        column = "vote_average"
                    else:
                        column = "vote_count"

                    print("cargando")
                    orderElementsByCriteria(funcion_orden, column, lista_details, orden)

                    counter = 0
                    iterator = it.newIterator(lista_details)
                    while it.hasNext(iterator) and counter < n_rank:
                        element = it.next(iterator)
                        print(element)
                        counter += 1

                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
