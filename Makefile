.PHONY: validate compile

validate:
	python3 scripts/validate_repository.py

compile:
	./scripts/compile_all.sh
