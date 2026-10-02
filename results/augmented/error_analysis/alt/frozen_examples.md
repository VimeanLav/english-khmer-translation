# Error analysis: B: NLLB frozen backbone

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 0.4** · `repetition_hallucination`
  - EN: Georgia led early in the second half and were threatening to score late in the match but Ireland's defence held to secure the four point victory.
  - REF: ក្រុមចចជា បាននាំមុខនៅតង់ទីពីរ និងកំពុងគំរាមរកពិន្ទុនៅការប្រកួតក្រោយ ប៉ុន្តែ ការការពាររបស់ក្រុមអៀឡង់ បានការពារជ័យជំនះបួនពិន្ទុ។
  - HYP: ចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចច

- **chrF++ 0.5** · `repetition_hallucination`
  - EN: Georgia kept up the pressure on Ireland in the late stages of the game, twice reaching Ireland's try line, but they could not get through and Ireland managed to scrape through with a four point lead.
  - REF: ក្រុមចចជា បន្តដាក់សម្ពាធលើក្រុមអៀឡង់នៅចុងការប្រកួត ពីរដងដែលឈានទៅដល់ខ្សែបន្ទាត់ try របស់ក្រុមអៀឡង់ ប៉ុន្តែ ពួកគេមិនអាចបុកទម្លោះបាន ហើយក្រុមអៀឡង់អាចប្រយុទ្ធដោយរកបានបួនពិន្ទុនាំមុខ។
  - HYP: ចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចច

- **chrF++ 0.9** · `repetition_hallucination`
  - EN: Georgia took a shock lead early in the second half, when Georgi Shkinin scored a try in the 45th minute.
  - REF: ក្រុមចចជា បាននាំមុខគួរឲ្យភ្ញាក់ផ្អើលនៅតង់ទីពីរ ខណៈដែលកីឡាករ ចចហ្គី ស្គីនីន រកបាន try មួយនៅនាទីទី45។
  - HYP: ចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចចច

- **chrF++ 3.1** · `repetition_hallucination`
  - EN: Flaming debris ignited small grass fires next to the roads.
  - REF: កំទេចភ្លើងបានបង្កអោយមានការឆេះស្មៅតូចៗនៅជាប់នឹងផ្លូវ។
  - HYP: កម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេ

- **chrF++ 4.0** · `repetition_hallucination`
  - EN: Opera singer-turned-talk show host Charlotte Church wanted to book hotel heiress Paris Hilton on her program, to insult her.
  - REF: អ្នករៀបចំកម្មវិធីសម្តែង Opera singer-turned-talk ឈ្មោះឆាលុត ឆឺជ ចង់កក់សណ្ឋាគារប៉ារីសហីលតុនដែលជាកេរមរតករបស់ប៉ារីសហីលតុន សំរាប់កម្មវិធីខ្លួន ដើម្បីអោយអោយនាងអាម៉ាស់មុខ។
  - HYP: អ្នកចម្រៀងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំង

- **chrF++ 5.4** · `repetition_hallucination`
  - EN: Ottawa ultra-runner Ray Zahab, age 39, adventure journalist and architect Kevin Vallely, age 44, of Lynn Valley, North Vancouver and North Pole expeditionist Richard Weber, age 49, said they completed the 700-mile (1,130-kilometer) journey, at 10,000 feet altitude, finally arriving early Wednesday morning.
  - REF: អ្នករត់ក្នុងរយៈចម្ងាយឆ្ងាយរបស់អូតាវ៉ា រ៉េ ហ្សាហាប់ អាយុ 39 ឆ្នាំ អ្នកកាសែតផ្សងព្រេង និងស្ថាបត្យករ ខេវីន វ៉ាលេលី អាយុ 44 ឆ្នាំ របស់លីន វ៉ាឡេ ភាគខាងជើងទីក្រុងវ៉ាន់ឃូវើ និងអ្នកធ្វើដំណើររុករកនៅប៉ូលខាងជើង រីឆាត វ៉េប៊ើ អាយុ 49ឆ្នាំ បាននិយាយថាពួកគេបានបញ្ចប់ការធ្វើដំណើរ 700-ម៉ាយ (1,130-គីឡូម៉ែត្រ) ក្នុងរយៈកម្ពស់ 10,000 ហ្វីត នៅទីបំផុតបានមកដល់ព្រឹកព្រលឹមថ្ងៃពុធ។
  - HYP: អ្នកប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំង

- **chrF++ 5.9** · `repetition_hallucination`
  - EN: The trio also suffered altitude sickness, vertigo, massive, painful blisters, and temperatures as low as minus 40.
  - REF: អ្នកទាំងបីក៏បានទទួលរងជំងឺរងសម្ពាធបរិយាកាស វិលមុខ ពងបែកដែលពោរពេញដោយការឈឺចាប់ និងសីតុណ្ហភាពទាបរហូតដល់ដក 40។
  - HYP: ក្រុមបីនាក់នេះក៏រងទុក្ខពីជំងឺកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិត

- **chrF++ 11.3** · `unseen_source_word`
  - EN: Dannie Abse is well-known for being a poet and a medical doctor.
  - REF: លោកដានី អាប់សេ ល្បីឈ្មោះជាកវី​តែងកំណាព្យ និង​ជាវេជ្ជបណ្ឌិត​ផ្នែកវេជ្ជសាស្រ្ត​។
  - HYP: Dannie Abse ត្រូវបានគេស្គាល់ថាជាកំណាព្យករ និងជាគ្រូពេទ្យ។

- **chrF++ 11.3** · `repetition_hallucination`
  - EN: In the women's race, the top two athletes remained the same as last year; Elisabeth "Liz" May from Luxembourg managed to stay ahead of a pursuing group the entire race, and finished first ahead of Jessica Mayon.
  - REF: នៅក្នុងការប្រណាំងផ្នែកស្ត្រី អត្តពលិកលំដាប់កំពូលទាំងពីរនៅតែដូចនឹងកាលពីឆ្នាំមុន; អេលីសាបិត "Liz" មេ មកពី លុចសំបួបានទទួលជ័យជំនះនាំមុខក្រុមអ្នកដេញតាមក្នុងការប្រណាំងទាំងមូល និងបានមកដល់ទីមុនជេសីកា ម៉ាយ៉ុន។
  - HYP: នៅក្នុងការប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណ

- **chrF++ 13.3** · `unseen_source_word`
  - EN: Shenouda was dressed in full regalia, complete with a gold crown.
  - REF: សេននូដា ត្រូវបានគេស្លៀកពាក់អោយក្នុងសំលៀកបំពាក់រាជា ជាមួយនឹងម្កុជមាស។
  - HYP: សេណូដាបានពាក់ខោអាវពេញលេញ ដែលពេញលេញជាមួយពានរង្វាន់ពណ៌មាស។

- **chrF++ 13.3** · `unseen_source_word`
  - EN: And hard-throwing closer Brad Lidge will be refreshed physically and mentally after an exhausting stretch.
  - REF: ហើយលោកប្រេត លិច្ច ដែលជាអ្នកគប់បាល់ដ៏ប៉ិនប្រសប់ នឹងត្រូវមានអារម្មណ៍ស្រស់ថ្លាទាំងរាងកាយ និងផ្លូវចិត្តក្រោយពីការហាត់ប្រាណឱ្យយឺតសសៃ។
  - HYP: ហើយប្រេដ លីតហ្គេមដ៏ជិតស្និទ្ធនឹងមានការកែលម្អដោយចលនា និងរូបរាង បន្ទាប់ពីការហត់នឿយៗ។

- **chrF++ 13.4** · `lexical_semantic`
  - EN: In addition to transport disruption, a number of sports have been affected.
  - REF: បន្ថែម​លើស​ពី​ការ​អាក់​ខាន​នៃ​មធ្យោបាយ​ធ្វើ​ដំណើរ​ កីឡា​ជា​ច្រើន​ប្រភេទ​បានរងផល​ប៉ះពាល់ផងដែរ​។
  - HYP: ក្រៅពីការរំខានដឹកជញ្ជូន កីឡាជាច្រើនត្រូវបានប៉ះពាល់។

- **chrF++ 15.2** · `repetition_hallucination`
  - EN: The report blames the type of cement used by Halliburton, designed to prevent harmful hydrocarbons from reaching the seabed, as well as criticizing the crew of Deepwater Horizon, for failing to realize for forty minutes that oil had started to leak from the well, and once it was realized, the crew "vented" the hydrocarbons "directly onto the rig".
  - REF: របាយការណ៍បានបន្ទោសប្រភេទស៊ីម៉ង់ត៍ដែលប្រើប្រាស់ដោយ ហាលីប៊ូតុនដើម្បីការពារហាយដ្រូកាបោនដ៏គ្រោះថ្នាក់ពីការទៅដល់បាតសមុទ្រ ព្រមទាំងរិះគន់ក្រុមបុគ្គលិក ឌិបវរ័ធើហរីហ្សិន អំពីការបរាជ័យមិនបានដោះស្រាយនូវការចាប់ផ្តើមលិចប្រងរយៈពេលសែសិបនាទីពីអណ្តូង ហើយនៅពេលដែលគេដឹង ក្រុមបុគ្គលិក "បានបញ្ចេញ" ហាយដ្រូកាបោន "ដោយផ្ទាល់ទៅលើហេដ្ឋារចនាសម្ព័ន្ធ។"
  - HYP: របាយការណ៍នេះបានស្តីបន្ទោសទៅលើប្រភេទស័ង្កសីតុណ្ហភាពដែលប្រើដោយហាលីប៊ឺតុន ដែលត្រូវបានរចនាឡើងដើម្បីរារាំងកាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូខាបូអ៊ីដ្រូ

- **chrF++ 15.4** · `repetition_hallucination`
  - EN: There are at least two big winners in Tuesday night's US$370 million Mega Millions lottery drawing which is held in 12 U.S. states.
  - REF: យ៉ាងហោចណាស់អ្នកឈ្នះរង្វាន់ធំមានចំនួនពីររូបក្នុងកម្មវិធីចាប់រង្វាន់ឆ្នោតមីលៀន មេហ្គា US$370 លាននាយប់ថ្ងៃអង្គារ៍ ដែលបានរៀបចំឡើងក្នុងរដ្ឋសហរដ្ឋអាមេរិកចំនួន 12 រដ្ឋ។
  - HYP: យ៉ាងហោចណាស់មានអ្នកឈ្នះធំចំនួនពីរនាក់នៅក្នុងការចាក់សំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរឹទ្ធសំរ

- **chrF++ 16.2** · `repetition_hallucination`
  - EN: The explosions sent flaming debris into the air and onto buildings and expressways.
  - REF: ការផ្ទុះនេះបានបញ្ជូនកំទេចអណ្តាតភ្លើងទៅក្នុងខ្យល់និងទៅក្នុងអគារនិងអ៊ិចប្រេសវេ។
  - HYP: ការផ្ទុះបានបញ្ជូនកម្ទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចក


## wrong_script (1 sentences)

- **chrF++ 27.6** · `wrong_script`
  - EN: That ticket is worth $250,000 and was bought at Burtonsville Crown Beer & Wine in Montgomery County, Maryland.
  - REF: សំបុត្រនោះឈ្នះបាន $250,000 នឹងត្រូវបានទិញនៅបើតុនស្វីល ក្រោនបៀ និងវ៉ាយក្នុងស្រុកមុនហ្គោមើរី មែរីឡេន។
  - HYP: សំបុត្រនោះមានតម្លៃ $250,000 ហើយត្រូវបានទិញនៅ Burtonsville Crown Beer & Wine ក្នុង Montgomery County រដ្ឋ Maryland។


## repetition_hallucination (19 sentences)

- **chrF++ 24.8** · `repetition_hallucination`
  - EN: While Sydney's spring racing carnival has been canceled, Melbourne's is expected to kick off this weekend with the Caufield Cup.
  - REF: ក្នុងពេលក្បូនហែរសំរាប់ប្រណាំងរដូវផ្ការីកនៅស៊ីតនីត្រូវលប់ចោល នៅមែលប៊ិន គេពិចារណាពីបើកឡើងវិញនៅចុងសប្តាហ៍នូវកម្មវិធីពាន់រង្វាន់ ឃូហ្វៀលខាប់។
  - HYP: ខណៈពេលដែលពិធីប្រណាំងប្រណាំងនៅរដូវក្តៅរបស់ទីក្រុងស៊ីដនីត្រូវបានលុបចោល ពិធីប្រណាំងប្រណាំងប្រណាំងនៅមែលប៊ឺនត្រូវបានរំពឹងថានឹងចាប់ផ្តើមនៅចុងសប្តាហ៍នេះជាមួយការប្រកួតកាហ្វៀលដ៍កុប។

- **chrF++ 16.2** · `repetition_hallucination`
  - EN: The explosions sent flaming debris into the air and onto buildings and expressways.
  - REF: ការផ្ទុះនេះបានបញ្ជូនកំទេចអណ្តាតភ្លើងទៅក្នុងខ្យល់និងទៅក្នុងអគារនិងអ៊ិចប្រេសវេ។
  - HYP: ការផ្ទុះបានបញ្ជូនកម្ទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចក

- **chrF++ 3.1** · `repetition_hallucination`
  - EN: Flaming debris ignited small grass fires next to the roads.
  - REF: កំទេចភ្លើងបានបង្កអោយមានការឆេះស្មៅតូចៗនៅជាប់នឹងផ្លូវ។
  - HYP: កម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេចកម្ទេ

- **chrF++ 34.8** · `repetition_hallucination`
  - EN: While the world knew him as a great storyteller that challenged our preconceived notions about the world around us — and entertained us all while doing so — his wife Sherri, daughter Taylor, family and friends knew Michael Crichton as a devoted husband, loving father and generous friend who inspired each of us to strive to see the wonders of our world through new eyes, said a statement by his family.
  - REF: យោងតាមពាក្យពេចន៍របស់គ្រួសារគាត់ ខណ:ដែលពិភពលោកបានស្គាល់ថាគាត់ជាអ្នកនិពន្ឋរឿងដ៏អស្ចារ្យម្នាក់ ដែលប្រជែងពីគំនិតរបស់យើងអំពីពិភពលោកជុំវិញខ្លួនយើង​- និងផ្តល់ការកំសាន្តដល់ពួកយើងខណៈដែលយើងកំពុងធ្វើដូចនោះ -ភរិយារបស់គាត់ឈ្មោះហ្សែ​ កូនស្រីឈ្មោះថែលឺ ក្រុមគ្រួសារ និងមិត្តភក្តិទទួលស្គាល់លោកមីឆេល ក្រីឆធុនជាស្វាមីដែលប្រកបដោយភក្តីភាព ជាឪពុកដែលពោរពេញដោយក្តីស្រឡាញ់ និង​ជាកល្យាណមិត្តដែលបំផុសគំនិតរបស់យើងម្នាក់ៗអោយតស៊ូប្រឹងប្រែងដើម្បីមើលឃើញភាពអស្ចារ្យនៃពិភពលោកដោយភ្នែកទាំងគូថ្មីរបស់យើងគ្រប់គ្នា។
  - HYP: បើទោះបីជាពិភពលោកបានស្គាល់គាត់ថាជាអ្នកនិពន្ធរឿងដ៏អស្ចារ្យដែលប្រជែងនឹងគំនិតចាស់របស់ពួកយើងអំពីពិភពលោកជុំវិញពួកយើង និងកំសាន្តដល់ពួកយើងទាំងអស់ ខណៈពេលដែលគាត់ធ្វើដូច្នេះ ប្រពន្ធរបស់គាត់ ស្រីរី កូនស្រី ថេល័រ គ្រួសារ និងមិត្តភក្តិរបស់គាត់បានស្គាល់លោកម៉ៃខល គ្រីតុនថាជាប្តីដ៏ស្មោះត្រង់ ឪពុកដ៏ស្រឡាញ់ និងជាមិត្តដ៏ថ្លៃថ្លៃថ្លៃដែលបានលើកទឹកចិត្តដល់យើងម្នាក់ៗឲ្យខិតខំប្រឹងប្រែងមើលការអស្ចារ្យនៃពិភពលោករបស់យើងតាមរយៈភ្នែក

- **chrF++ 31.0** · `repetition_hallucination`
  - EN: "We have accepted all the recommendations and are examining how best to implement them across our drilling operations worldwide."
  - REF: "យើងបានទទួលយកគ្រប់ការណែនាំទាំងអស់ ហើយកំពុងពិនិត្យពីរបៀបដ៏ល្អបំផុតដើម្បីអនុវត្តវា ឆ្លងកាត់ប្រតិបត្តិការហ្វឹកហាត់ទូទាំងពិភពលោករបស់យើង។"
  - HYP: "ពួកយើងបានទទួលយកនូវការណែនាំទាំងអស់ ហើយពួកយើងកំពុងពិចារណាអំពីវិធីដែលល្អបំផុតក្នុងការអនុវត្តវាទៅលើប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិ


## omission (1 sentences)

- **chrF++ 25.9** · `omission`
  - EN: His funeral was held at a packed in Cairo today.
  - REF: ពិធីបុណ្យសពរបស់គាត់ត្រូវបានប្រារព្ធឡើងនៅកន្លែងមួយដែលមានការចូលរួមពីមនុស្សយ៉ាងច្រើនកុះករ នៅទីក្រុងខារ៉ូ ក្នុងថ្ងៃនេះ។
  - HYP: សពរបស់គាត់ត្រូវបានរៀបចំនៅកន្លែងកកស្ទះនៅកៃរ៉ូថ្ងៃនេះ។


## number_mismatch (4 sentences)

- **chrF++ 35.9** · `number_mismatch`
  - EN: Traralgon's defence held strong as the team went inside their attacking fifty 63 times to Sales 57.
  - REF: កងការពាររបស់ Traralgon បានទប់ទល់យ៉ាងរឹងមាំ នៅពេលដែលក្រុមបានចូលទៅក្នុងតំបន់របស់ពួកគេ ហាសិប 63 ដងទល់នឹង Sale​ 57។
  - HYP: ការការពាររបស់ត្រារ៉ាល់ហ្គូនបានរក្សាភាពរឹងមាំ នៅពេលក្រុមបានចូលទៅក្នុងការវាយប្រហាររបស់ពួកគេហាសិបប្រាំបីបីបីដងទៅក្នុងទីផ្សារ57។

- **chrF++ 33.3** · `number_mismatch`
  - EN: In this series, the Astros won 4 games and the Cardinals won 2 games.
  - REF: ក្នុងការប្រកួតស៊េរីនេះ អាសត្រូសបានយកឈ្នះ 4 ប្រកួត និងកាឌីណលបានយកឈ្នះ 2ប្រកួត។
  - HYP: នៅក្នុងខ្សែក្រវាត់នេះ អាស្ទ្រូសបានឈ្នះបួនប្រកួត និង កាតដិនលបានឈ្នះពីរប្រកួត។

- **chrF++ 34.5** · `number_mismatch`
  - EN: The final series of the baseball season will be the ultimate North American baseball championship, the World Series, a best of 7-games match-up between the American League pennant winner, the Chicago White Sox, and the National League pennant winner, the Houston Astros.
  - REF: ការប្រកួតស៊េរីនៃរដូវកាលកីឡាបាល់បោះចុងក្រោយ នឹងក្លាយជាជើងឯកកីឡាបាល់បោះអាមេរិកខាងជើងចុងក្រោយ ក្នុងការប្រកួតស៊េរីពិភពលោក ដែលជាការប្រកួតដ៏ល្អបំផុតនៃការប្រកួតចំនួន 7 រវាងអ្នកឈ្នះផេននិនសម្ព័ន្ធអាមេរិក ឈីកាហ្គោវ៉ាយ សក និងអ្នកឈ្នះផេននិនសម្ព័ន្ធជាតិ ហោសស្តុន អាសស្ត្រូ។
  - HYP: ការប្រកួតចុងក្រោយនៃរដូវកាលកីឡាបេសបាល់នេះនឹងក្លាយជាជើងឯកកីឡាបេសបាល់អាមេរិកខាងជើងចុងក្រោយ World Series ដែលជាការប្រកួតល្អបំផុតក្នុងចំណោមប្រាំពីរប្រកួតរវាងអ្នកឈ្នះពានរង្វាន់ American League ក្រុម Chicago White Sox និងអ្នកឈ្នះពានរង្វាន់ National League ក្រុម Houston Astros។

- **chrF++ 37.8** · `number_mismatch`
  - EN: Game 1 of the World Series will start Saturday evening.
  - REF: ការប្រកួតទី1 នៃការប្រកួតស៊េរីពិភពលោកនឹងចាប់ផ្តើមនៅលា្ងចថ្ងៃសៅរ៍។
  - HYP: ការប្រកួតទីមួយនៃ World Series នឹងចាប់ផ្តើមនៅល្ងាចថ្ងៃសៅរ៍។


## unseen_source_word (256 sentences)

- **chrF++ 32.0** · `unseen_source_word`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: វាត្រូវបានបញ្ជាក់ថាសេះប្រណាំងពូជស្រស់ប្រាំបីនាក់នៅរង្វង់ប្រណាំងរ៉េនឌីវីក ក្នុងទីក្រុងស៊ីដនីត្រូវបានឆ្លងមេរោគដោយសារជំងឺផ្តាសាយសត្វត្រី។

- **chrF++ 26.8** · `unseen_source_word`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: រ៉េនឌីវីកត្រូវបានបិទហើយត្រូវបានរំពឹងថានឹងស្ថិតនៅក្នុងស្ថានភាពនេះរហូតដល់ពីរខែមុន។

- **chrF++ 28.0** · `unseen_source_word`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: វាត្រូវបានរំពឹងថាការឆ្លងផ្តាសាយធំនឹងប៉ះពាល់ដល់ភាគច្រើននៃសេះចំនួន 700 ដែលត្រូវបានដាក់នៅរ៉េនវីក។

- **chrF++ 31.6** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្រ្តីសំរាប់ឧស្សាហកម្មបឋមនៃ NSW បាននិយាយថា រោងចក្រនេះនឹងត្រូវបានដាក់បង្អែករហូតដល់ 30 ថ្ងៃបន្ទាប់ពីមានសញ្ញានៃគ្រុនផ្តាសាយចុងក្រោយ។

- **chrF++ 29.2** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណីនេះគឺជាការឆ្លងមេរោគលើកដំបូងនៃសេះប្រណាំង ទោះបីជាមានសេះសំរាប់កម្សាន្តជាច្រើននៅទូទាំង NSW និង Queensland ក៏ដោយ។


## lexical_semantic (150 sentences)

- **chrF++ 23.4** · `lexical_semantic`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: ផ្តាសាយធំគឺឆ្លងរាលដាលខ្លាំង ប៉ុន្តែមិនអាចឆ្លងទៅមនុស្សបានទេ។

- **chrF++ 30.2** · `lexical_semantic`
  - EN: The national racing shutdown was costing the industry tens of millions of dollars every day.
  - REF: ការបិទការប្រណាំងថ្នាក់ជាតិ បានធ្វើឲ្យវិស័យនេះខាតបង់រាប់លានដុល្លាក្នុងមួយថ្ងៃៗ។
  - HYP: ការបិទការប្រកួតប្រជែងជាតិនេះបានចំណាយដល់ឧស្សាហកម្មរាប់ទសវត្សរ៍លានដុល្លារជារៀងរាល់ថ្ងៃ។

- **chrF++ 39.8** · `lexical_semantic`
  - EN: Racing is expected to resume in all Australian states except NSW and Queensland on the weekend.
  - REF: កម្មវិធីប្រណាំងត្រូវបានរំពឹងថានឹងប្រព្រឹត្តទូទាំងរដ្ឋនៅប្រទេសអូស្រ្តាលីលើកលែងតែញូវសោវែលនិងឃ្ខីនសាឡេននៅចុងសប្តាហ៍។
  - HYP: ការប្រកួតប្រជែងត្រូវបានរំពឹងថានឹងបន្តនៅគ្រប់រដ្ឋអូស្រ្តាលី លើកលែងតែ NSW និង Queensland នៅចុងសប្តាហ៍នេះ។

- **chrF++ 26.4** · `lexical_semantic`
  - EN: The cup will be ran with special precautions in place to attempt to keep the state free of the virus.
  - REF: ពាន់រង្វាន់នោះត្រូវអនុវត្តដោយប្រុងប្រយ័ត្នបំផុតជាងមុន ធ្វើយ៉ាងណារក្សាស្ថានភាពគ្មានមេរោគ។
  - HYP: កែវនេះនឹងត្រូវធ្វើដំណើរដោយមានការប្រុងប្រយ័ត្នពិសេសដើម្បីព្យាយាមរក្សារដ្ឋនេះនៅសេរីពីមេរោគ។

- **chrF++ 37.1** · `lexical_semantic`
  - EN: The blast happened at 7:18PM, around the time workers change shifts.
  - REF: ការផ្ទុះបានកើតឡើងនៅម៉ោង7:18ល្ងាច ជាពេលវេលាកម្មករប្តូរវេន។
  - HYP: ការផ្ទុះបានកើតឡើងនៅម៉ោង៧និង១៨ រសៀល នៅពេលដែលកម្មករផ្លាស់ប្ដូរម៉ោង។
