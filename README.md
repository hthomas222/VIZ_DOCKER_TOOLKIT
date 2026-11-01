# Viz_Docker

Viz_Docker is a Python-based toolset designed to simplify Docker container and resource management. It offers two user interfaces depending on your workflow preference: an interactive **CLI tool** featuring formatted terminal output, and a lightweight **Web UI** built with Flask for browser-based operations.

```
Plaintext

viz_docker/
├── README.md               <-- Primary Overview & Workflow Guide
├── Makefile                <-- Automation & Deployment Tasks
├── cli/
│   ├── main.py             <-- Interactive Rich CLI application
│   └── README.md           <-- CLI-specific documentation
└── web/
    ├── app.py              <-- Flask Web dashboard application
    ├── templates/          <-- HTML templates for Web UI
    └── README.md           <-- Web app installation & setup guide
```

### Local Kubernetes Deployment (Makefile)

To streamline testing and deployment inside a local Kubernetes cluster (such as Minikube), this repository includes a Makefile that automates Docker image building, cluster loading, and Kubernetes manifests deployment

#### The Makefile (Makefile)

Create a file named Makefile in the root directory:

``` Makefile
IMAGE_NAME = viz-flask-app:latest

build:
	docker build -t $(IMAGE_NAME) .
	minikube image load $(IMAGE_NAME)

deploy:
	kubectl apply -f deployment.yaml

refresh: build deploy
	kubectl rollout restart deployment/viz

url:
	minikube service viz --url
```

Available Commands

Run these commands from the root of the repository:
```
    make build

    Builds the Docker container image from your Dockerfile and loads it directly into your local Minikube cluster daemon (avoiding the need for a remote container registry).

    make deploy

    Applies your Kubernetes deployment and service configuration (deployment.yaml) to the cluster.

    make refresh

    Chains commands together: it rebuilds the image, reloads it into Minikube, applies the manifest changes, and gracefully restarts the viz deployment pods to pull your latest code changes.

    make url

    Fetches and outputs the live local browser URL for your exposed viz service.
```
