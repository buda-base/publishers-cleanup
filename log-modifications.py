import csv
import os
from collections import defaultdict


def delete_log_files():
    """delete existing log files in order to have a clean dir for generating the logs"""
    abs_log_paths = ['logs/locations/'+filename for filename in os.listdir('logs/locations')]
    abs_log_paths.extend(['logs/publishers/'+filename for filename in os.listdir('logs/publishers')])

    for log in abs_log_paths:
        if os.path.isfile(log):
            os.remove(log)


def process_refined_csv():
    modifs_loc = defaultdict(list)
    unknown_loc = defaultdict(list)
    modifs_name = defaultdict(list)

    with open('csv/publishers.csv') as g:
        data = csv.reader(g)
        rows = list(data)[1:]
        rows = sorted(rows, key=lambda x: x[1])  # sort on new_loc

    for num, row in enumerate(rows):
        loc_orig, loc_new, name_orig, name_new, _ = row

        # I am certain of the modified location (capitals) and it needs to be added
        if loc_new[0].isupper() \
           and ((loc_new not in modifs_loc)
                or (loc_orig not in modifs_loc[loc_new])):

            # adding the header if it is not there
            if '\t'+loc_new not in modifs_loc[loc_new]:
                modifs_loc[loc_new].append('\t'+loc_new)

            # add current variant
            modifs_loc[loc_new].append(loc_orig)

        # all entries not already processed
        elif loc_new not in modifs_loc.keys():
            unknown_loc[loc_new].append(loc_orig)

        # if name_new != name_orig and ((name_new not in modifs_name) or (name_orig not in modifs_name[name_new])):
        #     if '\t'+name_new not in modifs_name[name_new]:
        #         modifs_name[name_new].append('\t'+name_new)
        #     modifs_name[loc_new].append(loc_orig)

    return modifs_loc, unknown_loc, modifs_name


def write_individual_entries(type, entry):
    for k, v in entry.items():
        with open('logs/{}/{}.txt'.format(type, k), 'w') as h:
            v = sorted(v)
            h.write('\n'.join(v))


def write_full_log(type, entries):
    chars_to_strip = '[]［］{}/／/?'
    with open('logs/{}.tsv'.format(type), 'w') as f:
        title = 'PublisherLocations\t\t\t\n'
        f.write(title)

        for name, variants in entries.items():
            entry = '\t{}\t\t\n'.format(name.strip(chars_to_strip).strip('\t').strip())
            f.write(entry)

            cleaned_variants = [v.strip(chars_to_strip).strip('\t').strip() for v in variants]
            sorted_variants = sorted(list(set(cleaned_variants)))
            for v in sorted_variants:
                v = v.strip()
                f.write('\t\t\t{}\n'.format(v))


if __name__ == '__main__':
    delete_log_files()
    modified_locs, unknown_locs, modified_names = process_refined_csv()
    write_individual_entries('locations', modified_locs)
    write_individual_entries('publishers', modified_names)
    write_full_log('locations', modified_locs)
    write_full_log('locations_unknown', unknown_locs)
