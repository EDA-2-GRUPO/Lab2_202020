from App.modulos import *
from DataStructures import listiterator as it
from ADT import list as lt
import config as cf
import sys
import os

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
    global lista_casting
    global lista_details
    lista_casting = lt.newList()  # se require usar lista definida
    lista_details = lt.newList()

    igual_str = lambda x, y: x == y
    esta_al = lambda x, y: y in x
    mayor = lambda x, y: float(x) > float(y)
    menor = lambda x, y: float(x) < float(y)
    while True:

        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')

        if len(inputs) > 0:
            if inputs[0].lower() == "q":  # opcion 1
                tipo_lista = input("Ingrese el tipo de lista que quiere usar, 0 linked, 1 array: ")
                if tipo_lista == "1":
                    tipo_lista = "ARRAY_LIST"
                elif tipo_lista == "2":
                    tipo_lista = "SINGLE_LINKED"
                valido = True
                C1 = input("¿Que archivos desea cargar? 1: prueba, 2: completos")
                if C1 == "1":
                    file_detail = "../Data/Movies/SmallMoviesDetailsCleaned.csv"
                    file_cast = "../Data/Movies/MoviesCastingRaw-small.csv"

                elif C1 == "2":
                    file_detail = "../Data/Movies/AllMoviesDetailsCleaned.csv"
                    file_cast = "../Data/Movies/AllMoviesCastingRaw.csv"

                else:
                    valido = False
                    print("Opcion invalida")

                if valido:
                    print(file_cast, lista_casting)
                    # llamar funcion cargar datos

                    lista_casting = loadCSVFile(file_cast, tipo_lista)
                    print("Datos cargados, " + str(lt.size(lista_casting)) + " elementos cargados")
                    # llamar funcion cargar datos
                    print(file_detail, lista_details)
                    lista_details = loadCSVFile(file_detail, tipo_lista)
                    print("Datos cargados, " + str(lt.size(lista_details)) + " elementos cargados")

            elif int(inputs[0]) == 1:  # opcion 2
                director = input("ingrese el nombre del director")
                mayor_2 = lambda x, y: float(x) > y
                global p1
                p1 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["id", "director_name"],
                                                  ["original_title", "vote_count", "vote_average"],
                                                  [["director_name"], igual_str, director],
                                                  [["vote_average"], mayor_2, 6])

            elif int(inputs[0]) == 3:  # opcion 3
                # obtener la longitud de la lista
                if lista_casting == None or lista_casting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    column = input('ingrese el nombre de la columna')
                    counter = countElementsFilteredByColumn(
                        criteria, column, lista_casting)  # filtrar una columna
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
                    col_orden = input(
                        "Desea ordenar por AVERAGE: 1 o por COUNT: 2")
                    orden_str = input(
                        "Ingrese, si desea las mayores: 1 si desea las menores: 0 : ")
                    funcion_str = input("ingrese el tipo dde ordenamiento que quiere hacer \n"
                                        "select:1, Insert:2, Shell:3\n quick:4, merge: 5 :")
                    n_rank = int(
                        input("ingrese el numero de peliculas que quiere ver"))
                    t1 = process_time()
                    funcion_orden = 3

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
