# from scripts.leitor_entrada import *
from operator import itemgetter, attrgetter
from scripts.escrita_saida import *

# Variáveis globais
tempo = 0
lista_prontos = []
lista_espera = []
lista_finalizados = []
executando = []


def removerProcesso(lista_processos, processo):
    for i in range(len(lista_processos)):
        print(lista_processos[i].nome_programa)

        if lista_processos[i].nome_programa == processo.nome_programa:
            lista_finalizados.append(lista_processos[i])  # adicionando processo finalizado a lista de finalizados
            lista_processos.pop(i)  # removendo processo da lista de processos
            return lista_processos

    return lista_processos


def atualiza_espera(tempo):
    # caso o tempo de I/0 seja maior que 0
    if lista_espera[0].burst_io[0] > 0:
        lista_espera[0].burst_io[0] -= 1  # decrementar em 1 o valor atual

    # caso o tempo de I/O seja igual a 0
    if lista_espera[0].burst_io[0] == 0:
        lista_espera[0].burst_io.pop(0)  # remove o tempo de I/O da lista de tempos de burst I/O
        lista_prontos.append(lista_espera[0])
        lista_espera.pop(0)
    return


def atualiza_prontos(lista_processos, tempo):
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
        elif executando[0].burst_io[0] == 0:

            executando[0].burst_io.pop(0)  # remove o tempo de burst da lista de tempos de burst I/O
            # lista_processos = removerProcesso(lista_processos, executando[0])  TODO: PROVISÓRIO

            # acabaram os tempos na lista de burst_io
            if len(executando[0].burst_io) == 0:
                lista_processos = removerProcesso(lista_processos, executando[0])  # TODO: PROVISÓRIO

            else:  # existe uma solicitação de I/O
                lista_espera.append(executando[0])

            executando.clear()

            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])
                lista_prontos.pop(0)

    return lista_processos


def escalonadorFIFO(lista_processos, tempo):
    while len(lista_processos) != 0:
        # atualiza a fila de prontos pelo tempo de admissão
        for processo in lista_processos:
            if tempo == processo.tempo_admissao:
                lista_prontos.append(processo)

        # Confere se existe algum processo em execução
        # 1) caso não exista
        if len(executando) == 0:
            if len(lista_prontos) != 0:
                executando.append(lista_prontos[0])  # move o primeiro processo na fila de prontos para e execução
                lista_prontos.pop(0)

        # 2) caso exista
        else:
            lista_processos = atualiza_prontos(lista_processos, tempo)

        if len(lista_espera) != 0:
            atualiza_espera(tempo)

        tempo += 1
        escreve_saida("saida/saida.out", lista_prontos, lista_espera, executando, tempo)
