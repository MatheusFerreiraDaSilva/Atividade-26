import tkinter as tk
from tkinter import messagebox

# Funções

def atualizar_total():
    total.config(text=f"Itens: {lista.size()}")

def adicionar():
    item = entrada.get()

    if item == "":
        messagebox.showwarning("Aviso", "Digite um item.")

    elif item in lista.get(0, tk.END):
        messagebox.showwarning("Aviso", "Esse item já está na lista.")

    else:
        lista.insert(tk.END, item)
        entrada.delete(0, tk.END)

    atualizar_total()

def remover():
    selecionado = lista.curselection()

    if not selecionado:
        messagebox.showinfo("Aviso", "Selecione um item para remover.")

    else:
        lista.delete(selecionado[0])

    atualizar_total()

def limpar():
    resposta = messagebox.askyesno("Confirmação", "Deseja apagar todos os itens?")

    if resposta:
        lista.delete(0, tk.END)

    atualizar_total()

# Configuração Padrão

janela = tk.Tk()
janela.title("Lista de Compras")

entrada = tk.Entry(janela)
entrada.grid(row=0, column=0, padx=5, pady=5)

# Botões Interativos

tk.Button(janela, text="Adicionar", command=adicionar).grid(row=0, column=1, padx=5, pady=5)

lista = tk.Listbox(janela, width=30)
lista.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

tk.Button(janela, text="Remover selecionado", command=remover).grid(row=2, column=0, padx=5, pady=5)

tk.Button(janela, text="Limpar lista", command=limpar).grid(row=2, column=1, padx=5, pady=5)

total = tk.Label(janela, text="Itens: 0")
total.grid(row=3, column=0, columnspan=2, pady=5)

janela.mainloop()
