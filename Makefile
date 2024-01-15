clean:
	rm -rf ./venv

build:
	py -m venv venv
	./venv/Scripts/pip install -r requirements.txt


run:
	./venv/Scripts/python src/main.py

	