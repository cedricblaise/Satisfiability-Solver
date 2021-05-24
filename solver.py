from sympy.logic.boolalg import is_cnf, to_cnf

def main():
    formula = input('Please enter a propositional formula: \n')
    horn = get_clauses(formula)
    if isinstance(horn, list):
        assignments = is_satisfiable(horn)
        if isinstance(assignments, dict): 
            print('Formula is satisfiable. \n')
            # get the truth assignments
            true_list = []
            for var, marked in assignments.items():
                if marked is True: true_list.append(var)    # variable was marked so it must be true
            print('The marking algorithm terminates after', len(true_list), 'iterations.')
            if len(true_list) > 0:
                print('These variables must be assigned to true for the formula to be satisfied:', 
                        ', '.join(true_list) + '.') 
                print('The rest of the variables can be assigned to either true or false.')
            else:
                print('None of the variables are required to be assigned to true for the formula to be satisfied.')
                print('Assigning all of the variables to false will satisfy the formula, for example.')
        else:
            print('Formula is not satisfiable')
    else: 
        print('Not a Horn Formula, so we cannot determine satisfiability.')

''' Converts formula to a CNF and returns a list of its clauses if it is a Horn formula.

    arguments:
    prop_formula -- a string propositional formula
'''
def get_clauses(prop_formula):

    # Turn prop_formula into CNF
    cnf = str(to_cnf(prop_formula))
    if is_cnf(prop_formula):
        print('This is already a CNF Formula') 
    else:
        print('CNF Equivalent Formula:', cnf)

    # list of clauses
    clauses = cnf.strip().split('&')

    # get rid of leading and trailing whitespaces in clauses
    clauses = [clause.strip() for clause in clauses]
    

    # get rid of parantheses in each clauses
    clauses = [clause.strip('()') for clause in clauses]

    # turn each clause into a list of literals
    clauses_list = []

    for clause in clauses:
        literals = clause.split('|')

        # get rid of leading and trailing whitespaces in each literal
        literals = [literal.strip() for literal in literals]
        clauses_list.append(literals)

    # below is the horn formula checker
    # clauses_list is a list of lists, where each list is a list of literals in the clause
    # check if each clause has at most one literal
    # clauses are ordered by positive literals being at the beginning
    for clause in clauses_list:
        if len(clause) == 1:
            continue

        # if there is more than one literal in the claues, return False
        # positive literals are of length 1 (p), negative literals are of length 2 (~p)
        # since clause is ordered by positive literals to negative, we check if the second index is positive
        elif len(clause[1]) == 1:
            return False # this implies that clause has more than 1 positive literal so it's not a Horn Formula

    return clauses_list

''' Determines whether a horn formula is satisfiable or not.

    arguments:
    formula -- a horn formula enocoded as a list of lists
'''
def is_satisfiable(formula):
    # mark all occurrences of T in formula
    marked = get_variables(formula)

    # while all the negative literals are marked and the positive literal is not marked do
    while (clause := find_clause(formula, marked)) is not None:
        # print('Yuh')
        literal = clause[0]
        # if there are no positive literals in the clause return unsatisfiable
        if len(literal) > 1: 
            return False
        # else mark the positive literal
        else:
            marked[literal] = True

    return marked

''' Returns a clause where all the negative literals are marked and the positive one is not, or None
    if there are none.

    arguments:
    formula -- a horn formula enocoded as a list of lists
    marked -- dictionary containing whether or not a variable is marked
'''
def find_clause(formula, marked):
    for clause in formula:
        if all_marked(clause, marked):
            return clause
             
    return None

''' Returns a clause where all the negative literals are marked and the positive one is not, or None
    if there are none.

    arguments:
    clause -- list of literals
    marked -- dictionary containing whether or not a variable is marked
'''
def all_marked(clause, marked):
    for literal in clause:
        # check if negative literal is marked
        if len(literal) > 1 and marked[literal[1]] is False: 
            return False
        # check if positive literal isn't marked already
        elif len(literal) == 1 and marked[literal] is True: 
            return False   

    return True

''' Returns a dictionary of all variables mapped to false.
    
    arguments:
    formula -- a formula encoded as a list of lists
'''
def get_variables(formula):
    variables = {}

    for clause in formula:
        for literal in clause:
            if len(literal) > 1: literal = literal[1]  # convert negative literal to a positive one
            variables[literal] = False

    return variables


if __name__ == '__main__':
    main()