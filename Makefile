COMPILE_FLAGS=-b -m -n
DEPLOY_DIR=${HOME}/Sites/transcrypt_reversi

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

setup:
	virtualenv venv
	venv/bin/python -m pip install transcrypt
	echo "Enter virtual environment with:  . venv/bin/activate"
