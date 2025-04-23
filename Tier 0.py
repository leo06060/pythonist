# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:49:02 2025

@author: leono
"""

from graphics import *


#criação da janela que representa a sala do restaurante e o respetivo sistema de coordenadas
def main():            
    win = GraphWin("Butão", 900, 900)
    win.setCoords(0, 0, 150, 150)

    if win.checkMouse():
        win.close()
        
main()
