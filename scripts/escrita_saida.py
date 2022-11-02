
def escreve_saida(nome_arq, lista_prontos, lista_espera, executando, tempo):

    arq_saida = open(nome_arq, 'a')
    arq_saida.write(f'Tempo corrente: {tempo} segundos\n')

    arq_saida.write('Em execução:\n')
    if len(executando) != 0:
        arq_saida.write(f'PID: , Nome: {executando[0].nome_programa}, Prioridade: {executando[0].prioridade}, Tempo restante: {executando[0].burst_io[0]}\n')
    else:
        arq_saida.write('Não há\n')

    arq_saida.write('Fila de Pronto:\n')
    for processo in lista_prontos:
        arq_saida.write(f'PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}\n')

    arq_saida.write('Fila de Espera:\n')
    for processo in lista_espera:
        arq_saida.write(f'PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}, Tempo restante: {processo.burst_io[0]}\n')
    
    arq_saida.write('\n')
    arq_saida.close()

    return


def print_saida_terminal(lista_prontos, lista_espera, executando, tempo):
    print(f'>>> Tempo corrente: {tempo} segundos')

    print('Em execução:')
    if len(executando) != 0:
        print(f'PID: , Nome: {executando[0].nome_programa}, Prioridade: {executando[0].prioridade}, Tempo restante: {executando[0].burst_io[0]}')
    else:
        print('Não há')

    print('Fila de Pronto:')
    for processo in lista_prontos:
        print(f'PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}')

    print('Fila de Espera:')
    for processo in lista_espera:
        print(f'PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}, Tempo restante: {processo.burst_io[0]}\n')

    print()

    return
