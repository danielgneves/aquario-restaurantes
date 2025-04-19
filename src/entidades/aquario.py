from entidades.peixe import get_peixes

aquários = {}

def get_aquários(): return aquários

class Aquario:

    def __init__(self, id_aquário, capacidade_peixes):
        self.id_aquário = id_aquário
        self.capacidade_peixes = capacidade_peixes
        self.peixes = {}

    def __str__(self):
        formato = '{} {:<3} {} {:<10 } {}'
        aquário_formatado = formato.format('|', self.id_aquário, '|', self.capacidade, '|')
        return aquário_formatado

    def inserir_peixe(self, ids_peixes):
        for id_peixe in ids_peixes:
            if id_peixe in get_peixes().keys():
                self.peixes[id_peixe] = get_peixes()[id_peixe]
            else:
                print('Peixe de ID = "' + id_peixe + '" não tem cadastro')
