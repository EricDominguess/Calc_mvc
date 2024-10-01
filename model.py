from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['calculadora']

def salvar_soma(db, a, b, resultado_add):
    soma = {
        "Num 1": a,
        "Num 2": b,
        "Resultado": resultado_add,
    }
    soma_collection = db['somas']
    result = soma_collection.insert_one(soma)
    return result.inserted_id

def salvar_sub(db, a, b, resultado_sub):
    sub = {
        "Num 1": a,
        "Num 2": b,
        "Resultado": resultado_sub,
    }
    sub_collection = db['Subtrações']
    result = sub_collection.insert_one(sub)
    return result.inserted_id

def calcular_model(num1, num2, operacao):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operacao == "Mais":
            resultado = num1 + num2
            salvar_soma(get_database(), num1, num2, resultado)
        elif operacao == "Menos":
            resultado = num1 - num2
            salvar_sub(get_database(), num1, num2, resultado)
        else:
            return "Selecione uma operação"

        return resultado
    except ValueError:
        return "Por favor, insira números válidos."
