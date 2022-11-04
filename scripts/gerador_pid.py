import random

def gerarPID(lista_processos):

    pids = random.sample(range(0,len(lista_processos)), len(lista_processos)) #Criação de lista com valores randomicos sem repetição

    for i in range(len(lista_processos)):
        lista_processos[i].pid = pids[i]  #Atribuição dos PIDS a cada processo
    
    return