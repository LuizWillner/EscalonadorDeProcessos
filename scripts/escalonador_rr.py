# /////////////////////////////// IMPORTS ///////////////////////////////
from scripts.processos_geral import *


def atualiza_prontosRR(lista_processos, quantum):

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
            executando[0].tempo_executado += 1  # incrementa em 1 o valor atual

            # caso o tempo que o processo em execução gastou se iguale ao quantum
            if executando[0].tempo_executado == quantum:
                executando[0].tempo_executado = 0
                # caso o processo não tenha terminado o tempo de CPU
                if executando[0].burst_io[0] > 0:        
                    lista_prontos.append(executando[0])  # tira o processo atual em execução e coloca na fila de prontos
                    executando.clear()
                    return lista_processos

        # caso o tempo de burst seja igual a 0
    
        if executando[0].burst_io[0] == 0 :

            executando[0].burst_io.pop(0)  # remove o tempo de burst da lista de tempos de burst I/O
            executando[0].tempo_executado = 0

            # acabaram os tempos na lista de burst_io
            if len(executando[0].burst_io) == 0:
                lista_processos = removerProcesso(lista_processos, executando[0])
            else:  # existe uma solicitação de I/O
                lista_espera.append(executando[0])
                # Se a lista de espera antes tava vazia...
                if len(lista_espera) == 1:
                    # ... o processo que acabou de ser adicionado é novo e o tempo de I/O dele não vai ser atualizado nessa iteração
                    lista_espera[0].novo_na_espera = True

            executando.clear()

            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])
                lista_prontos.pop(0)

    return lista_processos


def escalonadorRR(lista_processos, quantum, tempo):

    while len(lista_processos) != 0:
        
        recebeProcesso(lista_processos, tempo)

        if len(executando) == 0:
            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])  # move o primeiro processo na fila de prontos para e execução
                lista_prontos.pop(0)

        else:
            lista_processos = atualiza_prontosRR(lista_processos, quantum)
        
        if len(lista_espera) != 0:
            atualiza_espera()

        if len(executando) == 0 and len(lista_prontos) != 0:
            executando.append(lista_prontos[0])
            lista_prontos.pop(0)

        escreve_saida("saida/saida.out", lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        print_saida_terminal(lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        tempo += 1
