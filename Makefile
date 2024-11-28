format:
	poetry run black bin src
	poetry run flake8 src
	poetry run isort .
	@echo "formatting done!"

type-check:
	poetry run mypy src
	@echo "type-check done"

lint: format type-check
	@echo "linters done"

run:
	docker compose up --build -d

stop:
	docker compose down
