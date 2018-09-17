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


def export_newPlaceRIDs():
    content = yaml.load(Path('newPlaceRIDs.yaml').read_text(encoding='utf-8-sig'))
    out = json.dumps(content, indent=4, sort_keys=True)
    Path('newPlaceRIDs.json').write_text(out, encoding='utf-8-sig')


export_work_publisher()
export_newPlaceRIDs()
