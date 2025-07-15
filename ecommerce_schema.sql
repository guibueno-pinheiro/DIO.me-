-- Criação das tabelas

CREATE TABLE Cliente (
  cliente_id INT PRIMARY KEY,
  tipo_cliente CHAR(2) CHECK (tipo_cliente IN ('PF', 'PJ')),
  nome VARCHAR(100),
  email VARCHAR(100),
  telefone VARCHAR(20)
);

CREATE TABLE ContaClientePF (
  cliente_id INT PRIMARY KEY,
  cpf VARCHAR(14) UNIQUE,
  rg VARCHAR(20),
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id) ON DELETE CASCADE
);

CREATE TABLE ContaClientePJ (
  cliente_id INT PRIMARY KEY,
  razao_social VARCHAR(100),
  cnpj VARCHAR(18) UNIQUE,
  inscricao_estadual VARCHAR(20),
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id) ON DELETE CASCADE
);

CREATE TABLE Pagamento (
  pagamento_id INT PRIMARY KEY,
  cliente_id INT,
  tipo_pagamento VARCHAR(50),
  detalhes_pagamento TEXT,
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

CREATE TABLE Pedido (
  pedido_id INT PRIMARY KEY,
  cliente_id INT,
  data_pedido DATE,
  status VARCHAR(30),
  total DECIMAL(10,2),
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

CREATE TABLE Entrega (
  entrega_id INT PRIMARY KEY,
  pedido_id INT UNIQUE,
  status VARCHAR(30),
  codigo_rastreio VARCHAR(50),
  FOREIGN KEY (pedido_id) REFERENCES Pedido(pedido_id)
);

CREATE TABLE Produto (
  produto_id INT PRIMARY KEY,
  nome VARCHAR(100),
  descricao TEXT,
  preco DECIMAL(10,2),
  estoque INT
);

CREATE TABLE Fornecedor (
  fornecedor_id INT PRIMARY KEY,
  nome VARCHAR(100),
  cnpj VARCHAR(18),
  contato VARCHAR(100)
);

CREATE TABLE ProdutoFornecedor (
  produto_id INT,
  fornecedor_id INT,
  preco_fornecedor DECIMAL(10,2),
  PRIMARY KEY (produto_id, fornecedor_id),
  FOREIGN KEY (produto_id) REFERENCES Produto(produto_id),
  FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor(fornecedor_id)
);

CREATE TABLE Vendedor (
  vendedor_id INT PRIMARY KEY,
  nome VARCHAR(100),
  cpf VARCHAR(14),
  email VARCHAR(100)
);

CREATE TABLE VendedorFornecedor (
  vendedor_id INT,
  fornecedor_id INT,
  PRIMARY KEY (vendedor_id, fornecedor_id),
  FOREIGN KEY (vendedor_id) REFERENCES Vendedor(vendedor_id),
  FOREIGN KEY (fornecedor_id) REFERENCES Fornecedor(fornecedor_id)
);

-- Inserção de dados exemplo

INSERT INTO Cliente VALUES (1, 'PF', 'João Silva', 'joao@email.com', '11999999999');
INSERT INTO ContaClientePF VALUES (1, '123.456.789-00', 'MG1234567');
INSERT INTO Produto VALUES (1, 'Camiseta', 'Camiseta 100% algodão', 50.00, 100);
INSERT INTO Fornecedor VALUES (1, 'Fornecedor A', '12.345.678/0001-99', 'contato@fornecedor.com');
INSERT INTO ProdutoFornecedor VALUES (1, 1, 30.00);
INSERT INTO Pedido VALUES (1, 1, '2025-07-15', 'Enviado', 50.00);
INSERT INTO Entrega VALUES (1, 1, 'Em transporte', 'ABC123XYZ');

-- Queries de exemplo

-- Quantos pedidos foram feitos por cada cliente
SELECT c.cliente_id, c.nome, COUNT(p.pedido_id) AS total_pedidos
FROM Cliente c
LEFT JOIN Pedido p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nome
ORDER BY total_pedidos DESC;

-- Algum vendedor também é fornecedor?
SELECT v.vendedor_id, v.nome
FROM Vendedor v
JOIN VendedorFornecedor vf ON v.vendedor_id = vf.vendedor_id;

-- Relação de produtos, fornecedores e estoques
SELECT p.nome AS produto, f.nome AS fornecedor, p.estoque, pf.preco_fornecedor
FROM Produto p
JOIN ProdutoFornecedor pf ON p.produto_id = pf.produto_id
JOIN Fornecedor f ON pf.fornecedor_id = f.fornecedor_id
ORDER BY p.nome;

-- Relação de nomes dos fornecedores e nomes dos produtos
SELECT f.nome AS fornecedor, p.nome AS produto
FROM Fornecedor f
JOIN ProdutoFornecedor pf ON f.fornecedor_id = pf.fornecedor_id
JOIN Produto p ON pf.produto_id = p.produto_id
ORDER BY f.nome, p.nome;

-- Total gasto por cliente (atributo derivado)
SELECT c.cliente_id, c.nome, SUM(p.total) AS total_gasto
FROM Cliente c
JOIN Pedido p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nome
HAVING SUM(p.total) > 0
ORDER BY total_gasto DESC;
