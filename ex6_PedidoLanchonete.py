import tkinter as tk
from tkinter import messagebox

# Funções

def calcular():
    total = 0

    if hamburguer.get():
        total += 18

    if batata.get():
        total += 10

    if refrigerante.get():
        total += 6

    if suco.get():
        total += 7

    if total == 0:
        messagebox.showwarning("Aviso", "Selecione pelo menos um item.")
        return

    if gorjeta.get():
        total += total * 0.10

    resultado.config(text=f"Total: R$ {total:.2f}".replace(".", ","))

def novo_pedido():
    hamburguer.set(False)
    batata.set(False)
    refrigerante.set(False)
    suco.set(False)
    gorjeta.set(False)

    resultado.config(text="")

# Configuração Padrão

janela = tk.Tk()
janela.title("Pedido de Lanchonete")

hamburguer = tk.BooleanVar()
batata = tk.BooleanVar()
refrigerante = tk.BooleanVar()
suco = tk.BooleanVar()
gorjeta = tk.BooleanVar()

# Texto Padrão

tk.Label(janela, text="Escolha seus produtos:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

# Botões Interativos

tk.Checkbutton(janela, text="Hambúrguer - R$ 18,00", variable=hamburguer).grid(row=1, column=0, sticky="w")

tk.Checkbutton(janela, text="Batata frita - R$ 10,00", variable=batata).grid(row=2, column=0, sticky="w")

tk.Checkbutton(janela, text="Refrigerante - R$ 6,00", variable=refrigerante).grid(row=3, column=0, sticky="w")

tk.Checkbutton(janela, text="Suco - R$ 7,00", variable=suco).grid(row=4, column=0, sticky="w")

tk.Checkbutton(janela, text="Adicionar gorjeta de 10%", variable=gorjeta).grid(row=5, column=0, sticky="w")

tk.Button(janela, text="Calcular total", command=calcular).grid(row=6, column=0, padx=5, pady=5)

tk.Button(janela, text="Novo pedido", command=novo_pedido).grid(row=7, column=0, padx=5, pady=5)

resultado = tk.Label(janela, text="")
resultado.grid(row=8, column=0, pady=5)

janela.mainloop()