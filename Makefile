migration:
	alembic revision -m "your migration description" --autogenerate --head head

apply_migration:
	alembic upgrade head

etl:
	pipenv run python -m main.etl

webserver:
	pipenv run uvicorn main.webserver:app --reload
