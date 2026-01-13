FROM python:3.13-slim

ARG DEBIAN_FRONTEND=noninteractive
ARG USER_NAME=appuser
ARG USER_UID=1000
ARG USER_GID=1000

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Criar usuário não-root
RUN groupadd -r ${USER_NAME} && useradd -r -g ${USER_NAME} ${USER_NAME}

# Fazer upgrade do pip, setuptools e wheel
RUN pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

# Instalar Chalice e dependências Python
RUN pip install --no-cache-dir \
    chalice==1.32.0 \
    boto3==1.42.25 \
    python-dotenv==1.2.1

# Criar diretório para a aplicação e definir permissões
RUN mkdir -p /app && chown -R ${USER_NAME}:${USER_NAME} /app

# Trocar para o usuário não-root
USER ${USER_NAME}

EXPOSE 8000

CMD ["tail", "-f", "/dev/null"]