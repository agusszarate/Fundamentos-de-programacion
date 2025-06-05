#Nombre y apellido: Agustin Zarate
#Legajo: 113004

import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    
    ventana.title("Login grupo 10")

    ventana.resizable(0,0)
    
    ventana.geometry("300x130")

    #icono descargado desde https://icon-icons.com/es/icono/feliz-10-emo-emoticon/61016
    ventana.iconbitmap("IMG_Grupo_10.ico")

    ventana.configure(bg="#006400")

    ventana.mainloop()


if __name__ == "__main__":
    crear_ventana()