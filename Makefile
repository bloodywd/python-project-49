# Makefile

brain-games:
	poetry run brain-games
install: 
	poetry install
build: 
	poetry build
publish: 
	poetry publish --dry-run
package-install: 
	python3 -m pip install --user dist/*.whl
