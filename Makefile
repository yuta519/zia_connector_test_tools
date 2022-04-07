.PHONY: install run

install:
	poetry install

run:
	poetry shell
	python main.py
	exit
