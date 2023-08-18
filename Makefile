COMPILE_FLAGS=-b -m -n
PYTHON_HOME=/usr/local
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
	cp *.png $(DEPLOY_DIR)
	cp *.svg $(DEPLOY_DIR)
	cp *.ico $(DEPLOY_DIR)
	cp style.css $(DEPLOY_DIR)
	cp sw.js $(DEPLOY_DIR)
	cp site.webmanifest $(DEPLOY_DIR)
	cp LICENSE $(DEPLOY_DIR)

zip: build
	cp -rf __target__/ build/
	zip -r reversi.zip *.html *.png *.svg *.ico style.css sw.js site.webmanifest build LICENSE

setup:
	virtualenv venv --python=${PYTHON_HOME}/bin/python3
	venv/bin/python -m pip install transcrypt mypy
	echo "Enter virtual environment with:  . venv/bin/activate"
