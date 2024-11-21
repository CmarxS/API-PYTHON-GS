
# Gerenciamento de Eletrodomésticos - API
Esta API foi desenvolvida usando o framework Flask em Python e tem como objetivo fornecer um sistema de gerenciamento de eletrodomésticos, autenticação de usuários e acesso aos eletrodomésticos cadastrados por clientes. A API conecta-se a um banco de dados Oracle e permite o login de clientes, além de retornar eletrodomésticos associados a um cliente específico.

## Funcionalidades

### 1. Rota /login [POST]:

- Descrição: Realiza a autenticação do cliente com base em um e-mail e senha fornecidos.

- Entrada: JSON contendo email e senha.

- Saída: Retorna uma mensagem de sucesso com os detalhes do cliente (email e idCliente) se a autenticação for bem-sucedida, ou uma mensagem de erro caso contrário.

### 2. Rota /find-eletrodomesticos [GET]:

- Descrição: Retorna uma lista de eletrodomésticos cadastrados para um cliente específico com base no e-mail fornecido.

- Entrada: email fornecido via query string.

- Saída: Lista de eletrodomésticos do cliente, incluindo idEletrodomestico, nome, marca e custoEstimado. Retorna erro caso o cliente não seja encontrado.

## Configurações Necessárias para Rodar a API

### 1. Instalar Dependências

- A API depende do Flask, flask_cors para controle de origem cruzada, e oracledb para conexão ao banco de dados Oracle.

- Instale as dependências necessárias usando o seguinte comando:
        
        pip install flask flask-cors oracledb

### 2. Configurar o Banco de Dados Oracle

- Esta API conecta-se a um banco de dados Oracle. Certifique-se de que você tem as credenciais corretas e que o banco de dados está acessível.

- Atualize a função get_conexao() com suas credenciais corretas, se necessário:

        def get_conexao(): 
            return oracledb.connect(user="seu_usuario", password="sua_senha", dsn="oracle.fiap.com.br/orcl") 

### 3. Rodando a API
- Para rodar a API, execute o script com o Python: `API.py`

- Por padrão, a API rodará no endereço http://127.0.0.1:5000. Para alterar o endereço ou a porta, modifique a linha app.run().
