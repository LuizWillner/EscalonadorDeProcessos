# from scripts.leitor_entrada import *
from operator import itemgetter, attrgetter

# Variáveis globais
tempo = 0
lista_prontos = []
lista_espera = []
lista_finalizados = []
executando = []


def removerProcesso(lista_processos, processo):

    print(processo.nome_programa)
    print("\n")

    for i in range(len(lista_processos)):
        print(lista_processos[i].nome_programa)

        if lista_processos[i].nome_programa == processo.nome_programa:
            lista_finalizados.append(lista_processos[i])  # adicionando processo finalizado a lista de finalizados
            lista_processos.pop(i)  # removendo processo da lista de processos
            print("removido")
            return lista_processos

    print("Não foi possível remover o processo da lista")
    return lista_processos


def escalonadorFIFO(lista_processos, tempo):
    
    while len(lista_processos) != 0:
        # atualiza a fila de prontos pelo tempo de admissão
        for processo in lista_processos:
            if tempo == processo.tempo_admissao:
                lista_prontos.append(processo)

        # ### confere se existe algum processo em execução ####
        # caso não exista
        if len(executando) == 0:
            executando.append(lista_prontos[0])  # move o primeiro processo na fila de prontos para e execução
            lista_prontos.pop(0)

        # caso exista
        else:
            
            # verifica se acabou a lista de tempos de burst e I/O
            if len(executando[0].burst_io) == 0:

                lista_processos = removerProcesso(lista_processos, executando[0])  # remove o processo da lista de processos
                executando.clear() 
                executando.append(lista_prontos[0])  # atualiza a execução com o próximo na lista de prontos
                lista_prontos.pop(0)

            # ainda há tempos na lista burst_io
            else:
                
                # caso o tempo de burst seja maior que 0
                if executando[0].burst_io[0] > 0:
                    executando[0].burst_io[0] -= 1  # decrementar em 1 o valor atual

                # caso o tempo de burst seja igual a 0
                if executando[0].burst_io[0] == 0:    
                    executando[0].burst_io.pop(0)  # remove o tempo de burst da lista de tempos de burst I/O
                    lista_processos = removerProcesso(lista_processos, executando[0])  # TODO: PROVISÓRIO
                    executando.clear()
                    executando.append(lista_prontos[0])
                    lista_prontos.pop(0)
                    # lista_espera.append(executando)
        tempo += 1
