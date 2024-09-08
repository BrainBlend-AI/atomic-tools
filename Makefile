.PHONY: docs

docs:
	@echo "Generating documentation..."
	@cd docs && python generate_docs.py
	@cd docs && make html SPHINXOPTS="-W --keep-going -n"
