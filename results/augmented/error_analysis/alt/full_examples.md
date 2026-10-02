# Error analysis: C: NLLB full fine-tuning

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 1.7** · `repetition_hallucination`
  - EN: New Zealand's Kyle Mills led the bowling attack with 3 for 44.
  - REF: ឃីឡេ មៀលស៍នៃប្រទេសញ៉ូវហ្សេឡង់បាននាំមុខក្នុងការគប់បាល់ 3 ដោយទទួលបាន 44 ពិន្ទុ។
  - HYP: កីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករកីឡាករក

- **chrF++ 4.4** · `repetition_hallucination`
  - EN: A circus elephant managed to escape from her handler on Sunday night in the city of Zurich, Switzerland before being recaptured by local police and circus animal keepers.
  - REF: ដំរីញីសម្តែងសៀក​មួយក្បាល​បានរត់គេចចេញ​ពី​គ្រូបង្វឹក​របស់​វា​នៅយប់​ថ្ងៃអាទិត្យ​ក្នុងទីក្រុងហ្សូរិច ប្រទេស្វីស មុនពេល​ត្រូវចាប់មកជាថ្មី​ដោយ​នគរបាល​មូលដ្ឋាន និង​អ្នករក្សា​សត្វសម្តែងសៀក​។
  - HYP: ទាហានប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រ

- **chrF++ 4.6** · `repetition_hallucination`
  - EN: Australian paceman Michael Kasprowicz finished the match with figures of 4 for 29 from his 4 overs.
  - REF: កីឡាករប្រទេសអូស្ត្រាលីដែលគប់បាល់លឿនលោកមៃខើល ខាសផ្រូវវិកបានបញ្ចប់ការប្រកួតជាមួយនឹងកីឡាករ 4 រូប ដោយបានពិន្ទុ 29 ពីការគប់បាល់ 4 ជុំ។
  - HYP: ខ្សែការពារកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រ

- **chrF++ 4.6** · `repetition_hallucination`
  - EN: Tidal interactions between the planet and its star are pulling them together, and it will likely crash into its star in under one million years.
  - REF: អន្តរកម្មទឹកជោរទឹកនាចរវាងភព និងតារារបស់វាគឺរុញច្រានគ្នាទៅវិញទៅមក ហើយវាអាចនឹងបុកជាមួយតារារបស់វានៅក្នុងរយៈពេលមួយលានឆ្នាំ។
  - HYP: ការប៉ះទង្គិចរលករន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរន្ទះរ

- **chrF++ 5.4** · `repetition_hallucination`
  - EN: Ottawa ultra-runner Ray Zahab, age 39, adventure journalist and architect Kevin Vallely, age 44, of Lynn Valley, North Vancouver and North Pole expeditionist Richard Weber, age 49, said they completed the 700-mile (1,130-kilometer) journey, at 10,000 feet altitude, finally arriving early Wednesday morning.
  - REF: អ្នករត់ក្នុងរយៈចម្ងាយឆ្ងាយរបស់អូតាវ៉ា រ៉េ ហ្សាហាប់ អាយុ 39 ឆ្នាំ អ្នកកាសែតផ្សងព្រេង និងស្ថាបត្យករ ខេវីន វ៉ាលេលី អាយុ 44 ឆ្នាំ របស់លីន វ៉ាឡេ ភាគខាងជើងទីក្រុងវ៉ាន់ឃូវើ និងអ្នកធ្វើដំណើររុករកនៅប៉ូលខាងជើង រីឆាត វ៉េប៊ើ អាយុ 49ឆ្នាំ បាននិយាយថាពួកគេបានបញ្ចប់ការធ្វើដំណើរ 700-ម៉ាយ (1,130-គីឡូម៉ែត្រ) ក្នុងរយៈកម្ពស់ 10,000 ហ្វីត នៅទីបំផុតបានមកដល់ព្រឹកព្រលឹមថ្ងៃពុធ។
  - HYP: អ្នកប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំង

- **chrF++ 6.6** · `repetition_hallucination`
  - EN: Zahab had to pull 170-lb (77-kg) sleds of equipment, traveling on foot and on snowshoes while the other two men skied.
  - REF: ហ្សាហាប់បានទាញគ្រែរំកិលលើទឹកកកទម្ងន់ 170ផាន (77-kg) ធ្វើដំណើរថ្មើជើងនិងដោយពាក់ស្បែកជើងព្រិលខណៈពេលបុរសពីរនាក់ផ្សេងទៀតបានជិះស្គី។
  - HYP: លោកហ្សាហាបត្រូវទាញឧបករណ៍ប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំង

- **chrF++ 7.1** · `repetition_hallucination`
  - EN: For example a visual artist painting a landscape might move a tree to another area of their work, for better balance, or a poet ignoring pentameter when writing a traditional sonnet.
  - REF: ជាឧទាហរណ៍ សិល្បករគូរគំនូរទេសភាពម្នាក់អាចផ្លាស់ទីដើមឈើមួយដើមទៅកាន់កន្លែងផ្សេងទៀតនៃការងាររបស់ពួកគេ ដើម្បីឲ្យមានតុល្យភាពល្អប្រសើរជាងមុន បើមិនអញ្ចឹងទេ កវីនឹងមិនអើពើនឹងកាព្យបញ្ចបាទ ពេលសរសេរកាព្យឃ្លោងតាម ប្រពៃណីមួយ។
  - HYP: ឧទាហរណ៍ សិល្បករទស្សនីយភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាពរូបភាព

- **chrF++ 7.2** · `repetition_hallucination`
  - EN: The trio also suffered altitude sickness, vertigo, massive, painful blisters, and temperatures as low as minus 40.
  - REF: អ្នកទាំងបីក៏បានទទួលរងជំងឺរងសម្ពាធបរិយាកាស វិលមុខ ពងបែកដែលពោរពេញដោយការឈឺចាប់ និងសីតុណ្ហភាពទាបរហូតដល់ដក 40។
  - HYP: ក្រុមបីនាក់នេះក៏បានរងទុក្ខពីជំងឺកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រិតកម្រ

- **chrF++ 8.1** · `repetition_hallucination`
  - EN: In the men's race, Peter Croes (Belgium, Atriac team) and Dirk Bockel (Luxembourg, Celtic Diekirck team) started together for the final 10 kilometre run, but Bockel managed to outrun Croes by 23 seconds, prolonging his victory of last year.
  - REF: នៅក្នុងការប្រណាំងផ្នែកបុរស ភីតធ័រ ក្រូស (ប៊ែលហ្ស៊ិក ក្រុមអាទ្រីអាក) និងដឺក ប៊ុកខែល (លុចសំបួ ក្រុមសែលទិកឌៀខឺក) បានចាប់ផ្តើមរួមគ្នាសម្រាប់ការរត់ចម្ងាយ 10 គីឡូម៉ែត្រវគ្គផ្តាច់ព្រ័ត្រប៉ុន្តែ ប៊ុកខែល បានទទួលជោគជ័យលើការរត់ឈ្នះ ក្រូស រយៈពេល 23 វិនាទី ដោយបន្តជ័យជម្នះរបស់លោកពីឆ្នាំមុនទៀត។
  - HYP: ក្នុងការប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណ

- **chrF++ 10.5** · `repetition_hallucination`
  - EN: In the women's race, the top two athletes remained the same as last year; Elisabeth "Liz" May from Luxembourg managed to stay ahead of a pursuing group the entire race, and finished first ahead of Jessica Mayon.
  - REF: នៅក្នុងការប្រណាំងផ្នែកស្ត្រី អត្តពលិកលំដាប់កំពូលទាំងពីរនៅតែដូចនឹងកាលពីឆ្នាំមុន; អេលីសាបិត "Liz" មេ មកពី លុចសំបួបានទទួលជ័យជំនះនាំមុខក្រុមអ្នកដេញតាមក្នុងការប្រណាំងទាំងមូល និងបានមកដល់ទីមុនជេសីកា ម៉ាយ៉ុន។
  - HYP: ក្នុងការប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណ

- **chrF++ 11.2** · `unseen_source_word`
  - EN: A large police presence watched over the scenes as mourners wept.
  - REF: ប៉ូលីសជាច្រើនបានមានវត្តមាននៅកន្លែងផ្ទាល់ ដើម្បីមើលការខុសត្រូវដល់អ្នកកាន់ទុក្ខដែលបានយំ។
  - HYP: មានសមត្ថភាពនគរបាលធំមួយបានតាមដានលើតំបន់នោះ នៅពេលដែលអ្នកពួងសួងកំពុងស្រែក។

- **chrF++ 12.9** · `repetition_hallucination`
  - EN: Finnish theatrical hard rock band Lordi have released Beast Loose in Paradise - which will be the soundtrack to the band's upcoming horror movie Dark Floors - as a downloadable single.
  - REF: ក្រុមសម្តែងហាដរ៉ក់ហ្វាំងឡង់ឈ្មោះថា Lordi បានចេញបទចម្រៀងមានឈ្មោះថា Beast Loose in Paradise - ដែលនឹងជាបទចម្រៀងនៅក្នុងភាពយន្តរន្ធត់ញាប់ញ័រដែលនឹងដាក់បញ្ចាំងនៅក្នុងពេលឆាប់ៗនេះឈ្មោះ Dark Floors ដែលជាចម្រៀងអាចដោនឡូតបាន។
  - HYP: ក្រុមចម្រៀងហាដរ៉ុកហ្វាំងឡង់ឡូឌី បានចេញបទ "សត្វស្លាបនៅក្នុងផារ៉ាឌីស" ដែលជាសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងសម្លេងស

- **chrF++ 13.4** · `lexical_semantic`
  - EN: In addition to transport disruption, a number of sports have been affected.
  - REF: បន្ថែម​លើស​ពី​ការ​អាក់​ខាន​នៃ​មធ្យោបាយ​ធ្វើ​ដំណើរ​ កីឡា​ជា​ច្រើន​ប្រភេទ​បានរងផល​ប៉ះពាល់ផងដែរ​។
  - HYP: ក្រៅពីការរំខានដឹកជញ្ជូន កីឡាជាច្រើនត្រូវបានប៉ះពាល់។

- **chrF++ 13.5** · `repetition_hallucination`
  - EN: To further the "flying Peter Pan" motif, models donned such designs as a chiffon dress with ostrich feathers and a taffeta gown with a feather waistband.
  - REF: ដើម្បីបន្តតាមគំរូ "ភីតធើភែនដែលហោះ" តារាម៉ូដែលស្លៀកសម្លៀកបំពាក់ម៉ូតផ្សេងៗដូចសំពត់ស្ដើង ដែលមានស្លាបសត្វអូទ្រីស និងសំពត់សូត្រដែលមានស្លាបនៅលើត្រង់ផ្នែកចង្កេះ។
  - HYP: ដើម្បីបង្កើនភាព "ហោះហើរភីតធើផេន" ម៉ូដែលបានពាក់នូវរចនាប័ទ្មដូចជារ៉ូបខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌តាហ្វេតាពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវពណ៌ខោអាវព

- **chrF++ 15.3** · `unseen_source_word`
  - EN: Dannie Abse is well-known for being a poet and a medical doctor.
  - REF: លោកដានី អាប់សេ ល្បីឈ្មោះជាកវី​តែងកំណាព្យ និង​ជាវេជ្ជបណ្ឌិត​ផ្នែកវេជ្ជសាស្រ្ត​។
  - HYP: ឌានី អាបសេ ត្រូវបានគេស្គាល់ថាជាកំណាព្យករ និងជាគ្រូពេទ្យ។


## repetition_hallucination (32 sentences)

- **chrF++ 16.2** · `repetition_hallucination`
  - EN: The explosions sent flaming debris into the air and onto buildings and expressways.
  - REF: ការផ្ទុះនេះបានបញ្ជូនកំទេចអណ្តាតភ្លើងទៅក្នុងខ្យល់និងទៅក្នុងអគារនិងអ៊ិចប្រេសវេ។
  - HYP: ការផ្ទុះបានបញ្ជូនកម្ទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទេចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចកំទីចក

- **chrF++ 30.3** · `repetition_hallucination`
  - EN: "His commitment to Egypt's national unity is also a testament to what can be accomplished when people of all religions and creeds work together."
  - REF: "កិច្ចប្រឹងប្រែងរបស់គាត់ចំពោះការបង្រួបបង្រួមជាតិរបស់ប្រទេសអេហ្សីប គឺជាការបញ្ជាក់អំពីអ្វីដែលអ្នកប្រតិបត្តិសាសនា និងជំនឿទាំងអស់អាចបំពេញការងារជាមួយគ្នា។"
  - HYP: "ការប្តេជ្ញាចិត្តរបស់គាត់ចំពោះការសាមគ្គីជាតិរបស់ប្រទេសអេហ្ស៊ីបក៏ជាភស្តុតាងមួយសំរាប់អ្វីដែលអាចបំពេញបាននៅពេលដែលមនុស្សនៃសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសនានិងសាសន

- **chrF++ 32.4** · `repetition_hallucination`
  - EN: "We have accepted all the recommendations and are examining how best to implement them across our drilling operations worldwide."
  - REF: "យើងបានទទួលយកគ្រប់ការណែនាំទាំងអស់ ហើយកំពុងពិនិត្យពីរបៀបដ៏ល្អបំផុតដើម្បីអនុវត្តវា ឆ្លងកាត់ប្រតិបត្តិការហ្វឹកហាត់ទូទាំងពិភពលោករបស់យើង។"
  - HYP: "យើងបានទទួលនូវសេចក្តីណែនាំទាំងអស់ ហើយកំពុងពិនិត្យអំពីវិធីដែលល្អបំផុតក្នុងការអនុវត្តវានៅទូទាំងប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រតិបត្តិនៃប្រ

- **chrF++ 37.9** · `repetition_hallucination`
  - EN: The oil company has previously blamed Transocean and Halliburton, the well contractor, for the disaster and BP executives feel they have been unfairly blamed by US politicians for the disaster, and the report continues this view.
  - REF: ក្រុមហ៊ុនប្រេងកាលពីដំបូងបានធ្វើការស្តីបន្ទោសក្រុមហ៊ុនត្រានអូសិន និងហាលិប៊ូតុន ដែលជាក្រុមហ៊ុនម៉ៅការអណ្តូង ពីមហន្តរាយ និងអ្នកកាន់កាប់ប៊ីភីមានអារម្មណ៍ថាពួកគេទទួលការស្តីបន្ទោសពីអ្នកនយោបាយអាមេរិកដោយមិនសមហេតុផលអំពីគ្រោះមហន្តរាយនេះ ហើយរបាយ ការណ៍បន្តមើលពីហេតុការណ៍នេះ។
  - HYP: ក្រុមហ៊ុនប្រេងនេះបានចោទប្រកាន់ពីមុនថា ក្រុមហ៊ុនត្រាំងសូស៊ីន និងហាលីប៊ឺតុន ដែលជាអ្នកម៉ៅការប្រេងប្រេងប្រេងនេះបានទទួលគ្រោះមហន្តរាយនេះ ហើយអ្នកគ្រប់គ្រងក្រុមហ៊ុនប៊ីប៊ីមានអារម្មណ៍ថាពួកគេត្រូវបានចោទប្រកាន់ដោយអយុត្តិធម៌ដោយអ្នកនយោបាយសហរដ្ឋអាមេរិកចំពោះគ្រោះមហន្តរាយនេះ ហើយរបាយការណ៍នេះបន្តទស្សនៈនេះ។

- **chrF++ 15.7** · `repetition_hallucination`
  - EN: The report blames the type of cement used by Halliburton, designed to prevent harmful hydrocarbons from reaching the seabed, as well as criticizing the crew of Deepwater Horizon, for failing to realize for forty minutes that oil had started to leak from the well, and once it was realized, the crew "vented" the hydrocarbons "directly onto the rig".
  - REF: របាយការណ៍បានបន្ទោសប្រភេទស៊ីម៉ង់ត៍ដែលប្រើប្រាស់ដោយ ហាលីប៊ូតុនដើម្បីការពារហាយដ្រូកាបោនដ៏គ្រោះថ្នាក់ពីការទៅដល់បាតសមុទ្រ ព្រមទាំងរិះគន់ក្រុមបុគ្គលិក ឌិបវរ័ធើហរីហ្សិន អំពីការបរាជ័យមិនបានដោះស្រាយនូវការចាប់ផ្តើមលិចប្រងរយៈពេលសែសិបនាទីពីអណ្តូង ហើយនៅពេលដែលគេដឹង ក្រុមបុគ្គលិក "បានបញ្ចេញ" ហាយដ្រូកាបោន "ដោយផ្ទាល់ទៅលើហេដ្ឋារចនាសម្ព័ន្ធ។"
  - HYP: របាយការណ៍នេះបានចោទប្រកាន់លើប្រភេទសីតុណ្ហភាពដែលត្រូវបានប្រើដោយហាលីប៊ឺតុន ដែលត្រូវបានរចនាឡើងដើម្បីការពារកាបូអ៊ីដ្រូកាប៊ូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ្រូអេដ


## number_mismatch (1 sentences)

- **chrF++ 39.5** · `number_mismatch`
  - EN: "In the past eight days alone we have received reports on the killing of one journalist, Munir Shakir, in Balochistan on August 14 2011, and the disappearance of another journalist, Rehmatullah Daparkhel, three days earlier in North Waziristan on August 11," said spokesperson for the United Nations High Commissioner for Human Rights, Rupert Colville.
  - REF: ត្រឹមតែ8ថ្ងៃចុងក្រោយនេះ យើងបានទទួលរបាយការណ៍អំពីការសំលាប់អ្នកសារព័តិមានម្នាក់ឈ្មោះមុនាសាគា នៅប្រទេសបាឡូគីស្ថាននៅថ្ងៃទី14ខែសីហាឆ្នាំ2011 និងការបាត់ខ្លួនរបស់អ្នកសារព័តិមានម្នាក់ទៀតឈ្មោះរេម៉ាទុឡា ដាប៉ាខេល 3ថ្ងៃមុននោះនៅភាគខាងជើងនៃតំបន់វ៉ាហ្ស៊ីរីស្ថាននៅថ្ងៃទី11ខែសីហា នេះបើយោងតាមអ្នកនាំពាក្យនៃអង្គការត្រួតពិនិត្យសិទិ្ធមនុស្សជាន់ខ្ពស់នៃអង្គការសហប្រជាជាតិ លោករូភើត ខូវីល។
  - HYP: អ្នកនាំពាក្យរបស់មន្រ្តីជាន់ខ្ពស់អង្គការសហប្រជាជាតិសំរាប់សិទ្ធិមនុស្ស រ៉ូបឺត ខូលវីល បានមានប្រសាសន៍ថា "ក្នុងរយៈពេលប្រាំបីថ្ងៃកន្លងមកនេះយើងបានទទួលរបាយការណ៍អំពីការសម្លាប់អ្នកកាសែតម្នាក់ ឈ្មោះ មូនីរ សាគីរ នៅបាឡូឈីស្តង់ នៅថ្ងៃទី14 ខែសីហា ឆ្នាំ2011 និងការបាត់ខ្លួនអ្នកកាសែតម្នាក់ទៀត ឈ្មោះ រ៉េមាតុលឡា ដាផាកេឡ កាលពីបីថ្ងៃមុននៅប្រទេសវ៉ាហ្ស៊ីរីស្តង់ខាងជើង


## unseen_source_word (272 sentences)

- **chrF++ 31.0** · `unseen_source_word`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: វាត្រូវបានបញ្ជាក់ថាសេះប្រណាំងពូជស្រស់ប្រាំបីនាក់នៅរង្វង់រត់រ៉េនឌីវីកនៅស៊ីដនីត្រូវបានឆ្លងមេរោគផ្តាសាយសេះ។

- **chrF++ 19.6** · `unseen_source_word`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: រ៉េនឌ្វីកត្រូវបានបិទទ្វារ ហើយគេរំពឹងថានឹងបន្តធ្វើបែបនេះរហូតដល់ពីរខែ។

- **chrF++ 34.9** · `unseen_source_word`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: វាត្រូវបានរំពឹងថាការឆ្លងមេរោគផ្តាសាយធំនឹងប៉ះពាល់ដល់ភាគច្រើននៃសេះ700ក្បាលដែលស្ថិតនៅរេនដវីក។

- **chrF++ 31.7** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្រ្តីរដ្ឋ NSW សម្រាប់ឧស្សាហកម្មអប្បបរមាបាននិយាយថា រោងចក្រនេះនឹងត្រូវបានដាក់ឲ្យនៅដាច់ដោយឡែករហូតដល់30ថ្ងៃបន្ទាប់ពីមានសញ្ញានៃគ្រុនផ្តាសាយចុងក្រោយ។

- **chrF++ 29.1** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណីនេះគឺជាការឆ្លងមេរោគលើកដំបូងនៃសេះប្រណាំង ទោះបីជាមានសេះសំរាប់កម្សាន្តជាច្រើនដូសនៅទូទាំង NSW និងរដ្ឋ Queensland ក៏ដោយ។


## lexical_semantic (153 sentences)

- **chrF++ 29.2** · `lexical_semantic`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: មេរោគផ្តាសាយគឺឆ្លងរាលដាលខ្លាំង ប៉ុន្តែមិនអាចឆ្លងទៅកាន់មនុស្សបានទេ។

- **chrF++ 31.4** · `lexical_semantic`
  - EN: The national racing shutdown was costing the industry tens of millions of dollars every day.
  - REF: ការបិទការប្រណាំងថ្នាក់ជាតិ បានធ្វើឲ្យវិស័យនេះខាតបង់រាប់លានដុល្លាក្នុងមួយថ្ងៃៗ។
  - HYP: ការបិទការប្រកួតប្រជែងជាតិបានចំណាយដល់ឧស្សាហកម្មរាប់ទសវត្សរ៍លានដុល្លារជារៀងរាល់ថ្ងៃ។

- **chrF++ 25.2** · `lexical_semantic`
  - EN: The cup will be ran with special precautions in place to attempt to keep the state free of the virus.
  - REF: ពាន់រង្វាន់នោះត្រូវអនុវត្តដោយប្រុងប្រយ័ត្នបំផុតជាងមុន ធ្វើយ៉ាងណារក្សាស្ថានភាពគ្មានមេរោគ។
  - HYP: កែវនេះនឹងត្រូវដំណើរការដោយមានការប្រុងប្រយ័ត្នពិសេសដើម្បីព្យាយាមរក្សារដ្ឋនេះនៅសេរីពីមេរោគ។

- **chrF++ 35.2** · `lexical_semantic`
  - EN: A magnitude 5.8 earthquake has struck in a place where earthquakes are rare, but sometimes large.
  - REF: រញ្ជួយផែនដីទំហំ5.8 បានកើតឡើងនៅកន្លែងមួយដែលកំរមានការរញ្ជួយ ប៉ុន្តែពេលខ្លះមានទំហំធំ។
  - HYP: ការរញ្ជួយដីដែលមានកម្រិត 5.8 បានវាយប្រហារនៅកន្លែងដែលរញ្ជួយដីគឺកម្រ ប៉ុន្តែពេលខ្លះធំ។

- **chrF++ 39.9** · `lexical_semantic`
  - EN: Had any civilization existed on the frozen ice cap, the USGS says that damage could be "light to moderate."
  - REF: បើមានពពួកមានជីវិតនៅលើផ្ទាំងទឹកកក USGSនិយាយថាការខូចខាតអាចពី "ស្រាលទៅមធ្យម។"
  - HYP: បើសិនជាមានអរិយធម៌ណាមួយមាននៅលើទឹកកកកកកស្ទះ USGS និយាយថា ការខូចខាតអាច "មានភាពស្រាលដល់មធ្យម។"
