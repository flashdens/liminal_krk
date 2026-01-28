dev:
	poetry run flask --app app run --debug --port 8000
prod:
	poetry run waitress-serve --call 'app:create_app'
