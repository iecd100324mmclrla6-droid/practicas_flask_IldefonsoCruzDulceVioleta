numero=int(input("Ingresa un numero del 1 al 10:"))
if numero >=1 and numero <=10:
    print("Tabla de multiplicar del", numero)
    i = 1
    while i<=10:
        resultado = numero *i
        print(numero,"x", i, "=", resultado)
        i = i+1
    else:
        print("Error el numero deve de estar entre el 1 y 10")