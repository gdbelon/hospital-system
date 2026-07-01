# Sistema de Gerenciamento de Pacientes - Hospital

Projeto de estudo desenvolvido para aprender e praticar **FastAPI**, integração com **PostgreSQL** e conceitos de API REST. Implementa um CRUD (Create, Read, Update, Delete) completo para cadastro e gerenciamento de pacientes.

> ⚠️ Este é um projeto de aprendizado, com dados fictícios de teste — não é um sistema em produção com dados reais de pacientes.

## Tecnologias utilizadas

- **Python 3**
- **FastAPI** — framework para construção da API
- **PostgreSQL** — banco de dados relacional
- **psycopg2** — driver de conexão com o PostgreSQL
- **Pydantic** — validação de dados de entrada/saída
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **Uvicorn** — servidor ASGI para rodar a aplicação

## Funcionalidades

- Cadastrar novo paciente
- Buscar paciente por ID
- Atualizar dados de um paciente
- Deletar um paciente

## Endpoints

| Método | Rota            | Descrição                          |
|--------|-----------------|-------------------------------------|
| GET    | `/`              | Mensagem de boas-vindas             |
| POST   | `/pacientes`     | Cadastra um novo paciente           |
| GET    | `/pacientes/{id}`| Busca um paciente pelo ID           |
| PUT    | `/pacientes/{id}`| Atualiza os dados de um paciente    |
| DELETE | `/pacientes/{id}`| Remove um paciente                  |

## Estrutura do projeto

```
├── app.py           # Definição das rotas da API
├── crud.py          # Funções de acesso ao banco de dados (queries)
├── database.py       # Conexão com o PostgreSQL
├── schemas.py         # Modelos Pydantic (validação de dados)
├── main.py            # Ponto de entrada da aplicação (uvicorn)
├── requirements.txt   # Dependências do projeto
└── .env.example        # Exemplo de variáveis de ambiente necessárias
```

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone <url-do-seu-repositorio>
cd <nome-da-pasta>
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e preencha com os dados do seu banco:

```bash
cp .env.example .env
```

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hospital
DB_USER=seu_usuario
DB_PASS=sua_senha
```

### 5. Crie a tabela no PostgreSQL

```sql
CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);
```

### 6. Rode a aplicação

```bash
python main.py
```

A API estará disponível em `http://localhost:8000`.

A documentação interativa (Swagger) fica em `http://localhost:8000/docs`.

## Aprendizados do projeto

- Estruturação de uma API REST com FastAPI seguindo boas práticas (path params, verbos HTTP corretos)
- Conexão e manipulação de banco de dados PostgreSQL com psycopg2
- Validação de dados de entrada com Pydantic
- Boas práticas de configuração (variáveis de ambiente, `.gitignore`, ambiente virtual)

## Próximos passos

- Adicionar autenticação (JWT)
- Tratamento de status codes HTTP (404, 201, etc.)
- Separação em camadas (routes / services / repository)
