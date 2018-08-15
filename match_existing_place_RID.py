from pathlib import Path
import csv
from collections import defaultdict
import bophono
import unicodedata

from third_party.convert import wylie2unicode


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


def is_exact_match(text1, text2):
    return text1 == text2


def is_contained(text1, text2):
    if text1 != '' and text2 != '':
        if text1 in text2 or text2 in text1:
            return True
    return False


unicodes = {}
phonos = {}


def is_phonetic_match(text1, text2):
    global unicodes, phonos
    # attempt to detect non-wylie
    if text1 == ''\
            or text2 == ''\
            or 'CJK' in unicodedata.name(text1[0])\
            or 'CJK' in unicodedata.name(text2[0])\
            or text1[0].isupper()\
            or text2[0].isupper():
        return False

    else:
        options = {
            'aspirateLowTones': True,
            'prefixStrategy': 'always'
        }
        converter = bophono.UnicodeToApi(options=options)
        dir = str(Path.cwd() / 'third_party' / 'Lingua-BO-Wylie')
        if text1 not in unicodes.keys():
            uni1 = wylie2unicode(text1, dir)
            unicodes[text1] = uni1
        else:
            uni1 = unicodes[text1]

        if text2 not in unicodes.keys():
            uni2 = wylie2unicode(text2, dir)
            unicodes[text2] = uni2
        else:
            uni2 = unicodes[text2]

        if uni1 not in phonos.keys():
            phono1 = converter.get_api(uni1)
            phonos[uni1] = phono1
        else:
            phono1 = phonos[uni1]

        if uni2 not in phonos.keys():
            phono2 = converter.get_api(uni2)
            phonos[uni2] = phono2
        else:
            phono2 = phonos[uni2]
        if phono1 == phono2:
            print('\n', text1, text2, '\n')
        return phono1 == phono2


def match(rids, locations, match_func):
    matches = defaultdict(list)
    for loc, l_variants in locations.items():
        for rid, r_variants in rids.items():
            for l in l_variants:
                for r in r_variants:
                    if match_func(l, r):
                        matches[loc].append(rid)
    for k, v in matches.items():
        matches[k] = list(set(v))
    return matches


if __name__ == '__main__':
    parsed = parse_existing_places()
    locations = parse_locations()

    matches = match(parsed, locations, is_exact_match)
    out = '\n'.join(['{},{}'.format(k, ''.join(['\n,http://library.bdrc.io/show/bdr:{}'.format(w) for w in v])) for k, v in matches.items()])
    Path('exact_matches.csv').write_text(out)

    not_matched = {location: insts for location, insts in locations.items() if location not in matches}

    contained = match(parsed, not_matched, is_contained)
    out = '\n'.join(['{},{}'.format(k, ''.join(['\n,http://library.bdrc.io/show/bdr:{}'.format(w) for w in v])) for k, v in contained.items()])
    Path('containing_matches.csv').write_text(out)
