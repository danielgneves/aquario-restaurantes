restaurantes = []


def get_restaurantes(): return restaurantes


def inserir_restaurante(restaurante): restaurantes.append(restaurante)


def selecionar_restaurantes(prefixo_endereço=None, prefixo_cidade=None, sufixo_telefone_contato=None):
    filtros = '\nFiltros -- '
    if prefixo_endereço is not None: filtros += 'prefixo do endereço: ' + prefixo_endereço
    if prefixo_cidade is not None: filtros += ' - prefixo da cidade: ' + prefixo_cidade
    if sufixo_telefone_contato is not None: filtros += ' - sufixo do telefone: ' + sufixo_telefone_contato
    restaurantes_selecionados = []
    for restaurante in restaurantes:
        if prefixo_endereço is not None and not restaurante.endereço.startswith(prefixo_endereço): continue
        if prefixo_cidade is not None and not restaurante.cidade_estado.startswith(prefixo_cidade): continue
        if sufixo_telefone_contato is not None and not restaurante.telefone_contato.endswith(
            sufixo_telefone_contato): continue
        restaurantes_selecionados.append(restaurante)
    return filtros, restaurantes_selecionados


class Restaurante:
    def __init__(self, nome, endereço, cidade_estado, telefone_contato):
        self.nome = nome
        self.endereço = endereço
        self.cidade_estado = cidade_estado
        self.telefone_contato = telefone_contato

    def __str__(self):
        formato = '{} {:<18} {} {:<25} {} {:<19} {} {:<15} {}'
        restaurante_formato = formato.format('|', self.nome, '|', self.endereço, '|', self.cidade_estado, '|',
                                             self.telefone_contato, '|')
        return restaurante_formato
