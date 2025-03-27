def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    else:
        print("saldo insuficiente!")
        print("verifique seu saldo e tente novamente.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


sacar(1000)