from util.gerais import imprimir_objetos
from entidades.peixe import inserir_peixe, Peixe, get_peixes, selecionar_peixes
from entidades.restaurante import inserir_restaurante, get_restaurantes, selecionar_restaurantes, Restaurante


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
    inserir_restaurante(Restaurante('Mariscos & Cia', 'Praia do Forte, 789', 'Salvador - BA', '(71) 97777-9012'))
    inserir_restaurante(Restaurante('Baiacu Restaurante', 'Rua do Porto, 321', 'Florianópolis - SC', '(48) 95555-6789'))
    inserir_restaurante(Restaurante('Delícias do Oceano', 'Av. Beira-Mar, 654', 'Fortaleza - CE', '(85) 94444-3333'))
    inserir_restaurante(Restaurante('Ostra Feliz', 'Rua das Conchas, 999', 'Recife - PE', '(81) 93333-2222'))
    inserir_restaurante(Restaurante('Mar Azul', 'Av. Oceânica, 555', 'Natal - RN', '(84) 92222-1111'))
    inserir_restaurante(Restaurante('Peixes da Serra', 'Estrada do Mar, 777', 'Belo Horizonte - MG', '(31) 91111-0000'))
    inserir_restaurante(Restaurante('Tainha Dourada', 'Lagoa Grande, 222', 'Curitiba - PR', '(41) 96666-5555'))
    inserir_restaurante(Restaurante('Camarão Real', 'Porto Seguro, 888', 'Vitória - ES', '(27) 95555-4444'))
    inserir_restaurante(Restaurante('Oceano Azul', 'Rua das Palmeiras, 432', 'Porto Alegre - RS', '(51) 92222-3344'))
    inserir_restaurante(Restaurante('Maré Alta', 'Avenida do Sol, 987', 'Maceió - AL', '(82) 93333-4455'))
    inserir_restaurante(Restaurante('Salvador Marinho', 'Rua dos Corais, 678', 'Salvador - BA', '(71) 94444-5566'))
    inserir_restaurante(Restaurante('Peixe & Pimenta', 'Rua do Farol, 123', 'São Luís - MA', '(98) 95555-6677'))
    inserir_restaurante(Restaurante('Mestre do Mar', 'Avenida das Gaivotas, 456', 'Recife - PE', '(81) 96666-7788'))
    inserir_restaurante(Restaurante('Marinhos e Cia', 'Praia do Sol, 789', 'Fortaleza - CE', '(85) 97777-8899'))
    inserir_restaurante(Restaurante('Onda Azul', 'Rua das Águas, 567', 'Belém - PA', '(91) 98888-9900'))
    inserir_restaurante(Restaurante('Peixe na Brasa', 'Rua da Praia, 234', 'Aracaju - SE', '(79) 99999-1122'))


if __name__ == ('__main__'):
    cadastrar_peixes()
    cabeçalho = 'Peixes : id - tamanho - peso - forma de entrega'
    imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_peixes())
    filtros, peixes_selecionados = selecionar_peixes()
    imprimir_objetos(cabeçalho, peixes_selecionados, filtros)
    filtros, peixes_selecionados = selecionar_peixes(tamanho_mínimo=20.0)
    imprimir_objetos(cabeçalho, peixes_selecionados, filtros)
    filtros, peixes_selecionados = selecionar_peixes(20.0, peso_máximo=250)
    imprimir_objetos(cabeçalho, peixes_selecionados, filtros)
    filtros, peixes_selecionados = selecionar_peixes(20.0, 250, metodo_transporte='saco_oxigenado')
    imprimir_objetos(cabeçalho, peixes_selecionados, filtros)
    cadastrar_restaurantes()
    cabeçalho = 'Restaurantes : nome - endereço - cidade estado - telefone contato'
    imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_restaurantes())
    filtros, restaurantes_selecionados = selecionar_restaurantes()
    imprimir_objetos(cabeçalho, restaurantes_selecionados, filtros)
    filtros, restaurantes_selecionados = selecionar_restaurantes(prefixo_endereço='Rua')
    imprimir_objetos(cabeçalho, restaurantes_selecionados, filtros)
    filtros, restaurantes_selecionados = selecionar_restaurantes('Rua', prefixo_cidade='S')
    imprimir_objetos(cabeçalho, restaurantes_selecionados, filtros)
    filtros, restaurantes_selecionados = selecionar_restaurantes('Rua', 'S', sufixo_telefone_contato='77')
    imprimir_objetos(cabeçalho, restaurantes_selecionados, filtros)
