# Diseña un programa que, a partir del valor de un cuadrado(3 metros), muestre el valor de su perimetro en metros y el de su area en 
#   metros cuadrados.
# ENTENDER EL PROBLEMA
#   este programa es una estructura en sequencia, se introducen los datos, se hace la operacion y de da salida al resultado, un paso 
#   despues del otro 
# FLUJO
#   1.una entrada que reciba la medida de lado de un cuadrado
#   2.una variable que calcula el perimetro
#   3.una variable que calcule el area
#   4.dar salida a los resultados

entrada = int(input("Por favor ingrese lado de cuadradado: "))

perimetro = entrada * 4

area = entrada * entrada

print("\nLado de cuadrado: %d m.\nPerimetro de cuadrado: %d m.\nArea de cuadrado: %d m2." % (entrada,perimetro,area))




