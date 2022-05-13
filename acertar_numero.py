print("Programa para jugar a acertar el número\n")

#-------------------------------------------------------------------------------------------------------------------------------------
#Importación de la biblioteca / módulo para generar variables pseudo-aleatorias
import random

#Importación de la biblioteca /módulo para realizar paradas momentaneas
import time

#Importación de la biblioteca / módulo para poder realizar limpiezas de terminal
import os

#-------------------------------------------------------------------------------------------------------------------------------------
#Inicialización de variables
opcn_usuario = 0
contador_opciones = 0
limpiar_pantalla = str("n") #Para que por defecto no haga la limpieza del terminal o consola

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para informar de las opciones
def opciones_jugar():
    print("1.- Para jugar desde el rango del 1 al 100\n")
    print("2.- Para establecer rangos personalizados\n")
    print("3.- Finalizar la ejecución del programa\n")

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para limpiar el terminal o consola, codigo copiado vilmente de una web y modificado para realizar pregunta
#Principalmente es para Linux y sistemas operativos basados en MS-DOS
def limpiar():
    if contador_opciones >= 1:
        limpiar_pantalla = str(input("¿Quiere limpiar la pantalla? (s/n)\n"))
        if limpiar_pantalla == "s":
            command = 'clear'
            if os.name in ('nt', 'dos'):
                command = 'cls'
            os.system(command)

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para generar el número aleatorio desde el 1 al 100
def aleatorio_defecto():
    contador_intentos = 0
    aleatorio_generado = int(random.randint(1, 100))
    numero = int(-1) #Hago que esta variable provoque la entrada al bucle siguiente
    while numero != aleatorio_generado:
        numero = int(input("Introduzca un número\n"))
        if numero < aleatorio_generado:
            print("El número", numero, "es menor que el número a acertar\n")
        elif numero > aleatorio_generado:
            print("El número", numero, "es mayor que el número a acertar\n")
        else:
            print("¡¡Has acertado el número!!\n")
        contador_intentos = contador_intentos + 1
        if numero == aleatorio_generado:
            print("Has realizado", contador_intentos, "intentos\n")
        time.sleep(4)

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para generar un número aleatorio desde un rango personalizado
def aleatorio_personalizado():
    contador_intentos = 0
    primer_rango= int(input("Introduzca el primer rango\n"))
    print("")
    segundo_rango = int(input("Introduzca el segundo rango\n"))
    print("")
    if primer_rango < segundo_rango:
        aleatorio_generado = int(random.randint(primer_rango, segundo_rango))
    else:
        aleatorio_generado = int(random.randint(segundo_rango, primer_rango))
    numero = int(-999999999999999999999999999999999) #Provoco que entre al bucle con un número improbable
    while numero != aleatorio_generado:
        numero = int(input("Introduzca un número\n"))
        if numero < aleatorio_generado:
            print("El número", numero, "es menor que el número a acertar\n")
        elif numero > aleatorio_generado:
            print("El número", numero, "es mayor que el número a acertar\n")
        else:
            print("¡¡Has acertado el número!!\n")
        contador_intentos = contador_intentos + 1
        if numero == aleatorio_generado:
            print("Has realizado", contador_intentos, "intentos\n")
        time.sleep(4)

#-------------------------------------------------------------------------------------------------------------------------------------
#Código inicial y esencial para que el programa realice todas las instrucciones
while opcn_usuario != "3":
    limpiar()
    contador_opciones = contador_opciones + 1 #Contador para que después de la primera iteración pregunte por la función de limpiar
    opciones_jugar()
    opcn_usuario = str(input("Introduzca la opción deseada\n"))
    if opcn_usuario == "1":
        aleatorio_defecto()
    elif opcn_usuario == "2":
        aleatorio_personalizado()
    elif opcn_usuario == "3":
        print("Programa finalizado")
    else:
        print("Se ha equivocado al introducir las opciones, son:")
        opciones_jugar()
