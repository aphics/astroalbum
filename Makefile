run:
	python manage.py runserver --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

run-prod:
	python manage.py runserver --settings=settings.prod

shell_plus:
	python manage.py shell_plus --settings=settings.local --ipython

test:
	python manage.py test --settings=settings.local -v 3