dev:
	poetry run flask --app app run --debug
prod:
	poetry run waitress-serve --call 'app:create_app'
