import config as cf
from DataStructures import liststructure as list_a
from time import process_time
from DataStructures import listiterator as it
from ADT import list as lt
import sys
import csv
from Sorting.insertionsort import insertion_rank_mod as insertionSort
from Sorting.mergesort import mergesort
from Sorting.quicksort import quickSort
from Sorting.selectionsort import selectionSort_n_rank as selectionSort
from Sorting.shellsort import shellSort

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
        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')

        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                file = "Data/Movies/SmallMoviesDetailsCleaned.csv"
                tipo_lista = input(
                    "Ingrese el tipo de lista que quiere usar, 0 linked, 1 array: ")
                if tipo_lista == "1":
                    tipo_lista = "ARRAY_LIST"
                if tipo_lista == "2":
                    tipo_lista = "SINGLE_LINKED"
                valido = True
                C1 = input(
                    "¿Que archivos desea cargar? 1: prueba, 2: completos")
                if C1 == "1":
                    file_detail = "Data/Movies/test.csv"
                    file_cast = "Data/Movies/test.csv"

                elif int(C1) == 2:
                    file_detail = "Data/Movies/test.csv"
                    file_cast = "Data/Movies/test.csv"
                else:
                    valido = False
                    print("Opcion invalida")

                if valido:
                    c1_1 = input("Datos del elenco? 0 o 1: ")
                    if c1_1 == "1":
                        print(file_cast, lista_casting)
                        # llamar funcion cargar datos
                        lista_casting = loadCSVFile(file_cast, tipo_lista)
                        print("Datos cargados, " +
                              str(lt.size(lista_casting)) + " elementos cargados")
                        print(lista_casting["elements"][1]["id"])
                        # llamar funcion cargar datos
                    c1_2 = input("Datos de la pelicula? 0 o 1: ")
                    if c1_2 == "1":
                        print(file_detail, lista_details)
                        lista_details = loadCSVFile(file_detail, tipo_lista)
                        print
                        print("Datos cargados, " +
                              str(lt.size(lista_details)) + " elementos cargados")
                        print(lista_casting)

            elif int(inputs[0]) == 2:  # opcion 2
                """
                if ==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
                """
            elif int(inputs[0]) == 3:  # opcion 3
                # obtener la longitud de la lista
                if lista_casting == None or lista_casting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    column = input('ingrese el nombre de la columna')
                    counter = countElementsFilteredByColumn(criteria, column, lista_casting)  # filtrar una columna
                    # por criterio
                    print("Coinciden ", counter,
                          " elementos con el crtierio: ", criteria)
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
                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    dict_ord = {"1": selectionSort, "2": insertionSort,
                                "3": shellSort, "4": quickSort, "5": mergesort}
                    col_orden = input(
                        "Desea ordenar por AVERAGE: 1 o por COUNT: 2")
                    orden_str = input(
                        "Ingrese, si desea las mayores: 1 si desea las menores: 0 : ")
                    funcion_str = input("ingrese el tipo dde ordenamiento que quiere hacer \n"
                                        "select:1, Insert:2, Shell:3\n quick:4, merge: 5 :")
                    n_rank = int(
                        input("ingrese el numero de peliculas que quiere ver"))
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
                    ordenada = orderElementsByCriteria(
                        funcion_orden, column, lista_details, orden, n_rank)

                    counter = 0
                    iterator = it.newIterator(ordenada)
                    while it.hasNext(iterator) and counter < n_rank:
                        element = it.next(iterator)
                        print(element["id"], column, element[column])
                        counter += 1

                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()