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

Adopted convention for new RID:

`G5 PL 0123`

where:
 - 5 is chosen because no G RID starts with G5, so the new ones will be easy to identify and modify later on.
 - PL stands for Publisher Locations
 - incrementing number

Temporary RIDs:

`G51 TMP 0123`

where:
 - G51 to distinguish from G5
 - TMP for Temporary
 - incrementing number 

TODO: add language code to all strings
use "bo-x-pinyin" for Tibetan Pinyin names in strings