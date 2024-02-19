all:
	@echo installing package in editable mode ...
	@pip install -e . > /dev/null
	@echo finished installing package

	@echo installing documentation requirements ...
	@pip install -r ./documentation/requirements.txt > /dev/null
	@echo finished installing documentation requirements.

	@docop --help > ./documentation/docs/clihelp.txt
	@docop run --help > ./documentation/docs/runhelp.txt
	@echo created docop usage help as files for documentation.

	@echo building documentation ...
	@mkdocs build
	@echo documentation built.

	@cat ./documentation/docs/example-config.yaml | grep -v "\-\-8<\-\-" > docop/config.yaml.in
	@echo created config.yaml.in template.

	@echo building the distribution
	@python3 -m build

	@echo all done.
