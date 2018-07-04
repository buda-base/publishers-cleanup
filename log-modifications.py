import csv
import os
from collections import defaultdict

modifs_loc = defaultdict(list)
modifs_name = defaultdict(list)

in_path = 'csv'
for f in os.listdir(in_path):
    with open('{}/{}'.format(in_path, f)) as g:
        data = csv.reader(g)
        for num, row in enumerate(list(data)[1:]):
            loc_orig, loc_new, name_orig, name_new, _ = row

            if loc_new != loc_orig and ((loc_new not in modifs_loc) or (loc_orig not in modifs_loc[loc_new])):
                modifs_loc[loc_new].append(loc_orig)

            if name_new != name_orig and ((name_new not in modifs_name) or (name_orig not in modifs_name[name_new])):
                modifs_name[loc_new].append(loc_orig)

for k, v in modifs_loc.items():
    with open('logs/locations/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))

for k, v in modifs_name.items():
    with open('logs/publishers/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))
