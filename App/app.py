from App.modulos import *
from DataStructures import listiterator as it
from Sorting.insertionsort import insertion_rank_mod
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
    print("q- Cargar Datos")
    print("1- req1: Buenas peliculas por director")
    print("2- req2: Ranking de peliculas")
    print("3- req3: Conocer a un director")
    print("4- req4: Conocer a un actor")
    print("5- req5: Entender un genero")
    print("6- req6: Ranking por genero")
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
                    print(file_cast)
                    # llamar funcion cargar datos

                    lista_casting = loadCSVFile(file_cast, tipo_lista)
                    print("Datos cargados, " + str(lt.size(lista_casting)) + " elementos cargados")
                    # llamar funcion cargar datos
                    print(file_detail)
                    lista_details = loadCSVFile(file_detail, tipo_lista)
                    print("Datos cargados, " + str(lt.size(lista_details)) + " elementos cargados")

            elif int(inputs[0]) == 1:  # req1
                director = input("ingrese el nombre del director")
                t1 = process_time()
                mayor_2 = lambda x, y: float(x) > y

                p1 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["id", "director_name"],
                                                  ["original_title", "vote_count", "vote_average"],
                                                  [["director_name"], igual_str, director],
                                                  [["vote_average"], mayor_2, 6])

                size_1 = lt.size(p1)
                prom_1 = promedio_ADT(p1, "vote_average")

                print("el director tiene {} peliculas buenas con un promedio de votacion de {}".format(size_1, prom_1))
                t2 = process_time()
                print("tiempo de finalizacion", t2 - t1)

            elif int(inputs[0]) == 2:  # req2
                #
                if lista_casting == None or lista_casting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    ordenar_por = input("Si quiere ordenar por COUNT: 1, si AVERAGE:2")
                    mayor_menor = input("Ordenar en ascendete: 1 si es desendente: 0 : ")
                    n_rank = int(input("ingrese el numero de peliculas en el rank"))

                    t1 = process_time()
                    funcion_orden = insertion_rank_mod
                    orden = menor if mayor_menor == "0" else mayor
                    column = "vote_average" if ordenar_por == "1" else "vote_count"

                    print("cargando")
                    ordenada = orderElementsByCriteria(funcion_orden, column, lista_details, orden, n_rank)

                    iterator = it.newIterator(ordenada)
                    while it.hasNext(iterator):
                        element = it.next(iterator)
                        print(element["id"], column, element[column])

                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)

            elif int(inputs[0]) == 3:  # req3
                t1_3 = process_time()
                director = input("ingrese el nombre del director")
                p3 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["id", "director_name"],
                                                  ["original_title", "vote_count", "vote_average"],
                                                  [["director_name"], igual_str, director])

                size_3 = lt.size(p3)
                prom_3 = promedio_ADT(p3, "vote_average")

                print("el director tiene {} peliculas con un promedio de votacion de {}".format(size_3, prom_3))
                t2_3 = process_time()
                print("tiempo r3", t2_3 - t1_3)

            elif int(inputs[0]) == 4:  # req4
                # obtener la longitud de la lista
                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    actor = input("ingrese el nombre del actor")
                    t1 = process_time()
                    p4 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["id", "director_name"],
                                                      ["original_title", "vote_count", "vote_average"],
                                                      [["actor1_name", "actor2_name", "actor3_name", "actor4_name",
                                                        "actor5_name"],
                                                       igual_str, actor])
                    size_4 = lt.size(p4)
                    prom_4 = promedio_ADT(p4, "vote_average")
                    director_mas = freq_ADT(p4, "director_name")
                    print("El actor ha estado en {} peliculas con un promedio de votacion de {}".format(size_4, prom_4))
                    print("{} ha participado principalmente con:\n{} ".format(actor, director_mas))
                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)

            elif int(inputs[0]) == 5:  # req5
                # obtener la longitud de la lista
                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    genero = input("ingrese el nombre del genero cinematografico")
                    p5 = extraerColumsBycolumcriteria(lista_details,
                                                      ["genres", "original_title", "vote_count", "vote_average"],
                                                      [["genres"], esta_al, genero])
                    size_5 = lt.size(p5)
                    prom_5 = promedio_ADT(p5, "vote_count")
                    print(
                        "Del genero {} hay {} peliculas con un promedio de votos de {}".format(genero, size_5, prom_5))

            elif int(inputs[0]) == 6:  # req6

                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    t1 = process_time()
                    genero = input("ingrese el nombre del genero cinematografico")
                    ordenar_por = input("Si quiere ordenar por COUNT: 1, si AVERAGE:2")
                    mayor_menor = input("Ordenar en ascendete: 1 si es desendente: 0 : ")
                    n_rank = int(input("ingrese el numero de peliculas en el rank"))


                    t1 = process_time()
                    funcion_orden = insertion_rank_mod
                    orden = menor if mayor_menor == "0" else mayor
                    column = "vote_average" if ordenar_por == "1" else "vote_count"

                    print("cargando")

                    p6 = extraerColumsBycolumcriteria(lista_details,
                                                      ["genres", "original_title", "vote_count", "vote_average"],
                                                      [["genres"], esta_al, genero])

                    p6_rank = orderElementsByCriteria(funcion_orden,column,p6, orden, n_rank)
                    prom_6 = promedio_ADT(p6_rank, column)

                    print(
                        "Del ranking {} el promedio de calificacion es {}".format(genero, prom_6))




            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
