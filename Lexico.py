import tkinter as tk
import ply.lex as lex
from  tkinter import ttk
from tkinter import *

resultado_lexema = [] #Resultado

#Nombre de tokens
tokens =  ( 
    'PARENTESIS_APERTURA',
    'PARENTESIS_CIERRE',
    'INTERROGACION_APERTURA',
    'INTERROGACION_CIERRE',
    'ADMIRACION_APERTURA',
    'ADMIRACION_CIERRE',
    'COMILLA_SIMPLE',
    'PALABRA', 
    'NUMERO', 
    'SIMBOLOS', 
    'COMA'
)
#Expresiones regulares para los tokens
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_INTERROGACION_APERTURA = r'\¿'
t_INTERROGACION_CIERRE = r'\?'
t_ADMIRACION_APERTURA = r'\¡'
t_ADMIRACION_CIERRE = r'\!'
t_COMILLA_SIMPLE = r'\''
t_PALABRA = r'[A-Za-z-Ñ-ñ]+'
t_NUMERO = r'[0-9]+'
t_SIMBOLOS = r'\.|;|\/|\=|\+|\-|:|t_COMA'
t_COMA = r','
t_ignore =' \t' #Para ignorar los espacios

def t_error( t): #Si el token no es válido
    global resultado_lexema
    estado = [t.value]
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema
    analizador = lex.lex() #Instancia del analizador
    analizador.input(data) # Al analizador se le pasa el texto ingresado por el usuario
    resultado_lexema.clear()
    while True:
        tok = analizador.token()  #Se obtiene si los datos son coinciden con alguna expresion regular si es asi se obtiene el nombre del token
        if not tok:  #Si no coincide con ninguna expresion regular regresa None
            break

# instanciamos el analizador lexico
analizador = lex.lex()
