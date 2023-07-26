.PHONY: docker-build docker-run run-uvicorn

DOCKER_IMAGE=python:3.10-slim
CONTAINER_NAME=dev-env
DOCKER_TAG ?= translate_service:latest
DOCKER_BUILD_CONTEXT = .
DOCKER_FILE_PATH = Dockerfile


docker-build:
	@docker build -t $(DOCKER_TAG) -f $(DOCKER_FILE_PATH) $(DOCKER_BUILD_CONTEXT)

docker-run:
	@docker run -it --rm -v ${PWD}:/app -p 9527:9527 --name $(CONTAINER_NAME) $(DOCKER_TAG) /bin/bash

run-uvicorn:
	sh bin/entrypoint.sh --reload
