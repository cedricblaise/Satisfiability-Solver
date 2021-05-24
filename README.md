# SAT Solver 
## Vincent Dong and Cedric Blaise

To run our solver, first install the SymPy package:

```terminal
pip3 install sympy
```

cd into the project directory and in the command line write:

```terminal
python3 solver.py
```

The program will prompt the user to enter a propositional formula.
Use '&' for and, '|' for or, and '>>' for implication. For example:

(p >> q) & ((q & s) >> r) is a valid user input for a propositional formula.

The program checks whether the propositional formula has an equivalent horn formula,
and runs the marking algorithm on the horn formula. Our program returns if the propositional
formula is satisfiable or unsatisfiable, and if satisfiable our program returns an assignment
to the variables.
