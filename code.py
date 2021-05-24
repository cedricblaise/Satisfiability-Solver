from sympy import *

def main():
    formula = input("Please enter a propositional formula: \n")
    cnf = to_cnf(formula)
    print(cnf)

if __name__ == "__main__":
    main()