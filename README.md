# cloudwatch-playground

Um ambiente de testes para integração de uma aplicação Laravel e uma aplicação Chalice com o CloudWatch Logs usando o LocalStack.

## Requisitos
- Docker
- Docker Compose

## Como usar
1. Clone este repositório:
```bash
git clone https://github.com/gubsocosta/cloudwatch-playground.git
cd cloudwatch-playground
```
2. Inicie os serviços com Docker Compose:
```bash
   docker-compose up -d --build
```

3. Acesse o container da aplicação Laravel:
```bash
docker exec -it -u $(id -u) laravel-app bash
```
