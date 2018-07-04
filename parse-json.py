import json

with open('input/publishers.json', 'r') as f:
    data = json.load(f)

TLM = []
FPL = []
results = []
for result in data['results']['bindings']:
    uri = result['w']['value']

    location_value = result['workPublisherLocation']['value']
    location_lang = result['workPublisherLocation']['xml:lang']

    name_value = result['workPublisherName']['value']
    name_lang = result['workPublisherName']['xml:lang']

    if 'TLM' in uri:
        TLM.append((location_value, location_lang, name_value, name_lang, uri))
    elif 'FPL' in uri:
        FPL.append((location_value, location_lang, name_value, name_lang, uri))
    else:
        results.append((location_value, location_lang, name_value, name_lang, uri))


with open('csv/publishers.csv', 'w') as g:
    g.write('location_orig,location_new,location_lang,name_orig,name_new,name_lang,uri\n')
    for l_v, l_l, n_v, n_l, uri in results:
        g.write('{},{},{},{},{},{},{}\n'.format(l_v, l_v, l_l,
                                                n_v, n_v, n_l,
                                                uri))

with open('csv/TLM.csv', 'w') as g:
    g.write('location_orig,location_new,location_lang,name_orig,name_new,name_lang,uri\n')
    for l_v, l_l, n_v, n_l, uri in TLM:
        g.write('{},{},{},{},{},{},{}\n'.format(l_v, l_v, l_l,
                                                n_v, n_v, n_l,
                                                uri))

with open('csv/FPL.csv', 'w') as g:
    g.write('location_orig,location_new,location_lang,name_orig,name_new,name_lang,uri\n')
    for l_v, l_l, n_v, n_l, uri in FPL:
        g.write('{},{},{},{},{},{},{}\n'.format(l_v, l_v, l_l,
                                                n_v, n_v, n_l,
                                                uri))
