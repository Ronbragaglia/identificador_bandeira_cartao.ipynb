.PHONY: help install install-dev install-all clean test test-cov test-unit test-integration \
        lint format format-check type-check security check-all build publish \
        docker-build docker-run docker-stop docker-clean docs docs-serve \
        serve-web run-examples setup-env init pre-commit-install pre-commit-run \
        update-deps freeze version info

# Variáveis
PYTHON := python
PIP := pip
VENV := .venv
ACTIVATE := $(VENV)/bin/activate
PACKAGE_NAME := card-brand-identifier
SRC_DIR := src
TESTS_DIR := tests
DOCS_DIR := docs
EXAMPLES_DIR := examples

# Cores para output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Mostra esta mensagem de ajuda
	@echo "$(BLUE)Card Brand Identifier - Makefile$(NC)"
	@echo ""
	@echo "$(GREEN)Uso:$(NC) make [alvo]"
	@echo ""
	@echo "$(YELLOW)Alvos disponíveis:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(BLUE)%-20s$(NC) %s\n", $$1, $$2}'

install: ## Instala o pacote em modo desenvolvimento
	@echo "$(GREEN)Instalando o pacote...$(NC)"
	$(PIP) install -e .
	@echo "$(GREEN)✓ Instalação concluída$(NC)"

install-dev: ## Instala dependências de desenvolvimento
	@echo "$(GREEN)Instalando dependências de desenvolvimento...$(NC)"
	$(PIP) install -e ".[dev]"
	@echo "$(GREEN)✓ Dependências de desenvolvimento instaladas$(NC)"

install-all: ## Instala todas as dependências (dev + docs)
	@echo "$(GREEN)Instalando todas as dependências...$(NC)"
	$(PIP) install -e ".[all]"
	@echo "$(GREEN)✓ Todas as dependências instaladas$(NC)"

clean: ## Limpa arquivos temporários e de build
	@echo "$(YELLOW)Limpando arquivos temporários...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ htmlcov/ .coverage coverage.xml 2>/dev/null || true
	@echo "$(GREEN)✓ Limpeza concluída$(NC)"

test: ## Executa todos os testes
	@echo "$(GREEN)Executando testes...$(NC)"
	pytest $(TESTS_DIR) -v

test-cov: ## Executa testes com coverage
	@echo "$(GREEN)Executando testes com coverage...$(NC)"
	pytest $(TESTS_DIR) -v --cov=$(SRC_DIR) --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)✓ Relatório de coverage gerado em htmlcov/$(NC)"

test-unit: ## Executa apenas testes unitários
	@echo "$(GREEN)Executando testes unitários...$(NC)"
	pytest $(TESTS_DIR) -v -m "unit"

test-integration: ## Executa apenas testes de integração
	@echo "$(GREEN)Executando testes de integração...$(NC)"
	pytest $(TESTS_DIR) -v -m "integration"

lint: ## Executa verificação de código (flake8)
	@echo "$(GREEN)Verificando código com flake8...$(NC)"
	flake8 $(SRC_DIR) $(TESTS_DIR)
	@echo "$(GREEN)✓ Verificação concluída$(NC)"

format: ## Formata o código (black + isort)
	@echo "$(GREEN)Formatando código...$(NC)"
	black $(SRC_DIR) $(TESTS_DIR)
	isort $(SRC_DIR) $(TESTS_DIR)
	@echo "$(GREEN)✓ Código formatado$(NC)"

format-check: ## Verifica formatação do código
	@echo "$(GREEN)Verificando formatação...$(NC)"
	black --check $(SRC_DIR) $(TESTS_DIR)
	isort --check-only $(SRC_DIR) $(TESTS_DIR)
	@echo "$(GREEN)✓ Formatação OK$(NC)"

type-check: ## Executa verificação de tipos (mypy)
	@echo "$(GREEN)Verificando tipos...$(NC)"
	mypy $(SRC_DIR) --ignore-missing-imports
	@echo "$(GREEN)✓ Verificação de tipos concluída$(NC)"

security: ## Executa verificação de segurança (bandit)
	@echo "$(GREEN)Verificando segurança...$(NC)"
	bandit -r $(SRC_DIR) -ll
	@echo "$(GREEN)✓ Verificação de segurança concluída$(NC)"

check-all: format-check lint type-check security test ## Executa todas as verificações
	@echo "$(GREEN)✓ Todas as verificações passaram!$(NC)"

build: ## Constrói o pacote
	@echo "$(GREEN)Construindo pacote...$(NC)"
	python -m build
	@echo "$(GREEN)✓ Pacote construído em dist/$(NC)"

publish: build ## Publica o pacote no PyPI
	@echo "$(YELLOW)Publicando no PyPI...$(NC)"
	twine upload dist/*
	@echo "$(GREEN)✓ Pacote publicado$(NC)"

docker-build: ## Constrói a imagem Docker
	@echo "$(GREEN)Construindo imagem Docker...$(NC)"
	docker build -t $(PACKAGE_NAME):latest .
	@echo "$(GREEN)✓ Imagem Docker construída$(NC)"

docker-run: ## Executa o container Docker
	@echo "$(GREEN)Executando container Docker...$(NC)"
	docker run --rm -it $(PACKAGE_NAME):latest

docker-stop: ## Para todos os containers do projeto
	@echo "$(YELLOW)Parando containers...$(NC)"
	docker stop $$(docker ps -q --filter ancestor=$(PACKAGE_NAME):latest) 2>/dev/null || true
	@echo "$(GREEN)✓ Containers parados$(NC)"

docker-clean: ## Remove imagens e containers do projeto
	@echo "$(YELLOW)Limpando Docker...$(NC)"
	docker rmi $(PACKAGE_NAME):latest 2>/dev/null || true
	@echo "$(GREEN)✓ Limpeza Docker concluída$(NC)"

docs: ## Gera a documentação
	@echo "$(GREEN)Gerando documentação...$(NC)"
	cd $(DOCS_DIR) && make html
	@echo "$(GREEN)✓ Documentação gerada em $(DOCS_DIR)/_build/html/$(NC)"

docs-serve: ## Serve a documentação localmente
	@echo "$(GREEN)Servindo documentação...$(NC)"
	cd $(DOCS_DIR) && make livehtml

serve-web: ## Executa a aplicação web (se houver)
	@echo "$(GREEN)Executando aplicação web...$(NC)"
	$(PYTHON) -m card_brand_identifier.cli --help

run-examples: ## Executa exemplos
	@echo "$(GREEN)Executando exemplos...$(NC)"
	$(PYTHON) $(EXAMPLES_DIR)/basic_usage.py

setup-env: ## Configura ambiente virtual
	@echo "$(GREEN)Configurando ambiente virtual...$(NC)"
	$(PYTHON) -m venv $(VENV)
	@echo "$(GREEN)✓ Ambiente virtual criado em $(VENV)/$(NC)"
	@echo "$(YELLOW)Ative com: source $(ACTIVATE)$(NC)"

init: setup-env install-dev ## Inicializa o projeto (cria venv e instala dependências)
	@echo "$(GREEN)✓ Projeto inicializado!$(NC)"
	@echo "$(YELLOW)Ative o ambiente com: source $(ACTIVATE)$(NC)"

pre-commit-install: ## Instala hooks do pre-commit
	@echo "$(GREEN)Instalando hooks do pre-commit...$(NC)"
	pre-commit install
	@echo "$(GREEN)✓ Hooks instalados$(NC)"

pre-commit-run: ## Executa todos os hooks do pre-commit
	@echo "$(GREEN)Executando hooks...$(NC)"
	pre-commit run --all-files
	@echo "$(GREEN)✓ Hooks executados$(NC)"

update-deps: ## Atualiza dependências
	@echo "$(GREEN)Atualizando dependências...$(NC)"
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade -e ".[dev]"
	@echo "$(GREEN)✓ Dependências atualizadas$(NC)"

freeze: ## Congela as dependências instaladas
	@echo "$(GREEN)Congelando dependências...$(NC)"
	$(PIP) freeze > requirements-freeze.txt
	@echo "$(GREEN)✓ Dependências salvas em requirements-freeze.txt$(NC)"

version: ## Mostra a versão do pacote
	@echo "$(BLUE)Versão:$(NC) $(shell $(PYTHON) -c "import card_brand_identifier; print(card_brand_identifier.__version__)")"

info: ## Mostra informações do projeto
	@echo "$(BLUE)Card Brand Identifier$(NC)"
	@echo "$(BLUE)=====================$(NC)"
	@echo "$(GREEN)Pacote:$(NC) $(PACKAGE_NAME)"
	@echo "$(GREEN)Versão:$(NC) $(shell $(PYTHON) -c "import card_brand_identifier; print(card_brand_identifier.__version__)")"
	@echo "$(GREEN)Python:$(NC) $(shell $(PYTHON) --version)"
	@echo "$(GREEN)Diretório de código:$(NC) $(SRC_DIR)"
	@echo "$(GREEN)Diretório de testes:$(NC) $(TESTS_DIR)"
	@echo "$(GREEN)Diretório de documentação:$(NC) $(DOCS_DIR)"
