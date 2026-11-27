import tkinter as tk
from tkinter import messagebox

# Configuração Padrão
janela = tk.Tk()
janela.title("Contador de Cliques")
janela.geometry("380x160")
janela.resizable(False, False)
janela.config(bg="white")

# Variável
contador = 0

# Funções
def incrementar():
    global contador
    contador += 1
    label_contador.config(text=contador)

    # Verificação para exibir showinfo
    if contador == 10:
        messagebox.showinfo("Aviso", "Você chegou a 10!")

def remover():
    global contador
    if contador > 0:
        contador -= 1
        label_contador.config(text=contador)

# Texto da Janela
label_contador = tk.Label(
    janela, text=contador, font=("Arial", 60, "bold"), bg="white", fg="black"
)
label_contador.place(x=10, y=10)

# Botões Interativos
tk.Button(janela, text="Clique para incrementar", command=incrementar).place(x=10, y=120)
tk.Button(janela, text="Clique para remover", command=remover).place(x=160, y=120)

janela.mainloop()
