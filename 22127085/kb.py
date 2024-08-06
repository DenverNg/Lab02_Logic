class Literal:
    def __init__(self, name, negated=False):
        self.name = name
        self.negated = negated

    def __neg__(self):
        return Literal(self.name, not self.negated)

    def __eq__(self, other):
        return self.name == other.name and self.negated == other.negated
    
    def __hash__(self):
        return hash((self.name, self.negated))

    def __repr__(self):
        return f"-{self.name}" if self.negated else self.name

class Clause:
    def __init__(self, literals=None):
        if literals is None:
            literals = set()
        self.literals = set(literals)
        # sort alphabetically
    def sort_literals(self):
        self.literals = sorted(self.literals, key=lambda x: x.name)

    
    def add_literal(self, literal):
        self.literals.add(literal)

    def is_empty(self):
        return len(self.literals) == 0

    def is_tautology(self):
        for literal in self.literals:
            if -literal in self.literals:
                return True
        return False

    def __eq__(self, other):
        return self.literals == other.literals
    
    def __repr__(self):
        result = ""
        if len(self.literals) == 0:
            return "{}"
        self.literals = sorted(self.literals, key=lambda x: x.name)
        for i, literal in enumerate(self.literals):
            result += literal.__repr__()
            if i < len(self.literals) - 1:
                    result += " OR "
        return result

class PLResolution:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def resolve(self, clause1, clause2):
        for lit1 in clause1.literals:
            for lit2 in clause2.literals:
                if lit1 == -lit2:  
                    new_literals = (set(clause1.literals) | set(clause2.literals)) - {lit1, lit2}
                    return Clause(new_literals)
        return None

    def pl_resolution(self):
        
        result = []
        while True:
            new = []
            n = len(self.clauses)
            for i in range(n):
                for j in range(i + 1, n):
                    resolvent = self.resolve(self.clauses[i], self.clauses[j])
                    if resolvent is not None:
                        if resolvent.is_empty():
                            
                            new.append(frozenset(resolvent.literals))
                            result.append([Clause(set(literals)) for literals in new])
                            
                            return result, True  
                        if resolvent.is_tautology():
                            continue
                        if resolvent.literals in {frozenset(clause.literals) for clause in self.clauses}:
                            continue
                        if resolvent.literals in new:
                            continue  
                        new.append(frozenset(resolvent.literals))
            result.append([Clause(set(literals)) for literals in new])
            
            if set(new).issubset({frozenset(clause.literals) for clause in self.clauses}):
                return result, False
            else:
                for clause in new:
                    self.add_clause(Clause(clause))
                
            
            

    def __repr__(self):
        
        return "asdu"
def input_clauses(s):
    clause = Clause()
    literals = s.strip().split(" OR ")
    for literal in literals:
        if literal[0] == "-":
            clause.add_literal(Literal(literal[1:], True))
        else:
            clause.add_literal(Literal(literal))
    return clause

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        alpha = input_clauses(lines[0].strip())

        N = int(lines[1])
        clauses = []
        for i in range(2, N + 2):
            clause = input_clauses(lines[i].strip())
            
            clauses.append(clause)
    return alpha, clauses

def write_output(filename, satisfiable, result):
    with open(filename, 'w') as f:
        for iteration in result:
            f.write(str(len(iteration)))
            f.write("\n")
            for clause in iteration:
                f.write(f"{clause}\n")
        if satisfiable:
            f.write("YES\n")
        else:
            f.write("NO\n")
        
            

if __name__ == "__main__":
    for i in range(1, 8):
        alpha, clauses = read_input(f"Input/input0{i}.txt")
        pl = PLResolution()
        for clause in clauses:
            pl.add_clause(clause)
        for literal in alpha.literals:
            pl.add_clause(Clause({-literal}))
    
        result, satisfiable = pl.pl_resolution()
        write_output(f"output0{i}.txt", satisfiable, result)
    
