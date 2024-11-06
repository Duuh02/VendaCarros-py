listacarros = ["Chevette", "Opala", "Corsa"]
listaprecos = ["7500", "8000", "7000"]
meta = 50
vendas = 68

carros = print(listacarros)
valores = print("Os Preços são:",listaprecos)
def opcoes ():
    print("1 - Chevette")
    print("2 - Opala")
    print("3 - Corsa")
opcoes ()
def escolha ():
    escolha = int(input("Faça sua escolha: "))
    if escolha == 1:
        print("Você comprou um Chevette!")
    elif escolha == 2:
        print("Você comprou um Opala!")
    elif escolha == 3:
        print("Você comprou um Corsa!")
    else:
        print("Escolha Inválida, Digite Outro Número de 1 a 3 !!")
escolha ()
