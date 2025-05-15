import tkinter as tk
from tkinter import messagebox
def crear_ventana():
    ventana = tk.Tk()
    
    ventana.title("Ingreso de Datos")
    
    ventana.geometry("500x300")

    ventana.resizable(0,0)

    marco = tk.Frame(ventana, padx=20, pady=20)
    marco.pack(fill=tk.BOTH, expand=True)
    
    lbl_nombre = tk.Label(marco, text="Nombre:", font=("Arial", 12))
    lbl_nombre.grid(row=0, column=0, pady=10)
    
    entry_nombre = tk.Entry(marco, width=30, font=("Arial", 12))
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    lbl_apellido = tk.Label(marco, text="Apellido:", font=("Arial", 12))
    lbl_apellido.grid(row=1, column=0, pady=10)
    
    entry_apellido = tk.Entry(marco, width=30, font=("Arial", 12))
    entry_apellido.grid(row=1, column=1, padx=10, pady=10)
    
    lbl_email = tk.Label(marco, text="Email:", font=("Arial", 12))
    lbl_email.grid(row=2, column=0, pady=10)
    
    entry_email = tk.Entry(marco, width=30, font=("Arial", 12))
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    def enviar():
        enviar_datos(entry_nombre, entry_apellido, entry_email)

    btn_enviar = tk.Button(marco, text="Enviar", font=("Arial", 12), bg="#4CAF50", fg="white", command=enviar, padx=20, pady=5)
    btn_enviar.grid(row=3, column=1, pady=20, sticky=tk.E)
    
    lbl_autor = tk.Label(ventana, text="Hecho por: Agustin Zarate", font=("Arial", 10, "italic"))
    lbl_autor.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=5)
    
    ventana.mainloop()

def validar_nombre(texto: str) -> bool:
    MAX_LONGITUD = 25
    
    return len(texto) <= MAX_LONGITUD and texto.isalpha()
    
def validar_email(email: str) -> bool:
    MAX_LONGITUD_EMAIL = 20
    
    es_valido = True
    
    if len(email) > MAX_LONGITUD_EMAIL:
        es_valido = False
    
    elif email.count('@') != 1:
        es_valido = False
    else:
        arroba_pos = email.find('@')
        if arroba_pos == 0 or arroba_pos == len(email) - 1:
            es_valido = False
    
    return es_valido

def enviar_datos(entry_nombre: tk.Entry, entry_apellido: tk.Entry, entry_email: tk.Entry):
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    email = entry_email.get()
    
    datos_validos = True
    mensaje_error = ""
    campo_con_error = None
    
    if not nombre or not apellido or not email:
        datos_validos = False
        mensaje_error = "Todos los campos son obligatorios"
    
    elif not validar_nombre(nombre):
        datos_validos = False
        mensaje_error = "El nombre debe contener solo letras y tener máximo 25 caracteres"
        campo_con_error = entry_nombre
    
    elif not validar_nombre(apellido):
        datos_validos = False
        mensaje_error = "El apellido debe contener solo letras y tener máximo 25 caracteres"
        campo_con_error = entry_apellido
    
    elif not validar_email(email):
        datos_validos = False
        mensaje_error = "El email debe tener exactamente un @ (no al inicio ni al final) y máximo 20 caracteres"
        campo_con_error = entry_email
    
    if not datos_validos:
        messagebox.showerror("Error", mensaje_error)
        if campo_con_error:
            campo_con_error.focus()
    else:
        mensaje = f"Datos recibidos:\nNombre: {nombre}\nApellido: {apellido}\nEmail: {email}"
        messagebox.showinfo("Envío exitoso", mensaje)
        
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_email.delete(0, tk.END)


if __name__ == "__main__":
    crear_ventana()
