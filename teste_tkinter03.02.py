import tkinter as tk

janela = tk.Tk ()
janela.title("Estrutura do Formulário")


FrameSuperior = tk.Frame(janela, bg="lightblue")
FrameSuperior.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.15)


FrameMeio = tk.Frame(janela, bg="lightgreen")
FrameMeio.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.50)


FrameInferior = tk.Frame(janela, bg="yellow")
FrameInferior.place(relx=0.1, rely=0.80, relwidth=0.8, relheight=0.15)


tk.Label(FrameSuperior, text="Frame superior", bg="lightblue").place(relx=0.45, rely=0.2)
tk.Label(FrameMeio, text="Frame do meio", bg="lightgreen", fg="black").place(relx=0.45, rely=0.2)
tk.Label(FrameInferior, text="Frame inferior", bg="yellow").place(relx=0.45, rely=0.2)


janela.mainloop()
