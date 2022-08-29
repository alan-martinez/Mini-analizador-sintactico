from operator import is_

from stack import Stack
import tipos

def main():
    print("Entrada ejercicio 1: ")
    input1("hola+mundo$")
    print ("\n")
    print("Entrada ejercicio 2: ")
    input2("a+b+c+d+e+f$")

def input1(texto):
    print(texto)
    pila = Stack()
    #Estado actual
    estado = tipos.INICIAL
    d = 2
    lexema = ""

    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == tipos.INICIAL):
            if (es_Letra(c) or c == '_'):
                estado = tipos.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(tipos.SIMBOLO)
                pila.push(d)
                d+=1
                estado = tipos.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(tipos.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")

        elif(estado == tipos.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = tipos.IDENTIFICADOR
                lexema += c
            else:
                pila.push(tipos.IDENTIFICADOR)
                pila.push(d)
                d += 1
                estado = tipos.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1

def input2(texto):
    print(texto)

    pila = Stack()
    #Estado inicial
    estado = tipos.INICIAL
    d2 = 2
    d3 = 3
    lexema = ""
    
    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == tipos.INICIAL):
            if (es_Letra(c) or c == '_'):
                estado = tipos.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                pila.push(tipos.SIMBOLO)
                pila.push(d3)
                estado = tipos.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(tipos.E)
                nuevaPila.push(1)
                nuevaPila.mostrarPila()
            else:
                print("ERROR")

        elif(estado == tipos.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = tipos.IDENTIFICADOR
                lexema += c
            else:
                pila.push(tipos.IDENTIFICADOR)
                pila.push(d2)
                estado = tipos.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1

def isReal(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return True
    else:
        return False

def es_Letra(c):
    if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
        return True
    else:
        return False



main()
