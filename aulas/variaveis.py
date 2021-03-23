nome = str(input("Qual é o seu nome: "))
idade = int(input("Qual é a sua idade: "))
dinheiro = str(input("Você tem dinheiro: ").upper())

if dinheiro == "SIM":
    valor = float(input("Quanto tem em conta: "))

    print('<----->' * 10)

    print('nome: ', nome)
    print('Idade: ', idade)
    print('Tem dinheiro: ', dinheiro)
    print('Saldo: ', valor)

else:
    print('<----->' * 10)

    print('nome: ', nome)
    print('Idade: ', idade)
    print("Não tem dinheiro em conta!")





