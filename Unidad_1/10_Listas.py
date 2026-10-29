#Declaramos una lista
try:
    materias=["Progrmacion","Filosofia","Matematicas","Ingles"]
    print(materias[2])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("El indice no existe")