## 📌 Descrição

O **Bela Viagem Forms** é um sistema de gerenciamento de **clientes e viagens** desenvolvido em **Python**, com persistência em **SQLite** e operação via **linha de comando (CLI)**.

O projeto foi construído com foco em **organização**, **separação de responsabilidades** e **validações de entrada**, servindo como uma base sólida para evoluções futuras, como API, interface web e relatórios.

---

## 🚀 Funcionalidades

### 👤 Clientes
- Cadastrar cliente  
- Listar clientes  
- Buscar clientes por:
  - Nome  
  - Email  
  - Documento  

### ✈️ Viagens
- Criar viagem vinculada a um cliente  
- Informar:
  - Destino  
  - Data de ida e data de volta (ou somente ida)  
  - Quantidade de viajantes  
  - Serviços: passagem, hospedagem, aluguel de carro e seguro  
- Listar viagens por cliente  
- Atualizar status da viagem:
  - RASCUNHO  
  - COTAÇÃO  
  - RESERVADO  
  - PAGO  
  - CANCELADO

## 🧱 Estrutura do Projeto

├── main.py-----------------# Ponto de entrada e menu principal <br>
├── db.py-------------------# Camada de persistência (SQLite)<br>
├── utils.py-----------------# Funções utilitárias (validações e formatação)<br>
├── handlers_clients.py-----# Fluxos e regras de clientes<br>
├── handlers_trips.py-------# Fluxos e regras de viagens<br>
├── agencia.db--------------# Banco de dados SQLite<br>
└── README.md


---

## 📂 Responsabilidades

- **main.py**  
  Responsável pelo menu principal e roteamento das opções para os handlers.

- **handlers_clients.py**  
  Contém os fluxos relacionados a clientes (criação, listagem e busca).

- **handlers_trips.py**  
  Contém os fluxos relacionados a viagens (criação, listagem e atualização de status).

- **utils.py**  
  Funções utilitárias para validação de entradas e formatação de saídas.

- **db.py**  
  Camada de acesso ao banco de dados utilizando SQL puro e SQLite.

---

## ⚙️ Requisitos

- Python **3.10+**
- SQLite (já incluído na biblioteca padrão do Python)
- Nenhuma dependência externa

---

## ▶️ Como Executar

1. Clone o repositório:

git clone https://github.com/seu-usuario/bela-viagem-forms.git

2. Acesse o diretório do projeto:

cd bela-viagem-forms

3. Execute a aplicação:

python main.py

## 🎯 Objetivo Profissional

Este projeto demonstra:

- Organização de código em projetos reais  
- Separação clara de camadas  
- Validações robustas de entrada  
- Pensamento arquitetural voltado à manutenção e escalabilidade  

---

## 📌 Possíveis Evoluções

- Edição e exclusão de viagens  
- Relatórios e filtros por status  
- Cálculo de valores da viagem  
- Testes automatizados  
- API REST com FastAPI  
- Interface web  

---

<hr>

## 🇺🇸 English

### 📌 Description
**Bela Viagem Forms** is a **command-line (CLI)** travel agency management system developed in **Python**, using **SQLite** for data persistence.

The project was built with a strong focus on **code organization**, **separation of concerns**, and **input validation**, serving as a solid foundation for future improvements such as APIs, web interfaces, or reporting features.

---

### 🚀 Features

#### 👤 Clients
- Register clients  
- List clients  
- Search clients by:
  - Name  
  - Email  
  - Document  

#### ✈️ Trips
- Create trips linked to a client  
- Provide:
  - Destination  
  - Departure and return dates (or one-way trips)  
  - Number of travelers  
  - Services: flight, hotel, car rental, and insurance  
- List trips by client  
- Update trip status:
  - DRAFT  
  - QUOTATION  
  - RESERVED  
  - PAID  
  - CANCELED  

---

### 🧱 Project Structure

├── main.py -------------------# Application entry point and main menu <br>
├── db.py ---------------------# Persistence layer (SQLite)<br>
├── utils.py -------------------# Utility functions (validation and formatting)<br>
├── handlers_clients.py -------# Client-related flows and rules<br>
├── handlers_trips.py ---------# Trip-related flows and rules<br>
├── agencia.db ----------------# SQLite database<br>
└── README.md

---

### 📂 Responsibilities
- **main.py** → main menu and routing  
- **handlers_*.py** → business flow logic  
- **utils.py** → input validation and formatting  
- **db.py** → database access using raw SQL  

---

### ⚙️ Requirements
- Python **3.10+**  
- SQLite (included in the Python standard library)  
- No external dependencies  

---

### ▶️ How to Run

git clone https://github.com/your-username/bela-viagem-forms.git
cd bela-viagem-forms
python main.py

---

### 🎯 Professional Purpose
This project demonstrates:
- Code organization for real-world projects  
- Clear separation of concerns  
- Robust input validation  
- Architectural thinking focused on maintainability and scalability  

---

### 📌 Possible Enhancements
- Edit and delete trips  
- Reports and filtering by status  
- Trip cost calculation  
- Automated tests  
- REST API using FastAPI  
- Web interface  
