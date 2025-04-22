from entidades.aquario import get_aquários, Aquario, inserir_aquário
from entidades.encomenda import criar_encomendas, get_encomendas, selecionar_encomendas
from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, \
    imprimir_objetos_associação_filtros
from util.data import Data
from entidades.peixe import inserir_peixe, Peixe, get_peixes
from entidades.restaurante import inserir_restaurante, get_restaurantes, Restaurante


def cadastrar_peixes():
    inserir_peixe(Peixe(id_peixe='101', tamanho=15.2, peso=120, metodo_transporte='saco_oxigenado'))
    inserir_peixe(Peixe('102', 20.5, 245, 'caixa_térmica'))
    inserir_peixe(Peixe('103', 10.8, 90, 'tanque_portátil'))
    inserir_peixe(Peixe('104', 18.3, 180, 'saco_oxigenado'))
    inserir_peixe(Peixe('105', 22.0, 250, 'saco_oxigenado'))
    inserir_peixe(Peixe('106', 12.5, 110, 'tanque_portátil'))
    inserir_peixe(Peixe('107', 25.0, 350, 'caixa_térmica'))
    inserir_peixe(Peixe('108', 17.5, 200, 'saco_oxigenado'))
    inserir_peixe(Peixe('109', 14.0, 130, 'tanque_portátil'))
    inserir_peixe(Peixe('110', 30.0, 500, 'caixa_térmica'))


def cadastrar_restaurantes():
    inserir_restaurante(
        Restaurante(nome='Sabor do Mar', endereço='Rua das Ondas, 123', cidade_estado='Rio de Janeiro - RJ',
                    telefone_contato='(21) 99999-1234'))
    inserir_restaurante(Restaurante('Peixaria Gourmet', 'Av. Atlântica, 456', 'São Paulo - SP', '(11) 98888-5678'))
    #inserir_restaurante(Restaurante('Mariscos & Cia', 'Praia do Forte, 789', 'Salvador - BA', '(71) 97777-9012'))
    inserir_restaurante(Restaurante('Baiacu Restaurante', 'Rua do Porto, 321', 'Florianópolis - SC', '(48) 95555-6789'))
    inserir_restaurante(Restaurante('Delícias do Oceano', 'Av. Beira-Mar, 654', 'Fortaleza - CE', '(85) 94444-3333'))
    #inserir_restaurante(Restaurante('Ostra Feliz', 'Rua das Conchas, 999', 'Recife - PE', '(81) 93333-2222'))
    #inserir_restaurante(Restaurante('Mar Azul', 'Av. Oceânica, 555', 'Natal - RN', '(84) 92222-1111'))
    inserir_restaurante(Restaurante('Peixes da Serra', 'Estrada do Mar, 777', 'Belo Horizonte - MG', '(31) 91111-0000'))
    #inserir_restaurante(Restaurante('Tainha Dourada', 'Lagoa Grande, 222', 'Curitiba - PR', '(41) 96666-5555'))
    inserir_restaurante(Restaurante('Camarão Real', 'Porto Seguro, 888', 'Vitória - ES', '(27) 95555-4444'))
    #inserir_restaurante(Restaurante('Oceano Azul', 'Rua das Palmeiras, 432', 'Porto Alegre - RS', '(51) 92222-3344'))
    inserir_restaurante(Restaurante('Maré Alta', 'Avenida do Sol, 987', 'Maceió - AL', '(82) 93333-4455'))
    #inserir_restaurante(Restaurante('Salvador Marinho', 'Rua dos Corais, 678', 'Salvador - BA', '(71) 94444-5566'))
    inserir_restaurante(Restaurante('Peixe & Pimenta', 'Rua do Farol, 123', 'São Luís - MA', '(98) 95555-6677'))
    #inserir_restaurante(Restaurante('Mestre do Mar', 'Avenida das Gaivotas, 456', 'Recife - PE', '(81) 96666-7788'))
    inserir_restaurante(Restaurante('Marinhos e Cia', 'Praia do Sol, 789', 'Fortaleza - CE', '(85) 97777-8899'))
    inserir_restaurante(Restaurante('Onda Azul', 'Rua das Águas, 567', 'Belém - PA', '(91) 98888-9900'))
    inserir_restaurante(Restaurante('Peixe na Brasa', 'Rua da Praia, 234', 'Aracaju - SE', '(79) 99999-1122'))


def cadastrar_aquários():
    aquário = Aquario(id_aquário='AQ1', capacidade_peixes=5)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['101', '102', '103'])

    aquário = Aquario('AQ2', 3)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['104', '105', '106'])

    aquário = Aquario('AQ3', 4)
    inserir_aquário(aquário)
    aquário.inserir_peixe(['107', '108', '109', '110'])


def cadastrar_encomendas():
    criar_encomendas(id_aquário='AQ1', nome_restaurante='Sabor do Mar', data=Data(1, 4, 2025))
    criar_encomendas('AQ2', 'Peixaria Gourmet', Data(2, 4, 2025))
    criar_encomendas('AQ3', 'Delícias do Oceano', Data(3, 4, 2025))
    criar_encomendas('AQ2', 'Peixes da Serra', Data(4, 4, 2025))
    criar_encomendas('AQ2', 'Baiacu Restaurante', Data(4, 4, 2025))
    criar_encomendas('AQ2', 'Camarão Real', Data(5, 4, 2025))
    criar_encomendas('AQ2', 'Peixe & Pimenta', Data(6, 4, 2025))
    criar_encomendas('AQ2', 'Peixe na Brasa', Data(6, 4, 2025))
    criar_encomendas('AQ2', 'Maré Alta', Data(6, 4, 2025))
    criar_encomendas('AQ2', 'Marinhos e Cia', Data(7, 4, 2025))

def imprimir_somente_para_alinhar_formatação():
    print('\nAquários : ID do aquário - capacidade de peixes')
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
    print('\nAquários : ID do aquário - capacidade de peixes')
    print(' - Peixes : ID do peixe - tamanho - peso - método de transporte')
    for índice, aquário in enumerate(get_aquários().values()):
        imprimir_objeto(indice=índice, objeto_str=str(aquário))
        imprimir_objetos_internos(aquário.peixes.values())
    cadastrar_encomendas()
    cabeçalho_encomenda = 'Encomendas : ID do aquário - nome do restaurante - data da encomenda'
    imprimir_objetos('\n' + cabeçalho_encomenda, get_encomendas())
    filtros, encomendas_selecionadas = selecionar_encomendas()
    cabeçalho_encomenda_filtros = (cabeçalho_encomenda + '\n -- capacidade de peixes do aquário - estado do restaurante')
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(data_mínima_encomenda=Data(dia=4, mês=4, ano=2025))
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(Data(4, 4, 2025), capacidade_máxima_peixes_aquário=3)
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
    filtros, encomendas_selecionadas = selecionar_encomendas(Data(4, 4, 2025), 3, estado_restaurante='SC')
    imprimir_objetos_associação_filtros(cabeçalho_encomenda_filtros, encomendas_selecionadas, filtros)
