import random
import pandas as pd

dicionario = {0:'O', 1:'X'}
dicionario_inverso = {0:5, 1:0}
dicionario_final = {5:'X',10:'X',15:'X',0:'',1:'',2:'',3:'',4:'',6:''}

def gerador_linha():
    lista = [random.randint(0, 1) for i in range(0, 3)]
    return lista,sum(lista)

l1,soma1 = gerador_linha()
l2, soma2 = gerador_linha()
l3, soma3 = gerador_linha()

somatorio_global = soma1 + soma2 + soma3

while somatorio_global <= 2 or somatorio_global > 4:

    l1, soma1 = gerador_linha()
    l2, soma2 = gerador_linha()
    l3, soma3 = gerador_linha()
    somatorio_global = soma1 + soma2 + soma3

tabuleiro = pd.DataFrame([l1,l2,l3],columns=['a','b','c'])

vitorias_h = tabuleiro.copy()
vitorias_v = tabuleiro.copy()
vitorias_d = tabuleiro.copy()

for i in range(0,3):
    n = vitorias_h.iloc[i].sum()
    if n == 2:
       vitorias_h.iloc[i] = vitorias_h.iloc[i].replace(dicionario_inverso)

for i in range(0,3):
    n = vitorias_v.iloc[:, i].sum()
    if n == 2:
        vitorias_v.iloc[:, i] = vitorias_v.iloc[:,i].replace(dicionario_inverso)

if (vitorias_d.iloc[0,0] == 1 and vitorias_d.iloc[2,2] == 1) or (vitorias_d.iloc[0,2] == 1 and vitorias_d.iloc[2,0] == 1):
    vitorias_d.iloc[1,1] = 5

elif vitorias_d.iloc[0,0] == 1 and vitorias_d.iloc[1,1] == 1:
    vitorias_d.iloc[2, 2] = 5

elif vitorias_d.iloc[0,2] == 1 and vitorias_d.iloc[1,1] == 1:
    vitorias_d.iloc[2, 0] = 5

elif vitorias_d.iloc[2,0] == 1 and vitorias_d.iloc[1,1] == 1:
    vitorias_d.iloc[0, 2] = 5

elif vitorias_d.iloc[2,2] == 1 and vitorias_d.iloc[1,1] == 1:
    vitorias_d.iloc[0, 0] = 5

print('Jogadas aleatórias:')
print(tabuleiro.replace(dicionario))
print('\n')
print('As possibilidades de vitória para o jogador X em apenas um lance são:\n')

final = vitorias_v+ vitorias_h + vitorias_d
print(final.replace(dicionario_final))


