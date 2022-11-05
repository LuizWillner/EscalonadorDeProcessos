# /////////////////////////////// IMPORTS ///////////////////////////////

from scripts.leitor_entrada import *
from scripts.escalonador_fifo import *
from scripts.gerador_pid import *
from scripts.escalonador_rr import *

# //////////////////////////////// MAIN ////////////////////////////////

print("Digite o nome do arquivo de entrada:")
nome_arq_entrada = input(">> ")
# nome_arq_entrada = 'entrada3.in'
# print(nome_arq_entrada)
print()

arq_entrada = open("entrada/" + nome_arq_entrada, 'r')
arq_saida = open("saida/saida.out", 'w')

arq_saida.write("")
arq_saida.close()

processos = processarEntrada(arq_entrada)
# processos[0].print()
arq_entrada.close()

processos = sorted(processos, key=attrgetter("tempo_admissao"))  # organiza por tempo de entrada

gerarPID(processos) # Atribuição dos PIDS

print('Digite o numero da politica de escalonamento')
print("[1] FCFS")
print("[2] Round-Robin")
politica_escalonador = int(input(">> "))
# politica_escalonador = 1
# print(politica_escalonador)
print()

if politica_escalonador == 1:
    escalonadorFIFO(processos, 0)
elif politica_escalonador == 2:
    print('Digite o quantum')
    quantum = int(input(">> "))

    escalonadorRR(processos, quantum, 0)
    pass
else:
    print("Numero invalido!")
