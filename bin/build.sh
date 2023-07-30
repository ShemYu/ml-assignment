eval $(minikube -p minikube docker-env)
DOCKER_TAG ?= translate_service:latest
DOCKER_BUILD_CONTEXT = .
DOCKER_FILE_PATH = Dockerfile
docker build -t $(DOCKER_TAG) -f $(DOCKER_FILE_PATH) $(DOCKER_BUILD_CONTEXT)
kubectl apply -f k8s/deployment.yaml