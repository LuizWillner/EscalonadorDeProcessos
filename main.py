# /////////////////////////////// IMPORTS ///////////////////////////////

from scripts.leitor_entrada import *
from scripts.escalonador_fifo import *

# //////////////////////////////// MAIN ////////////////////////////////

print("Digite o nome do arquivo de entrada:")
nome_arq_entrada = input(">> ")
print()

arq_entrada = open("entrada/" + nome_arq_entrada, 'r')
arq_saida = open("saida/saida.out", 'w')

arq_saida.write("")
arq_saida.close()

processos = processarEntrada(arq_entrada)
# processos[0].print()
arq_entrada.close()

processos = sorted(processos, key=attrgetter("tempo_admissao"))  # organiza por tempo de entrada


print('Digite o numero da politica de escalonamento')
print("[1] FCFS")
print("[2] Round-Robin")
politica_escalonador = int(input(">> "))
print()

if politica_escalonador == 1:
    escalonadorFIFO(processos, 0)
elif politica_escalonador == 2:
    # escalonadorRR()
    pass
else:
    print("Numero invalido!")
