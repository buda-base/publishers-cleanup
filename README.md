`locations_cleaned_GID.tsv`: cleaned publisher locations strings in `bo`, `en` or `zh`.
All entries have been manually checked.

`publisher_locations_tree_GID.tsv`: the tree structure of all publisher locations with the geographic RID attributed.
This can serve to update the Geographic data with all the new locations.
Note some modern locations in TAR were not attributed a GID.

`publishers_GID.csv`: the same as csv/publishers.csv, but with the GID attributed
Note locations found in `logs/locations_unknown.tsv` are momentarily left unchanged

The content of `output/questions.csv` should be reviewed with the librarians.

The content of `logs/locations_unknown.tsv` should be processed by someone more knowledgeable and included in `logs/locations.csv` so the changes are propagated down the workflow.

`remaining_issues.csv`: all the remaining entries (excepting about 4000 [s.l.]) that could not be processed and thus didn't receive a new RID. 