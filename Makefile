
venv:
	virtualenv --python=python3 venv

clean:
	rm -rf venv

develop: venv
	. venv/bin/activate; \
	python setup.py develop; \
	pip install mypy-lang; \
    pip install -r requirements.txt	

start-redis:
	redis-server

install: develop

nopyc:
	find . -name '*.pyc' | xargs rm -f || true

