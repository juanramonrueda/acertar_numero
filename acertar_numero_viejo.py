#-------------------------------------------------------------------------------------------------------------------------------------
#Importación de la biblioteca / módulo para generar variables pseudo-aleatorias
import random

#Importación de la biblioteca / módulo para realizar paradas momentaneas
import time

#Importación de la biblioteca / módulo para poder realizar limpiezas de terminal
import os

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para informar de las opciones
def mostrar_menu():
    print("1.- Para jugar desde el rango del 1 al 100\n")
    print("2.- Para establecer rangos personalizados\n")
    print("3.- Finalizar la ejecución del programa\n")

#-------------------------------------------------------------------------------------------------------------------------------------
#Función para limpiar el terminal o consola, codigo copiado vilmente de una web y modificado para realizar pregunta
#Principalmente es para Linux y sistemas operativos basados en MS-DOS
def limpiar():
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
    aleatorio_generado = random.randint(1, 100)    
    numero = -1 #Hago que esta variable provoque la entrada al bucle siguiente
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
    cota_inferior = int(input("Introduzca la cota inferior\n"))
    print("")
    cota_superior = int(input("Introduzca la cota superior\n"))
    print("")

    # Si la cota inferior es mayor que la cota superior intercambiamos los valores
    if cota_inferior > cota_superior:
        aux = cota_inferior
        cota_inferior = cota_superior
        cota_superior = aux
    
    # Generamos un número aleatorio dentro del rango
    aleatorio_generado = random.randint(cota_inferior, cota_superior)

    # Incializamos el número con un número que está fuera de rango
    numero = cota_inferior - 1
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
# Programa Principal
def main():
    print("Programa para jugar a acertar el número\n")

    #Inicialización de variables
    opcn_usuario = 0

    #Código inicial y esencial para que el programa realice todas las instrucciones
    while opcn_usuario != 3:
        mostrar_menu()
        opcn_usuario = int(input("Introduzca la opción deseada\n"))
        while opcn_usuario < 1 or opcn_usuario > 3:
            print("La opción no es correcta. Seleccione un valor entre 1 y 3")
            opcn_usuario = int(input("Introduzca la opción deseada\n"))

        if opcn_usuario == 1:
            aleatorio_defecto()
        elif opcn_usuario == 2:
            aleatorio_personalizado()
        else:
            print("Programa finalizado")

        if opcn_usuario != 3:
            limpiar()

#-------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()