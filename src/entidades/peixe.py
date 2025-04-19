peixes = {}


def get_peixes(): return peixes


def inserir_peixe(self, peixe):
    id_peixe = peixe.id_peixe
    if id_peixe not in self.peixes.keys():
        self.peixes[id_peixe] = peixe
    else:
        print('Peixe com ID = "' + id_peixe + '" já adicionado ao Aquário')


class Peixe:
    def __init__(self, id_peixe, tamanho, peso, metodo_transporte):
        self.id_peixe = id_peixe
        self.tamanho = tamanho
        self.peso = peso
        self.metodo_transporte = metodo_transporte if metodo_transporte in ('saco_oxigenado', 'caixa_térmica', 'tanque_portátil') else 'indefinido'

    def __str__(self):
        formato = '{} {:<3} {} {:<7} {} {:<5} {} {:<15} {}'  # ajustar de acordo com as entradas
        peixe_formato = formato.format('|', self.id_peixe, '|', str(self.tamanho) + ' cm', '|', f'{self.peso:3d}' + ' g',
                                       '|', self.metodo_transporte, '|')
        return peixe_formato
