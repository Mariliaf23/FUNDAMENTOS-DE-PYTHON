import tkinter as tk

janela = tk.Tk()
janela.geometry('600x400')

button = tk.Button(janela, text='Entrar', bg='lightblue', command='')
button.pack(pady=20)

lbl = tk.Label(janela, text="Seja bem-vindo")
lbl.pack(pady=5)


campo_email = tk.Entry(janela, width = 40)
campo_email.pack(pady=10, ipady = 10)

campo_senha = tk.Entry(janela, show="*")
campo_senha.pack(pady=10)


janela.mainloop()

