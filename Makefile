test:
	@py.test -v test_getname.py
	@py.test --pep8 getname/*.py test_getname.py
