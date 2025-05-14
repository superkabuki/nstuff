PY3 = python3
PIP3 = pip3
PYPY3 = pypy3

default: install

clean:
	rm -f dist/*
	rm -rf build/*

pypy3: clean
	$(PYPY3) setup.py sdist bdist_wheel
	$(PYPY3) setup.py install --user	

install: clean pkg
	$(PY3)  setup.py install --user

pkg: clean
	$(PY3) setup.py sdist bdist_wheel
	
upload: clean pkg	
	twine upload dist/*



