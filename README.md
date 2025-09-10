# DogParks API

DogParks API é uma aplicação desenvolvida em Python utilizando o framework Flask. Ela fornece uma API para gerenciar informações sobre parques para cães, incluindo endereços, estruturas, finalidades e acessos.

## 🚀 Funcionalidades

- Listagem de parques, endereços, finalidades, estruturas e acessos.
- Criação, atualização e exclusão de parques.
- Integração com um banco de dados SQLite.

---

## 🛠️ Instruções de Instalação

Siga os passos abaixo para configurar o ambiente local e executar o projeto.

### 1. Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.10 ou superior
- `pip` (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

### 2. Clone o repositório (opcional)

Se você estiver utilizando Git, clone o repositório para sua máquina local:

```bash
git clone https://github.com/CamilaRedondo/dogs_parks_api.git
cd backend
```

### 3. Crie e ative um ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:
- Linux/MacOS
```bash
source venv/bin/activate
```

- Windows
```bash
venv\Scripts\activate
```

### 4. Instale as dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r [requirements.txt]
```

### 5. Configure o banco de dados
Certifique-se de que o arquivo dogparks.db está localizado na pasta database/. Este arquivo já está incluído no projeto.

## ▶️ Comandos de Inicialização

Para iniciar o servidor Flask, execute o seguinte comando na raiz do projeto:

```bash
python [app.py]
```
O servidor será iniciado em modo de desenvolvimento e estará disponível em http://127.0.0.1:5000.

## 📂 Estrutura do Projeto

```bash
backend/
├── database/
│   └── dogparks.db
├── dogparks_api/
│   ├── [app.py](http://_vscodecontentref_/2)
│   ├── controllers/
│   ├── models/
│   └── routes/
├── [requirements.txt](http://_vscodecontentref_/3)
└── .gitignore
```

## 📝 Endpoints Disponíveis

### Parques
- GET /parques/: Lista todos os parques.
- POST /parques/: Cria um novo parque.
- PUT /parques/<id>: Atualiza um parque existente.
- DELETE /parques/<id>: Exclui um parque.

### Endereços
- GET /enderecos/paises/: Lista todos os países.
- GET /enderecos/estados/: Lista estados de um país.
- GET /enderecos/cidades/: Lista cidades de um estado e país.

### Auxiliares
- GET /aux/finalidades/: Lista finalidades.
- GET /aux/estruturas/: Lista estruturas.
- GET /aux/tipos-acesso/: Lista tipos de acesso.

## 🛡️ Licença
Este projeto é de uso acadêmico e não possui uma licença específica.

## 📧 Contato
Para dúvidas ou sugestões, entre em contato com caredondo97@gmail.com
