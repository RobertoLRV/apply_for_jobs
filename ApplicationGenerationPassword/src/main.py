
# import time
import string

from random import choice
# from itertools import combinations_with_replacement

string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits  # 0123456789
string.punctuation  # <=>?@[\]^_`{|}~.

tamanho = 9
# Criação de Função para Geração de Senha:
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
    senha += choice(valores)

print(senha)


# def gerar_senhas(valores, tamanho):
#    comb = combinations_with_replacement(valores, tamanho)

#    print(list(comb))


# ini_t = time.time()
# gerar_senhas(valores, tamanho)
# fin_t = time.time()

# print("Tempo: " + str(fin_t - ini_t) + "s")
