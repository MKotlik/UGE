test: script.mdl lex.py mainMDL.py matrix.py mdl.py display.py draw.py matrixOps.py transformOps.py yacc.py
	python mainMDL.py script.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
