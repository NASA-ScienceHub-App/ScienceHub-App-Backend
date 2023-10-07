.PHONY: runserver makemigrations makemigrationapp migrate
runserver :
	python manage.py runserver
makemigrations :
	python manage.py makemigrations
# make makemigrationapp app=app
makemigrationapp :
	python manage.py makemigrations $(app)
migrate :
	python manage.py migrate