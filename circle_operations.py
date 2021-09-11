# diseña un programa legible que solicite el radio de una circunferencia y muestre su area y perimetro con solo dos decimales
# ENTENDER EL PROBLEMA
#   este programa es una sequencia sencilla que calcula el area y el perimetro de un circulo a partir de su radio, 
#    que es la entrada solicitada al usuario,     
#   es necesario importar la funcion py del modulo math
# FLUJO
#   1.una entrada tipo FLOAT que recibe el valor del radio del circulo
#   2.una variable que calcule el area del circulo
#   3.una variable que calcule el perimetro del circulo
#   4.dar salida a los resultados

from math import pi

radio = float(input("Por favor ingrese el radio del circulo: "))

area = pi * radio**2

perimetro = 2 * pi * radio 

print("\nEl radio del circulo es: %.2f\nEl area del circulo es: %.2f\nEL perimetro del circulo es: %.2f" % (radio,area,perimetro))




