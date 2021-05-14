migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

serve:
	python manage.py runserver

superuser:
	python manage.py createsuperuser

shell_plus:
	python manage.py shell_plus