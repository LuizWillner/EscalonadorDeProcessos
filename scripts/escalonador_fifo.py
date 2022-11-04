# from scripts.leitor_entrada import *
from operator import itemgetter, attrgetter
from scripts.escrita_saida import *

# Variáveis globais
lista_prontos = []
lista_espera = []
lista_finalizados = []
executando = []


def recebe_processo(lista_processos, tempo):
    # atualiza a fila de prontos pelo tempo de admissão
    # TODO: dar um jeito de apagar processo da lista de processos depois da admissão
    for processo in lista_processos:
        if tempo == processo.tempo_admissao:
            lista_prontos.append(processo)


def removerProcesso(lista_processos, processo):
    for i in range(len(lista_processos)):
        # print(lista_processos[i].nome_programa)

        if lista_processos[i].nome_programa == processo.nome_programa:
            lista_finalizados.append(lista_processos[i])  # adicionando processo finalizado a lista de finalizados
            lista_processos.pop(i)  # removendo processo da lista de processos
            return lista_processos

    return lista_processos


def atualiza_espera():
    # Verifica se o primeiro na lista de espera acabou de entrar
    if not lista_espera[0].novo_na_espera:

        # caso o tempo de I/0 seja maior que 0
        if lista_espera[0].burst_io[0] > 0:
            lista_espera[0].burst_io[0] -= 1  # decrementar em 1 o valor atual

        # caso o tempo de I/O seja igual a 0
        if lista_espera[0].burst_io[0] == 0:
            lista_espera[0].burst_io.pop(0)  # remove o tempo de I/O da lista de tempos de burst I/O
            if len(executando) == 0:  # se não há ninguém executando na CPU...
                # Na realidade, primeiro o processo vai pra lista de pronto e, caso não haja ninguém executando, vai em
                # seguida para execução
                executando.append(lista_espera[0])
            else:  # se tem alguém executando na CPU...
                lista_prontos.append(executando[0])  # ... interrupção gerada tira o processo da CPU e coloca na fila de pronto
                executando.clear()  # (Na realidade, o SO assume o controle da CPU)
                lista_prontos.append(lista_espera[0])  # ... o processo que gerou a interrupção vai pra fila de pronto
                executando.append(lista_prontos[0])  # ... o primeiro da fila de pronto entra em execução
                lista_prontos.pop(0)
                # (assume-se que a interrupção e a seleção do próximo processo são instantâeneos)
            lista_espera.pop(0)

    else:
        lista_espera[0].novo_na_espera = False

    return


def atualiza_prontosFIFO(lista_processos):
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


def atualiza_prontosRR(lista_processos, quantum, tempo):

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
            if executando[0].tempo_executado >= quantum:
                # caso o processo não tenha terminado o tempo de CPU
                if executando[0].burst_io[0] > 0: 
                    # caso a fila de prontos não esteja vazia
                    if len(lista_prontos) != 0:

                        executando[0].tempo_executado = 0
                        lista_prontos.append(executando[0]) # tira o processo atual em execução e coloca na fila de prontos
                        executando.clear()
                        executando.append(lista_prontos[0]) # entra o primeiro da fila de prontos para execução
                        lista_prontos.pop(0)

        # caso o tempo de burst seja igual a 0
        if executando[0].burst_io[0] == 0:

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



def escalonadorFIFO(lista_processos, tempo):

    while len(lista_processos) != 0:

        recebe_processo(lista_processos, tempo)
        # Confere se existe algum processo em execução
        # 1) caso não exista
        if len(executando) == 0:
            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])  # move o primeiro processo na fila de prontos para e execução
                lista_prontos.pop(0)

        # 2) caso exista
        else:
            lista_processos = atualiza_prontosFIFO(lista_processos)

        if len(lista_espera) != 0:
            atualiza_espera()

        escreve_saida("saida/saida.out", lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        print_saida_terminal(lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        tempo += 1

def escalonadorRR(lista_processos, quantum, tempo):

    while(len(lista_processos) != 0):
        
        recebe_processo(lista_processos, tempo)

        if len(executando) == 0:
            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])  # move o primeiro processo na fila de prontos para e execução
                lista_prontos.pop(0)

        else:
            lista_processos = atualiza_prontosRR(lista_processos, quantum, tempo)
        
        if len(lista_espera) != 0:
            atualiza_espera()

        escreve_saida("saida/saida.out", lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        print_saida_terminal(lista_prontos, lista_espera, lista_finalizados, executando, tempo)
        tempo += 1
