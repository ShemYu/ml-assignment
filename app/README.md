# Project Structure

This document provides an overview of the project structure. The project is designed to implement a translation inference service that runs on Kubernetes and provides a RESTful API.

Below is a quick description of what each file or directory in the project contains:

- `Dockerfile`: This is a script that contains commands to assemble an image for the application. It allows us to package our application and its dependencies into a Docker container.

- `Makefile`: This file contains a set of directives used by the make build automation tool to build the project. It includes commands for various project tasks like building the Docker image and running the container.

- `README.md`: This is a general introduction document for the project. It provides a description of the project, instructions on how to run it, and any other relevant information.

- `app/`: This directory contains the core application code for our service. 
    - `endpoints/api.py`: This file contains the API endpoints for our service, where the core business logic resides.
    - `example/translation_example.py`: An example script demonstrating how the translation model works.
    - `main.py`: The entry point for our application. This file bootstraps the application and gets it running.
    - `models/`: This directory is meant to contain the data models used in our service.
    - `requirements.txt`: This file lists the Python dependencies required by the project.

- `k8s/deployment.yaml`: This YAML file contains Kubernetes deployment configuration for our application.

- `swagger.yaml`: This file contains the API documentation for our service in Swagger format, which is a specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services.

Please refer to each individual file or directory for more detailed documentation if necessary.