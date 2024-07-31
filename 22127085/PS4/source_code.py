import argparse
from typing import List, Tuple, Set


class Clause:
    def __init__(self, literals: Set[str]):
        self.literals = literals

    @staticmethod
    def parse(clause_str: str) -> 'Clause':
        """Parse a clause string into a Clause object."""
        literals = set(clause_str.strip().split(' OR '))
        return Clause(literals)

    def negate(self) -> 'Clause':
        """Negate the clause."""
        return Clause({self.negate_literal(literal) for literal in self.literals})

    @staticmethod
    def negate_literal(literal: str) -> str:
        """Negate a single literal."""
        return literal[1:] if literal.startswith('-') else '-' + literal

    def resolve(self, other: 'Clause') -> List['Clause']:
        """Resolve this clause with another clause."""
        resolvents = []
        for literal in self.literals:
            negated_literal = self.negate_literal(literal)
            if negated_literal in other.literals:
                new_literals = (
                    self.literals - {literal}) | (other.literals - {negated_literal})
                new_clause = Clause(new_literals)
                if not new_clause.contains_tautology():
                    resolvents.append(new_clause)
        return resolvents

    def contains_tautology(self) -> bool:
        """Check if the clause contains a tautology."""
        for literal in self.literals:
            if self.negate_literal(literal) in self.literals:
                return True
        return False

    def __str__(self) -> str:
        return ' OR '.join(sorted(self.literals)) if self.literals else '{}'

    def __eq__(self, other) -> bool:
        return self.literals == other.literals

    def __hash__(self):
        return hash(frozenset(self.literals))


class KnowledgeBase:
    def __init__(self):
        self.clauses = []

    def add_clause(self, clause: Clause):
        """Add a clause to the knowledge base."""
        self.clauses.append(clause)

    def resolve_all(self, alpha: Clause) -> Tuple[List[List[Clause]], bool]:
        """Perform resolution to check if KB entails alpha."""
        negated_alpha = alpha.negate()
        self.add_clause(negated_alpha)

        new_clauses = []
        all_clauses = self.clauses.copy()  # Using a list to maintain order
        all_steps = []

        while True:
            # Generate all pairs of clauses
            pairs = [(ci, cj) for i, ci in enumerate(all_clauses)
                     for j, cj in enumerate(all_clauses) if i < j]
            step_clauses = []

            for (clause1, clause2) in pairs:
                resolvents = clause1.resolve(clause2)
                for resolvent in resolvents:
                    if not resolvent.literals:  # Empty clause
                        step_clauses.append(resolvent)
                        all_steps.append(list(step_clauses))
                        return all_steps, True
                    if resolvent not in all_clauses and resolvent not in step_clauses:
                        step_clauses.append(resolvent)

            if not step_clauses:
                return all_steps, False

            # Sorting step_clauses to maintain order for consistency
            step_clauses.sort(key=lambda c: sorted(c.literals))
            all_steps.append(list(step_clauses))
            all_clauses.extend(step_clauses)


def parse_input(file_path: str) -> Tuple[Clause, List[Clause]]:
    """Parse the input file into alpha and KB."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        alpha = Clause.parse(lines[0].strip())
        n = int(lines[1].strip())
        kb = [Clause.parse(lines[i + 2].strip()) for i in range(n)]
    return alpha, kb


def format_output(all_steps: List[List[Clause]], entails: bool) -> str:
    """Format the output data."""
    output_lines = []
    for step in all_steps:
        unique_clauses = set(step)  # Remove duplicate clauses
        output_lines.append(str(len(unique_clauses)))
        for clause in sorted(unique_clauses, key=lambda c: sorted(c.literals)):
            output_lines.append(str(clause))
    output_lines.append("YES" if entails else "NO")
    return '\n'.join(output_lines)


def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description='PL Resolution to check if KB entails alpha.')

    # Add input and output file arguments with -i and -o flags
    parser.add_argument('-i', '--input_file', type=str,
                        required=True, help='Path to the input file')
    parser.add_argument('-o', '--output_file', type=str,
                        required=True, help='Path to the output file')

    # Parse command line arguments
    args = parser.parse_args()

    # Read the input file and parse alpha and KB
    alpha, clauses = parse_input(args.input_file)

    # Initialize the knowledge base
    kb = KnowledgeBase()
    for clause in clauses:
        kb.add_clause(clause)

    # Perform resolution
    all_steps, entails = kb.resolve_all(alpha)

    # Format output
    output = format_output(all_steps, entails)

    # Write to the output file
    with open(args.output_file, 'w') as file:
        file.write(output)

    # Print the output to console
    print(output)


if __name__ == "__main__":
    main()
