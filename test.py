from sympy.logic.boolalg import to_cnf

def sat(prop_formula):

    #Turn prop_formula into CNF
    cnf = str(to_cnf(prop_formula))

    print(cnf)

    #list of clauses
    clauses = cnf.strip().split('&')

    #get rid of leading and trailing whitespaces in clauses
    clauses = [clause.strip() for clause in clauses]
    print(clauses)

    #get rid of parantheses in each clauses
    clauses = [clause.strip('()') for clause in clauses]
    print(clauses)

    #turn each clause into a list of literals
    clauses_list = []

    for clause in clauses:
        literals = clause.split('|')

        #get rid of leading and trailing whitespaces in each literal
        literals = [literal.strip() for literal in literals]
        clauses_list.append(literals)

    print(clauses_list)

    #below is the horn formula checker
    #clauses_list is a list of lists, where each list is a list of literals in the clause
    #check if each clause has at most one literal
    #clauses are ordered by positive literals being at the beginning
    for clause in clauses_list:
        if len(clause) == 1:
            continue

        #if there is more than one literal in the claues, return False
        #positive literals are of length 1 (p), negative literals are of length 2 (~p)
        #since clause is ordered by positive literals to negative, we check if the second index is positive
        elif len(clause[1]) == 1:
            return False #this implies that clause has more than 1 positive literal

    return clauses_list

sat('(p >> q) & ((q&s) >> r )')
