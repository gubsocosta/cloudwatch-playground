FROM python:3.13-slim

WORKDIR /var/www/chalice

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar Chalice e dependências Python
RUN pip install --no-cache-dir \
    chalice==1.26.6 \
    boto3==1.28.0 \
    python-dotenv==1.0.0

# Criar diretório para a aplicação
RUN mkdir -p /var/www/chalice

EXPOSE 8000

# Comando padrão - pode ser sobrescrito
CMD ["chalice", "local", "--host", "0.0.0.0", "--port", "8000"]