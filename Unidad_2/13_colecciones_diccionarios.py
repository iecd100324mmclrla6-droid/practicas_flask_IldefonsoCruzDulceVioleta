#Creando un Diccionario
persona={
    "Nombre":"Dulce",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":False 
}
print(persona)
#Acediendo a un valor en especifico
print(persona["Nombre"])
#Se puede usar el metodo get()
#Es util porque no marca error si el valor no existe
print(persona.get("Profesion"))
#Modificar un valor existente
persona["Edad"]=17
print(persona["Edad"])