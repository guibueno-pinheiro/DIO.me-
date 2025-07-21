# gera_readme_oficina.py

readme_content = """
# Descrição do Desafio

## Contexto

Você irá desenvolver, a partir do zero, um esquema conceitual para um sistema de controle e gerenciamento de ordens de serviço em uma oficina mecânica. Baseado na narrativa fornecida, seu desafio é identificar e modelar todas as entidades, seus atributos e relacionamentos. Caso algum detalhe não esteja explícito na narrativa, utilize seu conhecimento do domínio para tomar decisões fundamentadas e registre essas suposições no README do seu repositório.

## Objetivo

Criar um modelo conceitual robusto que represente fielmente o processo da oficina mecânica, contemplando:

- Clientes que levam veículos para consertos ou revisões periódicas.
- Veículos atribuídos a equipes de mecânicos responsáveis pela identificação e execução dos serviços.
- Ordens de Serviço (OS) geradas com informações detalhadas como número, data de emissão, valor, status e data prevista para conclusão.
- Cálculo do custo da OS com base na tabela de referência de mão-de-obra e no valor das peças utilizadas.
- Registro da autorização do cliente para a execução dos serviços.
- Detalhamento dos mecânicos com código, nome, endereço e especialidade.
- Controle do fluxo das OS, desde a avaliação até a execução pelos mesmos mecânicos responsáveis.

## Entregáveis

- Esquema conceitual (modelo entidade-relacionamento) completo, criado a partir da narrativa.
- Implementação do esquema em banco de dados relacional.
- Documentação no README do projeto explicando o modelo criado, as decisões de projeto e as possíveis suposições feitas durante o desenvolvimento.

## Próximos Passos

Implemente o modelo conforme descrito e suba seu projeto em um repositório GitHub próprio. Esta é uma excelente oportunidade para enriquecer seu portfólio com um projeto realista e valioso para avaliação.
"""

def criar_readme():
    with open("README.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(readme_content)
    print("Arquivo README.md criado com sucesso!")

if __name__ == "__main__":
    criar_readme()
