import tkinter as tk
from tkinter import messagebox

# Variável

tentativas = 0

# Funções

def entrar():
    global tentativas

    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "" or senha == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos")

    elif usuario == "aluno" and senha == "1234":
        messagebox.showinfo("Login", "Bem-vindo(a), aluno!")
        tentativas = 0

    else:
        tentativas += 1
        messagebox.showerror("Erro", "Usuário ou senha incorretos")

        if tentativas == 3:
            janela.destroy()

def limpar():
    entrada_usuario.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)

# Configuração Padrão

janela = tk.Tk()
janela.title("Tela de Login")

# Texto

tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=5, pady=5)

entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=5, pady=5)

entrada_senha = tk.Entry(janela, show="*")
entrada_senha.grid(row=1, column=1, padx=5, pady=5)

# Botões Interativos

tk.Button(janela, text="Entrar", command=entrar).grid(row=2, column=0, padx=5, pady=5)
tk.Button(janela, text="Limpar", command=limpar).grid(row=2, column=1, padx=5, pady=5)

janela.mainloop()
