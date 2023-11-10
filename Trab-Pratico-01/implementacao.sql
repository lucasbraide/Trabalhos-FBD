CREATE TABLE Bercos_Atracacao (
    id_bercos VARCHAR(2) PRIMARY KEY,
    estado VARCHAR(20) NOT NULL
)

CREATE TABLE Empresas (
	id_empresa SERIAL PRIMARY KEY,
	nome VARCHAR(50),
	cnpj VARCHAR(20) NOT NULL
);

CREATE TABLE Embarcacoes (
    id_embarcacao VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    numero_imo VARCHAR(7) NOT NULL,
    bandeira VARCHAR(50) NOT NULL,
    id_empresa_responsavel INT NOT NULL,
    tipo_embarcacao VARCHAR(50) NOT NULL,
    posicao_geografica VARCHAR(100),
    estado_embarcacao VARCHAR(50) 
        CHECK 
    (estado_embarcacao IN ('atracado', 'ancorado', 'transito', 'fila_espera', 'sob_carga', 'sob_descarga', 'quarentena', 'reparo_manutencao'))
    comprimento float,
	largura float,
	calado float,
	tonelagem float NOT NULL
)

CREATE TABLE Embarcacoes_Terceirizadas (
   	id_embarcacao INT PRIMARY KEY REFERENCES Embarcacoes(id_embarcacao),
	id_dona_carga INT REFERENCES Empresas(id_empresa)
);

CREATE TABLE Bills (
    id_bill integer PRIMARY KEY,
    id_embarcacao INT NOT NULL,
    livre_em date,
    CONSTRAINT bills_id_embarcacao_fkey FOREIGN KEY (id_embarcacao)
        REFERENCES embarcacoes (id_embarcacao) 
)

CREATE TABLE Tripulantes(
    id_tripulante serial primary key,
    nome varchar(100) NOT NULL,
    cpf varchar(11) NOT NULL,
    nacionalidade varchar(30) NOT NULL,
    gender varchar(20) NOT NULL,
    cargo varchar(20)
         CHECK
    (cargo IN ('comando', 'navegacao', 'maquinas', 'operacao_carga_descarga', 'seguranca', 'comunicacao', 'atendimento_medico', 'cozinha', 'limpeza', 'administracao', 'protecao_ambiental')) NOT NULL,
    data_nascimento date NOT NULL,
    id_embarcacao int unique NOT NULL,
    foreign key(id_embarcacao) references Embarcacoes(id_embarcacao),
)

CREATE TABLE Movimentacoes(
    id_movimentacao serial primary key,
    tipo_operation varchar(30) NOT NULL,
    id_embarcacao int unique NOT NULL,
    foreign key(id_embarcacao) references Embarcacoes(id_embarcacao)
)

CREATE TABLE Recursos_Portuarios(
    id_recurso_portuario serial primary key,
    nome varchar(50) NOT NULL,
    tipo varchar(50) NOT NULL, 
    estado varchar(30) NOT NULL
)

CREATE TABLE Conjunto_Recursos(
    id_conj_recursos serial primary key, 
    id_recurso_portuario int NOT NULL,
    id_movimentacao int NOT NULL,
    foreign key(id_recurso_portuario) references Recursos_Portuarios(id_recurso_portuario) NOT NULL,
    foreign key(id_movimentacao) references Movimentacoes(id_movimentacao)
)

CREATE TABLE Equipes_Movimentacoes(
    id_equipe_movimentacao serial primary key,
    id_empregado int NOT NULL,
    id_movimentacao int NOT NULL,
    foreign key(id_empregado) references Empregados(id_empregado) NOT NULL,
    foreign key(id_movimentacao) references Movimentacoes(id_movimentacao) NOT NULL
)

CREATE TABLE Empregados(
    id_empregado serial primary key,
    nome varchar(100) NOT NULL,
    cpf varchar(11) NOT NULL,
    email varchar(50) NOT NULL,
    telefone varchar(20) NOT NULL,
    nacionalidade varchar(30) NOT NULL,
    nasc_data date NOT NULL,
    gender varchar(15) NOT NULL,
    cargo varchar(15) NOT NULL
)