#Nombre y apellido: Agustin Zarate
#Legajo: 113004

import tkinter as tk

from tkinter import messagebox

def obtener_usuarios_claves():
    return {
        "agustin": "clave123",
        "francisco": "clave456",
        "manuel": "clave789",
        "elian": "clave101",
        "nahuel": "clave123",
        "dana": "clave223",
        "matias": "clave334"
    }

def validar_login(usuario, clave):
    usuarios_claves = obtener_usuarios_claves()
    if usuario in usuarios_claves and usuarios_claves[usuario] == clave:
        messagebox.showinfo("Login", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Login", "Algunos de los datos ingresados es Incorrecto")

def crear_ventana():
    ventana = tk.Tk()

    ventana.title("Login grupo 10")

    ventana.resizable(0,0)
    
    ventana.geometry("300x130")

    #icono descargado desde https://icon-icons.com/es/icono/feliz-10-emo-emoticon/61016
    ventana.iconbitmap("IMG_Grupo_10.ico")

    ventana.configure(bg="#006400")

    marco = tk.Frame(ventana, padx=20, pady=20, background="#006400")
    marco.pack(fill=tk.BOTH)

    lbl_usuario_alumno = tk.Label(marco, text="Usuario alumno:")
    lbl_usuario_alumno.grid(row=2, column=0, padx=10, pady=3, sticky="w")

    entry_usuario_alumno = tk.Entry(marco)
    entry_usuario_alumno.grid(row=2, column=1, padx=10, pady=3, sticky="w")

    lbl_clave = tk.Label(marco, text="Clave:")
    lbl_clave.grid(row=3, column=0, padx=10, pady=3, sticky="w")

    entry_clave = tk.Entry(marco, show="*")
    entry_clave.grid(row=3, column=1, padx=10, pady=3, sticky="w")

    btn_ingresar = tk.Button(
        marco,
        text="Ingresar",
        command=lambda: validar_login(entry_usuario_alumno.get(), entry_clave.get())
    )
    btn_ingresar.grid(row=4, column=0, columnspan=2, pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()