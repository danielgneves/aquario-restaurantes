from entidades.peixe import get_peixes

aquários = {}

def get_aquários(): return aquários

def inserir_aquário(aquário):
    id_aquário = aquário.id_aquário
    if id_aquário not in aquários.keys():
        aquários[id_aquário] = aquário
        return True
    else:
        print('Aquário ' + id_aquário + ' já existe')

class Aquario:

    def __init__(self, id_aquário, capacidade_peixes, ph_água):
        self.id_aquário = id_aquário
        self.capacidade_peixes = capacidade_peixes
        self.ph_água = ph_água
        self.peixes = {}

    def __str__(self):
        formato = '{} {:<3} {} {:<1} {} {:<3} {}'
        aquário_formatado = formato.format('|', self.id_aquário, '|', self.capacidade_peixes, '|', self.ph_água, '|')
        return aquário_formatado

    def inserir_peixe(self, ids_peixes):
        for id_peixe in ids_peixes:
            if len(self.peixes) >= self.capacidade_peixes:
                print(
                    'Aquário ' + self.id_aquário + ' atingiu a capacidade máxima de ' + str(self.capacidade_peixes) + ' peixes')
                break
            if id_peixe in get_peixes().keys():
                peixe = get_peixes()[id_peixe]
                self.peixes[id_peixe] = peixe
            else:
                print('Peixe de ID = "' + id_peixe + '" não tem cadastro')
