
import tkinter as tk

# Funções

def atualizar():
    janela.config(bg=cor.get())

    texto.config(
        bg=cor.get(),
        font=("Arial", tamanho.get(), "bold" if negrito.get() else "normal")
    )

    escolha.config(text=f"Cor: {cor.get()} · Letra: {tamanho.get()}")

    escolha.config(bg=cor.get())
    escolha.config(font=("Arial", 10))

def restaurar():
    cor.set("lightblue")
    tamanho.set(16)
    negrito.set(False)
    atualizar()

# Configuração Padrão

janela = tk.Tk()
janela.title("Mudando o Visual")
janela.geometry("350x350")

cor = tk.StringVar(value="lightblue")
tamanho = tk.IntVar(value=16)
negrito = tk.BooleanVar(value=False)

# Texto Padrão

texto = tk.Label(janela, text="Este é o meu texto", bg=cor.get(), font=("Arial", 16))
texto.grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(janela, text="Cor de fundo:").grid(row=1, column=0, sticky="w")

# Botões e Mudanças

tk.Radiobutton(janela, text="Azul claro", variable=cor, value="lightblue", command=atualizar).grid(row=2, column=0, sticky="w")

tk.Radiobutton(janela, text="Verde claro", variable=cor, value="lightgreen", command=atualizar).grid(row=3, column=0, sticky="w")

tk.Radiobutton(janela, text="Amarelo", variable=cor, value="lightyellow", command=atualizar).grid(row=4, column=0, sticky="w")

tk.Radiobutton(janela, text="Rosa", variable=cor, value="pink", command=atualizar).grid(row=5, column=0, sticky="w")

tk.Label(janela, text="Tamanho da letra:").grid(row=1, column=1, sticky="w")

tk.Radiobutton(janela, text="Pequena (12)", variable=tamanho, value=12, command=atualizar).grid(row=2, column=1, sticky="w")

tk.Radiobutton(janela, text="Média (16)", variable=tamanho, value=16, command=atualizar).grid(row=3, column=1, sticky="w")

tk.Radiobutton(janela, text="Grande (22)", variable=tamanho, value=22, command=atualizar).grid(row=4, column=1, sticky="w")

tk.Checkbutton(janela, text="Negrito", variable=negrito, command=atualizar).grid(row=6, column=0, columnspan=2, pady=5)

escolha = tk.Label(janela, text="")
escolha.grid(row=7, column=0, columnspan=2, pady=10)

tk.Button(janela, text="Restaurar", command=restaurar).grid(row=8, column=0, columnspan=2, pady=5)

atualizar()

janela.mainloop()
