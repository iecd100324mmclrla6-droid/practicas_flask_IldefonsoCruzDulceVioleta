# Realizar un programa en el que se creen 2 listas
try:
    alumnos = ["Sherlin", "Mariel", "Valeria", "Darina", "Carlos"]
    calificaciones = [9, 8, 10, 7, 9]
    print(alumnos)
    print(calificaciones)
    print("Alumnos en indice impar:")
    print("Indice i: alumnos[i] - Calificacion: calificaciones[i]")
except IndexError:
    print("Este indice no existe")