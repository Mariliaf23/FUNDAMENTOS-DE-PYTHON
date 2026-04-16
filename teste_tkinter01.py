import tkinter as tk

janela = tk.Tk()
janela.title("Olá, Mundo!")

frame = tk.Frame(janela, bg="lightblue", width=200, height=100, bd=3, relief=tk.RIDGE)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Olá, Mundo!", bg="lightblue")
label.pack(side= "top", padx= 200, pady=10)


janela.mainloop()