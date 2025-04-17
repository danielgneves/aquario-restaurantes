aquários = {}

def get_aquários(): return aquários

class Aquario:

    def __init__(self, id_aquário, capacidade_peixes):
        self.id_aquário = id_aquário
        self.capacidade_peixes = capacidade_peixes
        self.peixes = {}

    def __str__(self):
        formato = '{} {:<3} {} {:<10} {}'
        aquário_formatado = formato.format('|', self.id_aquário, '|', self.capacidade, '|')
        return aquário_formatado

    def inserir_peixe(self, peixe):
        id_peixe = peixe.id_peixe
        if id_peixe not in self.peixes.keys(): self.peixes[id_peixe] = peixe
        else: print('Peixe com ID = "' + id_peixe + '" já adicionado ao Aquário')
