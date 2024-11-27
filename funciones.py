import random
import pygame


#CREAR MATRIZ:
#################################################################################
#################################################################################

def crear_matriz(filas:int, columnas:int, valor)->list:
    matriz=[]
    for i in range(filas):
        fila=[]
        matriz+=[fila]
        for j in range(columnas):
            fila+=[valor]
    return matriz

#MOSTRAR MATRIZ
#################################################################################
#################################################################################


def mostrar_matriz(matriz:list)->None:
    if type(matriz) != list:
        print("Debe ingresar una matriz")
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                print(matriz[i][j], end=" ")
            print(" ")



#COLOCAR NAVIOS:
#########################################################################
#########################################################################

def colocar_navio(matriz:list, tipo_navio:str, cantidad:int):
    """
    recibe una matriz, un tipo de navio ("submarino"/"destructor"/"crucero"/"acorazado")
    y la cantidad de navios que se quiere colocar.    
    """
    lista_barcos_colocados=[]


    match tipo_navio:
        case "submarino":
            largo=1
            objeto=1
        case "destructor":
            largo=2
            objeto=2
        case "crucero":
            largo=3
            objeto=3
        case "acorazado":
            largo=4
            objeto=4

    contador_colocados=0

    while contador_colocados < cantidad:

        fila_inicial = random.randint(0,len(matriz) - (largo)) #yo tenia (largo+1)
        columna_inicial = random.randint(0, len(matriz[0]) - (largo)) #yo tenia (largo+1)
        orientacion = random.choice(["H", "V"])
        lista_un_barco=[]
        if validar_casilleros(matriz, fila_inicial, columna_inicial, largo, orientacion) == True:
            contador_colocados += 1
            for i in range(largo):
                if orientacion == "H":
                    matriz[fila_inicial][columna_inicial + i] = objeto  # Coloca el barco horizontalmente
                    un_bloque = {'fila': fila_inicial, 'columna': columna_inicial + i, 'valor': objeto}  # Guarda un bloque
                else:
                    matriz[fila_inicial + i][columna_inicial] = objeto  # Coloca el barco verticalmente
                    un_bloque = {'fila': fila_inicial + i, 'columna': columna_inicial, 'valor': objeto}  # Guarda un bloque
                
                lista_un_barco.append(un_bloque)  # Agrega el bloque al barco
        
            lista_barcos_colocados.append(lista_un_barco)
    return lista_barcos_colocados

#VALIDAR CASILLEROS:
#########################################################################
#########################################################################
def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto ("H"/"V")
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) <= len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) <= len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio


#COLOCAR TODOS LOS NAVIOS:
#########################################################################
#########################################################################

def colocar_totalidad_navios(matriz):

    lista_totalidad_navios = []


    dimension_matriz = len(matriz)


    match dimension_matriz:
        case 10:
            cantidad_submarino = 4
            cantidad_destructores = 3
            cantidad_cruceros = 2
            cantidad_acorazados = 1
        case 20:
            cantidad_submarino =8
            cantidad_destructores =6
            cantidad_cruceros =4
            cantidad_acorazados =2
        case 40:
            cantidad_submarino =12
            cantidad_destructores =9
            cantidad_cruceros =6
            cantidad_acorazados =3

    
    lista_totalidad_navios.append(colocar_navio(matriz,"submarino", cantidad_submarino))
    lista_totalidad_navios.append(colocar_navio(matriz,"destructor", cantidad_destructores))
    lista_totalidad_navios.append(colocar_navio(matriz,"crucero", cantidad_cruceros))
    lista_totalidad_navios.append(colocar_navio(matriz,"acorazado", cantidad_acorazados))


    return lista_totalidad_navios





#DESIGNAR COORDENADAS:
###################################################################
###################################################################

def designar_coordenadas(matriz_coordenadas):

    for i in range(len(matriz_coordenadas)):
        for j in range(len(matriz_coordenadas[0])):

            matriz_coordenadas[i][j] = [i,j]


#CENTRAR OBJETOS:
###################################################################
###################################################################
def centrar_objetos(ancho_rectangulo_fondo,alto_rectangulo_fondo,ancho_rectangulo_colocar,alto_rectangulo_colocar):

    mitad_ancho_fondo = ancho_rectangulo_fondo // 2
    mitad_ancho_colocar = ancho_rectangulo_colocar // 2

    eje_x_centrado = mitad_ancho_fondo - mitad_ancho_colocar

    mitad_alto_fondo = alto_rectangulo_fondo // 2
    mitad_alto_colocar = alto_rectangulo_colocar // 2

    eje_y_centrado = mitad_alto_fondo - mitad_alto_colocar

    # eje_x_centrado = (ancho_rectangulo_fondo - ancho_rectangulo_colocar) // 2
    # eje_y_centrado = (alto_rectangulo_fondo - alto_rectangulo_colocar) // 2

    coordenadas=[eje_x_centrado,eje_y_centrado]

    return coordenadas


# def centrar_objetos_2(rectangulo_fondo, rectangulo_colocar):

def centrar_objetos_2(rectangulo_fondo, rectangulo_colocar):

    #PASO 1
    ancho_fondo = rectangulo_fondo[0]
    alto_fondo = rectangulo_fondo[1]

    #PASO 2
    ancho_colocar = rectangulo_colocar[0]
    alto_colocar = rectangulo_colocar[1]

    #PASO 3
    mitad_ancho_fondo = ancho_fondo // 2
    mitad_alto_fondo = alto_fondo // 2

    #PASO 4
    mitad_ancho_colocar = ancho_colocar // 2
    mitad_alto_colocar = alto_colocar // 2

    #PASO 5
    eje_x_centrado = mitad_ancho_fondo - mitad_ancho_colocar
    eje_y_centrado = mitad_alto_fondo - mitad_alto_colocar

    # Devolver las coordenadas centradas
    coordenada_centrada = [eje_x_centrado, eje_y_centrado]
    return coordenada_centrada




    # eje_x_centrado = (ancho_rectangulo_fondo - ancho_rectangulo_colocar) // 2
    # eje_y_centrado = (alto_rectangulo_fondo - alto_rectangulo_colocar) // 2

    # coordenadas=[eje_x_centrado,eje_y_centrado]

    # return coordenadas


#CENTRAR EJE_X:
###################################################################
###################################################################

def centrar_eje_x(ancho_fondo, ancho_colocar):

    centro_fondo = ancho_fondo //2
    centro_colocar = ancho_colocar//2

    eje_x_centrado = centro_fondo - centro_colocar

    return eje_x_centrado


###################################################################
###################################################################
