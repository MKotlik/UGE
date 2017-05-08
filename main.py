from script import run
import sys

if len(sys.argv) == 2:
    run(sys.argv[1])
elif len(sys.argv) == 1:
    run(raw_input("UGE: please enter the filename of an mdl script file: \n"))
else:
    print "UGE: too many arguments"
