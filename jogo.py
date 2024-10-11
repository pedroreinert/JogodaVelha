# Jogo da Velha em Python

# Inicializar o tabuleiro
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    print(' ' + tabuleiro[0][0] + ' | ' + tabuleiro[0][1] + ' | ' + tabuleiro[0][2])
    print('-----------')
    print(' ' + tabuleiro[1][0] + ' | ' + tabuleiro[1][1] + ' | ' + tabuleiro[1][2])
    print('-----------')
    print(' ' + tabuleiro[2][0] + ' | ' + tabuleiro[2][1] + ' | ' + tabuleiro[2][2])

# Função para verificar se há um vencedor
def verificar_vencedor():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]
    return None

# Função para jogar
def jogar():
    jogador_atual = 'X'
    while True:
        imprimir_tabuleiro()
        print('Jogador atual:', jogador_atual)
        linha = int(input('Digite a linha (1-3): ')) - 1
        coluna = int(input('Digite a coluna (1-3): ')) - 1
        if tabuleiro[linha][coluna] != ' ':
            print('Posição já ocupada!')
            continue
        tabuleiro[linha][coluna] = jogador_atual
        vencedor = verificar_vencedor()
        if vencedor:
            imprimir_tabuleiro()
            print('Vencedor:', vencedor)
            break
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Iniciar o jogo
jogar()