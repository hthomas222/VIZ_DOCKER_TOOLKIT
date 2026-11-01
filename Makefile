IMAGE_NAME = my-flask-app:latest

build:
	docker build -t $(IMAGE_NAME) .
	minikube image load $(IMAGE_NAME)

deploy:
	kubectl apply -f deployment.yaml

refresh: build deploy
	kubectl rollout restart deployment/viz

url:
	minikube service viz --url
