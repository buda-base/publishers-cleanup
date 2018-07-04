import json
import csv

with open('publishers.json', 'r') as f:
    data = json.load(f)

TLM = []
FPL = []
results = []
for result in data['results']['bindings']:
    uri = result['w']['value']

    location_value = result['workPublisherLocation']['value']

    name_value = result['workPublisherName']['value']

    if 'TLM' in uri:
        TLM.append((location_value, name_value, uri))
    elif 'FPL' in uri:
        FPL.append((location_value, name_value, uri))
    else:
        results.append((location_value, name_value, uri))

fieldnames = ['location_orig', 'location_new', 'name_orig', 'name_new', 'uri']

with open('../csv/publishers.csv', 'w') as g:
    writer = csv.writer(g, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, uri in results:
        writer.writerow((l_v, l_v, n_v, n_v, uri))

with open('../csv/TLM.csv', 'w') as h:
    writer = csv.writer(h, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, uri in TLM:
        writer.writerow((l_v, l_v, n_v, n_v, uri))

with open('../csv/FPL.csv', 'w') as i:
    writer = csv.writer(i, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, uri in FPL:
        writer.writerow((l_v, l_v, n_v, n_v, uri))
