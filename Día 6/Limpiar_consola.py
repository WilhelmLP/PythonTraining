'''
Limpiar consola con Python
'''

from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls')

print(f'Tu nomnbre es {nombre} y tienes {edad} años')
