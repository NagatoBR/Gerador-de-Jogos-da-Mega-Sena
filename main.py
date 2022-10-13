from random import randint
from time import sleep


def linha():
    print('=' * 60)


def titulo(txt):
    linha()
    print(f'{txt}'.center(60))
    linha()


lista = list()
jogos = list()
contar = 0

while True:
    titulo('GERADOR DE JOGOS DA MEGA-SENA')
    palpites = int(input('Quantos jogos você gerar? '))
    linha()

    if palpites == 0:
        break

    for c in range(palpites):
        while True:
            numeros = randint(1, 60)

            if numeros not in lista:
                lista.append(numeros)
                contar += 1

            if contar >= 6:
                break

        jogos.append(lista[:])
        lista.clear()
        contar = 0

    for c in range(palpites):
        print(f'JOGO {c + 1}: {sorted(jogos[c])}')
        sleep(0.5)

    jogos.clear()
    sleep(0.5)
