- add all printeries (G####) in the csv
- add publisher RID (C0OP) to publisherName.csv
  - normalize and consolidate with synonyms.csv
  - if printery name like སྡེ་དགེ་པར་ཁང་། move to printeries.csv
- populate publisher-template.csv with above data
- populate version-publisher-template
  - add above data
  - check for inconsistencies like publisher/printery mixup 

-------------------------------
By Drupchen:

Please find below issues I stumbled upon while working on the PublisherLocations.

### On PublisherLocation:
- [x] [W23633](https://www.tbrc.org/#!rid=W23633): bo ra given, but colophon cites another name (sgnon thang ....) See [here](https://www.tbrc.org/browser/ImageService?work=W23633&igroup=I1KG463&image=939&first=1&last=940&fetchimg=yes)
- [ ] [W1KG13585](https://www.tbrc.org/#!rid=W1KG13585): printed in Delhi, by Shechen Publications, Nepal See [here](https://www.tbrc.org/browser/ImageService?work=W1KG13585&igroup=I1KG13587&image=4&first=1&last=750&fetchimg=yes)
- [x] [W8LS16458](https://www.tbrc.org/#!rid=W8LS16458): Jakar Dzong, as seen in the Catalog Information in the above link	
- [x] [W4CZ33249](https://www.tbrc.org/#!rid=W4CZ33249): Halle (saale) not found in the book. maybe Konigswinter See [here](https://www.tbrc.org/browser/ImageService?work=W4CZ33249&igroup=I1KG16639&image=9&first=1&last=578&fetchimg=yes)
- [x] [W00KG03892](https://www.tbrc.org/#!rid=W00KG03892): Most probably St Petersburg. See [here](https://encyclopedia2.thefreedictionary.com/Schmidt%2c+Isaac+Jakob)
- [ ] [W1KG12212](https://www.tbrc.org/#!rid=W1KG12212): very unlikely to be published in England. no information about England to be found except the nationality of the "author"(the one who compiled and had it printed) Sean Price, aka Tenzin Jamchen	
- [ ] [W13942](https://www.tbrc.org/#!rid=W13942): second last line of the image. See [here](https://www.tbrc.org/browser/ImageService?work=W13942&igroup=I1KG13072&image=165&first=1&last=166&fetchimg=yes)
- [x] [W1KG12657](https://www.tbrc.org/#!rid=W1KG12657): year instead of place	
- [x] [W1KG12657](https://www.tbrc.org/#!rid=W1KG12657): year instead of place	
- [x] [W8LS20655](https://www.tbrc.org/#!rid=W8LS20655): lho nub given here, but other works with the same publisher info have Chengdu instead. putting Chengdu here would be easier ?	See [here](https://www.tbrc.org/browser/ImageService?work=W30037&igroup=I1KG12943&image=531&first=1&last=536&fetchimg=yes)
- [x] [W3CN15720](https://www.tbrc.org/#!rid=W3CN15720): Publisher Location is SRPM. What does the acronym mean ?	
- [x] [W4CZ302688](https://www.tbrc.org/#!rid=W4CZ302688): Drip (grib) seems to be an addition to the location name (tshe-mchog gling), not the name of the place itself.	
- [x] [W1KG12657](https://www.tbrc.org/#!rid=W1KG12657): name : Sakya Center, location: rajpur See [here](https://www.tbrc.org/browser/ImageService?work=W1KG12657&igroup=I1KG12857&image=400&first=1&last=402&fetchimg=yes)

### On publisher roles to be refined:
- [ ] [W1KG14799](https://www.tbrc.org/#!rid=W1KG14799): See [here](https://www.tbrc.org/browser/ImageService?work=W1KG14799&igroup=I1KG14857&image=214&first=1&last=214&fetchimg=yes)
- [x] [W3CN700](https://www.tbrc.org/#!rid=W3CN700): publisher location and name to review
- [x] [W2CZ8097](https://www.tbrc.org/#!rid=W2CZ8097): Combination of Location and Name	location is publisher name, name is author or sponsor	
- [ ] [W21500](https://www.tbrc.org/#!rid=W21500): publisher is the sponsor organisation	
- [ ] [W1AC260](https://www.tbrc.org/#!rid=W1AC260): roles to be refined See [here](https://www.tbrc.org/browser/ImageService?work=W1AC260&igroup=I4PD4408&image=218&first=1&last=222&fetchimg=yes)
- [x] [W4CZ74192](https://www.tbrc.org/#!rid=W4CZ74192)	PublisherName is the place where the work is stored. the sponsor is found [here](https://www.tbrc.org/browser/ImageService?work=W4CZ74192&igroup=I4CZ74255&image=252&first=1&last=254&fetchimg=yes)
- [x] [W1EE8](https://www.tbrc.org/#!rid=W1EE8)		The colophon says that the work was included in the collected writings of Khure Chenmo, not that it is located in a place called Khure Chenmo. (the folio where the end of the text and the beginning of the colophon is located is missing) See [here](https://www.tbrc.org/browser/ImageService?work=W1EE8&igroup=I1KG16958&image=160&first=1&last=160&fetchimg=yes)
- [ ] [W1KG3967](https://www.tbrc.org/#!rid=W1KG3967)	both	location is Ballimoran. See [here](https://www.tbrc.org/browser/ImageService?work=W1KG3967&igroup=I1KG4024&image=4&first=1&last=462&fetchimg=yes)
- [x] [W1KG15419](https://www.tbrc.org/#!rid=W1KG15419): publisher roles need to be detailed: Gongkar Palace is given as Publisher Name, but it looks like a place.  The only place where I found Phodrang Gongkar was in the colophon attached below, but it leads to the name of TashiLhunpo Palgyi Dechen Monastery built by Panchen Rinpoche.	See [here](https://www.tbrc.org/browser/ImageService?work=W27406&igroup=I1CZ2221&image=51&first=1&last=52&fetchimg=yes)
- [x] [W2CZ8013](https://www.tbrc.org/#!rid=W2CZ8013): roles to refine: Should be Toong Soong, instead of Freedom Press, Darjeeling	

### Inverted PublisherLocation and PublisherName:
- [x] [W00EGS1016937](https://www.tbrc.org/#!rid=W00EGS1016937)
- [x] [W2PD17416](https://www.tbrc.org/#!rid=W2PD17416)
- [x] [W00EGS1017306](https://www.tbrc.org/#!rid=W00EGS1017306)
- [x] [W00EGS1017306](https://www.tbrc.org/#!rid=W00EGS1017306)
- [x] [W00EGS1016937](https://www.tbrc.org/#!rid=W00EGS1016937)
- [x] [W4CZ45282](https://www.tbrc.org/#!rid=W4CZ45282): location is a publisher	

### Other:
- [ ] [W2PD16917](https://www.tbrc.org/#!rid=W2PD16917)	Combination of Location and Name	the Publication tab says that the texts are in dbu med, but at least the 1st volume is in uchen.
- [x] [W3CN535](https://www.tbrc.org/#!rid=W3CN535)	Combination of Location and Name	"the current data says sakya, but the title page says ""བཀྲས་དགོན་ནང་བསྟན་གསུང་རབ་པར་ཁང་"". Other works of the same publisher indicate: 
    Publisher Name        gdan sa chen po bkra shis lhun po'i nang bstan gsung rab par khang /
    Publisher Location        gzhis ka rtse/"	for https://www.tbrc.org/#!rid=W3CN3030
- [ ] [W4CZ45267](https://www.tbrc.org/#!rid=W4CZ45267)		pages are inverted (at least 2 and 3)	
- [x] [W8LS18072](https://www.tbrc.org/#!rid=W8LS18072)	content	there are 4 or 5 different short texts. the publisher info of the second last one is retained in the data	
- [x] [W3CN15295](https://www.tbrc.org/#!rid=W3CN15295)	Publisher Name	"it seems to be the colophon instead of the publisher name: ""Publisher Name	bya yul dpon sa tshogs gnyis grub pas mdzad/"""	
- [x] [W3CN5096](https://www.tbrc.org/#!rid=W3CN5096)		W3CN5096, W3CN553, W3CN549, W3CN555, W3CN551, W3CN550, W3CN556 all have stod lung as location. Is it really stod lung ? Maybe stod rgyud ? (it was printed in 2012 and prefaced by the Karmapa in Gyuto)	
