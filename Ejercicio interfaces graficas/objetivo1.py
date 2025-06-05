import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    
    ventana.title("Ingreso de Datos")
    
    ventana.geometry("500x300")

    ventana.resizable(0,0)
    
    ventana.mainloop()


if __name__ == "__main__":
    crear_ventana()