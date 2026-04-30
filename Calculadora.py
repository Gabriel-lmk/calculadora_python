def convertor(valor):
    while True:
        try:
            return int(valor)
        except ValueError:
            try:
                return float(valor)
            except ValueError:
                valor = input("Valor inválido! Digite novamente: ")

def calcular(x, y, operador):
    op = operador.lower().strip()

    operacoes = {
        "+": x + y,
        "soma": x + y,
        "-": x - y,
        "subtração": x - y,
        "subtracao": x - y,
        "*": x * y,
        "multiplicação": x * y,
        "multiplicacao": x * y,
        "/": x / y if y != 0 else "Erro: Divisão por zero!",
        "divisão": x / y if y != 0 else "Erro: Divisão por zero!",
        "divisao": x / y if y != 0 else "Erro: Divisão por zero!",
    }

    return operacoes.get(op, "Operação inválida!")
        
while True:
    x = convertor(input("Digite um número: "))
    y = convertor(input("Digite o segundo número da operação: "))

    operador = input("Digite uma operação entre: \n\n Soma\n Subtração\n Multiplicação \n Divisão \n\nOperação desejada: ")

    print("Resultado:", calcular(x, y, operador))
    
    continuar = input("Deseja continuar? (s/n): ")

    if continuar.lower() == "n":
        break