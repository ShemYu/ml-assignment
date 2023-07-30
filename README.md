# Translation Inference Service

## Introduction

### Project Overview
This project aims to implement a translation inference service that runs on Kubernetes and provides a RESTful API on port 9527.

Utilizing the `M2M100` translation model, this service is capable of translating text, accessible through a simple HTTP request.

The primary goal of this project is to create a scalable and efficient translation service that can fully leverage CPU and GPU resources for optimal performance.

## Features

### Multilingual Translation with M2M100
This service leverages the state-of-the-art `M2M100` translation model, allowing it to provide high-quality translations among multiple languages.

### CPU and GPU Support
Built with efficiency in mind, the translation service is designed to run on both CPU and GPU environments. Whether you need to scale it on robust GPU-powered machines or deploy it in CPU-only clusters, the service maintains performance and flexibility.

- Based Image: `pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel` depends on `transformers[torch]==4.21.0`
- The GPU support has been successfully tested on AWS AMI: `Deep Learning AMI GPU PyTorch 1.11.0 (Amazon Linux 2) 20221018`

## Getting Started

### 1. Clone the Project
First, you need to clone this repository to your local environment.

```bash
git clone https://github.com/yourusername/translation-service.git
cd translation-service
```

### 2. Install Minikube and Kubectl
If you haven't installed Minikube and Kubectl, you can run the scripts `bin/minikube/kubectl_install.sh` and `bin/minikube/minikube_install.sh` for installation.

```bash
# Install minikube's dependency module `kubectl`
sh bin/minikube/kubectl_install.sh
# Install minikube
sh bin/minikube/minikube_install.sh
```

### 3. Deploy to Kubernetes
Run the following command to deploy the service to your Kubernetes cluster.

#### 3.1. CUDA (Optional, based on the environment)

If you're env support cuda, please unmark lines below (`k8s/deployment.yaml`22:24).
```yaml
    spec:
      containers:
      - name: translation
        image: ${REGISTRY_CLUSTER_IP}/translate_service:latest
        ports:
        - containerPort: 9527
        # resources: # Minikube when using the Docker driver doesn't support GPU access
        #   limits:
        #     nvidia.com/gpu: 1
```

Run the script, it will build the docker image, push it to local registry, and deploy it to minikube:
```bash
sh bin/minikube_build_and_deploy.sh
```

### 3. Deploy to local container (Optional)
If you want to deploy local without minikube, you can build and run by docker:
```bash
docker build -t translate_service:latest -f Dockerfile .
docker run -p 9527:9527 translate_service:latest
```
or if you can use `make` command:
```bash
make docker-build
make docker-run
```


### 4. Test the Service
Once the service is deployed, you can test it using the following curl command:

```bash
curl --location --request POST 'http://127.0.0.1:9527/translation' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": {
        "fromLang": "en",
        "records": [
            {
                "id": "123",
                "text": "Life is like a box of chocolates."
            }
        ],
        "toLang": "ja"
    }
}'
```

You should see the following response:

```json
{
   "result":[
      {
         "id":"123",
         "text":"人生はチョコレートの箱のようなものだ。"
      }
   ]
}
```

Or, you could see the document at `http://localhost:9527/docs`

### 5. Clean up (Optional)
If you want to delete your local deployment, you can run:

```bash
kubectl delete -f k8s/deployment.yaml
```

## Project Structure

```bash
.
├── Dockerfile                     
├── Makefile                       # Makefile for automating common tasks
├── README.md                      
├── app                            # Main application code
│   ├── endpoints                  # Endpoint definitions for the API
│   │   └── translation.py
│   ├── example                    # Example scripts or usage supplied by G123
│   │   ├── README.md
│   │   └── translation_example.py
│   ├── main.py                    # Main entry point for the application
│   ├── models                     # Data models used by the application
│   │   └── translation.py
│   ├── requirements.txt           # Required dependencies
│   └── utils                      # Utility functions and classes
│       ├── exception_handler.py   # Exception handling logic
│       └── load_model.py          # Model loading functions
├── bin                            # Shell scripts
│   ├── entrypoint.sh              # Entry point for the Docker container
│   ├── minikube                   # Scripts related to Minikube
│   │   ├── kubectl_install.sh
│   │   └── minikube_install.sh
│   └── minikube_build_and_deploy.sh # Script to build and deploy to Minikube
├── k8s                            # Kubernetes deployment files
│   └── deployment.yaml
├── pyproject.toml                 # Linter's configuration
└── swagger.yaml                   # Swagger definition for the API

```
