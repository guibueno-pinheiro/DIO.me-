-- Criação das tabelas

CREATE TABLE Cliente (
  cliente_id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  telefone VARCHAR(20),
  email VARCHAR(100) UNIQUE
);

CREATE TABLE Veiculo (
  veiculo_id SERIAL PRIMARY KEY,
  placa VARCHAR(10) UNIQUE NOT NULL,
  modelo VARCHAR(50),
  ano INT CHECK (ano >= 1900 AND ano <= EXTRACT(YEAR FROM CURRENT_DATE)),
  cliente_id INT NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

CREATE TABLE Servico (
  servico_id SERIAL PRIMARY KEY,
  descricao VARCHAR(100) NOT NULL,
  preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0)
);

CREATE TABLE OrdemServico (
  os_id SERIAL PRIMARY KEY,
  data_abertura DATE NOT NULL,
  data_fechamento DATE,
  cliente_id INT NOT NULL,
  veiculo_id INT NOT NULL,
  FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id),
  FOREIGN KEY (veiculo_id) REFERENCES Veiculo(veiculo_id)
);

CREATE TABLE ItemOrdemServico (
  os_id INT NOT NULL,
  servico_id INT NOT NULL,
  quantidade INT NOT NULL CHECK (quantidade > 0),
  preco_unitario DECIMAL(10,2) NOT NULL CHECK (preco_unitario >= 0),
  PRIMARY KEY (os_id, servico_id),
  FOREIGN KEY (os_id) REFERENCES OrdemServico(os_id),
  FOREIGN KEY (servico_id) REFERENCES Servico(servico_id)
);

CREATE TABLE Funcionario (
  funcionario_id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cargo VARCHAR(50)
);

CREATE TABLE FuncionarioOS (
  os_id INT NOT NULL,
  funcionario_id INT NOT NULL,
  PRIMARY KEY (os_id, funcionario_id),
  FOREIGN KEY (os_id) REFERENCES OrdemServico(os_id),
  FOREIGN KEY (funcionario_id) REFERENCES Funcionario(funcionario_id)
);

-- Inserção de dados para testes

INSERT INTO Cliente (nome, telefone, email) VALUES
('Carlos Silva', '11999999999', 'carlos@example.com'),
('Ana Pereira', '11988888888', 'ana@example.com');

INSERT INTO Veiculo (placa, modelo, ano, cliente_id) VALUES
('ABC1234', 'Fiat Uno', 2010, 1),
('XYZ9876', 'Honda Civic', 2018, 2);

INSERT INTO Servico (descricao, preco) VALUES
('Troca de óleo', 150.00),
('Alinhamento', 80.00),
('Balanceamento', 70.00);

INSERT INTO OrdemServico (data_abertura, data_fechamento, cliente_id, veiculo_id) VALUES
('2025-07-01', '2025-07-02', 1, 1),
('2025-07-05', NULL, 2, 2);

INSERT INTO ItemOrdemServico (os_id, servico_id, quantidade, preco_unitario) VALUES
(1, 1, 1, 150.00),
(1, 2, 1, 80.00),
(2, 3, 1, 70.00);

INSERT INTO Funcionario (nome, cargo) VALUES
('José Almeida', 'Mecânico'),
('Mariana Costa', 'Auxiliar');

INSERT INTO FuncionarioOS (os_id, funcionario_id) VALUES
(1, 1),
(1, 2),
(2, 1);

-- Queries complexas para o desafio:

-- 1. Quantos serviços cada cliente já realizou?
SELECT c.nome, COUNT(DISTINCT os.os_id) AS total_ordens
FROM Cliente c
JOIN OrdemServico os ON c.cliente_id = os.cliente_id
GROUP BY c.nome
ORDER BY total_ordens DESC;

-- 2. Qual o total gasto por cliente (valor total das ordens)?
SELECT c.nome, SUM(i.quantidade * i.preco_unitario) AS total_gasto
FROM Cliente c
JOIN OrdemServico os ON c.cliente_id = os.cliente_id
JOIN ItemOrdemServico i ON os.os_id = i.os_id
GROUP BY c.nome
HAVING SUM(i.quantidade * i.preco_unitario) > 0
ORDER BY total_gasto DESC;

-- 3. Quais funcionários participaram de cada ordem de serviço?
SELECT os.os_id, f.nome AS funcionario
FROM OrdemServico os
JOIN FuncionarioOS fo ON os.os_id = fo.os_id
JOIN Funcionario f ON fo.funcionario_id = f.funcionario_id
ORDER BY os.os_id, funcionario;

-- 4. Listar veículos e seus clientes, ordenando pelo nome do cliente:
SELECT v.placa, v.modelo, v.ano, c.nome
FROM Veiculo v
JOIN Cliente c ON v.cliente_id = c.cliente_id
ORDER BY c.nome, v.placa;

-- 5. Valor médio gasto por serviço (preço médio por serviço vendido)
SELECT s.descricao, AVG(i.preco_unitario) AS preco_medio
FROM Servico s
JOIN ItemOrdemServico i ON s.servico_id = i.servico_id
GROUP BY s.descricao
ORDER BY preco_medio DESC;
