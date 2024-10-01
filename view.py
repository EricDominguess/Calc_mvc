import tkinter as tk
from tkinter import ttk

class CalculadoraView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.master.title("Calculadora - Operação")
        self.master.geometry("300x250")  # Largura x Altura

        # Variável para armazenar a operação selecionada
        self.operacao = tk.StringVar(value="")

        # Frame para os campos de entrada
        self.frame_input = ttk.Frame(master)
        self.frame_input.pack(pady=10)

        # Labels e campos de entrada para os números
        ttk.Label(self.frame_input, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_num1 = ttk.Entry(self.frame_input, width=10)  # Largura ajustada
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_num2 = ttk.Entry(self.frame_input, width=10)  # Largura ajustada
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        # Frame para os RadioButtons
        self.frame_radio = ttk.Frame(master)
        self.frame_radio.pack(pady=10)

        # Criação dos RadioButtons abaixo dos campos de entrada
        self.radio_mais = ttk.Radiobutton(self.frame_radio, text="Mais", variable=self.operacao, value="Mais")
        self.radio_menos = ttk.Radiobutton(self.frame_radio, text="Menos", variable=self.operacao, value="Menos")

        # Exibição dos RadioButtons no frame
        self.radio_mais.grid(row=0, column=0, padx=10, pady=5)
        self.radio_menos.grid(row=0, column=1, padx=10, pady=5)

        # Botão de calcular
        ttk.Button(master, text="Calcular", command=self.calcular).pack(pady=10)

        # Label para exibir o resultado
        self.label_resultado = ttk.Label(master, text="Resultado: ", font=("Arial", 12))
        self.label_resultado.pack(pady=10)

    def calcular(self):
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()
        operacao_selecionada = self.operacao.get()

        # Chama o método do controller que agora chama o model
        resultado = self.controller.calcular(num1, num2, operacao_selecionada)

        # Usa o método do controller para exibir o resultado
        resultado_exibido = self.controller.exibir_resultado(resultado)

        # Atualiza o label para mostrar o resultado na interface
        self.label_resultado.config(text=resultado_exibido)


