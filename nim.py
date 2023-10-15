def parametros_do_jogo():
    global total_inicial_de_pecas
    total_inicial_de_pecas = int(input("\nQuantas peças? "))

    while total_inicial_de_pecas < 1:
        print("\nvalor invalida: Quantidade de peças não pode ser 0")
        total_inicial_de_pecas = int(input("\nQuantas peças no tabuleiro? "))

    global limite_de_pecas_por_jogada
    limite_de_pecas_por_jogada = int(input("Limite de peças por jogada? "))

    while limite_de_pecas_por_jogada < 1 or limite_de_pecas_por_jogada > total_inicial_de_pecas:
        print("\nvalor invalida: Limite de peças por jogada não pode ser 0 ou maior que quantidade de peças do tabuleiro")
        limite_de_pecas_por_jogada = int(
            input("\nLimite de peças por jogada? "))


def quem_comeca():
    calcular_multiplicidade = total_inicial_de_pecas % (
        limite_de_pecas_por_jogada + 1)
    if calcular_multiplicidade == 0:
        print("\nVocê começa!")
        return "Você começa!"
    else:
        print("\nComputador começa!")
        return "Computador começa!"


def computador_joga(saldo, jogada):
    calcular_jogada = saldo % (jogada + 1)
    if calcular_jogada == 0:
        return limite_de_pecas_por_jogada
    else:
        return calcular_jogada


def usuario_joga():  # criar validador de input de string
    jogada = int(input("\nquantas peças você vai tirar? "))
    while jogada > limite_de_pecas_por_jogada or jogada < 1:
        print("\nOops! Jogada inválida! Tente de novo.")
        jogada = int(input("\nquantas peças você vai tirar? "))
    return jogada


def print_resposta_singular_ou_pural(jogada_atual, pecas_restantes_no_tabuleiro, jogador):
    if jogada_atual == 1:
        if jogador == "usuario":
            print("\nVocê tirou uma peça")
        else:
            print("\nO computador tirou uma peça")
    if jogada_atual > 1:
        if jogador == "usuario":
            print("\nVocê tirou", jogada_atual, "peças")
        else:
            print("\nO computador tirou", jogada_atual, "peças")
    if pecas_restantes_no_tabuleiro == 1:
        print("Agora resta apenas",
              pecas_restantes_no_tabuleiro, "peça no tabuleiro")
    if pecas_restantes_no_tabuleiro > 1:
        print("Agora restam", pecas_restantes_no_tabuleiro, "peças no tabuleiro")

    if pecas_restantes_no_tabuleiro == 0:
        return "fim de jogo"


def partida():

    parametros_do_jogo()

    if quem_comeca() == "Você começa!":
        proximo_jogador = "usuario"
    else:
        proximo_jogador = "computador"

    pecas_restantes_no_tabuleiro = total_inicial_de_pecas

    while pecas_restantes_no_tabuleiro > 0:
        if proximo_jogador == "computador":
            jogada_atual = computador_joga(
                pecas_restantes_no_tabuleiro, limite_de_pecas_por_jogada)  # jogada do robo
            pecas_restantes_no_tabuleiro = pecas_restantes_no_tabuleiro - jogada_atual
            print_resposta_singular_ou_pural(
                jogada_atual, pecas_restantes_no_tabuleiro, proximo_jogador)
            if pecas_restantes_no_tabuleiro == 0:
                print("Fim do jogo! O computador ganhou!")
                return "computador ganhou"

            proximo_jogador = "usuario"

        else:
            if pecas_restantes_no_tabuleiro > 0:
                jogada_atual = usuario_joga()  # jogada do usuario
                pecas_restantes_no_tabuleiro = pecas_restantes_no_tabuleiro - jogada_atual
                print_resposta_singular_ou_pural(
                    jogada_atual, pecas_restantes_no_tabuleiro, proximo_jogador)

                if pecas_restantes_no_tabuleiro == 0:
                    print("Fim do jogo! Você ganhou!")
                    return "você ganhou"

                proximo_jogador = "computador"


def campeonato():
    rodada = 1
    vitorias_computador = 0
    vitorias_usuario = 0
    while rodada < 4:
        print("\n**** Rodada", rodada, "****")
        vencedor = partida()
        if vencedor == "computador ganhou":
            vitorias_computador = vitorias_computador + 1
        if vencedor == "você ganhou":
            vitorias_usuario = vitorias_usuario + 1
        rodada = rodada + 1

    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você", vitorias_usuario,
          "X Computador", vitorias_computador)


def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    escolha = 0
    while escolha != 1 and escolha != 2:
        escolha = int(
            input("\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato! \n"))
        if escolha == 1:
            print("\nVoce escolheu uma partida isolada!")
            partida()
        if escolha == 2:
            print("\nVoce escolheu um campeonato!")
            campeonato()
        if escolha != 1 and escolha != 2:
            print("\nOpção invalida!")


main()
