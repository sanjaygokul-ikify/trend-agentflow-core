build:
	poetry build

develop:
	poetry install --dev

test:
	pytest --cov=agentflow

lint:
	pylint agentflow

format:
	python -m black agentflow

docker:
	docker-compose build