#Creando una Tupla
coordenadas=(10.5,20.3,30.5,10.5)#Tupla numerica
nombres=("Luis","Ana","Angel")#Tupla de cadena de texto
coordenadas[0]=10.9
for indice,coordenada in enumerate(coordenadas):
    print(f"Indice[{indice}]---Coordenada[{coordenada}]")