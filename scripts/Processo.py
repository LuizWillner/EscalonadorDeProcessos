# /////////////////////////////// CLASSES ///////////////////////////////

class Processo:
    def __init__(self, tempo_admissao, nome_programa, prioridade, burst_io):
        self.tempo_admissao = tempo_admissao
        self.nome_programa = nome_programa
        self.prioridade = prioridade
        self.burst_io = burst_io
        self.novo_na_espera = False

    def print(self):
        print(f'{self.tempo_admissao:.2f}', end='\t')
        print(self.nome_programa, end='\t')
        print(self.prioridade, end='\t')
        print(self.burst_io, end='\n')
