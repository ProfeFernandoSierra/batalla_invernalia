import os
os.system("cls")


VIDRIAGON_POR_SOLDADO = 3
TEMPERATURA_CONGELACION = -15

cantidad_inmaculados = int(input("Ingrese cantidad de soldados inmaculados\n"))
cantidad_dothrakis = int(input("Ingrese cantidad de soldados dothrakis\n"))
vidriagon_disponible = int(input("Ingrese cantidad de dagas disponibles\n"))
temperatura_actual = float(input("Ingrese temperatura actual en Invernalia\n"))
existen_dragones = input("Daenerys llevo sus dragones?  si - no \n").lower()

ejercito_total =  cantidad_inmaculados + cantidad_dothrakis
vidriagon_necesario = ejercito_total * VIDRIAGON_POR_SOLDADO 
deficit_de_armas =  vidriagon_necesario - vidriagon_disponible

if ejercito_total >= 20000 and existen_dragones == "si" and vidriagon_disponible >= vidriagon_necesario:
    mensaje = "¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas." 

elif ejercito_total >= 10000 and existen_dragones == "si" and temperatura_actual <= TEMPERATURA_CONGELACION or deficit_de_armas < 0:
    mensaje = f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_de_armas} dagas."

elif ejercito_total < 10000 and existen_dragones == "si" and temperatura_actual > TEMPERATURA_CONGELACION:
    mensaje = "Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur."

else:
    mensaje = "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."
print(mensaje)

