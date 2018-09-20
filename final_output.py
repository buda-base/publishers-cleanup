from pathlib import Path
import yaml
import json
import csv


def export_work_publisher():
    data = csv.reader(Path('publishers_GID.csv').open())
    data = list(data)

    out = 'workRID,locationRID\n'
    for d in data[1:]:
        work = d[4].split('=')[1]
        out += f'{work},{d[1]}\n'

    Path('work-publisherPlaceRID.csv').write_text(out)


def generate_new_places():
    content = Path('locations_cleaned_GID.tsv').read_text(encoding='utf-8-sig').strip().split('\n')
    content = content[1:]  # delete root

    previous = ''
    current = ''
    total = {}
    RID = {'key': '', 'langs': {}}
    current_lang = {'tag': '', 'strings': {}}
    for num, line in enumerate(content):
        # update state
        if line.startswith('\t\t\t'):
            current = 'lang_str'
        elif line.startswith('\t\t'):
            current = 'lang_tag'
        elif line.startswith('\t'):
            current = 'RID'
        else:
            raise SyntaxError(f'line {num}: "{line}" is not well formatted')

        # fill content
        line = line.strip()
        if current == 'RID':
            if previous == 'lang_str':
                RID['langs'][current_lang['tag']] = current_lang['strings']  # update
                current_lang = {'tag': '', 'strings': {}}  # reinitialize

                total[RID['key']] = {'isLocatedIn': '', 'langs': RID['langs']}
                RID = {'key': '', 'langs': {}}
            RID['key'] = line
        if current == 'lang_tag':
            if previous == 'lang_str':
                RID['langs'][current_lang['tag']] = current_lang['strings']  # update
                current_lang = {'tag': '', 'strings': {}}  # reinitialize
            current_lang['tag'] = line
        if current == 'lang_str':
            current_lang['strings'][line] = ''

        previous = current

    out = json.dumps(total, ensure_ascii=False, indent=4, sort_keys=True)
    Path('newPlaceRIDs_raw.json').write_text(out, encoding='utf-8-sig')


generate_new_places()
export_work_publisher()
