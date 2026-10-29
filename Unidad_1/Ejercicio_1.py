#Realizar un programa que calcule
#La compra total de 4 productos, si la compra total
#Es mayor a 2000 pesos me haga un descuento 
#del 10%
#Datos De Entrada
precio1=float(input("Introduce el precio del producto1:"))
precio2=float(input("Introduce el precio del producto2:"))
precio3=float(input("Introduce el precio del producto3:"))
precio4=float(input("Introduce el precio del producto4:"))
#Proceso
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #Total=(3000*.10)
    print(total)
else:
    print("No tienes descuento")