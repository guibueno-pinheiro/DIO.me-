-- Modelo Dimensional (Esquema em Estrela) com foco no Professor

-- Tabela Fato: Fato_Professor
CREATE TABLE Fato_Professor (
    idFato INT PRIMARY KEY,
    idProfessor INT,
    idDisciplina INT,
    idCurso INT,
    idDepartamento INT,
    idData INT,
    cargaHoraria INT,
    semestre VARCHAR(10),
    FOREIGN KEY (idProfessor) REFERENCES Dim_Professor(idProfessor),
    FOREIGN KEY (idDisciplina) REFERENCES Dim_Disciplina(idDisciplina),
    FOREIGN KEY (idCurso) REFERENCES Dim_Curso(idCurso),
    FOREIGN KEY (idDepartamento) REFERENCES Dim_Departamento(idDepartamento),
    FOREIGN KEY (idData) REFERENCES Dim_Tempo(idData)
);

-- Dimensão: Professor
CREATE TABLE Dim_Professor (
    idProfessor INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    tipoVinculo VARCHAR(50)
);

-- Dimensão: Disciplina
CREATE TABLE Dim_Disciplina (
    idDisciplina INT PRIMARY KEY,
    nome VARCHAR(100),
    codigo VARCHAR(10),
    cargaHoraria INT
);

-- Dimensão: Curso
CREATE TABLE Dim_Curso (
    idCurso INT PRIMARY KEY,
    nome VARCHAR(100),
    modalidade VARCHAR(50)
);

-- Dimensão: Departamento
CREATE TABLE Dim_Departamento (
    idDepartamento INT PRIMARY KEY,
    nome VARCHAR(100),
    campus VARCHAR(50),
    idProfessorCoordenador INT
);

-- Dimensão: Tempo
CREATE TABLE Dim_Tempo (
    idData INT PRIMARY KEY,
    data DATE,
    ano INT,
    semestre VARCHAR(10),
    trimestre VARCHAR(10),
    mes INT,
    nomeMes VARCHAR(20),
    dia INT,
    diaSemana VARCHAR(20)
);

-- Observação:
-- Este modelo considera que as informações de datas (como data de início das disciplinas, cursos ou semestre letivo) estarão disponíveis para a população da Dim_Tempo.
-- Dados como "tipoVinculo" do professor (efetivo, substituto, etc.) ou "modalidade" do curso (presencial, EAD) podem ser adaptados conforme o dicionário de dados da universidade.
-- A granularidade da tabela fato está ao nível de professor-disciplina-curso-semestre.
