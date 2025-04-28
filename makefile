include .env
export $(shell sed 's/=.*//' .env)

COMPOSE_FILE := docker_compose.yaml
COMPOSE := docker-compose --file $(COMPOSE_FILE)

.PHONY: help up down build

help:  ## Показать справку
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up:  ## Запустить сервисы
	$(COMPOSE) up -d

down:  ## Остановить сервисы
	$(COMPOSE) down

build:  ## Пересобрать контейнеры
	$(COMPOSE) build

logs:  ## Показать логи
	$(COMPOSE) logs -f

