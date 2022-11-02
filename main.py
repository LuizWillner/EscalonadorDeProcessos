# /////////////////////////////// IMPORTS ///////////////////////////////

from scripts.leitor_entrada import *
from scripts.escalonador_fifo import *

# //////////////////////////////// MAIN ////////////////////////////////

arq_entrada = open("entrada/entrada2.in", 'r')
arq_saida = open("saida/saida.out", 'w')

arq_saida.write("")
arq_saida.close()

processos = processarEntrada(arq_entrada)
# processos[0].print()
arq_entrada.close()

processos = sorted(processos, key=attrgetter("tempo_admissao"))  # organiza por tempo de entrada
escalonadorFIFO(processos, 0)
