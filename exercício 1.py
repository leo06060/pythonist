# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Ficheiro: exercício1.py
# Programa caótico que imprime um número variável de termos



def main():
        print("Este programa ilustra uma função caótica")
        x = (input("Introduza um número de 1 a 10: "))
        n = (input("Quantos números quer imprimir?: "))
        average(x,n)

def average(x,n):

    for i in range (n):
        x = 3.9 * x * (1 - x)
        print (x)
    
main()
    