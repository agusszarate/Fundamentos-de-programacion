import tkinter as tk

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
    
    ventana.mainloop()


if __name__ == "__main__":
    crear_ventana()