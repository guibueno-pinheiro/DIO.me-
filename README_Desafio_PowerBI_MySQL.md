
# 📄 README.md – Desafio de Integração e Transformação de Dados com Power BI e MySQL no Azure

## 📌 Objetivo do Projeto

Integrar dados provenientes de um banco de dados relacional MySQL hospedado no Azure, realizar transformações e modelagens necessárias no Power BI, visando preparar os dados para visualizações e análises futuras com base em boas práticas de ETL e modelagem dimensional.

---

## ☁️ 1. Configuração da Instância MySQL no Azure

- **Serviço Utilizado**: Banco de Dados do Azure para MySQL – servidor único.
- **Configurações**:
  - Nome do servidor: `mysql-nome-do-servidor`
  - Local: `Região`
  - Autenticação: `usuário/senha`
- **Observação**: Criadas regras de firewall para permitir acesso ao Power BI.

---

## 🗃️ 2. Criação e Popularização do Banco de Dados

- Fonte dos scripts SQL: [GitHub Repository Link]
- Tabelas criadas:
  - `employee`
  - `department`
  - `project`
  - `works_on`
  - `dependent`
- Scripts executados com sucesso via [MySQL Workbench / Azure Data Studio].

---

## 📊 3. Integração com Power BI

- Conexão realizada via conector MySQL.
- Utilizado modo de importação.
- Navegação e seleção das tabelas necessárias.
- Primeira verificação feita na **visualização de dados brutos**.

---

## 🔧 4. Transformações Realizadas no Power Query

| Passo | Transformação | Observações |
|------|----------------|-------------|
| 1 | Verificação de cabeçalhos e tipos de dados | Ajustes feitos para datas, textos e números |
| 2 | Valores monetários convertidos para tipo `Decimal Number` | Ex: salário |
| 3 | Análise e tratamento de valores nulos | Substituições e preenchimentos com base em regras de negócio |
| 4 | Identificação de gerentes (Super_ssn nulo) | Adicionada coluna condicional para marcação |
| 5 | Departamentos sem gerente | Verificação feita, preenchimento simulado conforme suposição |
| 6 | Verificação de horas em projetos | Corrigidos valores inconsistentes |
| 7 | Separação de colunas compostas, se necessário | Ex: endereço ou nome completo |
| 8 | Mescla de Employee com Department | Left Join sobre `employee.dno = department.dnumber` |
| 9 | Remoção de colunas desnecessárias após mescla | Como `dno`, `dnumber` |
| 10 | Mescla de colaboradores com nomes de gerentes | Usada mescla de `employee.super_ssn = employee.ssn` |
| 11 | Criação da coluna “Nome Completo” | `Nome & " " & Sobrenome` |
| 12 | Criação da coluna “Departamento - Localização” | `dname & " - " & location` |
| 13 | Agrupamento por gerente | Contagem de colaboradores subordinados |
| 14 | Limpeza final | Remoção de colunas sem uso analítico |

---

## 🧠 5. Justificativas Técnicas

### 🔹 Por que usar *Mesclar* e não *Atribuir*:

A função **mesclar** permite combinar registros de duas tabelas com base em uma chave comum, o que é essencial quando queremos unir dados de múltiplas origens relacionais. Já o *atribuir* cria colunas derivadas dentro da própria tabela, o que não atende à necessidade de cruzar dados de múltiplas tabelas.

### 🔹 Escolha do tipo de junção:

Foi utilizada a junção do tipo **Left Outer Join** para manter todos os registros da tabela `employee`, mesmo que não haja departamento correspondente, garantindo integridade para a análise de RH.

---

## 💡 6. Query SQL Utilizada para Junção Colaborador-Gerente (Alternativa via SQL)

```sql
SELECT 
  e.fname AS nome_funcionario,
  e.lname AS sobrenome_funcionario,
  m.fname AS nome_gerente,
  m.lname AS sobrenome_gerente
FROM 
  employee e
LEFT JOIN 
  employee m ON e.super_ssn = m.ssn;
```

---

## 📦 7. Próximos Passos (para o modelo estrela futuro)

- Criação de tabelas dimensionais: `dim_colaborador`, `dim_departamento_local`, `dim_projetos`.
- Construção de fatos: `fato_alocacao`, `fato_remuneracao`.
- Relacionamentos bem definidos no modelo de dados.

---

## 🧾 8. Observações Finais

- Todos os dados utilizados são fictícios e de uso educacional.
- Transformações realizadas de acordo com boas práticas de ETL.
- O projeto está pronto para seguir para a modelagem dimensional e visualização de dados.

---

## ✅ 9. Ferramentas Utilizadas

- Power BI Desktop
- Microsoft Azure
- MySQL Workbench / Azure Data Studio
- Power Query
