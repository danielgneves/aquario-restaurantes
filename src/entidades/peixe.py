peixes = []


def get_peixes(): return peixes


def inserir_peixe(peixe): peixes.append(peixe)


def selecionar_peixes(tamanho_mínimo=None, peso_máximo=None, metodo_transporte=None):
    filtros = '\nFiltros -- '
    if tamanho_mínimo is not None: filtros += 'tamanho mínimo: ' + str(tamanho_mínimo) + ' cm'
    if peso_máximo is not None: filtros += ' - peso máximo: ' + str(peso_máximo) + ' g'
    if metodo_transporte is not None: filtros += ' - metodo transporte: ' + metodo_transporte
    peixes_selecionados = []
    for peixe in peixes:
        if tamanho_mínimo is not None and peixe.tamanho < tamanho_mínimo: continue
        if peso_máximo is not None and peixe.peso > peso_máximo: continue
        if metodo_transporte is not None and peixe.metodo_transporte != metodo_transporte: continue
        peixes_selecionados.append(peixe)
    return filtros, peixes_selecionados


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
