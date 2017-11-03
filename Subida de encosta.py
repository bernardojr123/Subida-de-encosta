from Cidades import getDicCidades
from random import shuffle
import math

cidades = getDicCidades()
lista = list(cidades.keys())

def getVizinhos(caminho):
    '''
    Obter caminhos vizinhos.

    Caminhos vizinhos são obtidos a partir da troca de somente 2 elementos
    proximos (colados)

    EX: lista_exemplo = [1,2,3,4]
        visinhos = [[2,1,3,4],[1,2,4,3],[1,3,2,4]]
    '''
    visinhos = []
    for i in range(len(caminho) - 3):
        novoCaminho = caminho[:]
        x = novoCaminho[i + 1]
        y = novoCaminho[i + 2]
        novoCaminho[i + 1] = y
        novoCaminho[i + 2] = x
        visinhos.append(novoCaminho)
    return visinhos

#distancia entre 2 pontos
def distancia2Pontos(ponto1, ponto2):
    x = abs(ponto1[0]-ponto2[0])
    y = abs(ponto1[1]-ponto2[1])
    return math.hypot(x,y)

#calculo de distancia do caminho
def calcDistanciaCaminho(caminho):
    distancia = 0
    for i in range(len(caminho)-1):
        lugar1 = cidades[caminho[i]]
        lugar2 = cidades[caminho[i+1]]
        distancia += distancia2Pontos(lugar1,lugar2)
    return distancia

#calcular verificar se tem algum vizinho melhor
def calcMenorDistancia(visinhos,caminho):
    menorCaminho = caminho
    menorDistancia = calcDistanciaCaminho(caminho)
    for i in visinhos:
        distancia = calcDistanciaCaminho(i)
        if distancia < menorDistancia:
            menorCaminho = i
            menorDistancia = distancia
    if menorCaminho == caminho:
        return False
    return menorCaminho

#core do código
def subidaEncosta(inicio):
    menorCaminho = inicio
    while True:
        vizinhos = getVizinhos(menorCaminho)
        resposta = calcMenorDistancia(vizinhos,menorCaminho)
        if resposta == False:
            break
        menorCaminho = resposta
    return menorCaminho


inicio = lista[:]
inicio.append(inicio[0])
menor = subidaEncosta(inicio)

# testando caminhos de "partida" diferentes
for i in range(500):
    novoInicio = lista[:]
    shuffle(novoInicio)
    novoInicio.append(novoInicio[0])
    outroMenor = subidaEncosta(novoInicio)
    if outroMenor < menor:
        menor = outroMenor

menorDistancia = calcDistanciaCaminho(menor)
print (menor,menorDistancia)

