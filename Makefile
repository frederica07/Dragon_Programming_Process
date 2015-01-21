PYTHON		= python
PYCS		= $(shell find . -name "*.pyc")
PYOPENGL	= PyOpenGL-3.0.2
OPENGL		= OpenGL
TARGET		= dragon.py
BASEPKG		= jp.ac.kyoto_su.aokilab
PACKAGE		= dragon
NAME		= Dragon_Programming_Process

all:
	@if [ ! -e $(PYOPENGL) ] ; then unzip $(PYOPENGL).zip ; fi
	@if [ ! -e $(OPENGL) ] ; then ln -s $(PYOPENGL)/$(OPENGL) $(OPENGL) ; fi

test: all
	$(PYTHON) $(TARGET)

clean:
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	rm -f MANIFEST

wipe:
	if [ -e $(OPENGL) ] ; then rm -f $(OPENGL) ; fi
	if [ -e $(PYOPENGL) ] ; then rm -f -r $(PYOPENGL) ; fi

zip: clean
	(cd .. ; zip -r $(NAME).zip ./$(NAME)/)

sdist: clean
	find . -name ".DS_Store" -print -exec rm {} ";"
	python setup.py sdist

pydoc: clean
	(sleep 3 ; open http://localhost:9999/$(BASEPKG).$(PACKAGE).html) & pydoc -p 9999

01: all
	$(PYTHON) $(BASE)$@.py

02: all
	$(PYTHON) $(BASE)$@.py

03: all
	$(PYTHON) $(BASE)$@.py

04: all
	$(PYTHON) $(BASE)$@.py

05: all
	$(PYTHON) $(BASE)$@.py

06: all
	$(PYTHON) $(BASE)$@.py

07: all
	$(PYTHON) $(BASE)$@.py

08: all
	$(PYTHON) $(BASE)$@.py

09: all
	$(PYTHON) $(BASE)$@.py

10: all
	$(PYTHON) $(BASE)$@.py

11: all
	$(PYTHON) $(BASE)$@.py

12: all
	$(PYTHON) $(BASE)$@.py

13: all
	$(PYTHON) $(BASE)$@.py

14: all
	$(PYTHON) $(BASE)$@.py

15: all
	$(PYTHON) $(BASE)$@.py

16: all
	$(PYTHON) $(BASE)$@.py

17: all
	$(PYTHON) $(BASE)$@.py

18: all
	$(PYTHON) $(BASE)$@.py

19: all
	$(PYTHON) $(BASE)$@.py

20: all
	$(PYTHON) $(BASE)$@.py

21: all
	$(PYTHON) $(BASE)$@.py

22: all
	$(PYTHON) $(BASE)$@.py
