import config as cf
import sys
import os
from App.modulos import *
from DataStructures import listiterator as it
from Sorting.insertionsort import insertion_rank_mod
from ADT import list as lt

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
"""Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, 
y hacer búsquedas sobre una lista . """


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
    lista_casting = lt.newList()
    lista_details = lt.newList()

    def igual_str(x, y):
        return x.lower() == y.lower()

    def esta_al(x, y):
        return y.lower() in x.lower()

    def mayor(x, y):
        return float(x) > float(y)

    def menor(x, y):
        return float(x) < float(y)

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
                    file_detail = "../Data/theMoviesdb/SmallMoviesDetailsCleaned.csv"
                    file_cast = "../Data/theMoviesdb/MoviesCastingRaw-small.csv"
                elif C1 == "2":
                    file_detail = "../Data/theMoviesdb/AllMoviesDetailsCleaned.csv"
                    file_cast = "../Data/theMoviesdb/AllMoviesCastingRaw.csv"
                else:
                    valido = False
                    print("Opcion invalida")

                if valido:
                    t1 = process_time()

                    lista_casting = loadCSVFile(file_cast, tipo_lista, cmpfunctionmovies)
                    print(file_cast)
                    # llamar funcion cargar datos
                    print("Datos cargados, " + str(lt.size(lista_casting)) + " elementos cargados")
                    lista_details = loadCSVFile(file_detail, tipo_lista, cmpfunctionmovies)
                    # llamar funcion cargar datos
                    print(file_detail)
                    print("Datos cargados, " + str(lt.size(lista_details)) + " elementos cargados")

                    t2 = process_time()

                    print("tiempo de carga", t2 - t1)
            elif int(inputs[0]) == 1:  # req1
                director = input("ingrese el nombre del director")
                t1 = process_time()

                def mayor_2(x, y):
                    return float(x) > y

                p1 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["director_name"],
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
                if lista_casting['size'] == 0 or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    ordenar_por = input("Si quiere ordenar por COUNT: 1, si AVERAGE:2")
                    mayor_menor = input("Ordenar en ascendete: 1 si es desendente: 0 : ")
                    n_rank = int(input("ingrese el numero de peliculas en el rank"))

                    t1 = process_time()
                    funcion_orden = insertion_rank_mod
                    orden = menor if mayor_menor == "0" else mayor
                    column = "vote_average" if ordenar_por == "2" else "vote_count"
                    print("cargando")
                    ordenada = orderElementsByCriteria(funcion_orden, column, lista_details, orden, n_rank)
                    print("Las 10 Películas más(" + str(column) + ") votadas(" + str(ordenar_por) + ")")
                    print("Película, Director, vote_average, vote_count")
                    iterator = it.newIterator(ordenada)
                    w = 0
                    while it.hasNext(iterator):
                        w += 1
                        element = it.next(iterator)
                        print("P" + str(w) + "  ", element["title"], element["vote_average"], element["vote_count"])

                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)

            elif int(inputs[0]) == 3:  # req3
                t1_3 = process_time()
                director = input("ingrese el nombre del director")
                p3 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["director_name"],
                                                  ["original_title", "vote_count", "vote_average"],
                                                  [["director_name"], igual_str, director])

                size_3 = lt.size(p3)
                prom_3 = promedio_ADT(p3, "vote_average")

                print("Película, Director, vote_average, vote_count")
                print("-----------------------------------------------------")
                l = 0
                litair = it.newIterator(p3)
                while it.hasNext(litair):
                    l += 1
                    w = it.next(litair)
                    print("P" + str(l) + "   " + "," + str(w["original_title"]) + "," + str(
                        w['director_name']) + "," + str(w["vote_average"]) + "," + str(w["vote_count"]))
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
                    p4 = Join_Extract_2_list_m_filter("id", lista_casting, lista_details, ["director_name"],
                                                      ["original_title", "vote_count", "vote_average"],
                                                      [["actor1_name", "actor2_name", "actor3_name", "actor4_name",
                                                        "actor5_name"],
                                                       igual_str, actor])
                    size_4 = lt.size(p4)
                    prom_4 = promedio_ADT(p4, "vote_average")
                    director_mas = freq_ADT(p4, "director_name")
                    print('Pelicula,    Director,    vote_average')
                    print('-----------------------------------------------')
                    iterador = it.newIterator(p4)
                    cant_p = 0
                    while it.hasNext(iterador):
                        cant_p += 1
                        i = it.next(iterador)
                        print('P' + str(cant_p) + ',' + '    ' + str(i['director_name']) + ',' + '    ' + str(
                            i['vote_average']))
                    print("Numero de Peliculas " + str(size_4))
                    print("Promedio Peliculas (vote_average): " + str(round(prom_4, 2)))
                    print('Director con más colaboraciones: ' + str(director_mas['director']))
                    t2 = process_time()
                    print("tiempo de finalizacion", t2 - t1)

            elif int(inputs[0]) == 5:  # req5
                # obtener la longitud de la lista
                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    genero = input("ingrese el nombre del genero cinematografico")
                    t1 = process_time()
                    p5 = extraerColumsBycolumcriteria(lista_details,
                                                      ["genres", "original_title", "vote_count", "vote_average"],
                                                      [["genres"], esta_al, genero])
                    size_5 = lt.size(p5)
                    prom_5 = promedio_ADT(p5, "vote_count")
                    litair = it.newIterator(p5)
                    l = 0
                    while it.hasNext(litair):
                        l += 1
                        w = it.next(litair)
                        print("P" + str(l) + "   " + "," + str(w["genres"]) + "," + str(w["vote_count"]))
                    print(
                        "Del genero {} hay {} peliculas con un promedio de votos de {}".format(genero, size_5, prom_5))
                    t2 = process_time()
                    print("Tiempo de ejecucion", t2 - t1)
            elif int(inputs[0]) == 6:  # req6

                if lista_details is None or lista_details['size'] == 0:
                    print("La lista esta vacía")
                else:
                    genero = input("ingrese el nombre del genero cinematografico")
                    ordenar_por = input("Si quiere ordenar por COUNT: 1, si AVERAGE:2")
                    mayor_menor = input("Ordenar en ascendete: 1 si es desendente: 0 : ")
                    n_rank = int(input("ingrese el numero de peliculas en el rank"))

                    t1 = process_time()
                    funcion_orden = insertion_rank_mod
                    orden = menor if mayor_menor == "0" else mayor
                    column = "vote_average" if ordenar_por == "2" else "vote_count"

                    print("cargando")

                    p6 = extraerColumsBycolumcriteria(lista_details,
                                                      ["genres", "original_title", "vote_count", "vote_average"],
                                                      [["genres"], esta_al, genero])

                    p6_rank = orderElementsByCriteria(funcion_orden, column, p6, orden, n_rank)
                    prom_6 = promedio_ADT(p6_rank, column)
                    litair = it.newIterator(p6_rank)
                    l = 0
                    while it.hasNext(litair):
                        l += 1
                        w = it.next(litair)
                        print("P" + str(l) + "   " + "," + str(w['genres']) + "," + str(w["vote_average"]) + "," + str(
                            w["vote_count"]))
                    print(
                        "Del ranking {} el promedio de calificacion es {}".format(genero, prom_6))
                    t2 = process_time()
                    print("Tiempo de ejecucion", t2 - t1)

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
