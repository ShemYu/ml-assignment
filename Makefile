# Makefile

DOCKER_IMAGE=python:3.11-slim
CONTAINER_NAME=dev-env

dev-run:
	@docker run -it --rm -v ${PWD}:/app -w /app --name $(CONTAINER_NAME) $(DOCKER_IMAGE) /bin/bash
