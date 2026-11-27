import tkinter as tk
from tkinter import messagebox

# Funções

def converter():
    try:
        celsius = float(entrada.get().replace(",", "."))
        fahrenheit = celsius * 9 / 5 + 32

        resultado.config(text=f"{celsius:.1f} °C = {fahrenheit:.1f} °F")

    except ValueError:
        messagebox.showerror("Erro", "Digite uma temperatura válida.")

def limpar():
    entrada.delete(0, tk.END)
    resultado.config(text="")

def converter_inverso():
    try:
        fahrenheit = float(entrada.get().replace(",", "."))
        celsius = (fahrenheit - 32) * 5 / 9

        resultado.config(text=f"{fahrenheit:.1f} °F = {celsius:.1f} °C")

    except ValueError:
        messagebox.showerror("Erro", "Digite uma temperatura válida.")

# Configuração Padrão

janela = tk.Tk()
janela.title("Conversor de Temperatura")

# Texto

tk.Label(janela, text="Celsius:").grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=5, pady=5)

# Botões Interativos

tk.Button(janela, text="Converter", command=converter).grid(row=1, column=0, padx=5, pady=5)
tk.Button(janela, text="Limpar", command=limpar).grid(row=1, column=1, padx=5, pady=5)

tk.Button(janela, text="Converter para Celsius", command=converter_inverso).grid(row=2, column=0, columnspan=2, pady=5)

# Final

resultado = tk.Label(janela, text="")
resultado.grid(row=3, column=0, columnspan=2, pady=5)

janela.mainloop()
