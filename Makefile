.PHONY: install-editable test lint clean list-docs

install-editable:
	pip install -r requirements.txt
	pip install -e .

test:
	python3 -m pytest tests/ -q

lint:
	pre-commit run --all-files

clean:
	rm -rf build dist *.egg-info .pytest_cache

list-docs:
	@echo "Markdown guides under docs/:"
	@ls -1 docs/*.md 2>/dev/null || true
