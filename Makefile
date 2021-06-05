COMPILE_FLAGS=-b -m -n
PYTHON_HOME=/usr/local/opt/python@3.8
DEPLOY_DIR=${HOME}/Sites/reversi

build:    bedlam.py board.py eval_functions.py reversi.py
	transcrypt $(COMPILE_FLAGS) reversi.py

clean:
	rm -rf __target__
	rm -rf build

deploy: build index.html LICENSE
	cp -rf __target__/ build/
	cp index.html $(DEPLOY_DIR)
	cp -r build $(DEPLOY_DIR)
	cp LICENSE $(DEPLOY_DIR)
	cp *.png $(DEPLOY_DIR)
	cp style.css $(DEPLOY_DIR)

setup:
	virtualenv venv --python=${PYTHON_HOME}/bin/python3
	venv/bin/python -m pip install transcrypt mypy
	echo "Enter virtual environment with:  . venv/bin/activate"
