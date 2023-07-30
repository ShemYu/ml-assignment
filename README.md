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

## Getting Started
The entire process has been successfully tested on AWS AMI: `Deep Learning AMI GPU PyTorch 1.11.0 (Amazon Linux 2) 20221018`, follow these steps to quickly set up and run the multilingual translation service locally:

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

```bash
sh bin/minikube_build_and_deploy.sh
```

### Test the Service
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

### Clean up
If you want to delete your local deployment, you can run:

```bash
kubectl delete -f k8s/deployment.yaml
```

## Project Structure
This project is organized with a focus on modularity and extensibility. The core of the application is contained within the app/ directory. Here's a brief overview of its structure:

```bash
.
├── Dockerfile
├── Makefile
├── README.md
├── app
│   ├── endpoints
│   │   └── translation.py
│   ├── example
│   │   ├── README.md
│   │   └── translation_example.py
│   ├── main.py
│   ├── models
│   │   └── translation.py
│   ├── requirements.txt
│   └── utils
│       ├── exception_handler.py
│       └── load_model.py
├── bin
│   ├── entrypoint.sh
│   ├── minikube
│   │   ├── kubectl_install.sh
│   │   └── minikube_install.sh
│   └── minikube_build_and_deploy.sh
├── k8s
│   └── deployment.yaml
├── pyproject.toml
└── swagger.yaml
```

### app/
- endpoints/: Contains the definitions for all the API endpoints. For example, translation-related endpoints can be found in translation.py.
- example/: Includes the example code given by assignment, such as translation_example.py.
- main.py: The entry point of the application, where the FastAPI app is instantiated and routers are included.
- models/: Houses the data models for the application, defined using Pydantic.
- utils/: Contains utility functions and classes, such as exception handling and model loading.
- requirements.txt: Lists the Python package dependencies required for the application.

The structure is designed to make it easy to add new endpoints, models, or utilities without affecting the existing system. It provides clear separation and organization, supporting both development flexibility and maintainability.

### Other Directories
- k8s/: Kubernetes deployment files.
- bin/: Contains scripts related to building and deploying the application.
- Dockerfile: Defines the Docker image for the application.
