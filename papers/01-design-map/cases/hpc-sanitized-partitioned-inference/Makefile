.PHONY: run test verify

run:
	python3 run_case.py --record

test:
	python3 -m unittest -v test_case.py

verify: test
	python3 run_case.py --verify
