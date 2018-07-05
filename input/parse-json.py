import json
import csv


# Parses the json file, retaining three fields from the input:
# - workPublisherLocation
# - workPublisherName
# - uri
#
# The columns of each .csv to be processed by OpenRefine is formatted as follows:
#      location_orig, location_new, name_orig, name_new, url, uri
# - (...)_orig columns are left untouched
# - (...)_new columns are normalized in OpenRefine
# - url leads to the work in the tbrc.org website. It is directly clickable from OpenRefine


with open('publishers.json', 'r') as f:
    data = json.load(f)

##################################################
# separate the entries in the json in three csv
TLM = []
FPL = []
results = []
for result in data['results']['bindings']:
    url = 'https://www.tbrc.org/#!rid=' + result['w']['value'].split('/')[-1]

    location_value = result['workPublisherLocation']['value']

    name_value = result['workPublisherName']['value']

    if 'TLM' in url:
        TLM.append((location_value, name_value, url))
    elif 'FPL' in url:
        FPL.append((location_value, name_value, url))
    else:
        results.append((location_value, name_value, url))

##################################################
# write the three csvs with the same headings
fieldnames = ['location_orig', 'location_new', 'name_orig', 'name_new', 'url', 'uri']

with open('../csv/publishers.csv', 'w') as g:
    writer = csv.writer(g, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, url in results:
        writer.writerow((l_v, l_v, n_v, n_v, url))

with open('../csv/TLM.csv', 'w') as h:
    writer = csv.writer(h, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, url in TLM:
        writer.writerow((l_v, l_v, n_v, n_v, url))

with open('../csv/FPL.csv', 'w') as i:
    writer = csv.writer(i, dialect='excel')
    writer.writerow(fieldnames)
    for l_v, n_v, url in FPL:
        writer.writerow((l_v, l_v, n_v, n_v, url))
