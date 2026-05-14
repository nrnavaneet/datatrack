.PHONY: install-editable test lint clean

install-editable:
	pip install -r requirements.txt
	pip install -e .

test:
	python3 -m pytest tests/ -q

lint:
	pre-commit run --all-files

clean:
	rm -rf build dist *.egg-info .pytest_cache
