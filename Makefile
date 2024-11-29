png: png/petersen-total.png png/petersen-edge.png png/petersen-node.png

png/petersen-total.png: src/petersen-total.py
	poetry run python $<

png/petersen-edge.png: src/petersen-edge.py
	poetry run python $<

png/petersen-node.png: src/petersen-node.py
	poetry run python $<

install:
	poetry install

