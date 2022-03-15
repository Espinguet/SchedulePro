# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:29:31 2022

@author: Jordi Castillo
"""

import tkinter
from tkinter import *
from PIL import ImageTk, Image
import datetime

ventana = Tk()
ventana.title("SchedulePro")
ventana.geometry("870x550")
ventana.configure(background = 'grey24')

#Entrada
etiqueta_establecer = Label(ventana, text = "Establir horari:", 
                      font = ("Calibri 20"), bg = 'grey24', fg = 'white')
etiqueta_entrada = Label(ventana, text = "Hora d'entrada:", 
                   font = ("Calibri 18"), bg = 'grey24', fg = 'white')
etiqueta_sortida = Label(ventana, text = "Hora de sortida:", 
                   font = ("Calibri 18"), bg = 'grey24', fg = 'white')

etiqueta_establecer.grid(row = 0, column = 0, padx = 10, pady = 5)
etiqueta_entrada.grid(row = 1, column = 1, padx = 10, pady = 5)
etiqueta_sortida.grid(row = 1, column = 2, padx = 10, pady = 5)

#Càlcul d'hores

def hores():
    entr1 = clicked_1.get()
    y = datetime.datetime().strptime(entr1, '%H %M')
    print(y)

#Días
lunes = Label(ventana, text = "Dilluns", font = ("Calibri 15"), 
        bg = 'grey24', fg = 'white')
martes = Label(ventana, text = "Dimarts", font = ("Calibri 15"), 
         bg = 'grey24', fg = 'white')
miercoles = Label(ventana, text = "Dimecres", font = ("Calibri 15"), 
            bg = 'grey24', fg = 'white')
jueves = Label(ventana, text = "Dijous", font = ("Calibri 15"), 
         bg = 'grey24', fg = 'white')
viernes = Label(ventana, text = "Divendres", font = ("Calibri 15"), 
          bg = 'grey24', fg = 'white')
sabado = Label(ventana, text = "Dissabte", font = ("Calibri 15"), 
         bg = 'grey24', fg = 'white')
domingo = Label(ventana, text = "Diumenge", font = ("Calibri 15"), 
          bg = 'grey24', fg = 'white')

lunes.grid(row = 2, column = 0, padx = 10, pady = 5 )
martes.grid(row = 3, column = 0, padx = 10, pady = 5 )
miercoles.grid(row = 4, column = 0, padx = 10, pady = 5 )
jueves.grid(row = 5, column = 0, padx = 10, pady = 5 )
viernes.grid(row = 6, column = 0, padx = 10, pady = 5 )
sabado.grid(row = 7, column = 0, padx = 10, pady = 5 )
domingo.grid(row = 8, column = 0, padx = 10, pady = 5 )

options = ["00:00", "00:30",
           "01:00", "01:30",
           "02:00", "02:30",
           "03:00", "03:30",
           "04:00", "04:30",
           "05:00", "05:30",
           "06:00", "06:30",
           "07:00", "07:30",
           "08:00", "08:30",
           "09:00", "09:30",
           "10:00", "10:30",
           "11:00", "11:30",
           "12:00", "12:30",
           "13:00", "13:30",
           "14:00", "14:30",
           "15:00", "15:30",
           "16:00", "16:30",
           "17:00", "17:30",
           "18:00", "18:30",
           "19:00", "19:30",
           "20:00", "20:30",
           "21:00", "21:30",
           "22:00", "22:30",
           "23:00", "23:30",
           "24:00", "24:30",
]

clicked_1 = StringVar()
clicked_2 = StringVar()
clicked_3 = StringVar()
clicked_4 = StringVar()
clicked_5 = StringVar()
clicked_6 = StringVar()
clicked_7 = StringVar()
clicked_8 = StringVar()
clicked_9 = StringVar()
clicked_10 = StringVar()
clicked_11 = StringVar()
clicked_12 = StringVar()
clicked_13 = StringVar()
clicked_14 = StringVar()

clicked.set(options[0])

#Horas de entrada
entrada1 = OptionMenu(ventana, clicked_1, *options)
entrada2 = OptionMenu(ventana, clicked_2, *options)
entrada3 = OptionMenu(ventana, clicked_3, *options)
entrada4 = OptionMenu(ventana, clicked_4, *options)
entrada5 = OptionMenu(ventana, clicked_5, *options)
entrada6 = OptionMenu(ventana, clicked_6, *options)
entrada7 = OptionMenu(ventana, clicked_7, *options)

entrada1.grid(row = 2, column = 1, padx = 10, pady = 5 )
entrada2.grid(row = 3, column = 1, padx = 10, pady = 5 )
entrada3.grid(row = 4, column = 1, padx = 10, pady = 5 )
entrada4.grid(row = 5, column = 1, padx = 10, pady = 5 )
entrada5.grid(row = 6, column = 1, padx = 10, pady = 5 )
entrada6.grid(row = 7, column = 1, padx = 10, pady = 5 )
entrada7.grid(row = 8, column = 1, padx = 10, pady = 5 )

#Horas de salida
sortida1 = OptionMenu(ventana, clicked_8, *options)
sortida2 = OptionMenu(ventana, clicked_9, *options)
sortida3 = OptionMenu(ventana, clicked_10, *options)
sortida4 = OptionMenu(ventana, clicked_11, *options)
sortida5 = OptionMenu(ventana, clicked_12, *options)
sortida6 = OptionMenu(ventana, clicked_13, *options)
sortida7 = OptionMenu(ventana, clicked_14, *options)

sortida1.grid(row = 2, column = 2, padx = 10, pady = 5 )
sortida2.grid(row = 3, column = 2, padx = 10, pady = 5 )
sortida3.grid(row = 4, column = 2, padx = 10, pady = 5 )
sortida4.grid(row = 5, column = 2, padx = 10, pady = 5 )
sortida5.grid(row = 6, column = 2, padx = 10, pady = 5 )
sortida6.grid(row = 7, column = 2, padx = 10, pady = 5 )
sortida7.grid(row = 8, column = 2, padx = 10, pady = 5 )

#Número trabajadores
Num_trab = Label(ventana, text = "Número de treballadors:", font = ("Calibri 15"), 
           bg = 'grey24', fg = 'white')
Num = Entry(ventana, font = ("Calibri"))

Num_trab.grid(row = 9, column = 1, padx = 10, pady = 5 )
Num.grid(row = 9, column = 2, padx = 10, pady = 5)

key = Label(ventana, text = "Important: Introduir horari entre 00:00h i 23:59h", 
      font = ("Calibri 15"), bg = 'grey24', fg = 'white')
key.grid(row = 10, column = 1, columnspan = 2, padx = 10, pady = 10 )

#Botón cambio de ventana
def envia_boton():
    n = int(Num.get())
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("800x500")
    ventana_nueva1.title("Treballadors")
    ventana_nueva1.configure(bg = 'grey24')



    #Entrada 2
    etiqueta_treballador = Label(ventana_nueva1, text="Establir tasques:", 
                           font=("Calibri 20"), bg = 'grey24', fg = 'white')
    etiqueta_nom = Label(ventana_nueva1, text="Nom del treballador:", 
                   font=("Calibri 18"), bg = 'grey24', fg = 'white')
    etiqueta_tasca = Label(ventana_nueva1, text="Tasca assignada:", 
                     font=("Calibri 18"), bg = 'grey24', fg = 'white')

    etiqueta_treballador.grid(row=0, column=0, padx=10, pady=5)
    etiqueta_nom.grid(row=1, column=0, padx=10, pady=5)
    etiqueta_tasca.grid(row=1, column=1, padx=10, pady=5)
        
    if n == 1:
        treballador1 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca1 = Entry(ventana_nueva1, font=("Calibri 15"))

        treballador1.grid(row=2, column=0, padx=10, pady=5)
        tasca1.grid(row=2, column=1, padx=10, pady=5)
    elif n == 2:
        treballador1 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca1 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador2 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca2 = Entry(ventana_nueva1, font=("Calibri 15"))

        treballador1.grid(row=2, column=0, padx=10, pady=5)
        tasca1.grid(row=2, column=1, padx=10, pady=5)

        treballador2.grid(row=3, column=0, padx=10, pady=5)
        tasca2.grid(row=3, column=1, padx=10, pady=5)

    elif n == 3:
        treballador1 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca1 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador2 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca2 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador3 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca3 = Entry(ventana_nueva1, font=("Calibri 15"))

        treballador1.grid(row=2, column=0, padx=10, pady=5)
        tasca1.grid(row=2, column=1, padx=10, pady=5)

        treballador2.grid(row=3, column=0, padx=10, pady=5)
        tasca2.grid(row=3, column=1, padx=10, pady=5)

        treballador3.grid(row=4, column=0, padx=10, pady=5)
        tasca3.grid(row=4, column=1, padx=10, pady=5)

    elif n == 4:
        treballador1 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca1 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador2 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca2 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador3 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca3 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador4 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca4 = Entry(ventana_nueva1, font=("Calibri 15"))

        treballador1.grid(row=2, column=0, padx=10, pady=5)
        tasca1.grid(row=2, column=1, padx=10, pady=5)

        treballador2.grid(row=3, column=0, padx=10, pady=5)
        tasca2.grid(row=3, column=1, padx=10, pady=5)

        treballador3.grid(row=4, column=0, padx=10, pady=5)
        tasca3.grid(row=4, column=1, padx=10, pady=5)

        treballador4.grid(row=5, column=0, padx=10, pady=5)
        tasca4.grid(row=5, column=1, padx=10, pady=5)

    elif n == 5:
        treballador1 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca1 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador2 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca2 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador3 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca3 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador4 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca4 = Entry(ventana_nueva1, font=("Calibri 15"))
        treballador5 = Entry(ventana_nueva1, font=("Calibri 15"))
        tasca5 = Entry(ventana_nueva1, font=("Calibri 15"))

        treballador1.grid(row=2, column=0, padx=10, pady=5)
        tasca1.grid(row=2, column=1, padx=10, pady=5)

        treballador2.grid(row=3, column=0, padx=10, pady=5)
        tasca2.grid(row=3, column=1, padx=10, pady=5)

        treballador3.grid(row=4, column=0, padx=10, pady=5)
        tasca3.grid(row=4, column=1, padx=10, pady=5)

        treballador4.grid(row=5, column=0, padx=10, pady=5)
        tasca4.grid(row=5, column=1, padx=10, pady=5)

        treballador5.grid(row=6, column=0, padx=10, pady=5)
        tasca5.grid(row=6, column=1, padx=10, pady=5)

    else:
        etiqueta_error = Label(ventana_nueva1, 
                         text="*Introdueixi un número de treballadors entre 1 i 5.", 
                         font=("Calibri 15"), bg='grey24', fg='white')
        etiqueta_error.grid(row=2, column=0, columnspan = 3, padx=10, pady=5)
        
    def calcular_boton():
        ventana_nueva2 = Toplevel()
        ventana_nueva2.geometry("800x500")
        ventana_nueva2.title("Horari de cada treballador")
        ventana_nueva2.configure(bg = 'grey24')
        
        if n == 1:
            treb1 = treballador1.get() + ": " + tasca1.get() 
            
            trb1 = Label(ventana_nueva2, text = treb1, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb1.grid(row = 1, column = 0, padx = 10, pady = 5)
            
        elif n == 2:
            treb1 = treballador1.get() + ": " + tasca1.get() 
            trb1 = Label(ventana_nueva2, text = treb1, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb1.grid(row = 1, column = 0, padx = 10, pady = 5)
            
            treb2 = treballador2.get() + ": " + tasca2.get() 
            trb2 = Label(ventana_nueva2, text = treb2, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb2.grid(row = 2, column = 0, padx= 10, pady = 5)
            
        elif n == 3:
            treb1 = treballador1.get() + ": " + tasca1.get()
            trb1 = Label(ventana_nueva2, text = treb1, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb1.grid(row = 1, column = 0, padx = 10, pady = 5)
            
            treb2 = treballador2.get() + ": " + tasca2.get()
            trb2 = Label(ventana_nueva2, text = treb2, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb2.grid(row = 2, column = 0, padx= 10, pady = 5)
            
            treb3 = treballador3.get() + ": " + tasca3.get() 
            trb3 = Label(ventana_nueva2, text = treb2, font = ("Calibri 20"), 
                   bg = 'grey24', fg = 'White')
            trb3.grid(row = 3, column = 0, padx= 10, pady = 5)
            
        elif n == 4:
                treb1 = treballador1.get() + ": " + tasca1.get() 
                trb1 = Label(ventana_nueva2, text = treb1, font = ("Calibri 20"), 
                       bg = 'grey24', fg = 'White')
                trb1.grid(row = 1, column = 0, padx = 10, pady = 5)
                
                treb2 = treballador2.get() + ": " + tasca2.get() 
                trb2 = Label(ventana_nueva2, text = treb2, font = ("Calibri 20"), 
                       bg = 'grey24', fg = 'White')
                trb2.grid(row = 2, column = 0, padx= 10, pady = 5)
                
                treb3 = treballador3.get() + ": " + tasca3.get() 
                trb3 = Label(ventana_nueva2, text = treb3, font = ("Calibri 20"), 
                       bg = 'grey24', fg = 'White')
                trb3.grid(row = 3, column = 0, padx= 10, pady = 5)
                
                treb4 = treballador4.get() + ": " + tasca4.get()
                trb4 = Label(ventana_nueva2, text = treb4, font = ("Calibri 20"), 
                       bg = 'grey24', fg = 'White')
                trb4.grid(row = 4, column = 0, padx= 10, pady = 5)
                
        elif n == 5:
                    treb1 = treballador1.get() + ": " + tasca1.get() 
                    trb1 = Label(ventana_nueva2, text = treb1, font = ("Calibri 20"), 
                           bg = 'grey24', fg = 'White')
                    trb1.grid(row = 1, column = 0, padx = 10, pady = 5)
                    
                    treb2 = treballador2.get() + ": " + tasca2.get() 
                    trb2 = Label(ventana_nueva2, text = treb2, font = ("Calibri 20"), 
                           bg = 'grey24', fg = 'White')
                    trb2.grid(row = 2, column = 0, padx= 10, pady = 5)
                    
                    treb3 = treballador3.get() + ": " + tasca3.get()
                    trb3 = Label(ventana_nueva2, text = treb3, font = ("Calibri 20"), 
                           bg = 'grey24', fg = 'White')
                    trb3.grid(row = 3, column = 0, padx= 10, pady = 5)
                    
                    treb4 = treballador4.get() + ": " + tasca4.get()
                    trb4 = Label(ventana_nueva2, text = treb4, font = ("Calibri 20"), 
                           bg = 'grey24', fg = 'White')
                    trb4.grid(row = 4, column = 0, padx= 10, pady = 5)
                    
                    treb5 = treballador5.get() + ": " + tasca5.get()
                    trb5 = Label(ventana_nueva2, text = treb5, font = ("Calibri 20"), 
                           bg = 'grey24', fg = 'White')
                    trb5.grid(row = 5, column = 0, padx= 10, pady = 5)
        
    calcular = Button(ventana_nueva1, text="Calcular",
                         font=("Calibri 15"),
                         bg="red",
                         fg="white",
                         bd=7.5,
                         cursor = "hand1",
                         relief="groove",
                         command = calcular_boton).grid(row=10, column=5, padx=10, pady=10)

envia = Button(ventana, text = "Següent",
                        font = ("Calibri 15"),
                        bg = "red",
                        fg = "white",
                        bd = 7.5,
                        relief = "groove",
                        cursor = "hand1",
                        command = envia_boton).grid(row = 10, column = 6, padx = 10, pady = 10 )
print(type(Num))

ventana.mainloop()