#Ciclo externo para el numero de la base de la tabla 
for i in range(1,4):
    print(f"---Tabla del {i}---")
    #Ciclo interno nos multiplicas la base(i) por el numero(j)
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
    print(f"AQUI TERMINA LA TABLA DEL {i}")