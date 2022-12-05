# /////////////////////////////// IMPORTS ///////////////////////////////
from operator import itemgetter, attrgetter
from scripts.escrita_saida import *


# Variáveis globais
lista_prontos = []
lista_espera = []
lista_finalizados = []
executando = []


def recebeProcesso(lista_processos, tempo):
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
                lista_prontos.append(lista_espera[0])
            else:  # se tem alguém executando na CPU...
                # if executando[0].              
                lista_prontos.append(executando[0])  # ... interrupção gerada tira o processo da CPU e coloca na fila de pronto
                executando[0].tempo_executado = 0 #Controle apenas para o caso de escalonamento RR
                executando.clear()  # (Na realidade, o SO assume o controle da CPU)
                lista_prontos.append(lista_espera[0])  # ... o processo que gerou a interrupção vai pra fila de pronto
                executando.append(lista_prontos[0])  # ... o primeiro da fila de pronto entra em execução
                lista_prontos.pop(0)
                # (assume-se que a interrupção e a seleção do próximo processo são instantâeneos)
            lista_espera.pop(0)

    else:
        lista_espera[0].novo_na_espera = False

    return
