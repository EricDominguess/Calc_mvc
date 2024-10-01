from tkinter import Tk
from controller import CalculadoraController
from view import CalculadoraView
from model import get_database  # Se for necessário passar o DB para o Controller

def main():
    # Inicializa o banco de dados
    db = get_database()

    # Inicializa o Controller
    controller = CalculadoraController(db)  # Passa o DB se necessário

    # Inicializa a janela principal e a View
    root = Tk()
    view = CalculadoraView(root, controller)  # View precisa do controller para interagir com a lógica

    # Iniciar a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
