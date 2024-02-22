import formulaConvertidor

unidadDeMedida = input ("Selecciona la unidad de medida que quieres convertir A: Centimetros B: Inches C: Celsius o D: Farenheit => " )
unidadDeMedida = unidadDeMedida.lower()
unidadBase = input("Escribe el numero a convertir a Centimetros, Inches, Celsuis o Farenheit ")

while True:
    unidadBase = formulaConvertidor.operacion(unidadBase)
    if unidadBase is not None:
        break
    else:
        unidadBase = input("Escribe el numero a convertir a Centimetros, Inches, Celsuis o Farenheit ")

if (unidadDeMedida == "a"):
    inches = (str(unidadBase/2.54) + " inches")
    print(inches)
elif(unidadDeMedida == "b"):
    centimetros = (str(unidadBase * 2.54) + " centimetros")
    print(centimetros)
elif(unidadDeMedida == "c"):
    farenheit = (str(unidadBase * (9/5) + 32) + " farenheit")
    print(farenheit)
elif(unidadDeMedida == "d"):
    celsius = (str((unidadBase - 32) * (5/9)) + " celsius")
    print(celsius)
else:
    print("No tenemos esa unidad en la base de datos")