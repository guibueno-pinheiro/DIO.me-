# Modelo Dimensional - Financial Sample (Star Schema)

## ✨ Descrição do Desafio

Este projeto consiste em construir um modelo dimensional (esquema em estrela) a partir da tabela "Financial Sample". O objetivo é organizar os dados em tabelas de dimensão e fato, melhorando a eficiência analítica e permitindo a criação de relatórios mais robustos e performáticos.

---

## 📈 Tabelas Criadas

### ⭐ Tabela Original

* **Financials\_origem**: backup oculto da tabela original.

### 🔄 Tabela Fato

* **F\_Vendas**:

  * SK\_ID (chave substituta)
  * ID\_Produto
  * Produto
  * Units Sold
  * Sales Price
  * Discount Band
  * Segment
  * Country
  * Salers
  * Profit
  * Date

### 📆 Tabela de Calendário

* **D\_Calendário**:

  * Criada com a função DAX `CALENDAR()` baseada nos campos de data presentes na tabela fato.

### 🏦 Tabelas Dimensão

* **D\_Produtos**:

  * ID\_Produto
  * Produto
  * Média de Unidades Vendidas
  * Média de Valor de Vendas
  * Mediana de Valor de Vendas
  * Valor Máximo de Venda
  * Valor Mínimo de Venda

* **D\_Produtos\_Detalhes**:

  * ID\_Produto
  * Discount Band
  * Sale Price
  * Units Sold
  * Manufactoring Price

* **D\_Descontos**:

  * ID\_Produto
  * Discount
  * Discount Band

* **D\_Detalhes**:

  * Tabela com atributos adicionais que não foram incluídos nas demais dimensões (ex: combinações de Segment, Country, Saler, etc.)

---

## 🎓 Funções e Etapas Aplicadas

* Criação da **Tabela Calendário** com `CALENDAR(MIN(Data), MAX(Data))`
* Uso de **agrupamento** para gerar médias, medianas, máximos e mínimos nas dimensões
* Construção de colunas com **condicionais DAX** (ex: classificação de produtos por performance ou margens de lucro)
* Reorganização das colunas para otimização do modelo
* Relacionamentos entre tabelas usando as chaves de produto e datas

---

## 📁 Repositório

* Projeto salvo como:

  * `modelo_dimensional_professor.pbix`
  * `modelo_dimensional_professor.sql`
  * Imagem do esquema estrela (salvar como: `modelo_estrela.png`)
  * Este README como descrição

---

## 📚 Conclusão

Este modelo tem como finalidade otimizar a consulta e análise de dados financeiros, tornando mais fácil extrair insights como: desempenho por produto, impacto de descontos, sazonalidade de vendas e rentabilidade por segmento ou país.

O repositório serve como base para estudos em Power BI e modelagem dimensional, além de apresentar boas práticas para portfólios profissionais.
