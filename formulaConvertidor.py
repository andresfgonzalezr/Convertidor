def operacion(numero):
    while True:
        try:
            numero_cast = int(numero)
            break
        except ValueError:
            try:
                numero_cast = float(numero)
                break
            except ValueError:
                print("el valor ingresado no es un numero valido")
            return None
    return numero_cast
