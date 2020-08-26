PYTHON?=$(shell [ -f venv/bin/python ] && echo 'venv/bin/python' ||  echo 'python')

test:
	 xvfb-run -a -e xvfb.log ${PYTHON} -m unittest discover -s "tests/" -p "test_*.py"

venv: requirements.txt
	python3 -m venv venv
	venv/bin/python -m pip install -Ur requirements.txt
