# /////////////////////////////// IMPORTS ///////////////////////////////

from scripts.leitor_entrada import *
from scripts.escalonador_fifo import *

# //////////////////////////////// MAIN ////////////////////////////////

arq_entrada = open("entrada/processos.in", 'r')

processos = processarEntrada(arq_entrada)
print(processos)

processos = sorted(processos, key=attrgetter("tempo_admissao"))  # organiza por tempo de entrada
escalonadorFIFO(processos, 0)

arq_entrada.close()
