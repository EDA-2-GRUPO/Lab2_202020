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

def find_id(allar,lista):
    print(lista["elements"][0]["id"])
    p= lt.size(lista)
    w = 1
    x = round(lt.size(lista)/2)
    d = True  
    while d:
       if x>p:
           x = p
       if x<0:
           x = 0
       print(x)
       print(w)
       print("\n")
       print(lista["elements"][x]["id"])
       print("\n")
       w+=1
       if (int(lista["elements"][x]["id"]) == allar):
          return "Yes"
       
       elif x>allar:
           x=round(x-1/2*w)
       else:
           x= round(x+1/2*w)
    return 0

def busqueda_logaritmica(allar,lista):
    mini=0
    maxi=lt.size(lista)
    x= int((mini+maxi)/2)
    d = True  
    while d:
        x=int((mini+maxi)/2)
        w=int(lista["elements"][x]["id"])
        if w==allar:
            return "Yes" 
        elif allar>w:
            mini = x+1
        elif allar<w:
            maxi= x-1
print(busqueda_logaritmica(2991,(loadCSVFile("Data/Movies/MoviesCastingRaw-small.csv","ARRAY_LIST"))))