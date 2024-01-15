# Projeto Django REST Framework

Este é um projeto em Python utilizando o Django REST Framework para criar uma API. Siga as instruções abaixo para configurar e executar o projeto.

## Configuração do Ambiente

Certifique-se de ter o Python e o pip instalados na sua máquina.

### 1. Clone o Repositório

```bash
git clone git@github.com:brunobastosfer/estudo-python.git
cd estudo-python
```

### 2. Crie e Ative o Ambiente Virtual

```bash
python -m venv venv
```

**No Linux/Mac:**
```bash
source venv/bin/activate
```

**No Windows:**
```bash
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

### 1. Aplicar as Migrações

```bash
python manage.py migrate
```

### 2. Criar um Superusuário (opcional)

```bash
python manage.py createsuperuser
```

## Executando o Servidor

```bash
python manage.py runserver
```

O servidor estará rodando em http://127.0.0.1:8000/.

## Acessando a API

Você pode acessar a API através do navegador ou utilizando ferramentas como [curl](https://curl.se/) ou [Postman](https://www.postman.com/).

Para a interface de administração, acesse http://127.0.0.1:8000/admin/ e faça login com as credenciais do superusuário criado.

## Encerrando o Ambiente Virtual (quando necessário)

```bash
deactivate
```

Certifique-se de que o ambiente virtual está desativado antes de fechar a sessão do terminal.

## A aplicação possui rota de:

#Login
#Signup
#Create Todo
#Update Todo
#Detail Todo
#List Todos
#Destroy Todo

## Para realizar requisições, é necessário solicitar o token na rota: api/token/ com usuário válido.
