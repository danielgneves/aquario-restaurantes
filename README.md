# 🐟 Encomendas de Peixes para Restaurantes

Um sistema para gerenciar encomendas de **peixes ornamentais** (como GoldFish e TretaNeon) de aquários para restaurantes, desenvolvido como projeto acadêmico para a disciplina de **Linguagem de Programação 1**.

---

## 📋 Descrição do Projeto

O projeto modela o processo de encomenda de peixes ornamentais para aquários de restaurantes, incluindo:
- Cadastro de **peixes** com características específicas.
- Gestão de **aquários** e **restaurantes**.
- Registro de **encomendas** com métodos de transporte especializados.

---

## 🎯 Funcionalidades Principais

- ✅ Cadastro de peixes ornamentais (GoldFish e TretaNeon).
- ✅ Controle de aquários e capacidade máxima.
- ✅ Registro de encomendas e método de transporte.
- ✅ Relacionamento entre entidades (herança, associações e cardinalidades).

---

## 🗄️ Modelo de Dados

### Entidades Principais

| Entidade       | Descrição                                  | Atributos                               |
|----------------|-------------------------------------------|------------------------------------------|
| **Peixe**      | Classe base para peixes ornamentais.      | `id_peixe`, `tamanho`, `peso`, `metodo_transporte` |
| **GoldFish**   | Peixe dourado (herda de `Peixe`).         | `cor`, `tempo_vida`                     |
| **TretaNeon**  | Peixe neon (herda de `Peixe`).            | `brilho`, `origem`                      |
| **Restaurante**| Estabelecimento que recebe os peixes.     | `nome`, `endereço`, `cidade_estado`, `telefone_contato`  |
| **Aquario**    | Local de origem dos peixes.               | `id_aquario`, `capacidade_maxima`, `peixes`      |
| **Encomenda**  | Registro de entrega.                      | `data`, `aquario`, `restaurante` |

### Relacionamentos

| Tipo de Relacionamento       | Descrição                                | Entidades Envolvidas               |
|------------------------------|------------------------------------------|------------------------------------|
| **Herança**                  | Especialização de peixes.               | `Peixe` → `GoldFish`, `TretaNeon` |
| **Associação**               | Encomenda liga Aquário e Restaurante.    | `Encomenda` → `Aquario`, `Restaurante` |
| **Muitos-para-Muitos**       | Aquário pode conter múltiplos peixes.    | `Aquario` [n:n] `Peixe`           |
