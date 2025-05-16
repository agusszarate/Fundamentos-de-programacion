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

    marco = tk.Frame(ventana, padx=20, pady=20, background="#006400")
    marco.pack(fill=tk.BOTH, expand=True)

    lbl_usuario_alumno = tk.Label(marco, text="Usuario alumno:")
    lbl_usuario_alumno.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    entry_usuario_alumno = tk.Entry(marco)
    entry_usuario_alumno.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lbl_clave = tk.Label(marco, text="Clave:")
    lbl_clave.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    entry_clave = tk.Entry(marco)
    entry_clave.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    ventana.mainloop()


if __name__ == "__main__":
    crear_ventana()