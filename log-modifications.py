import csv
import os
from collections import defaultdict

in_path = 'csv'
for f in os.listdir(in_path):
    modifs_loc = defaultdict(list)
    modifs_name = defaultdict(list)

    with open('{}/{}'.format(in_path, f)) as g:
        data = csv.reader(g)
        for num, row in enumerate(list(data)[1:]):
            loc_orig, loc_new, _, name_orig, name_new, _, _ = row

            if loc_new != loc_orig and ((loc_new not in modifs_loc) or (loc_orig not in modifs_loc[loc_new])):
                modifs_loc[loc_new].append(loc_orig)

            if name_new != name_orig and ((name_new not in modifs_name) or (name_orig not in modifs_name[name_new])):
                modifs_name[loc_new].append(loc_orig)

    if modifs_loc:
        with open('logs/Dharamsala.txt', 'w') as h:
            h.write('\n'.join(sorted(modifs_loc['Dharamsala'])))
