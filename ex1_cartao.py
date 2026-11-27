import tkinter as tk

# Configuração Padrão

janela = tk.Tk()
janela.title("Cartão de Visita")
janela.geometry("380x160")
janela.resizable(False, False)
janela.config(bg = "purple")

# Texto do Cartão

tk.Label(janela, text = "Matheus Ferreira da Silva", font = ("Arial", 20, "bold"), bg = "purple", fg = "white").place(x = 12, y = 10)
tk.Label(janela, text = "Curso de Informática", font = ("Arial", 19), bg = "purple", fg = "white").place(x = 12, y = 40)
tk.Label(janela, text = "Etec Alberto Santos Dumont", font = ("Arial", 18), bg = "purple", fg = "white").place(x = 12, y = 70)
tk.Label(janela, text = "+55 13 99999 9999", font = ("Arial", 18), bg = "purple", fg = "white").place(x = 150, y = 115)

# Botão Saída

tk.Button(janela, text = "Fechar", command = janela.destroy).place(x = 10, y = 120)

janela.mainloop()