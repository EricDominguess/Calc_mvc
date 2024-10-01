from model import calcular_model

class CalculadoraController:
    def __init__(self, db):
        self.db = db

    def calcular(self, num1, num2, operacao):
        # Chama a função de cálculo do model
        return calcular_model(num1, num2, operacao)

    def exibir_resultado(self, resultado):
        return f"Resultado: {resultado}"
