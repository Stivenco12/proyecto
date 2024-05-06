from os import system
import sys 
import json
from enum import Enum

def borrar_pantalla():
    if sys.platform == "Linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform == "Linux" or sys.platform == "darwin":
        x=input("presione una tecla para continuar")
    else:
        system("pause")

usuario = {
    "datos_usuario" : {}
}