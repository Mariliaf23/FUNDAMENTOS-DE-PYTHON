import tkinter as tk

janela = tk.Tk ()
janela.title("Estrutura base")
janela.geometry('600x400')

main_frame = tk.Frame(janela, bg="lightgreen")
main_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.8)


FrameEsquerdo = tk.Frame(janela, bg="lightblue")
FrameEsquerdo.place(relx=0, rely=0, relwidth=0.2, relheight=1.0)


terminal = tk.Frame(janela, bg="yellow")
terminal.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)


tk.Label(FrameEsquerdo, text="Frame Esquerdo", bg="lightblue").pack(pady=10)
tk.Label(main_frame, text="Frame Direito", bg="lightgreen", fg="black").pack()
tk.Label(terminal, text="Frame Inferior Direito", bg="yellow").pack(expand=True)


janela.mainloop()
