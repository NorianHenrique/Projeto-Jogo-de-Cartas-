import random

# Definindo as cartas
naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

# Criando o baralho
baralho = [(valor, naipe) for valor in valores for naipe in naipes]

# Embaralhando o baralho
random.shuffle(baralho)

# Distribuindo as cartas
jogador1 = baralho[:5]
jogador2 = baralho[5:10]

def obter_valor(carta):
    valores = {
        'Ás': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Valete': 11,
        'Dama': 12,
        'Rei': 13
    }

    return valores[carta]

def calcular_pontuacao(cartas):
    pontuacao = 0
    for carta in cartas:
        valor = obter_valor(carta[0])  # Alteração aqui para obter o valor da carta corretamente
        pontuacao += valor
    return pontuacao

# Exibindo as cartas dos jogadores
print("Cartas do Jogador 1:")
for carta in jogador1:
    print(carta[0], "de", carta[1])

print("\nCartas do Jogador 2:")
for carta in jogador2:
    print(carta[0], "de", carta[1])

pontuacao_jogador1 = calcular_pontuacao(jogador1)
pontuacao_jogador2 = calcular_pontuacao(jogador2)

print("Pontuação do Jogador 1:", pontuacao_jogador1)
print("Pontuação do Jogador 2:", pontuacao_jogador2)

if pontuacao_jogador1 > pontuacao_jogador2:
    print("Jogador 1 é o vencedor!")
elif pontuacao_jogador2 > pontuacao_jogador1:
    print("Jogador 2 é o vencedor!")
else:
    print("O jogo é um empate!")