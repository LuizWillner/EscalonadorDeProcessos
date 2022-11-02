
def escreve_saida(nome_arq, lista_prontos, lista_espera, executando, tempo):

    arq_saida = open(nome_arq, 'a')
    arq_saida.write(f'Tempo corrente: {tempo} segundos\n')

    if len(executando) != 0:
        arq_saida.write(f'Processo em execução: PID: , Nome: {executando[0].nome_programa}, Prioridade: {executando[0].prioridade}, Tempo restante: {executando[0].burst_io[0]}\n')
    else:
        arq_saida.write('Processo em execução: Não há\n')

    arq_saida.write('Fila Prontos\n')

    for processo in lista_prontos:
        arq_saida.write(f'Processo em execução: PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}\n')

    arq_saida.write('Fila Espera\n')

    for processo in lista_espera:
        arq_saida.write(f'Processo em execução: PID: , Nome: {processo.nome_programa}, Prioridade: {processo.prioridade}, Tempo restante: {processo.burst_io[0]}\n')
    
    arq_saida.write('\n')
    arq_saida.close()

    return
