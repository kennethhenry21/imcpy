import tkinter as tk
from tkinter import messagebox

def calcular_imc(peso, altura):
    """
    Calcula el IMC dado el peso (en kg) y la altura (en metros).
    Fórmula: IMC = peso / (altura ** 2)
    """
    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura ** 2)
        return imc
    except ValueError:
        return None

def mostrar_resultado():
    peso = entry_peso.get()
    altura = entry_altura.get()

    imc = calcular_imc(peso, altura)
    if imc is not None:
        resultado_label.config(text=f"Tu IMC es: {imc:.2f}")
    else:
        messagebox.showerror("Error", "Ingresa valores válidos para peso y altura.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de IMC")

# Etiquetas y campos de entrada
label_peso = tk.Label(ventana, text="Peso (kg):")
entry_peso = tk.Entry(ventana)
label_altura = tk.Label(ventana, text="Altura (m):")
entry_altura = tk.Entry(ventana)

# Botón para calcular
calcular_button = tk.Button(ventana, text="Calcular IMC", command=mostrar_resultado)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")

# Posicionamiento de widgets
label_peso.grid(row=0, column=0)
entry_peso.grid(row=0, column=1)
label_altura.grid(row=1, column=0)
entry_altura.grid(row=1, column=1)
calcular_button.grid(row=2, columnspan=2)
resultado_label.grid(row=3, columnspan=2)

ventana.mainloop()

