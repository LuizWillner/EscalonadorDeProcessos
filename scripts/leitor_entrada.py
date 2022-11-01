# /////////////////////////////// CLASSES ///////////////////////////////

class Processo:
    def __init__(self, tempo_admissao, nome_programa, prioridade, burst_io):
        self.tempo_admissao = tempo_admissao
        self.nome_programa = nome_programa
        self.prioridade = prioridade
        self.burst_io = burst_io

    def print(self):
        print(f'{self.tempo_admissao:.2f}', end='\t')
        print(self.nome_programa, end='\t')
        print(self.prioridade, end='\t')
        print(self.burst_io, end='\n')


# ////////////////////////////// FUNCTIONS //////////////////////////////

def processarEntrada(arq):
    # matriz para armazenar todas as listas-processos
    all_processos = []
    for linha in arq:
        linha_split = linha.replace('\n', '')
        linha_split = linha_split.split(maxsplit=3)   # split para formar lista do processo
        linha_split[-1] = linha_split[-1].split()  # split para formar sublista de tempos de burst e de I/O

        # fazendo os castings adequados
        linha_split[0] = float(linha_split[0])
        linha_split[2] = int(linha_split[2])
        for i in range(len(linha_split[-1])):
            linha_split[-1][i] = float(linha_split[-1][i])

        processo = Processo(tempo_admissao=linha_split[0],
                            nome_programa=linha_split[1],
                            prioridade=linha_split[2],
                            burst_io=linha_split[3])

        all_processos.append(processo)

    return all_processos
