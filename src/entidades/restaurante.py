restaurantes = {}


def get_restaurantes(): return restaurantes


def inserir_restaurante(restaurante):
    nome_restaurante = restaurante.nome
    if nome_restaurante not in restaurantes.keys():
        restaurantes[nome_restaurante] = restaurante
        return True
    else:
        print('Restaurante ' + nome_restaurante +' já tem cadastro')
        return False

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
