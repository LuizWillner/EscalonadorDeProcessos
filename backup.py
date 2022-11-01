#from scripts.leitor_entrada import *
from operator import itemgetter, attrgetter

global lista_prontos # pode executar
global lista_espera # esperando I/O
global executando # executando na CPU
global tempo

tempo = 0
lista_prontos = []
lista_espera = []
executando = []

def remover(lista_processos, processo):

    print(processo.nome_programa)
    print("\n")

    for i in range(len(lista_processos)):
        print(lista_processos[i].nome_programa)

        if lista_processos[i].nome_programa == processo.nome_programa:
            lista_processos.remove(processo)
            print("removido")
            return lista_processos

    print("Não foi possível remover o processo da lista")
    return lista_processos


def escalonador(lista_processos, tempo):
    
    if len(lista_processos) == 0:
        return

    # atualiza a fila de prontos pelo tempo de admissão
    for i in range(len(lista_processos)):
        if tempo == lista_processos[i].tempo_admissao:
            lista_prontos.append(lista_processos[i])


    # confere se existe algum processo em execução #

    # caso não exista
    if len(executando) == 0:
        executando.append(lista_prontos[0]) # move o primeiro processo na fila de prontos para e execução

    # caso exista
    else:
        
        # verifica se acabou a lista de tempos
        if len(executando[0].burst_io) == 0:

            lista_processos = remover(lista_processos, executando[0]) # remove o processo da lista de processos
            executando.clear() 
            executando.append(lista_prontos[0]) # atualiza a execução com o próximo na lista de prontos
        
        # ainda há tempos na lista burst_io
        else:
            
            # caso o tempo de burst seja maior que 0
            if executando[0].burst_io[0] > 0:
                executando[0].burst_io[0] -= 1 # decrementar em 1 o valor atual

            # caso o tempo de burst seja igual a 0
            if executando[0].burst_io[0] == 0:    
                executando[0].burst_io.remove(0) # remove o tempo de burst da lista burst_io
                lista_processos = remover(lista_processos, executando[0]) 
                executando.clear()
                executando.append(lista_prontos[0])
                #lista_espera.append(executando)          



    escalonador(lista_processos, tempo + 1)
    pass

