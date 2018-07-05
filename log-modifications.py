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
modifs_name = defaultdict(list)

##################################################
# find all the spelling variants in the csv files
# a spelling variant is found when the (...)_orig and the (...)_new are not equal.
# this shows the field was normalized using OpenRefine
in_path = 'csv'
for f in os.listdir(in_path):
    with open('{}/{}'.format(in_path, f)) as g:
        data = csv.reader(g)
        for num, row in enumerate(list(data)[1:]):
            loc_orig, loc_new, name_orig, name_new, _ = row

            if loc_new != loc_orig and ((loc_new not in modifs_loc) or (loc_orig not in modifs_loc[loc_new])):
                if '\t'+loc_new not in modifs_loc[loc_new]:
                    modifs_loc[loc_new].append('\t'+loc_new)
                modifs_loc[loc_new].append(loc_orig)

            if name_new != name_orig and ((name_new not in modifs_name) or (name_orig not in modifs_name[name_new])):
                if '\t'+name_new not in modifs_name[name_new]:
                    modifs_name[name_new].append('\t'+name_new)
                modifs_name[loc_new].append(loc_orig)

####################################################
# each normalized entity gets a file with itself preceded by a tab as the first line,
# then a list of each spelling variant per line
for k, v in modifs_loc.items():
    with open('logs/locations/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))

for k, v in modifs_name.items():
    with open('logs/publishers/{}.txt'.format(k), 'w') as h:
        h.write('\n'.join(sorted(v)))
