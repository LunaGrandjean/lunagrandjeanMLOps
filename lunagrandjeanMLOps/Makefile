prepare:
	poetry install

run:
	poetry run streamlit run app.py

check:
	poetry run vulture .
	poetry run isort .
	poetry run black .
	poetry run mypy .

build:
	docker build -t {imagedocker} .

push:
	docker push {imagedocker}

deploy:
	echo "Déploiement non spécifié dans les instructions initiales"
