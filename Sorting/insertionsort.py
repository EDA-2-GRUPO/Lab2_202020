"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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

import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


def insertionSort(lst, lessfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (lessfunction(lt.getElement(lst, pos2), lt.getElement(lst, pos2 - 1))):
            lt.exchange(lst, pos2, pos2 - 1)
            pos2 -= 1
        pos1 += 1


def insertion_rank_mod(lst, lessfunction, n_rank):
    pos_list = 1
    rank = lt.newList('ARRAY_LIST')

    iterator_lst = it.newIterator(lst)
    element = it.next(iterator_lst)
    lt.addLast(rank, element)

    while it.hasNext(iterator_lst):
        pos_rank = lt.size(rank) + 1
        continua = True
        element = it.next(iterator_lst)
        while pos_rank > 1 and continua:
            if lessfunction(element, lt.getElement(rank, pos_rank - 1)):
                pos_rank -= 1
            else:
                continua = False

        if pos_rank < n_rank:
            lt.insertElement(rank, element, pos_rank)
            if lt.size(rank) > n_rank:
                lt.removeLast(rank)
        pos_list += 1

    return rank

