import csv
import json
import io


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


def get_positions(level):
    outa = []
    outb = []
    side = True
    position = 1
    for l in level:
        if side:
            outa.append((str(position), l))
            side = not side
        else:
            outb.append(('-'+str(position), l))
            position += 1
            side = not side
    return outa + outb


def create_mindmup(title, csv_file):
    '''
    :return:
    '''
    output = {
        'formatVersion': 3,
        'id': 'root',
        'ideas': {},
        'title': 'None'
    }
    csv_tree = tree_from_csv(csv_file)
    roots = get_positions(csv_tree.keys())
    id = 1
    for pos, title in roots:
        level = {
            'title': title,
            'id': id,
            'ideas': {}
        }
        output['ideas'][pos] = level
        id += 1

        roots1 = get_positions(csv_tree[title].keys())
        for pos1, title1 in roots1:
            level1 = {
                'title': title1,
                'id': id,
                'ideas': {}
            }
            output['ideas'][pos]['ideas'][pos1] = level1
            id += 1

            roots2 = get_positions(csv_tree[title][title1].keys())
            for pos2, title2 in roots2:
                level2 = {
                    'title': title2,
                    'id': id,
                    'ideas': {}
                }
                output['ideas'][pos]['ideas'][pos1]['ideas'][pos2] = level2
                id += 1

                roots3 = get_positions(csv_tree[title][title1][title2].keys())
                for pos3, title3 in roots3:
                    level3 = {
                        'title': title3,
                        'id': id,
                        'ideas': {}
                    }
                    output['ideas'][pos]['ideas'][pos1]['ideas'][pos2]['ideas'][pos3] = level3
                    id += 1

    return output


mindmup = create_mindmup('PublisherLocations', 'locations.tsv')
with open('logs/locations.mup', 'w') as f:
    f.write(json.dumps(mindmup, sort_keys=True, indent=2))

