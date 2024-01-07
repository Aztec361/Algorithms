import random

class ThreeSAT:
    def __init__(self, num_clauses, num_variables):
        self.clauses = []
        self.var_assignments = []
        self.num_clauses = num_clauses
        self.num_variables = num_variables

    class Variable:
        def __init__(self, var_id):
            self.id = abs(var_id)
            self.negated = var_id < 0

        def get_boolean(self, assignment):
            if assignment == 1 and not self.negated:
                return True
            elif assignment == 1 and self.negated:
                return False
            elif assignment == -1 and not self.negated:
                return False
            else:  # assignment == -1 and self.negated
                return True

    class Clause:
        def __init__(self):
            self.variables = []
            self.state = []

        def add_to_clause(self, var):
            self.variables.append(var)

        def set_variables(self, var_assignments):
            self.state = [var.get_boolean(var_assignments[var.id - 1]) for var in self.variables]

        def is_satisfied(self):
            return any(self.state)

    def parse_input(self):
        for _ in range(self.num_clauses):
            clause_input = input().split()
            var1 = self.Variable(int(clause_input[0]))
            var2 = self.Variable(int(clause_input[1]))
            var3 = self.Variable(int(clause_input[2]))

            clause = self.Clause()
            clause.add_to_clause(var1)
            clause.add_to_clause(var2)
            clause.add_to_clause(var3)

            self.clauses.append(clause)

    def num_clauses_satisfied(self):
        return sum(1 for clause in self.clauses if clause.is_satisfied())

    def assign_literals(self):
        values = [-1, 1]
        self.var_assignments = [random.choice(values) for _ in range(self.num_variables)]

    def set_clauses(self):
        for clause in self.clauses:
            clause.set_variables(self.var_assignments)

    def run_algorithm(self):
        while True:
            self.assign_literals()
            self.set_clauses()
            num_satisfied = self.num_clauses_satisfied()
            if num_satisfied >= (7 / 8) * self.num_clauses:
                break

        print(" ".join(map(str, self.var_assignments)))

if __name__ == "__main__":
    num_variables = int(input())
    num_clauses = int(input())

    three_sat = ThreeSAT(num_clauses, num_variables)
    three_sat.parse_input()
    three_sat.run_algorithm()
