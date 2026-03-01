# aws-playground

Ambiente de desenvolvimento local para testar integrações com AWS.

Nesse ambiente, temos as seguintes aplicações:
- uma aplicacao com php/laravel
- uma aplicação com python/chalice
- LocalStack para simular os serviços da AWS
- AWS CLI para interagir com o LocalStack

O objetivo é criar um ambiente de desenvolvimento completo para testar integrações com AWS sem precisar de uma conta real.

## Requisitos
- Docker
- Docker Compose

## Como usar
1. Clone este repositório:
```bash
git clone https://github.com/gubsocosta/aws-playground.git
cd aws-playground
```

2. Inicie os serviços com Docker Compose:
```bash
   docker compose up -d --build
```

3. Para acessar uma das aplicações, use os seguintes comandos:
- Para acessar o container do Laravel:
```bash
docker compose exec -it laravel-app bash
```
- Para acessar o container do Chalice:
```bash
docker compose exec -it chalice-app sh
```