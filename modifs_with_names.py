import json
from pathlib import Path


def parse_modifs():
    json_dump = json.load(Path('newPlaceRIDs_raw.json').open(encoding='utf-8-sig'))
    rid_dict = {}
    for rid, entry in json_dump.items():
        name = ''
        if 'bo' in entry['langs'].values() or 'bo-x-ewts' in entry['langs'].values():
            lg = 'bo'
        else:
            lg = 'en'
        for lang, tag in entry['langs'].items():
            if name:
                continue

            if lg == 'en' and tag == 'en':
                name = lang
            if lg == 'bo' and tag.startswith('bo'):
                name = lang
        rid_dict[rid] = name

    matches = Path('output/matches.csv').read_text(encoding='utf-8-sig').strip().split('\n')
    for m in matches:
        name, rid = m.split(',')
        if '\t' not in rid and rid not in rid_dict:
            rid_dict[rid] = name

    news = Path('output/needs_attribution.csv').read_text(encoding='utf-8-sig').strip().split('\n')
    for m in news:
        name, rid = m.split(',')
        if '\t' not in rid and rid not in rid_dict:
            rid_dict[rid] = name

    content = Path('RID_node_modifs.csv').read_text(encoding='utf-8-sig').strip().split('\n')[1:]
    out = ['RID,,isLocatedIn,,type']
    for line in content:
        if line != ',,':
            rid, loc, type = line.split(',')
            out.append(f'{rid},{rid_dict[rid]},{loc},{rid_dict[loc]},{type}')
    Path('RID_modifs.csv').write_text('\n'.join(out), encoding='utf-8-sig')

parse_modifs()