#EJEMPLO 1 SIN MANEJO DE EXCEPCIONES
numero1=5
numero2=4
try:
    numero1=float(input("Ingresa el primer numero:"))
    numero2=float(input("Ingresa el segundo numero:"))
    resultado=numero1 / numero2
    print(resultado)
except ZeroDivisionError:
    print("Error:No se puede dividir una letra")
except ValueError:
    print("Error:No se puede dividir un numero entre cero")
    
