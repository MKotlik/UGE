test: script.mdl lex.py main.py matrix.py mdl.py display.py draw.py matrixOps.py transformOps.py yacc.py
	python main.py script.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
