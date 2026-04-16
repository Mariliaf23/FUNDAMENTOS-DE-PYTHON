import tkinter as tk

janela = tk.Tk ()
janela.title("Estrutura VS Code")
janela.geometry('600x400')

Editor = tk.Frame(janela, bg="lightgreen")
Editor.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)


Paginas = tk.Frame(janela, bg="green")
Paginas.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.1)


Explorador = tk.Frame(janela, bg="lightblue")
Explorador.place(relx=0, rely=0, relwidth=0.2, relheight=1.0)


Terminal = tk.Frame(janela, bg="yellow")
Terminal.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)


tk.Label(Explorador, text="explorador", bg="lightblue").place(relx=0, rely=0.2)
tk.Label(Paginas, text="páginas de código", bg="green", fg="white").place(relx=0.2, rely=0.2)
tk.Label(Editor, text="editor de código", bg="lightgreen", fg="black").place(relx=0.2, rely=0.2)
tk.Label(Terminal, text="terminal", bg="yellow").place(relx=0.2, rely=0.2)


janela.mainloop()
