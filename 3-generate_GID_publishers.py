from pathlib import Path
import csv

def parse_GIDs(f):
    content = Path(f).read_text(encoding='utf-8-sig').strip().split('\n')
    content = {a.split(',')[0]: a.split(',')[1] for a in content}
    return content


matches = parse_GIDs('output/matches.csv')
attributed = parse_GIDs('output/needs_attribution.csv')

all_Gs = {**attributed, **matches}

data = csv.reader(Path('csv/publishers.csv').open())
data = list(data)

for n, row in enumerate(data):
    GID = ''
    if row[1] in all_Gs.keys():
        GID = all_Gs[row[1]]
        row[1] = GID
data[0][1] = 'GID'

with open('publishers_GID.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerows(data)

