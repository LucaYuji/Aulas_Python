import tkinter as tk

janela = tk.Tk()
janela.geometry('500x500')
janela.title('TESTE')
text = tk.Label(janela, text = 'HELLO WORLD')
text.pack()

input_entry = tk.Entry(janela)
input_entry.pack()

input_entry2 = tk.Entry(janela)
input_entry2.pack()

btn = tk.Button(janela, text= 'Clique aqui')
btn.pack()

resultado = tk.Label(janela, text='')
resultado.pack()

janela.mainloop()