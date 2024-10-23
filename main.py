
import json 
from validaciones import *
from modulos.empleado import *
from modulos.s4lario import *


def menu():
    while True:
        print("1. Registrar Empleado")
        print("2. Ingresar Inasistencias")
        print("3. Extra Bonos")
        print("4. Sacar Nomina")
        print("5. Salir")
        OP=input("Ingrese la opcion que desea realizar : ")


        if OP=="1":
            registrarEmpleado()
        elif OP=="2":
            ingresarInasistencias()
        elif OP=="3":
            bonosExtra(emplead0)
        elif OP=="4":
            sacarNomina()
        elif OP =="5":
            print("Adios !")
            break

menu()
            
