# Dockerfile para Card Brand Identifier

FROM python:3.11-slim

# Define metadados
LABEL maintainer="Rone Bragaglia <ronbragaglia@gmail.com>"
LABEL description="Identificador de Bandeira de Cartão de Crédito"
LABEL version="1.0.0"

# Define diretório de trabalho
WORKDIR /app

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos do projeto
COPY pyproject.toml ./
COPY src/ ./src/
COPY requirements.txt ./

# Instala o pacote
RUN pip install --no-cache-dir -e ".[dev]"

# Cria usuário não-root
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Troca para usuário não-root
USER appuser

# Comando padrão
CMD ["python", "-m", "card_brand_identifier.cli", "--help"]

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import card_brand_identifier; print('OK')" || exit 1
