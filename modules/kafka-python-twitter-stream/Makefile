#Makefile -> Below sample doc from - https://ljvmiranda921.github.io/notebook/2021/05/12/how-to-manage-python-envs/
venv:
	python3 -m venv myEnv

# Separating prod and dev dependencies

requirements.txt:  venv requirements.in  ## generate requirements for release
    myEnv/bin/pip-compile -o requirements.txt requirements.in

dev:  ## creates a development environment, install deps
    myEnv/bin/pip-sync requirements.txt
    myEnv/bin/pre-commit install

requirements-prod-envName.txt:  venv requirements-prod-envName.in  ## generate requirements for release
    myEnv/bin/pip-compile -o requirements-prod-envName.txt requirements-prod-envName.in

prod: ## creates a production environment, install deps
	myEnv/bin/pip-sync requirements-prod.txt
	myEnv/bin/pre-commit install

# make run: runs a web server (maybe calling gunicorn or something)
run:
	myEnv/bin/python3 runserver.py


# make test: runs all your tests using pytest
test: dev ## Run all tests with coverage
    myEnv/bin/pytest tests --cov=src -v --cov-report=term-missing

# make clean: remove artifact files like __pycache__, .ipynb_checkpoints
clean:  ## Remove general artifact files
    find . -name '.coverage' -delete
    find . -name '*.pyc' -delete
    find . -name '*.pyo' -delete
    find . -name '.pytest_cache' -type d | xargs rm -rf
    find . -name '__pycache__' -type d | xargs rm -rf
    find . -name '.ipynb_checkpoints' -type d | xargs rm -rf

format: dev ## Scan and format all files with pre-commit
    myEnv/bin/pre-commit run --all-files