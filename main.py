from tkinter import *
import tkinter as tk
import Sintactico

def inicio():
    texto = input1.get()
    if len(texto) > 0:
        Sintactico.prueba_sintactica(texto)

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Analizador Semántico")
    ventana.geometry('700x400')
    ventana.configure(bg='#04A9C7')
    ventana.resizable(0,0)    
    label1 = Label(ventana, text="Analizador Semántico", bg="#04A9C7",font=("Arial", 30)).place(x=150,y=10)
    label2 = Label(ventana, text="Inserte un texto para convertirlo en código morse",bg="#04A9C7",font=("Arial", 20)).place(x=60, y= 110)
    input1 = Entry(ventana, width=60,font=('Consolas',15))
    input1.place(x=30,y= 160, height=30) 
    submit1 = Button(ventana, text="Analizar",width=20, height=2, bg="#ffffff",command= lambda:inicio()).place(x=250,y= 220)   
    ventana.mainloop()