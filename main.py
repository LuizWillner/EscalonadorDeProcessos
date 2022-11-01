# /////////////////////////////// IMPORTS ///////////////////////////////

from scripts.leitor_entrada import *


# //////////////////////////////// MAIN ////////////////////////////////

arq_entrada = open("entrada/processos.in", 'r')

processos = processarEntrada(arq_entrada)
print(processos)

arq_entrada.close()
