SHELL = /bin/sh

# Python variables
python = python3
venv := $(shell cat .venv-path 2>/dev/null || echo ~/.venv/dev/$$(date +'%Y%m%dT%H%M%S'))
requirements = requirements.txt
vpython = . $(venv)/bin/activate && python3

# paths
src = $(shell find src -mindepth 1 -maxdepth 1 -type d -not -name '*.*')

# install Python packages in a virtual environment
.PHONY : venv
venv : $(venv)/installed.txt

# install Python packages in a virtual environment
$(venv)/installed.txt: $(requirements)
ifeq (,$(wildcard $(venv)))
	$(python) -m venv $(venv)
	echo $(venv) > .venv-path
endif
	$(vpython) -m pip install --upgrade --requirement $<
	$(vpython) -m pip install --editable .
	cp $< $@

# delete all files except those that people normally don’t want to recompile
.PHONY : mostlyclean
mostlyclean :
	rm -f -r docs/source/package
	rm -f -r docs/build
	rm -f -r src/*.egg-info

# delete all files that are normally created by running make
.PHONY : clean
clean : mostlyclean
	rm -f -r $(venv)

# generate documentation
.PHONY : html
html : venv
	rm -rf docs/source/package
	rm -rf docs/build
	. $(venv)/bin/activate && sphinx-apidoc $(src) --output-dir docs/source/package --force --no-toc --module-first --separate --maxdepth 1
	. $(venv)/bin/activate && make html --directory docs

.PHONY : dist
dist : venv
	$(vpython) -m build

.PHONY : upload
upload : dist
	$(vpython) -m twine upload $(shell find dist -name "*.tar.gz" -o -name "*-none-any.whl") --skip-existing

.PHONY : check
check : venv
	@$(vpython) --version
	@$(vpython) tests/run.py
	@$(vpython) -m pylint $(src) tests/run.py --rcfile .pylintrc || true
	@$(vpython) -m flake8 $(src) tests/run.py || true
