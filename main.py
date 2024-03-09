#!/usr/bin/env python3

from pwn import *
import signal, sys, time
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\n[!] Saliendo...\n", 'red'))
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def def_main():

    def suma(a, b):
        return a + b
    
    def resta(a, b):
        return a - b
    
    def multiplicacion(a, b):
        return a * b
    
    def division(a, b):
        if b != 0:
            return a / b
        
        else:
            return colored("\n[!] Error: No se puede dividir por cero.\n", 'red')

    p1 = log.progress("Calculator initialize")
    p1.status("Cargando calculadora...")

    time.sleep(2)

    while True:
        print(colored("\n\n[*] Seleccione un operación: \n", 'blue'))
        print(colored("[*] 1. Suma", 'blue'))
        print(colored("[*] 2. Resta", 'blue'))
        print(colored("[*] 3. Multiplicación", 'blue'))
        print(colored("[*] 4. División", 'blue'))
        print(colored("[*] 5. Salir", 'blue'))

        time.sleep(2)

        opc = int(input(colored("\n[*] Ingrese el número: ", 'yellow')))

        time.sleep(2)

        # Salir
        if opc == 5:
            print(colored("\n\n[!] Saliendo satisfactoriamente...\n", 'red'))
            break

        try:
            n1 = float(input(colored("\n[*] Ingrese el primer número: ", 'yellow')))
            n2 = float(input(colored("[*] Ingrese el segundo número: ", 'yellow')))
        
        except ValueError:
            print(colored("\n\n[!] Error: Ingresaste números invalidos.\n", 'red'))
            continue

        if opc == 1:
            print(colored("\n\n[+] Resultado: ", 'blue'), suma(n1, n2))

        elif opc == 2:
            print(colored("\n\n[+] Resultado: ", 'blue'), resta(n1, n2))

        elif opc == 3:
            print(colored("\n\n[+] Resultado: ", 'blue'), multiplicacion(n1, n2))

        elif opc == 4:
            print(colored("\n\n[+] Resultado: ", 'blue'), division(n1, n2))

        else:
            print(colored("\n\n[!] Opción invalida. Por favor elija bien...\n", 'red'))

if __name__ == "__main__":
    def_main()








        

    