eval $(minikube -p minikube docker-env)
DOCKER_TAG=translate_service:latest
DOCKER_BUILD_CONTEXT=.
DOCKER_FILE_PATH=Dockerfile
REGISTRY_CLUSTER_IP=$(kubectl get svc registry -n kube-system -o=jsonpath='{.spec.clusterIP}')
export REGISTRY_CLUSTER_IP
docker build -t $DOCKER_TAG -f $DOCKER_FILE_PATH $DOCKER_BUILD_CONTEXT
docker tag $DOCKER_TAG $REGISTRY_CLUSTER_IP:80/$DOCKER_TAG
docker push $REGISTRY_CLUSTER_IP:80/$DOCKER_TAG
envsubst < k8s/deployment.yaml | kubectl apply -f -
kubectl rollout status deployment/translation-deployment
kubectl port-forward svc/translation-service 9527:9527 # Only for testing on local