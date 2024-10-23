def validarNumero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                raise ValueError("( ⚠️ ) El número debe ser positivo.")
            return numero
        except ValueError as e:
            print(e)

def validarPalabra(mensaje):
    while True:
        try:
            palabra = input(mensaje)
            if any(char.isdigit() for char in palabra) or any(not char.isalpha() for char in palabra): #isdigit= numeros char.isalpha= letras
                raise ValueError("( ⚠️ ) Solo se permiten letras.")
            return palabra
        except ValueError as e:
            print(e)