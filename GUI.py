from tkinter import *
import tkinter.ttk
from tkinter import font
from tkinter import PhotoImage
import main

# funcion de degradado de color de la ventana
def degradado (canvas, width, height, color1, color2):
    for i in range(height):
        r = int(color1[0]+(color2[0]- color1[0])*i/height)
        g = int(color1[1]+(color2[1]-color1[1])*i/height)
        b = int(color1[2]+(color2[2]- color1[2])*i/height)

        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

ventana = tkinter.Tk()
# creacion del tipo de fuente
fuente = font.Font(family="Noto Sans JP", size=12, weight="normal")

# titulo de la ventana
ventana.title("Clima")

# icono de la GUI
ventana.iconbitmap("icons8-clima-16.ico")

# etiqueta para agregar texto
''' color_fondo01 = "#%02x%02x%02x" % (93, 109, 126) # se define el color tipo RGB
etiqueta = tkinter.Label(ventana, text="Clima", fg="black", font=fuente, bg=color_fondo01) 
etiqueta.pack() '''

#boton lupa img 
lupa_ruta="lupa.png"
lupa = PhotoImage(file=lupa_ruta)
ventana.lupa=lupa
boton_lupa = tkinter.Button(ventana, image=lupa)
boton_lupa.pack()

# dimension de la ventana 
width = 500
height = 500
ventana.geometry(f"{width}x{height}") # dimension de entrada de la ventana

# se establace el color del degradado y se manda a llamar a la funcion
canvas = tkinter.Canvas(ventana, width=width, height=height)
canvas.pack()
color1 = (93, 109, 126)
color2 = (40, 55, 71 )
degradado(canvas, width, height, color1, color2)

ventana.mainloop()


