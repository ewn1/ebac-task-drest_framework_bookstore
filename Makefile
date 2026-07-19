# Infraestrutura e Banco de Dados
up:
	docker compose up -d

down:
	docker compose down

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

# Qualidade de Código e Testes
format:
	docker compose exec web black .

lint:
	docker compose exec web flake8 .

test:
	docker compose exec web python manage.py test