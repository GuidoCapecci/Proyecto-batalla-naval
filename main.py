import pygame
from funciones import *
from configuraciones import *

pygame.init()


#ICONO
imagen_logo = pygame.image.load("ZEGUNDO_PARCIAL/archivos/imagen_brujula.webp")
pygame.display.set_icon(imagen_logo)
#TITULO
pygame.display.set_caption("Batalla Naval UTN")
#VENTANA

ventana_principal = pygame.display.set_mode((DIMENCIONES_VENTANA))


#IMAGENES:

#INICIO:
imagen_inicio = pygame.image.load("ZEGUNDO_PARCIAL/archivos/fondo_barco.jpg")
imagen_inicio = pygame.transform.scale(imagen_inicio, DIMENCIONES_VENTANA)

#FONDO TABLERO
imagen_fondo_tablero = pygame.image.load("ZEGUNDO_PARCIAL/archivos/imagen_fondo_tablero.webp")
imagen_fondo_tablero = pygame.transform.scale(imagen_fondo_tablero, DIMENCIONES_VENTANA)



##########################################################################################################
# FUNCIONES
##########################################################################################################



#BIBUJAR TABLERO

def dibujar_tablero(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    matriz_rectangulos = crear_matriz(filas,columnas,None)

    # Esto quizas haya que convertirlo en funcion
    if len(matriz) == 10:
        tamaño_celda = 40
    elif len(matriz) == 20:
        tamaño_celda = 30
    else:
        tamaño_celda = 15

    #Esto hay que convertirlo en funcion:
    #Centrar eje_X
    ancho_matriz = tamaño_celda * len(matriz[0])
    ancho_matriz_mitad = ancho_matriz // 2
    eje_x_centrado = (ANCHO_VENTANA // 2) - ancho_matriz_mitad
    #Centrar eje_y
    alto_matriz = tamaño_celda * len(matriz)
    alto_matriz_mitad = alto_matriz // 2
    eje_y_centrado = (ALTO_VENTANA // 2) - alto_matriz_mitad

    #Fondo tablero
    pygame.draw.rect(ventana_principal, GRIS,(eje_x_centrado,eje_y_centrado,ancho_matriz,alto_matriz))
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz[0])):

            eje_x = j*tamaño_celda
            eje_y = i*tamaño_celda

            rectangulo = pygame.Rect(eje_x_centrado + eje_x, eje_y_centrado + eje_y, tamaño_celda, tamaño_celda)
            
            matriz_rectangulos[i][j] = rectangulo

            valor = matriz[i][j]

            match valor:
                case 0:
                    color = COLOR_AGUA
                case 1:
                    color = COLOR_SUBMARINO
                case 2:
                    color = COLOR_DESTRUCTOR
                case 3:
                    color = COLOR_CRUCERO
                case 4:
                    color = COLOR_ACORAZADO


            pygame.draw.rect(ventana_principal, color, rectangulo)    #creo que se le puede pasar como coordenada y dimencion un rectangulo 
            pygame.draw.rect(ventana_principal, NEGRO, rectangulo, width=2)  # Borde negro

    return matriz_rectangulos


#CREAR BOTONES

def crear_botones_tablero (matriz_rectangulos):
    
    for i in range(len(matriz_rectangulos)):
        for j in range(len(matriz_rectangulos[0])):

            # rectangulo = matriz_rectangulos[i][j]
            

            pygame.draw.rect(ventana_principal, GRIS, (matriz_rectangulos[i][j]))
            
            pygame.draw.rect(ventana_principal, NEGRO, (matriz_rectangulos[i][j]),2)





# ventana_principal.blit(imagen_inicio,(0,0))
# dimension_texto_nivel = texto_nivel.get_size()
# coordenadas_texto_volver = centrar_objetos_2(rectangulo_volver.size, texto_volver.get_size())


#MENU INICIO:

def crear_menu():
    fuente = pygame.font.SysFont("consola", 30)

    lista_opciones=["Nivel","Jugar","Ver puntaje","Salir"]
    ancho_boton=200
    alto_boton=50
    eje_x=400
    eje_y=50

    for i in range(4):
        pygame.draw.rect(ventana_principal,NEGRO,(eje_x,eje_y,ancho_boton,alto_boton),width=5, border_radius=5)
        pygame.draw.rect(ventana_principal, GRIS,(eje_x+3,eje_y+3,ancho_boton-6,alto_boton-6), border_radius=5)
        texto = fuente.render(lista_opciones[i],True,ROJO,None) #el none es para que no tenga fondo
        dimension_opcion = texto.get_size()
        coordenada_opciones = centrar_objetos(ancho_boton,alto_boton,dimension_opcion[0],dimension_opcion[1])
        ventana_principal.blit(texto,(eje_x+coordenada_opciones[0], eje_y+coordenada_opciones[1]))

        eje_y+=alto_boton + 10






#################################################################################################################
#PANTALLA 1 (MENU)
#################################################################################################################

#Botones:

boton_x_centrado = centrar_eje_x(ANCHO_VENTANA,BOTON_ANCHO)

pos_nivel=(boton_x_centrado,50)
pos_jugar=(boton_x_centrado,110)
pos_puntaje=(boton_x_centrado,170)
pos_salir=(boton_x_centrado,230)


rectangulo_nivel = pygame.Rect(pos_nivel[0],pos_nivel[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_jugar = pygame.Rect(pos_jugar[0],pos_jugar[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_puntaje = pygame.Rect(pos_puntaje[0],pos_puntaje[1],BOTON_ANCHO,BOTON_ALTO,)
rectangulo_salir = pygame.Rect(pos_salir[0],pos_salir[1],BOTON_ANCHO,BOTON_ALTO,)




#Textos:

fuente_botones = pygame.font.SysFont("consola", 45)

texto_nivel = fuente_botones.render("Nivel", True, NEGRO,None)
texto_jugar = fuente_botones.render("Jugar", True, NEGRO,None)
texto_puntaje = fuente_botones.render("Puntaje", True, NEGRO,None)
texto_salir = fuente_botones.render("Salir", True, NEGRO,None)


#Dimenciones para centrar

dimension_texto_nivel = texto_nivel.get_size()
dimension_texto_jugar = texto_jugar.get_size()
dimension_texto_puntaje = texto_puntaje.get_size()
dimension_texto_salir = texto_salir.get_size()

# Centrar los textos en los botones
coordenadas_texto_nivel = centrar_objetos_2(rectangulo_nivel.size, texto_nivel.get_size())
coordenadas_texto_jugar = centrar_objetos_2(rectangulo_jugar.size, texto_jugar.get_size())
coordenadas_texto_puntaje = centrar_objetos_2(rectangulo_puntaje.size, texto_puntaje.get_size())
coordenadas_texto_salir = centrar_objetos_2(rectangulo_salir.size, texto_salir.get_size())


######################################################################################################################
#PANTALLA 2 (JUEGO)
######################################################################################################################
pos_volver = [50,50]

rectangulo_volver = pygame.Rect(pos_volver[0], pos_volver[1],BOTON_ANCHO,BOTON_ALTO,)
fuente_volver = pygame.font.SysFont("consola", 45)
texto_volver = fuente_volver.render("Volver", True, NEGRO,None)
dimension_texto_volver = texto_volver.get_size()
coordenadas_texto_volver = centrar_objetos_2(rectangulo_volver.size, texto_volver.get_size())


#########################################################################################################################
#PANTALLA 3 (nivel)
#########################################################################################################################

#########################################################################################################################
#PANTALLA 4 (puntajes)
#########################################################################################################################








###########################################################################################################################
# EJECUCION
###########################################################################################################################

# matriz_coordenadas = crear_matriz(10,10,(0,0))

matriz_principal = crear_matriz(10,10,0)
lista_totalidad_navios = colocar_totalidad_navios(matriz_principal)
matriz_rectangulos=dibujar_tablero(matriz_principal)


#control que sea tipo Rect
# crear_botones_tablero(matriz_rectangulos)
# print("----------------------")
# print(type(matriz_rectangulos[0][0]))


#mostrar lista de {barcos}
# for i in range(len(lista_totalidad_navios)):
#     for j in range(len(lista_totalidad_navios[i])):
#         print(lista_totalidad_navios[i][j])


# #control de que se creo bien la matriz rectangulos
# for i in range(len(matriz_rectangulos)):
#     for j in range(len(matriz_rectangulos[0])):
#         print("0",end="")
#     print(" ")


#No se que es esto
# lista_submarinos = colocar_navio(matriz_principal, "submarino", 2)
# lista_destructor = colocar_navio(matriz_principal, "destructor", 2)
# lista_crucero = colocar_navio(matriz_principal, "crucero", 2) 
# lista_acorazado = colocar_navio(matriz_principal, "acorazado", 2)





############################################################################################################################
"""#########################################################################################################################
############################################################################################################################
"""#########################################################################################################################
############################################################################################################################
"""#########################################################################################################################
############################################################################################################################
"""#########################################################################################################################



#BANDERAS_PANTALLAS:
bandera_ventana = 1
bandera_corriendo = True

#WHILE PRINCIPAL

while bandera_corriendo == True:

    # FOR PRINCIPAL
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_corriendo = False

        ############### BOTONES ##################
        ###########################################

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()

            if rectangulo_salir.collidepoint(pos_mouse): #Salir
                bandera_corriendo = False
            
            if rectangulo_jugar.collidepoint(pos_mouse): #Jugar
                bandera_ventana = 2

            if rectangulo_volver.collidepoint(pos_mouse): #Volver
                bandera_ventana = 1

        ############### PANTALLAS ################
        ###########################################

        if bandera_ventana == 1: #MENU PRINCIPAL

            #Imagen inicio
            ventana_principal.blit(imagen_inicio,(0,0))
            #Textos
            ventana_principal.blit(texto_nivel,( pos_nivel[0]+coordenadas_texto_nivel[0], pos_nivel[1] + coordenadas_texto_nivel[1]))
            ventana_principal.blit(texto_jugar,( pos_jugar[0]+coordenadas_texto_jugar[0], pos_jugar[1] + coordenadas_texto_jugar[1]))
            ventana_principal.blit(texto_puntaje,(pos_puntaje[0] + coordenadas_texto_puntaje[0], pos_puntaje[1] + coordenadas_texto_puntaje[1]))
            ventana_principal.blit(texto_salir,(pos_salir[0] + coordenadas_texto_salir[0], pos_salir[1] + coordenadas_texto_salir[1]))

            # Rectangulos/Botones
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_nivel,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_jugar,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_puntaje,width=5, border_radius=5)
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_salir,width=5, border_radius=5)
    
                
        if bandera_ventana == 2: #JUEGO

            # Fondo tablero: (MAR)
            ventana_principal.blit(imagen_fondo_tablero,(0,0))

            # # Tablero:
            dibujar_tablero(matriz_principal)
            # crear_botones_tablero(matriz_rectangulos)
            # Volver
            ventana_principal.blit(texto_volver,(pos_volver[0] + coordenadas_texto_volver[0], pos_volver[1] + coordenadas_texto_volver[1]))
            pygame.draw.rect(ventana_principal,NEGRO,rectangulo_volver,width=5, border_radius=5)


                



    # pygame.display.update()
    pygame.display.flip() 

pygame.quit()