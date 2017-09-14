.PHONY: init clean celery assets devserver db test admin

init:
	conda env create -f=environment.yml

clean:
	find . -name '*.pyc' -delete

celery:
	python runcelery.py -A app.tasks worker

db:
	python manage.py db upgrade head

admin:
	python manage.py create_admin

assets:
	cd app/static && yarn install && cd ../..

devserver:
	python manage.py run --host 0.0.0.0 --port 5000

test:
	python tests.py

