import csv
import os
from collections import defaultdict

#################################################
# delete existing log files in order to have a clean dir for generating the logs
abs_log_paths = ['logs/locations/'+filename for filename in os.listdir('logs/locations')]
abs_log_paths.extend(['logs/publishers/'+filename for filename in os.listdir('logs/publishers')])

for log in abs_log_paths:
    if os.path.isfile(log):
        os.remove(log)

modifs_loc = defaultdict(list)
unknown_loc = defaultdict(list)
modifs_name = defaultdict(list)

##################################################
# find all the spelling variants in the csv files
# a spelling variant is found when the (...)_orig and the (...)_new are not equal.
# this shows the field was normalized using OpenRefine
with open('csv/publishers.csv') as g:
    data = csv.reader(g)
    rows = list(data)[1:]
    sorted_rows = sorted(rows, key=lambda x: x[1])

    for num, row in enumerate(sorted_rows):
        loc_orig, loc_new, name_orig, name_new, _ = row

        if loc_new[0].isupper() and ((loc_new not in modifs_loc) or (loc_orig not in modifs_loc[loc_new])):
            if '\t'+loc_new not in modifs_loc[loc_new]:
                modifs_loc[loc_new].append('\t'+loc_new)
            modifs_loc[loc_new].append(loc_orig)

        #
        elif loc_new not in modifs_loc.keys():
            unknown_loc[loc_new].append(loc_orig)

        # if name_new != name_orig and ((name_new not in modifs_name) or (name_orig not in modifs_name[name_new])):
        #     if '\t'+name_new not in modifs_name[name_new]:
        #         modifs_name[name_new].append('\t'+name_new)
        #     modifs_name[loc_new].append(loc_orig)

####################################################
# each normalized entity gets a file with itself preceded by a tab as the first line,
# then a list of each spelling variant per line
for k, v in modifs_loc.items():
    with open('logs/locations/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))

for k, v in modifs_name.items():
    with open('logs/publishers/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))


chars_to_strip = '[]［］{}/／/?'
with open('logs/locations.tsv', 'w') as f:
    f.write('PublisherLocations\t\t\t\n')
    for name, variants in modifs_loc.items():
        f.write('\t{}\t\t\n'.format(name.strip(chars_to_strip).strip('\t').strip()))
        variants = [v.strip(chars_to_strip).strip('\t').strip() for v in variants]
        for v in sorted(list(set(variants))):
            f.write('\t\t\t{}\n'.format(v.strip()))

with open('logs/locations_unknown.tsv', 'w') as f:
    f.write('PublisherLocations\t\t\t\n')
    for name, variants in unknown_loc.items():
        f.write('\t{}\t\t\n'.format(name.strip(chars_to_strip).strip('\t').strip()))
        variants = [v.strip(chars_to_strip).strip('\t').strip() for v in variants]
        for v in sorted(list(set(variants))):
            f.write('\t\t\t{}\n'.format(v.strip()))
