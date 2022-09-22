print("Bem vindo ao jogo de quiz")

pontos = 0

resposta = input("Quem Criou A Lampada ").lower()
if resposta == "thomas edison":
    print("Parabens Voce Acertou!")
    pontos += 100


else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

resposta = input("Quem Criou O Aviao ").lower()
if resposta == "santos dumont":
    print("Parabens Voce Acertou!")
    pontos += 100

else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

resposta = input("quem foi o primeiro homem a pisar na lua ").lower()
if resposta == "neil armstrong":
    print("Parabens Voce Acertou!")
    pontos += 100

else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

resposta = input("quem foi o primeiro presidente dos estados unidos ").lower()
if resposta == "george washington":
    print("Parabens Voce Acertou!")
    pontos += 100


else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

print("""
Quem, descobriu o brasil ?

[1] Pedro alvares cabral
[2] Dom pedro Primeiro
[3] Santos Dumon
""")
opcao = input(':> ')

if opcao not in ["1", "2", "3"]:
    opcao = input ("Escolha uma opção valida:  ")
if opcao == "1":
    print("Parabens Voce Acertou!")
    pontos += 100
else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

print("""
Quem foi o maior traficante do mundo ?

[1] Amado Carrillo Fuentes
[2] El Chapo
[3] Osama bin Laden
""")
opcao = input(':> ')

if opcao not in ["1", "2", "3"]:
    opcao = input ("Escolha uma opção valida:  ")
if opcao == "2":
    print("Parabens Voce Acertou!")
    pontos += 100
else:
    print("Que pena voce errou!")
    if pontos == 0:
       pass
    else:
       pontos = pontos - 50

print("""
O Brasil Participou De Uma Guerra ?

[1] Falso
[2]Verdadeiro 
""")
opcao = int(input(':> '))

if opcao not in [1, 2]:
    opcao = input ("Escolha uma opção valida:  ")
if opcao == 2:
    print("Parabens Voce Acertou!")
    pontos += 100

    print("""
    Getulio Vargas For Assasinado ?

    [1]Falso
    [2]Verdadeiro 
    """)
    opcao = int(input(':> '))

    if opcao not in [1, 2]:
        opcao = input("Escolha uma opção valida:  ")
    if opcao == 1:
        print("Parabens Voce Acertou!")
        pontos += 100

print("O jogo terminou, voce fez", pontos, "pontos")