#!/usr/bin/make -f

PROJECT_NAME := 'Key Value cache API'
FLAGSHIP_STORE_SERVICE := key-value-cache-py-api
CONTAINER_NAME := key-value-cache-py_api_1

FLAGSHIP_STORE_ROOT_FOLDER := $(shell pwd)
DOCKER_COMPOSE_FILE := $(FLAGSHIP_STORE_ROOT_FOLDER)/docker-compose.yaml
DOCKER_PROJECT_NAME := key-value-cache-py
DOCKER_COMMAND := docker-compose -p $(DOCKER_PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE)


build: ## Build project image
	$(DOCKER_COMMAND) build --no-cache

env-start: ## Start project containers defined in docker-compose
	$(DOCKER_COMMAND) up -d

env-stop: ## Stop project containers defined in docker-compose
	$(DOCKER_COMMAND) stop

env-recreate: env-stop build env-start

env-restart: env-stop env-start

test: ## Run test suite in project's main container
	docker exec -it $(CONTAINER_NAME) pytest -vv

bash: ## Open a bash shell in project's main container
	docker exec -it ${CONTAINER_NAME} bash

view-logs: ## Display interactive logs of all project containers
	$(DOCKER_COMMAND) logs -f
