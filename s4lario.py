
import json
from modulos.empleado import *
from validaciones import *

salarioMin = 1000000
salud = 40.000
pension = 40.000
auxilio = 100.000
salarioTotal = []
emplead0 = []  # Lista para almacenar empleados en memoria

def cargarEmpleados():
    global emplead0
    emplead0.clear()

    for ID in range(1, 101):  # Asumiendo IDs del 1 al 100
        try:
            filename = f"empleado_{ID}.json"
            with open(filename, 'r') as file:
                empleado_data = json.load(file)
                emplead0.append(empleado_data)
        except FileNotFoundError:
            continue  # Ignorar si el archivo no existe


def bonosExtra():
    global emplead0

    if not emplead0:
        print("No hay empleados registrados.")
        return

    ID = validarNumero("Por favor ingrese el ID del empleado: ")
    for emple in emplead0:
        if ID == emple["ID"]:
            cantidad = validarNumero("¿Cuántos bonos extra desea generar?: ")
            if cantidad <= 2:
                for _ in range(cantidad):
                    tipo = validarPalabra("Ingrese el concepto de bono extra: ")
                    valor = validarNumero("Ingrese el valor del bono extra: ")
                    emple["salario"] += valor  # Actualizar salario

                    print(f"Se ha generado un bono extra a {emple['nombre']} por: {tipo} con un valor de: {valor}")

                # Guardar cambios en el archivo JSON del empleado
                filename = f"empleado_{ID}.json"
                with open(filename, 'w') as file:
                    json.dump(emple, file, indent=4)

            else:
                print("Solo puede generar dos bonos extra por empleado.")
            return
    print("ID inválido, no se encontró el empleado.")

def sacarNomina():
    global emplead0

    if not emplead0:
        print("No hay empleados registrados.")
        return

    ID = validarNumero("Por favor ingrese el ID del empleado: ")
    for emple in emplead0:
        if ID == emple["ID"]:
            print(f"Su salario actual es: {emple['salario']}")
            if emple["salario"] < 2000000:
                print(f"Su salario: {emple['salario']} es menor a la mínima, por lo tanto se le dará un auxilio de: {auxilio}")
                emple["salario"] += auxilio
                print(f"Se le ha aplicado el auxilio y su salario actual es: {emple['salario']}")
            else:
                print(f"Su salario {emple['salario']} es mayor o igual a la mínima, por lo tanto no se le dará un auxilio.")

            emple["salario"] -= salud  # Descontar salud
            emple["salario"] -= pension  # Descontar pensión
            salarioTotal.append(emple["salario"])

            print(f"Se le ha descontado salud y pensión, su salario total es: {emple['salario']}")
            return
    print("ID inválido, no se encontró el empleado.")

# Cargar empleados al inicio del programa
cargarEmpleados()
