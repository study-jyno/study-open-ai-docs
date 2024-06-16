.PHONY: lint
lint:
	@poetry run ruff check . --fix

.PHONY: format
format:
	@poetry run ruff format .


.PHONY: shell
shell:
	@poetry run ipython