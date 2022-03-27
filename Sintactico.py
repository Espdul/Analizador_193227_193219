from tokenize import String
import ply.yacc as yacc
from Lexico import tokens
import Lexico
import Semantico
from tkinter import *
import tkinter as tk
# resultado del analisis
resultado_gramatica = []

nombres = {}

def p_gt1(t):
    'gt : letra resto'
    nombres[t[0]] = t[1]

def p_gt2(t):
    'gt : digito resto'
    nombres[t[0]] = t[1]
    
def p_gt3(t):
    'gt : pg resto'
    nombres[t[0]] = t[1]
    
def p_gt4(t):
    'gt : ex resto'
    nombres[t[0]] = t[1]
    
def p_gt5(t):
    'gt : ps resto'
    nombres[t[0]] = t[1]
    
def p_gt6(t):
    'gt : c resto'
    nombres[t[0]] = t[1]
    
def p_resto1(t):
    'resto : letra resto'
    t[0] = t[1]

def p_resto2(t):
    'resto : digito resto'
    t[0] = t[1]

def p_resto3(t):
    'resto : simbolo resto'
    t[0] = t[1]

def p_resto4(t):
    'resto : pg resto'
    t[0] = t[1]

def p_resto5(t):
    'resto : ex resto'
    t[0] = t[1]

def p_resto6(t):
    'resto : ps resto'
    t[0] = t[1]

def p_resto7(t):
    'resto : c resto'
    t[0] = t[1]

def p_resto8(t):
    'resto : empty'
    t[0] = t[1]

def p_simbolo1(t):
    'simbolo : SIMBOLOS'
    t[0] = t[1]

def p_simbolo2(t):
    'simbolo : COMA'
    t[0] = t[1]

def p_pg(t):
    'pg : ia pb ic'
    t[0] = t[1]
    
def p_ex(t):
    'ex : ea pb ec'
    t[0] = t[1]
    
def p_ps(t):
    'ps : pa pb pc'
    t[0] = t[1]
    
def p_c(t):
    'c : cs pb cs'
    t[0] = t[1]
    
def p_ia(t):
    'ia : INTERROGACION_APERTURA'
    t[0] = t[1]
    
def p_ic(t):
    'ic : INTERROGACION_CIERRE'
    t[0] = t[1]
    
def p_ea(t):
    'ea : ADMIRACION_APERTURA'
    t[0] = t[1]
    
def p_ec(t):
    'ec : ADMIRACION_CIERRE'
    t[0] = t[1]
    
def p_pa(t):
    'pa : PARENTESIS_APERTURA'
    t[0] = t[1]
    
def p_pc(t):
    'pc : PARENTESIS_CIERRE'
    t[0] = t[1]
    
def p_cs(t):
    'cs : COMILLA_SIMPLE'
    t[0] = t[1]
    
def p_pb1(t):
    'pb : letra comp'
    t[0] = t[1]
    
def p_pb2(t):
    'pb : digito comp'
    t[0] = t[1]
   
def p_comp1(t):
    'comp : letra comp'
    t[0] = t[1]
    
def p_comp2(t):
    'comp : digito comp'
    t[0] = t[1]
    
def p_comp3(t):
    'comp : coma comp'
    t[0] = t[1]
    
def p_comp4(t):
    'comp : empty'
    t[0] = t[1]
    
def p_letra(t):
    'letra : PALABRA'
    t[0] = t[1]

def p_digito(t):
    'digito : NUMERO'
    t[0] = t[1]

def p_coma(t):
    'coma : COMA'
    t[0] = t[1]

def p_empty(t):
    '''empty :'''
    pass

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {} en la posición  {} ".format( str(t.type),str(t.value),str(t.lexpos))
    else:
        if t is None:
            resultado = "Error sintactico 'Hace falta completar la expresion'"
    resultado_gramatica.append(resultado)
    
# instanciamos el analizador sistactico
parser = yacc.yacc()
def prueba_sintactica(data):
    texto = data
    Lexico.prueba(data)
    if len(Lexico.resultado_lexema) == 0:
        global resultado_gramatica
        resultado_gramatica.clear()

        for item in data.splitlines():
            if item:
                gram = parser.parse(item)
                if gram:
                    resultado_gramatica.append(str(gram))
                    
        if len(resultado_gramatica) == 0 :
            resultado = "La expresion '" + data + "' es correcta"
            resultado_gramatica.append(resultado)
            mayus = texto.upper()
            Semantico.turing_M(mayus)
        else:
            root = tk.Tk()
            root.title("Resultado")
            root.geometry('500x200')
            label2 = Label(root, text=resultado_gramatica).place(x=10,y=10)
            root.mainloop()
    else:
        resultado_gramatica.clear()
        resultado = "Error léxico " + str(Lexico.resultado_lexema[0])
        resultado_gramatica.append(resultado)
        root = tk.Tk()
        root.title("Resultado")
        root.geometry('500x200')
        label2 = Label(root, text=resultado_gramatica).place(x=10,y=10)
        root.mainloop()
    return resultado_gramatica