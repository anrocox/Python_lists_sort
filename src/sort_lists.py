#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

How can sort items containing a python list in ascending order?

¿como se puede ordenar los elementos que contiene una lista python de forma
ascendente?
'''

#create a list
lista = [9, 2, 5, 10, 9, 1, 3]
print (lista)

#sorted in ascending order of the list items
lista.sort()
print (lista)

#sorted in descending order of the list items
lista.sort(reverse=True)
print (lista)

#create a list
lista = ['abc', 'a', 'bcd', 'c', 'bb', 'abcd']
print (lista)

#sorted in ascending order of the list items
lista.sort()
print (lista)
