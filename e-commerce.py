# gera_readme.py

readme_content = """
# Projeto: Modelo de Banco de Dados para Sistema de Vendas

## Descrição do Projeto

Este projeto apresenta um modelo relacional para um sistema de vendas que contempla clientes Pessoa Física (PF) e Pessoa Jurídica (PJ), formas de pagamento múltiplas, controle de entregas com status e código de rastreamento, além do gerenciamento de produtos, fornecedores, vendedores e pedidos.

O objetivo principal é representar, de forma consistente e normalizada, as relações entre os diferentes atores e entidades do sistema, garantindo integridade dos dados e flexibilidade para futuras expansões.

---

## Contexto e Requisitos

- **Clientes:** Podem ser Pessoa Física (PF) ou Pessoa Jurídica (PJ), mas uma conta não pode conter informações dos dois tipos simultaneamente. Por isso, a tabela `Cliente` registra o tipo do cliente, e informações específicas de PF e PJ ficam em tabelas separadas (`ContaClientePF` e `ContaClientePJ`).

- **Pagamentos:** Cada cliente pode possuir diversas formas de pagamento cadastradas, armazenadas na tabela `Pagamento`.

- **Pedidos e Entregas:** Os pedidos realizados pelos clientes são registrados na tabela `Pedido`. Cada pedido tem uma entrega associada, que possui status (ex: "Em transporte", "Entregue") e código de rastreamento para acompanhamento.

- **Produtos e Fornecedores:** Produtos são relacionados a fornecedores através da tabela associativa `ProdutoFornecedor`, permitindo registrar preços específicos por fornecedor. O estoque dos produtos também é controlado.

- **Vendedores:** Também são gerenciados e podem se relacionar com fornecedores via tabela `VendedorFornecedor`.

---

## Modelo de Dados

O esquema implementado possui as seguintes tabelas principais:

- `Cliente` (cliente_id, tipo_cliente, nome, email, telefone)
- `ContaClientePF` (cliente_id, cpf, rg)
- `ContaClientePJ` (cliente_id, razao_social, cnpj, inscricao_estadual)
- `Pagamento` (pagamento_id, cliente_id, tipo_pagamento, detalhes_pagamento)
- `Pedido` (pedido_id, cliente_id, data_pedido, status, total)
- `Entrega` (entrega_id, pedido_id, status, codigo_rastreio)
- `Produto` (produto_id, nome, descricao, preco, estoque)
- `Fornecedor` (fornecedor_id, nome, cnpj, contato)
- `ProdutoFornecedor` (produto_id, fornecedor_id, preco_fornecedor)
- `Vendedor` (vendedor_id, nome, cpf, email)
- `VendedorFornecedor` (vendedor_id, fornecedor_id)

---

## Considerações Técnicas

- Uso de chaves primárias e estrangeiras para garantir a integridade referencial.
- Uso de restrições para garantir que um cliente seja apenas PF ou PJ.
- Permite múltiplas formas de pagamento por cliente.
- Cada pedido está associado a uma única entrega, que possui controle de status e rastreamento.
- Relacionamentos muitos-para-muitos entre produtos e fornecedores, e entre vendedores e fornecedores.

---

## Exemplos de Consultas

- Quantidade de pedidos por cliente.
- Verificar se algum vendedor também é fornecedor.
- Listagem de produtos com seus fornecedores e estoques.
- Total gasto por cliente.

---

Este projeto serve como base para desenvolvimento de sistemas comerciais e pode ser expandido para incluir funcionalidades como gerenciamento de usuários, integração com sistemas de pagamento, análise de vendas, entre outros.
"""

def criar_readme():
    with open("README.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(readme_content)
    print("Arquivo README.md criado com sucesso!")

if __name__ == "__main__":
    criar_readme()
