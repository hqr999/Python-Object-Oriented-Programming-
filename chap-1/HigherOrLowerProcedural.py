import random

NAIPE_TUPLA = ("Espada", "Copas", "Paus", "Ouros")
RANK_TUPLA = (
    "AS",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Valete",
    "Rainha",
    "Rei",
)

NCARTAS = 8


# Passa um deck e essa função retorna uma carta aleatória (pseudo-aleatória) do mesmo deck
def pegaCarta(deckLista):
    essaCarta = deckLista.pop()  # Tira um carta do topo e retorna ela

    return essaCarta


# Passa um deck e essa função retorna uma cópia do deck embaralhado
def embaralha(deckLista):
    deckListCopia = deckLista.copy()  # Faz uma cópia do deck inicial

    random.shuffle(deckListCopia)
    return deckListCopia


# Código principal
print('Bem Vindo ao "Maior ou Menor"')
print(
    "Você deve escolher se a próxima carta carta á ser mostrada será Maior ou Menor do que a carta atual "
)
print("Acertando você ganha 20 pontos; Errando você perde 15 pontos.")
print("Você começa com 50 pontos.")
print()

inicioDeckLista = []
for naipe in NAIPE_TUPLA:
    for valor, rank in enumerate(RANK_TUPLA):
        cartaDic = {"rank": rank, "naipe": naipe, "valor": valor + 1}
        inicioDeckLista.append(cartaDic)


pontuacao = 50

while True:  # Jogue vária vezes
    print()
    jogoDeckLista = embaralha(inicioDeckLista)

    cartaAtualDic = pegaCarta(jogoDeckLista)
    cartaAtualRank = cartaAtualDic["rank"]
    cartaAtualVal = cartaAtualDic["valor"]
    cartaAtualNaipe = cartaAtualDic["naipe"]
    print("Carta inicial é:", cartaAtualRank + " de " + cartaAtualNaipe)
    print()

    for cartaNum in range(0, NCARTAS):  # Jogue um jogo com essa quantidade de cartas
        resp = input(
            "Será a proxima carta maior ou menor que "
            + cartaAtualRank
            + " de "
            + cartaAtualNaipe
            + "? (pressione h (maior) ou l (menor) ):"
        )

        resp = resp.casefold()  # força lowercase
        proxCartaDic = pegaCarta(jogoDeckLista)
        proxCartaRank = proxCartaDic["rank"]
        proxCartaNaipe = proxCartaDic["naipe"]
        proxCartaVal = proxCartaDic["valor"]

        print("A próxima carta é:", proxCartaRank, " de ", proxCartaNaipe)

        if resp == "h":
            if proxCartaVal > cartaAtualVal:
                print("Você acertou, era maior")
                pontuacao += 20
            else:
                print("Desculpe, não era maior")
                pontuacao -= 15
        elif resp == "l":
            if proxCartaVal < cartaAtualVal:
                pontuacao += 20
                print("Você acertou, era menor")
            else:
                pontuacao -= 15
                print("Desculpe, não era menor")

        print('Sua pontuação é:', pontuacao)
        print() 
        cartaAtualRank = proxCartaRank 
        cartaAtualVal = proxCartaVal # Não precisamos do naipe atual


    irDeNovo = input('Para jogar de novo aprete ENTER, ou "q" para sair: ')
    if irDeNovo.casefold() == 'q':
        break 

print('Ok adeus')
