migration:
	alembic revision -m "your migration description" --autogenerate --head head

apply_migration:
	alembic upgrade head

webserver:
	pipenv run uvicorn main.webserver:app --reload
