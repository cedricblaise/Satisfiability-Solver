from sympy import *

def main():
    formula = input('Please enter a propositional formula: \n')
    cnf = to_cnf(formula)
    print(cnf)

''' Determines whether a horn formula is satisfiable or not.

    arguments:
    formula -- a horn formula enocoded as a list of lists
'''
def is_satisfiable(formula):
    # mark all occurrences of T in formula
    marked = get_literals(formula)

    # while all the negative literals are marked and the positive literal is not marked do
    while (clause := find_clause(formula, marked)) is not None:
        literal = clause[0]
        # if there are no positive literals in the clause return unsatisfiable
        if len(literal) > 1: 
            return False
        # else mark the positive literal
        else:
            marked[literal] = True

    return True

''' Returns a clause where all the negative literals are marked and the positive one is not, or None
    if there are none.

    arguments:
    formula -- a horn formula enocoded as a list of lists
    marked -- dictionary containing whether or not a literal is marked
'''
def find_clause(formula, marked):
    for clause in formula:
        if all_marked(clause, marked):
            return clause
             
    return None

def all_marked(clause, marked):
    for literal in clause:
        # check if negative literal is marked
        if len(literal) > 1 and marked[literal[1]] is False: 
            return False
        # check if positive literal isn't marked already
        elif len(literal) == 1 and marked[literal] is True: 
            return False   

    return True

''' Returns a dictionary of all literals mapped to false.
    
    arguments:
    formula -- a formula encoded as a list of lists
'''
def get_literals(formula):
    literals = {}

    for clause in formula:
        for literal in clause:
            if len(literal) > 1: literal = literal[1]  # convert negative literal to a positive one
            literals[literal] = False

    return literals


if __name__ == "__main__":
    main()