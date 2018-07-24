import hashlib
import csv
import json

import io

level0 = {
    'formatVersion': 3,
    'id': '',
    'ideas': {},
    'title': 'Root'
}

truc = {
          'title': 'a',
          'id': ''
}


def find_levels(rows):
    last_level = 0
    leveled = []
    for row in rows:
        if len([a for a in row if a != '']) > 1:
            raise ValueError('There is more than one value per row.')
        for n, r in enumerate(row):
            if r:
                if n > last_level + 1:
                    raise ValueError('The identation increments more than once at a time')
                leveled.append((n, r))
                last_level = n
    return leveled


def from_indented_csv_to_json(rows):
    length = 0
    for r in rows:
        if length < len(r):
            length = len(r)

    leveled = find_levels(rows)

    out = ''
    for n, entry in enumerate(leveled):
        indent, title = entry
        previous = -1
        next = -1
        if n > 0:
            previous = leveled[n - 1][0]
        if n < len(leveled) - 1:
            next = leveled[n + 1][0]

        # beginning
        if previous == -1:
            out += '{' + '\t' * indent + '"' + title + '"'

        # end
        elif next == -1:
            if indent > previous:
                out += ': {'
            out += '\n' + '\t' * indent + '"' + title + '": {}'
            for i in reversed(range(indent)):
                out += '\n' + '\t' * i + '}'
            # last closing braces
            out += '\n}'

        # in between
        else:
            if indent > previous:
                out += ': {'

            out += '\n' + '\t' * indent + f'"{title}"'

            if next < indent:
                out += ': {}'
                for i in range(indent - next):
                    out += '\n' + '\t' * (indent - i) + '}'
                out += ','
            elif next == indent:
                out += ': {},'
    return out


def tree_from_csv(input_file):
    with open(input_file) as f:
        reader = csv.reader(f, delimiter='\t')
        lines = list(reader)
    json_str = from_indented_csv_to_json(lines)

    structure = json.load(io.StringIO(json_str))
    return structure


def create_mindmup(title, csv_file):
    '''
    :return:
    '''
    root = {
        'formatVersion': 3,
        'id': '',
        'ideas': {},
        'title': title
    }
    csv_tree = tree_from_csv(csv_file)


json_structure = tree_from_csv('locations.tsv')
print(json_structure)
