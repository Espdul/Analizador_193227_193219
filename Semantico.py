import tkinter as tk
from tkinter import *
from tkinter import filedialog
import re
from tkinter import ttk

def turing_M (textoCodificado):
    textoPlano = ""
    state = 'q0' #estados de la maquina de turing
    blank = '#' #simbolo blanco de el alfabeto dela cinta
    
    rules = map(tuple,#reglas de transicion
    ["q0, , / ,right,q0".split(","),
    "q0,A, .- ,right,q0".split(","),
    "q0,B, -... ,right,q0".split(","),
    "q0,C, -.-. ,right,q0".split(","),
    "q0,D, -.. ,right,q0".split(","),
    "q0,E, . ,right,q0".split(","),
    "q0,F, ..-. ,right,q0".split(","),
    "q0,G, --. ,right,q0".split(","),
    "q0,H, .... ,right,q0".split(","),
    "q0,I, .. ,right,q0".split(","),
    "q0,J, .--- ,right,q0".split(","),
    "q0,K, -.- ,right,q0".split(","),
    "q0,L, .-.. ,right,q0".split(","),
    "q0,M, -- ,right,q0".split(","),
    "q0,N, -. ,right,q0".split(","),
    "q0,O, --- ,right,q0".split(","),
    "q0,P, .--. ,right,q0".split(","),
    "q0,Q, --.- ,right,q0".split(","),
    "q0,R, .-. ,right,q0".split(","),
    "q0,S, ... ,right,q0".split(","),
    "q0,T, - ,right,q0".split(","),
    "q0,U, ..- ,right,q0".split(","),
    "q0,V, ...- ,right,q0".split(","),
    "q0,W, .-- ,right,q0".split(","),
    "q0,X, -..- ,right,q0".split(","),
    "q0,Y, -.-- ,right,q0".split(","),
    "q0,Z, --.. ,right,q0".split(","),
    "q0,0, ----- ,right,q0".split(","),
    "q0,1, .---- ,right,q0".split(","),
    "q0,2, ..--- ,right,q0".split(","),
    "q0,3, ...-- ,right,q0".split(","),
    "q0,4, ....- ,right,q0".split(","),
    "q0,5, ..... ,right,q0".split(","),
    "q0,6,-.... ,right,q0".split(","),
    "q0,7,--... ,right,q0".split(","),
    "q0,8,---.. ,right,q0".split(","),
    "q0,9,----. ,right,q0".split(","),
    "q0,Ñ, --.-- ,right,q0".split(","),
    "q0,¿, ..-.- ,right,q0".split(","),
    "q0,?, ..--.. ,right,q0".split(","),
    "q0,(, -.--. ,right,q0".split(","),
    "q0,), -.--.- ,right,q0".split(","),
    "q0,., .-.-.- ,right,q0".split(","),
    "q0,', .----. ,right,q0".split(","),
    "q0,;, -.-.-. ,right,q0".split(","),
    "q0,:, ---... ,right,q0".split(","),
    "q0,/, -..-. ,right,q0".split(","),
    "q0,+, .-.-. ,right,q0".split(","),
    "q0,-, -....- ,right,q0".split(","),
    "q0,=, -...- ,right,q0".split(","),
    "q0 , --..-- right q0".split(),
    "q0,¡, --...- ,right,q0".split(","),
    "q0,!, -.-.-- ,right,q0".split(","),
    "q0  # # right q1".split(),])
    tape = list(textoCodificado)    #cinta
    final = 'q1'  #estado valido y/o final
    pos = 0 #posicion siguiente de la maquina de turing
    st = state
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)
    while True:
        if st == final: break
        if (st, tape[pos]) not in rules: break
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
        if dr == 'left':  #movimiento del cabezal
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1
    for i in tape:
        if i != "#":
            textoPlano = textoPlano + i
    
    resultado = Tk()
    resultado.title("Resultado")
    mensake = Text(resultado ,width=50, height=20)
    mensake.insert(tk.INSERT, textoPlano)
    mensake.grid(row=1,column=0)
    resultado.mainloop()
