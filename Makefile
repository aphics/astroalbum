run-local:
	python manage.py runserver --settings=settings.local

migrate-local:
	python manage.py migrate --settings=settings.local

makemigrations-local:
	python manage.py makemigrations --settings=settings.local

shell_plus-local:
	python manage.py shell_plus --settings=settings.local --ipython

test-local:
	python manage.py test --settings=settings.local -v 3

run-prod:
	python manage.py runserver 0.0.0.0:8000 --settings=settings.prod

migrate-prod:
	python manage.py migrate --settings=settings.prod

makemigrations-prod:
	python manage.py makemigrations --settings=settings.prod

shell_plus-prod:
	python manage.py shell_plus --settings=settings.prod --ipython

test-prod:
	python manage.py test --settings=settings.prod -v 3

collectstatic:
	python manage.py collectstatic --settings=settings.prod
