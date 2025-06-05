#Nombre y apellido: Agustin Zarate
#Legajo: 113004

import tkinter as tk

from tkinter import messagebox

usuarios_claves_dict = {
    "agustin": "clave123",
    "francisco": "clave456",
    "manuel": "clave789",
    "elian": "clave101",
    "nahuel": "clave123",
    "dana": "clave223",
    "matias": "clave334"
}

def obtener_usuarios_claves():
    return usuarios_claves_dict

def validar_login(usuario, clave):
    usuarios_claves = obtener_usuarios_claves()
    if usuario in usuarios_claves and usuarios_claves[usuario] == clave:
        messagebox.showinfo("Login", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Login", "Algunos de los datos ingresados es Incorrecto")

def registrar_usuario(ventana_registro, usuario, clave):
    usuarios_claves = obtener_usuarios_claves()
    if usuario == "":
        messagebox.showerror("Error", "El campo de usuario no puede estar vacío")
        return
    
    if clave == "":
        messagebox.showerror("Error", "El campo de clave no puede estar vacío")
        return
    
    if usuario in usuarios_claves:
        messagebox.showerror("Error", "El usuario ya existe")
        return
    
    usuarios_claves_dict[usuario] = clave
    messagebox.showinfo("Registro exitoso", f"El usuario '{usuario}' ha sido registrado correctamente")
    ventana_registro.destroy()

def abrir_ventana_registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de nuevo usuario")
    ventana_registro.resizable(0, 0)
    ventana_registro.geometry("300x150")
    ventana_registro.iconbitmap("IMG_Grupo_10.ico")
    ventana_registro.configure(bg="#006400")
    
    marco = tk.Frame(ventana_registro, padx=20, pady=20, background="#006400")
    marco.pack(fill=tk.BOTH)
    
    lbl_nuevo_usuario = tk.Label(marco, text="Nuevo usuario:")
    lbl_nuevo_usuario.grid(row=0, column=0, padx=10, pady=3, sticky="w")
    
    entry_nuevo_usuario = tk.Entry(marco)
    entry_nuevo_usuario.grid(row=0, column=1, padx=10, pady=3, sticky="w")
    
    lbl_nueva_clave = tk.Label(marco, text="Nueva clave:")
    lbl_nueva_clave.grid(row=1, column=0, padx=10, pady=3, sticky="w")
    
    entry_nueva_clave = tk.Entry(marco, show="*")
    entry_nueva_clave.grid(row=1, column=1, padx=10, pady=3, sticky="w")
    
    btn_registrar = tk.Button(
        marco,
        text="Registrar",
        command=lambda: registrar_usuario(ventana_registro, entry_nuevo_usuario.get(), entry_nueva_clave.get())
    )
    btn_registrar.grid(row=2, column=0, columnspan=2, pady=10)

def crear_ventana():
    ventana = tk.Tk()

    ventana.title("Login grupo 10")

    ventana.resizable(0,0)
    
    ventana.geometry("300x130")

    #icono descargado desde https://icon-icons.com/es/icono/feliz-10-emo-emoticon/61016
    ventana.iconbitmap("IMG_Grupo_10.ico")

    ventana.configure(bg="#006400")

    marco = tk.Frame(ventana, padx=5, pady=5, background="#006400")
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
    btn_ingresar.grid(row=4, column=1, padx=5, pady=10)
    
    btn_registrarse = tk.Button(
        marco,
        text="Registrarse",
        command=abrir_ventana_registro
    )
    btn_registrarse.grid(row=4, column=0, padx=5, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()