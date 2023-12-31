import pyttsx3
import tkinter as tk
from tkinter import Entry, Button, Frame

def falar_texto():
    # Obtém o texto do campo de entrada
    texto = entry.get()

    # Obtém a taxa de fala do mecanismo
    rate = engine.getProperty('rate')

    # Define uma taxa de fala mais baixa (por exemplo, 150)
    engine.setProperty('rate', 150)

    # Fala o texto com a taxa de fala definida
    engine.say(texto)
    engine.runAndWait()

    # Limpa o campo de entrada após falar o texto
    entry.delete(0, 'end')

# Inicializa o mecanismo TTS
engine = pyttsx3.init()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Texto para Fala")

# Cria um quadro para conter os widgets
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Adiciona um campo de entrada de texto com fonte aumentada e largura reduzida
entry = Entry(frame, width=2, font=('Arial', 100))  # Ajuste a fonte e o tamanho aqui
entry.grid(row=0, column=0, padx=5, pady=5)

# Adiciona um botão para acionar a função de falar
button = Button(frame, text="Falar", command=falar_texto)
button.grid(row=0, column=1, padx=5, pady=5)

# Adiciona um rótulo informativo
info_label = tk.Label(frame, text="Digite o texto e pressione Enter para falar.")
info_label.grid(row=1, column=0, columnspan=2, pady=5)

# Configura o foco inicial no campo de entrada
entry.focus()

# Adiciona a capacidade de chamar a função de falar ao pressionar Enter
root.bind('<Return>', lambda event=None: falar_texto())

# Inicia o loop da interface gráfica
root.mainloop()