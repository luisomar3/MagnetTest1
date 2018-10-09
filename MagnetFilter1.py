# -*- coding: utf-8 -*-
"""
Created on Tuesday Oct 8 12:47:50 2018
Author: luisomar3
Python Version: 3.6.2
usage: python MagnetFilter1.py
"""



def validar(expresion):
    """Funcion para validar si una formula matematica esta bien formulada

    :param expresion: Expresion matematica a validar.
    :type expresion: str
    
    :returns: boolean
    """
    
    brackets = {')':'('}
    pila = [] #Las listas en python pueden comportarse como pilas lo cual es muy util
    
    if type(expresion) != str : #Me aseguro que siempre reciba un string
        raise TypeError
        
    for char in expresion: #recorro el string
        if char == "(":
            pila.append(char) #Si me encuentro con un parentesis de apertura lo agrego a la pila
        elif char in ")":
            if not pila or pila.pop() != "(": #Me aseguro que la pila no esté vacia antes de extraer el parentesis
                return False

    return not pila #Si esta vacio esta bien formada la expresion, si no, esta mal. 
                    #Por como funciona las listas en python usamos el not
    
def main():
    print("Bienvenido")
    while True:
        formula = str(input( '''Introduzca la formula matemática:
        '''))
        a = validar(formula)
        print(a)

if __name__ == '__main__':
    
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Hasta luego")
    
    