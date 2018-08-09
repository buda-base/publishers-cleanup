from pathlib import Path
import csv
from collections import defaultdict


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


def parse_locations():
    in_file = Path('logs/locations.tsv')
    reader = csv.reader(in_file.open(), dialect='excel-tab')

    locations = defaultdict(list)
    key = ''
    for row in reader:
        if row[1]:
            key = row[1]
        elif row[3] and key:
            locations[key].append(row[3])

    return locations


def exact_match_places(rids, locations):
    matches = {}
    for loc, l_variants in locations.items():
        for rid, r_variants in rids.items():
            for l in l_variants:
                for r in r_variants:
                    if l == r:
                        matches[loc] = rid
    return matches


if __name__ == '__main__':
    parsed = parse_existing_places()
    locations = parse_locations()
    matches = exact_match_places(parsed, locations)
    out = '\n'.join(['{},{}'.format(k, v) for k, v in matches.items()])
    Path('exact_matches.csv').write_text(out)
