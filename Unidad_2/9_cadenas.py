cadena1='Hola'
cadena2= 'Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)#print(f"{cadena}")
#Cadenas y repeticion
eco='ja'*3
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre='Dulce'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minuscula 
print(tu_nombre.lower()) 
#Remplazar texto en una cadena
frase="Me gusta programación"
print(frase.replace("programación","matematicas"))
#Formato de cadenas (F-String)
edad=16
nombre='Dulce'
mensaje=f"Hola me llamo {nombre} y tengo {edad} años"
print(mensaje)
#Contar los caracteres de una cadena
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si tu texto contiene una palabra
oracion="Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
 print("No esta")
#Validar contenido en una cadena
nlista="Luis"
#print(nlista.is_integer())
print(nlista.isalpha())
print(nlista.isdigit())