.PHONY: init clean celery assets devserver db

init:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -delete

celery:
	python runcelery.py -A app.tasks worker

assets:
	cd app/static && bower install && cd ../..

devserver:
	python manage.py run --host 0.0.0.0
