from pathlib import Path
import csv
from collections import defaultdict

### IMPORTANT: needs to be executed after 1-match_existing_place_RID.py, not before

def clean_entry(entry):
    chars_to_strip = '[]［］{}/／/?'
    return entry.strip(chars_to_strip).strip('\t').strip().strip('"')


def parse_existing_places():
    in_file = Path('input/placenames.csv')
    data = csv.reader(in_file.open())
    data = [[clean_entry(e) for e in d if e] for d in data if d]
    # join data incorrectly split
    for n, d in enumerate(data):
        data[n] = [d[0], ', '.join(d[1:])]
    # remove url prefix and cleanup
    for i in range(len(data)):
        data[i][0] = data[i][0].replace('http://purl.bdrc.io/resource/', '')
        data[i][1] = clean_entry(data[i][1])

    parsed = defaultdict(list)
    for d in data:
        key, name = d
        parsed[key].append(name)

    return parsed


locations = parse_existing_places()
keys = sorted(list(locations.keys()))

attrib = Path('output/needs_attribution.csv').read_text(encoding='utf-8-sig').split('\n')

attributed = []
for n, a in enumerate(attrib):
    attributed.append(f'{a.split(",")[0]},G5PL{n+1}')
Path('output/needs_attribution.csv').write_text('\n'.join(attributed))

attributed = {a.split(',')[0]: a.split(',')[1] for a in attributed}

matches = Path('output/matches.csv').read_text(encoding='utf-8-sig').split('\n')
matches = {a.split(',')[0]: a.split(',')[1] for a in matches}

multiple = Path('output/multiple_locations.csv').read_text(encoding='utf-8-sig').split('\n')
multiple = {a.split(',')[0]: a.split(',')[1] for a in multiple}

all_Gs = {**attributed, **matches, **multiple}

locs_cleaned = Path('output/locations_cleaned.tsv').read_text(encoding='utf-8-sig').split('\n')
for n in range(len(locs_cleaned)):
    bits = locs_cleaned[n].split('\t')
    if len(bits) > 1:
        if bits[1] != '':
            if bits[1] in all_Gs:
                bits[1] = all_Gs[bits[1]]
    locs_cleaned[n] = '\t'.join(bits)
Path('locations_cleaned_GID.tsv').write_text('\n'.join(locs_cleaned), encoding='utf-8-sig')

tree = Path('output/publisher_locations_tree.tsv').read_text(encoding='utf-8-sig').split('\n')
for n in range(len(tree)):
    parts = tree[n].split('\t')
    if parts[-1] in all_Gs:
        parts.append(all_Gs[parts[-1]])
    tree[n] = '\t'.join(parts)
Path('publisher_locations_tree_GID.tsv').write_text('\n'.join(tree), encoding='utf-8-sig')
