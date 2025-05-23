from entidades.aquario import get_aquários, Aquario, inserir_aquário
from entidades.encomenda import criar_encomendas, get_encomendas, selecionar_encomendas
from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.peixe import inserir_peixe, Peixe, get_peixes
from entidades.restaurante import inserir_restaurante, get_restaurantes, Restaurante


def cadastrar_peixes():
    inserir_peixe(Peixe(id_peixe='101', tamanho=15.2, peso=120, método_transporte='tanque_portátil'))
    inserir_peixe(Peixe('102', 20.5, 245, 'caixa_térmica'))
    inserir_peixe(Peixe('103', 10.8, 90, 'caixa_térmica'))
    inserir_peixe(Peixe('104', 18.3, 180, 'saco_oxigenado'))
    inserir_peixe(Peixe('105', 22.0, 250, 'saco_oxigenado'))
    inserir_peixe(Peixe('106', 12.5, 110, 'caixa_térmica'))
    inserir_peixe(Peixe('107', 25.0, 350, 'caixa_térmica'))
    inserir_peixe(Peixe('108', 17.5, 200, 'saco_oxigenado'))
    inserir_peixe(Peixe('109', 14.0, 130, 'saco_oxigenado'))
    inserir_peixe(Peixe('110', 30.0, 500, 'caixa_térmica'))
    inserir_peixe(Peixe('111', 16.0, 150, 'tanque_portátil'))
    inserir_peixe(Peixe('112', 28.5, 400, 'caixa_térmica'))
    inserir_peixe(Peixe('113', 9.5, 80, 'saco_oxigenado'))
    inserir_peixe(Peixe('114', 15.0, 600, 'caixa_térmica'))
    inserir_peixe(Peixe('115', 19.0, 210, 'tanque_portátil'))


def cadastrar_restaurantes():
    inserir_restaurante(
        Restaurante(nome='Sabor do Mar', endereço='Rua das Ondas, 123', cidade_estado='Rio de Janeiro - RJ',
                    telefone_contato='(21) 99999-1234'))
    inserir_restaurante(Restaurante('Peixaria Gourmet', 'Av. Atlântica, 456', 'São Paulo - SP', '(11) 98888-5678'))
    inserir_restaurante(Restaurante('Baiacu Restaurante', 'Rua do Porto, 321', 'Florianópolis - SC', '(48) 95555-6789'))
    inserir_restaurante(Restaurante('Delícias do Oceano', 'Av. Beira-Mar, 654', 'Fortaleza - CE', '(85) 94444-3333'))
    inserir_restaurante(Restaurante('Peixes da Serra', 'Estrada do Mar, 777', 'Belo Horizonte - MG', '(31) 91111-0000'))
    inserir_restaurante(Restaurante('Camarão Real', 'Porto Seguro, 888', 'Vitória - ES', '(27) 95555-4444'))
    inserir_restaurante(Restaurante('Maré Alta', 'Avenida do Sol, 987', 'Maceió - AL', '(82) 93333-4455'))
    inserir_restaurante(Restaurante('Peixe & Pimenta', 'Rua do Farol, 123', 'São Luís - MA', '(98) 95555-6677'))
    inserir_restaurante(Restaurante('Marinhos e Cia', 'Praia do Sol, 789', 'Fortaleza - CE', '(85) 97777-8899'))
    inserir_restaurante(Restaurante('Onda Azul', 'Rua das Águas, 567', 'Belém - PA', '(91) 98888-9900'))
    inserir_restaurante(Restaurante('Peixe na Brasa', 'Rua da Praia, 234', 'Aracaju - SE', '(79) 99999-1122'))
    inserir_restaurante(Restaurante('Tubarão Azul', 'Av. Costa e Silva, 101', 'Santos - SP', '(13) 97777-1234'))
    inserir_restaurante(Restaurante('Costa Brava', 'Av. do Mar, 100', 'Itajaí - SC', '(47) 97777-1122'))
    inserir_restaurante(Restaurante('Mariscaria Real', 'Av. dos Pescadores, 321', 'Salvador - BA', '(71) 95555-8765'))
    inserir_restaurante(Restaurante('Sushi do Mar', 'Rua das Pérolas, 78', 'Manaus - AM', '(92) 93333-4567'))
    inserir_restaurante(Restaurante('Barra do Peixe', 'Av. Beira Rio, 210', 'Porto Alegre - RS', '(51) 94444-3210'))


def cadastrar_aquários():
    aquário = Aquario(id_aquário='AQ1', capacidade_peixes=5, ph_água=7.0 )
    inserir_aquário(aquário)
    aquário.inserir_peixe(['101', '102', '103'])

    aquário = Aquario('AQ2', 3, 6.5)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['104', '105', '106'])

    aquário = Aquario('AQ3', 4, 6.8)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['107', '108', '109', '110'])

    aquário = Aquario('AQ4', 6, 7.0)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['112', '113', '114'])

    aquário = Aquario('AQ5', 2, 6.7)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['115', '104'])


def cadastrar_encomendas():
    criar_encomendas(id_aquário='AQ1', nome_restaurante='Sabor do Mar', data=Data(1, 4, 2025))
    criar_encomendas('AQ3', 'Peixaria Gourmet', Data(2, 4, 2025))
    criar_encomendas('AQ1', 'Delícias do Oceano', Data(3, 4, 2025))
    criar_encomendas('AQ3', 'Peixes da Serra', Data(4, 4, 2025))
    criar_encomendas('AQ2', 'Baiacu Restaurante', Data(4, 4, 2025))
    criar_encomendas('AQ3', 'Camarão Real', Data(5, 4, 2025))
    criar_encomendas('AQ3', 'Peixe & Pimenta', Data(6, 4, 2025))
    criar_encomendas('AQ1', 'Peixe na Brasa', Data(6, 4, 2025))
    criar_encomendas('AQ2', 'Maré Alta', Data(6, 4, 2025))
    criar_encomendas('AQ2', 'Marinhos e Cia', Data(7, 4, 2025))
    criar_encomendas('AQ4', 'Tubarão Azul', Data(8, 4, 2025))
    criar_encomendas('AQ5', 'Costa Brava', Data(9, 4, 2025))
    criar_encomendas('AQ1', 'Mariscaria Real', Data(10, 4, 2025))
    criar_encomendas('AQ4', 'Sushi do Mar', Data(11, 4, 2025))
    criar_encomendas('AQ5', 'Barra do Peixe', Data(12, 4, 2025))

def imprimir_somente_para_alinhar_formatação():
    print('\nAquários : ID do aquário - capacidade de peixes - pH da água')
    for índice, aquário in enumerate(get_aquários().values()): print(aquário)
    print('\nPeixes : ID do peixe - tamanho - peso - forma de entrega')
    for aquário in get_aquários().values():
        for peixe in aquário.peixes.values(): print(peixe)


if __name__ == ('__main__'):
    cadastrar_restaurantes()
    imprimir_objetos(cabeçalho='\nRestaurantes : nome - endereço - cidade e estado - contato', objetos=get_restaurantes().values())
    cadastrar_peixes()
    cadastrar_aquários()
    imprimir_somente_para_alinhar_formatação()
    print('\nAquários : ID do aquário - capacidade de peixes - pH da água')
    print(' - Peixes : ID do peixe - tamanho - peso - método de transporte')
    for índice, aquário in enumerate(get_aquários().values()):
        imprimir_objeto(indice=índice, objeto_str=str(aquário))
        imprimir_objetos_internos(aquário.peixes.values())
    cadastrar_encomendas()
    cabeçalho_encomenda = 'Encomendas : ID do aquário - nome do restaurante - data da encomenda'
    imprimir_objetos('\n' + cabeçalho_encomenda, get_encomendas())
    filtros, encomendas_selecionadas = selecionar_encomendas()
    cabeçalho_encomenda_filtros = (cabeçalho_encomenda + '\n -- capacidade de peixes do aquário - cidade e estado do restaurante - métodos de transporte dos peixes')
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(data_mínima_encomenda=Data(dia=4, mês=4, ano=2025))
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(Data(4, 4, 2025), capacidade_máxima_peixes_aquário=4)
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(Data(4, 4, 2025), 4, estado_restaurante='SC')
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(Data(4, 4, 2025), 4, 'SC', método_transporte_peixe='caixa_térmica')
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)

