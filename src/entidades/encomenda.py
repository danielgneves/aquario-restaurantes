from entidades.aquario import get_aquários
from entidades.restaurante import get_restaurantes

encomendas = []

def get_encomendas(): return encomendas

def inserir_encomenda(encomenda):
    if encomenda not in encomendas:
        encomendas.append(encomenda)
    else:
        print('Encomenda de Peixe já tem cadastro --- ' + str(encomenda))

def criar_encomendas(id_aquário, nome_restaurante, data):
    aquário = get_aquários()[id_aquário]
    if aquário is None:
        print('Aquário de ID ' + id_aquário + ' não cadastrado')
        return
    restaurante = get_restaurantes()[nome_restaurante]
    if restaurante is None:
        print('Restaurante ' + nome_restaurante + ' não cadastrado')
        return
    encomenda = Encomenda(aquário, restaurante, data)
    inserir_encomenda(encomenda)

def selecionar_encomendas(data_mínima_encomenda=None, capacidade_máxima_peixes_aquário=None, estado_restaurante=None, método_transporte_peixe=None):
    filtros = '\nFiltros -- '
    if data_mínima_encomenda is not None: filtros += 'data mínima da encomenda: ' + str(data_mínima_encomenda)
    if capacidade_máxima_peixes_aquário is not None: filtros += ' - capacidade máxima de peixes no aquário: ' + str(capacidade_máxima_peixes_aquário)
    if estado_restaurante is not None: filtros += ' - estado do restaurante: ' + estado_restaurante
    if método_transporte_peixe is not None: filtros += ' - método de transporte do peixe: ' + método_transporte_peixe
    encomendas_selecionadas = []
    for encomenda in encomendas:
        if data_mínima_encomenda is not None and encomenda.data < data_mínima_encomenda: continue
        if capacidade_máxima_peixes_aquário is not None and encomenda.aquário.capacidade_peixes > capacidade_máxima_peixes_aquário: continue
        if estado_restaurante is not None and not encomenda.restaurante.cidade_estado.endswith(estado_restaurante): continue
        if método_transporte_peixe is not None:
            peixes_com_transporte = False
            for peixe in encomenda.aquário.peixes.values():
                if peixe.método_transporte == método_transporte_peixe:
                    peixes_com_transporte = True
                    break
            if not peixes_com_transporte:
                continue
        encomendas_selecionadas.append(encomenda)
    return filtros, encomendas_selecionadas

class Encomenda:

    def __init__(self, aquário, restaurante, data):
        self.aquário = aquário
        self.restaurante = restaurante
        self.data = data

    def __str__(self):
        formato = '{} {:<3} {} {:<18} {} {:<10} {}'
        encomenda_formata = formato.format('|', self.aquário.id_aquário, '|', self.restaurante.nome,
                                            '|', str(self.data), '|')
        return encomenda_formata

    def str_filtro(self):
        metodos_transporte = ', '.join({peixe.método_transporte for peixe in self.aquário.peixes.values()})
        formato = '{:>2} {} {:<19} {} {:<31} {}'
        filtro_formato = formato.format(self.aquário.capacidade_peixes, '|', self.restaurante.cidade_estado, '|', metodos_transporte, '|')
        return self.__str__() + filtro_formato