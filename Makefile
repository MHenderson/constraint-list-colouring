png: png/petersen-node.png

png/petersen-node.png: src/petersen-node.py
	poetry run python $<

install:
	poetry install

