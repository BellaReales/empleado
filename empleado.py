import json
from validaciones import *

inasistencias = []
emplead0 = []
personas = []
mDia = 33.33

def registrarEmpleado():
    global personas  # Para poder modificar la lista personas
    personas.clear()  # Limpiamos la lista antes de registrar nuevos empleados

    ID = validarNumero("Por favor digite el ID del empleado: ")
    nombre = validarPalabra("El nombre del empleado es: ")
    cargo = validarPalabra("Su cargo en la empresa es: ")
    salarioEm = validarNumero("Su salario actual es: ")

  # Crear un diccionario para el nuevo empleado
    empleado_data = {
        "ID": ID,
        "nombre": nombre,
        "cargo": cargo,
        "salario": salarioEm,
        "bono": bono,
        "inasistencias": 0,
        "nomina": {
            "salario_actual": salarioEm,
            "dias_trabajados": 0
        }
    }

    # Añadir el nuevo empleado a la lista personas
    personas.append(empleadoData)

    # Guardar el empleado en un archivo JSON
    filename = f"empleado_{ID}.json"
    with open(filename, 'w') as file:
        json.dump(empleadoData, file, indent=4)

    print("Se registró el empleado correctamente!")
    print(f"Id: {ID} Nombre: {nombre} Cargo: {cargo} Salario: {salarioEm} \n")

def ingresarInasistencias():
    global personas  # Para poder modificar la lista personas

    if not personas:
        print("( X ) No hay empleados registrados.")
        return

    ID = validarNumero("Por favor digite el Id del empleado: ")

    for emple in personas:
        if ID == emple["ID"]:
            cantidad = validarNumero("Digite la cantidad de inasistencias:")
            inasistencias.append(cantidad)
            emple["salario"] -= (cantidad * mDia)  # Actualizar salario
            emple["inasistencias"] += cantidad  # Actualizar inasistencias

            # Guardar la actualización en el archivo del empleado
            filename = f"empleado_{ID}.json"
            with open(filename, 'w') as file:
                json.dump(emple, file, indent=4)

            print("Se registró de manera correcta las inasistencias!")
            print(f"El empleado {emple['nombre']} tiene {inasistencias[-1]} inasistencias y su salario actual es: {emple['salario']}")
            return  # Salir después de registrar para evitar imprimir ID inválido

    print("ID inválido, no se encontró el empleado.")
