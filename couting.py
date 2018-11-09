import operator
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
import crayons

KEYS = {
    'B': 'En blanco',
    'N': 'Votos nulos'
}


class Counting(object):
    def __init__(self, file):
        self.datafile = Path(file)
        votes, self.num_votes, keys = defaultdict(int), 0, self.get_keys()
        with open(self.datafile) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                for choice in re.split(r'\s+', line):
                    if choice not in keys:
                        sys.exit(crayons.red(
                            (f'Clave <{choice}> no encontrada en el fichero '
                             'de claves!!'), bold=True))
                    votes[choice] += 1
                self.num_votes += 1
        self.votes = {v: votes[k] for k, v in keys.items()}

    def get_keys(self):
        self.keyfile = self.datafile.parent / (self.datafile.stem + '.key')
        self.choices, code = {}, 1
        with open(self.keyfile) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                self.choices[str(code)] = line
                code += 1
        return {**self.choices, **KEYS}

    def __str__(self):
        buf = []
        for k, v in sorted(
                self.votes.items(), key=operator.itemgetter(1), reverse=True):
            buf.append(f'{k}: {v}')
        buf.append(crayons.white(f'{os.linesep}TOTAL VOTOS: ', bold=True) +
                   crayons.cyan(f'{self.num_votes}', bold=True))
        return os.linesep.join(buf)


if __name__ == "__main__":
    c = Counting(sys.argv[1])
    print(c)
