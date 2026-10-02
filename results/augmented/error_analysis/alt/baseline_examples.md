# Error analysis: Zero-shot NLLB-600M (reference)

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 1.2** · `omission`
  - EN: The new “price indexing” formula will reduce individual benefits and overall Social Security outlays because the inflation rate typically is much lower than the rise in wages.
  - REF: រូបមន្ត "កំណត់សន្ទទស្សន៍តម្លៃ" ថ្មីនឹងកាត់បន្ថយអត្ថប្រយោជន៍បុគ្គលិកម្នាក់ៗ និងប្រាក់ចំណាយលើរបបសន្តិសុខសង្គម ដោយសារអត្រាអតិផរណាជាទូទៅ មានកម្រិតទាបខ្លាំងជាងការបង្កើនលើប្រាក់ឈ្នួល។
  - HYP: រចនាសម្ព័ន្ធ

- **chrF++ 2.5** · `omission`
  - EN: A large police presence watched over the scenes as mourners wept.
  - REF: ប៉ូលីសជាច្រើនបានមានវត្តមាននៅកន្លែងផ្ទាល់ ដើម្បីមើលការខុសត្រូវដល់អ្នកកាន់ទុក្ខដែលបានយំ។
  - HYP: ការ សោក ស្តាយ

- **chrF++ 3.0** · `repetition_hallucination`
  - EN: In fact, the state's lottery system, for reasons still not known, went off-line at 10:25 p.m., just over a half hour before the drawing was to be held.
  - REF: ជាការពិត ប្រព័ន្ធឆ្នោតផ្សងសំណាងរបស់រដ្ឋ ដែលមិនមានអ្នកណាដឹងពីមូលហេតុ ត្រូវបានឈប់ទទួលនៅម៉ោង 10:25 នាទីយប់ គឺត្រឹមតែកន្លះម៉ោងមុនការចាប់ឆ្នោតត្រូវបានធ្វើឡើង។
  - HYP: ការ លេង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល្បែង ល

- **chrF++ 3.0** · `repetition_hallucination`
  - EN: Finnish theatrical hard rock band Lordi have released Beast Loose in Paradise - which will be the soundtrack to the band's upcoming horror movie Dark Floors - as a downloadable single.
  - REF: ក្រុមសម្តែងហាដរ៉ក់ហ្វាំងឡង់ឈ្មោះថា Lordi បានចេញបទចម្រៀងមានឈ្មោះថា Beast Loose in Paradise - ដែលនឹងជាបទចម្រៀងនៅក្នុងភាពយន្តរន្ធត់ញាប់ញ័រដែលនឹងដាក់បញ្ចាំងនៅក្នុងពេលឆាប់ៗនេះឈ្មោះ Dark Floors ដែលជាចម្រៀងអាចដោនឡូតបាន។
  - HYP: ក្រុម តារា ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេម ហ្គេ

- **chrF++ 3.5** · `repetition_hallucination`
  - EN: Torrential rains have been plaguing the nine southernmost provinces of the country for nearly two weeks and further downpours are forecast for later this week.
  - REF: ទឹកភ្លៀងតូរេនធៀលបានរំខានដល់ខេត្តនៃភាគខាងត្បូងចំនួនប្រាំបួននៃប្រទេសនេះជិតពីរសប្តាហ៍ និងទឹកភ្លៀងខ្លាំងបន្ថែមទៀតត្រូវបានព្យាករណ៍ថានឹងមកដល់នៅចុងសប្តាហ៍នេះ។
  - HYP: ភ្លៀង ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ្លាក់ ធ

- **chrF++ 3.9** · `omission`
  - EN: After he had repeated this publicly, he was arrested and charged with apostasy.
  - REF: បន្ទាប់ពីលោកបានប្រព្រឹត្តដូច្នេះម្តងហើយម្តងទៀតជាសាធារណៈ លោកត្រូវបានចាប់ខ្លួន និងចោទប្រកាន់ពីបទក្បត់សាសនា។
  - HYP: ១៧ . តើ ព្រះ យេហូវ៉ា បាន ធ្វើ អ្វី?

- **chrF++ 4.8** · `repetition_hallucination`
  - EN: Shenouda spent 40 years as pope to the Coptics, who make up the majority of the nation's estimated ten million Christians.
  - REF: សេននូដា បានចំណាយពេល40ឆ្នាំ បម្រើការជាសម្តេចប៉ាបនៅខូបស្ទីក មានអ្នកកាន់គ្រិស្តសាសនាភាគច្រើនក្នុងប្រទេសនេះដែលប៉ាន់ស្មានថាមានរហូតដល់ដប់លាននាក់។
  - HYP: ព្រះមហាក្សត្រ នៃ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះ

- **chrF++ 6.6** · `repetition_hallucination`
  - EN: Had any civilization existed on the frozen ice cap, the USGS says that damage could be "light to moderate."
  - REF: បើមានពពួកមានជីវិតនៅលើផ្ទាំងទឹកកក USGSនិយាយថាការខូចខាតអាចពី "ស្រាលទៅមធ្យម។"
  - HYP: ប្រសិន បើ មាន វប្បធម៌ ណា មួយ កើត មាន នៅ លើ ក្រពះ កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត ក

- **chrF++ 6.8** · `repetition_hallucination`
  - EN: The trio also suffered altitude sickness, vertigo, massive, painful blisters, and temperatures as low as minus 40.
  - REF: អ្នកទាំងបីក៏បានទទួលរងជំងឺរងសម្ពាធបរិយាកាស វិលមុខ ពងបែកដែលពោរពេញដោយការឈឺចាប់ និងសីតុណ្ហភាពទាបរហូតដល់ដក 40។
  - HYP: ក្រុម ៣ នាក់ នេះ ក៏ បាន រង ការ ឈឺ ជំងឺ កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត

- **chrF++ 6.8** · `repetition_hallucination`
  - EN: In the men's race, Peter Croes (Belgium, Atriac team) and Dirk Bockel (Luxembourg, Celtic Diekirck team) started together for the final 10 kilometre run, but Bockel managed to outrun Croes by 23 seconds, prolonging his victory of last year.
  - REF: នៅក្នុងការប្រណាំងផ្នែកបុរស ភីតធ័រ ក្រូស (ប៊ែលហ្ស៊ិក ក្រុមអាទ្រីអាក) និងដឺក ប៊ុកខែល (លុចសំបួ ក្រុមសែលទិកឌៀខឺក) បានចាប់ផ្តើមរួមគ្នាសម្រាប់ការរត់ចម្ងាយ 10 គីឡូម៉ែត្រវគ្គផ្តាច់ព្រ័ត្រប៉ុន្តែ ប៊ុកខែល បានទទួលជោគជ័យលើការរត់ឈ្នះ ក្រូស រយៈពេល 23 វិនាទី ដោយបន្តជ័យជម្នះរបស់លោកពីឆ្នាំមុនទៀត។
  - HYP: ក្នុង ការ ប្រកួត ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់ ប្រដាល់

- **chrF++ 8.0** · `repetition_hallucination`
  - EN: The previous record for the highest multi-state lottery was set back in 2006 when the Power Ball jackpot paid out at least $365 million dollars to eight people in Nebraska.
  - REF: កំណត់ត្រាកន្លងទៅចំពោះឆ្នោតរដ្ឋចម្រុះដែលខ្ពស់បំផុតបានឈ្នះក្នុងឆ្នាំ 2006 នៅពេលរង្វាន់ធំបល ផៅវើ បានទូទាត់យ៉ាងហោចណាស់អស់ចំនួន $365 លានដុល្លារ ទៅមនុស្សចំនួនប្រាំបីនាក់ក្នុងនេប្រាស្កា។
  - HYP: កំណត់ត្រា កន្លងមក សម្រាប់ ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្បី ល្ប

- **chrF++ 8.2** · `wrong_script`
  - EN: However tries from Brendon Leonard, Nick Evans, Andrew Ellis, Leon MacDonald, Carl Hayman and two from Conrad Smith completed New Zealand's victory.
  - REF: ប៉ុន្តែ ការរកបានពិន្ទុពីកីឡាករ ប្រេនដុន លីអូណាត កីឡាករ និក អ៊ីវិន កីឡាករ អេនឌ្រូ អ៊ីលលីស កីឡាករ លីអូង ម៉ាកដូណល កីឡាករ កាល់ ហេមេន និងពីរពិន្ទុពីកីឡាករ កុងរ៉ាដ ស្មីត បានបញ្ចប់ ដោយក្រុមញូវហ្ស៊េលែនទទួលបានជ័យជំនះ។
  - HYP: ទោះ ជា យ៉ាង ណា ការ ព្យាយាម របស់ Brendon Leonard, Nick Evans, Andrew Ellis, Leon MacDonald, Carl Hayman និង ពីរ នាក់ ពី Conrad Smith បាន បញ្ចប់ ជ័យជម្នះ របស់ New Zealand ។

- **chrF++ 8.4** · `unseen_source_word`
  - EN: Dannie Abse is well-known for being a poet and a medical doctor.
  - REF: លោកដានី អាប់សេ ល្បីឈ្មោះជាកវី​តែងកំណាព្យ និង​ជាវេជ្ជបណ្ឌិត​ផ្នែកវេជ្ជសាស្រ្ត​។
  - HYP: Dannie Abse ត្រូវបានគេស្គាល់ថាជាកំប្លែង និងជាគ្រូពេទ្យ។

- **chrF++ 8.6** · `repetition_hallucination`
  - EN: And hard-throwing closer Brad Lidge will be refreshed physically and mentally after an exhausting stretch.
  - REF: ហើយលោកប្រេត លិច្ច ដែលជាអ្នកគប់បាល់ដ៏ប៉ិនប្រសប់ នឹងត្រូវមានអារម្មណ៍ស្រស់ថ្លាទាំងរាងកាយ និងផ្លូវចិត្តក្រោយពីការហាត់ប្រាណឱ្យយឺតសសៃ។
  - HYP: ហើយ Brad Lidge ដែល ប្រឈម នឹង ការ ប្រឈម មុខ នឹង ការ ប្រកប របរ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្ចាត់ កម្

- **chrF++ 9.3** · `unseen_source_word`
  - EN: Former Tag Team Champion Matt Hardy and WWE legend Mick Foley paid tributes to Cade.
  - REF: អតីតជើងឯក Tag Team ម៉ាត់ ហាឌី និងកីឡាករល្បីឈ្មោះនៃ WWE មិក ហ្វឡេយ បានសម្តែងការគោរពចំពោះកេដ។
  - HYP: អតីត ខ្សែប្រយុទ្ធ Matt Hardy និង WWE Legend Mick Foley បាន ថ្លែងអំណរគុណ ដល់ Cade ។


## wrong_script (7 sentences)

- **chrF++ 11.1** · `wrong_script`
  - EN: Hepburn's government legacy includes the Queen Elizabeth Way and Rainbow Bridge to Niagara Falls, New York.
  - REF: កេរ្តី៏ដំណែលរដ្ឋាភិបាល ហេភបឺន រួមមានដូចជា មហាវិថីព្រះមហាក្សត្រត្រិយ៍អេលីហ្សាបែត និង ស្ពានឥន្ទធនូទៅកាន់ទឹកជ្រោះនាហ្គារ៉ា ក្រុងញ៉ូយ៉ក។
  - HYP: បេតិកភណ្ឌ រដ្ឋាភិបាល របស់ Hepburn រួមមាន Queen Elizabeth Way និង Rainbow Bridge ទៅ Niagara Falls, New York ។

- **chrF++ 14.7** · `wrong_script`
  - EN: He also published The Andromeda Strain, Congo, Rising Sun, Timeline, Eaters of the Dead, all of which became major motion pictures.
  - REF: លោកក៏បានបោះពុម្ពរឿងអេដ្រូមាដា ស្ត្រេន រឿងកុងហ្គូ រឿងរាយស៊ីង សាន់ រឿងថាមឡាញ រឿងអ៊ីស្ទឺ អហ្វ ដឹ ដេដថ៍ ដែលរឿងទាំងនេះបានក្លាយជាគំនូរជីវចលដ៏សំខាន់។
  - HYP: លោក ក៏បាន បោះពុម្ពផ្សាយ The Andromeda Strain, Congo, Rising Sun, Timeline, Eaters of the Dead ដែល បាន ក្លាយជា ខ្សែភាពយន្ត ធំៗ

- **chrF++ 15.6** · `wrong_script`
  - EN: Chicago Fire plays the winner of the New England Revolution/New York Red Bulls 2 Leg affair which is currently tied 0-0.
  - REF: ក្រុមឈីខាហ្គូនឹងជួបក្រុមឈ្នះរវាងក្រុមញូ អ៊ីនឡេន រីវ៉ូលូសុន/ញូយ៉ក រេត ប៊ូល 2ជើងដែលបច្ចុប្បន្នមានពន្ទុស្មើ 0-0។
  - HYP: Chicago Fire ប្រកួត ជា ម្ចាស់ ជ័យជម្នះ នៃ ការ ប្រកួត New England Revolution / New York Red Bulls 2 Leg affair ដែល បច្ចុប្បន្ន ស្មើ 0-0.

- **chrF++ 25.7** · `wrong_script`
  - EN: As well as LACFD, firefighters from Los Angeles City Fire Department, California Department of Forestry and Fire Protection (Cal Fire) are also helping to battle the fire.
  - REF: ជាមួយគ្នានេះដែរ LACFD អ្នកពន្លត់អគ្គីភ័យមកពីក្រសួងអគ្គិភ័យទីក្រុងឡូសអេនជើឡេស ក្រសួងការពារព្រៃឈើ និងអគ្គិភ័យកាលីហ្វរនីញ៉ា (Cal Fire) ក៏កំពុងជួយដល់ការប្រយុទ្ធជាមួយអគ្គិភ័យនេះដែរ។
  - HYP: ក៏ដូចជា LACFD, ក្រុមអគ្គិភ័យពី Los Angeles City Fire Department, California Department of Forestry and Fire Protection (Cal Fire) ក៏កំពុងជួយប្រយុទ្ធប្រឆាំងនឹងភ្លើង។

- **chrF++ 19.2** · `wrong_script`
  - EN: Residents of Leona Valley, Lake Elizabeth, Ritter Ranch, Rancho Vista, Ana Verde and Palmdale received Reverse 911 telephone calls last night alerting them of mandatory evacuations.
  - REF: ប្រជាជនតំបន់លីអូណា វ៉ាឡេ, ឡេក អ៊ីលីហ្សាប៊េត, រីធើ រ៉ាន, រ៉េនចូ វីស្តា, អាណា វែត និងផាមដាល់ បានទទួលការហៅទូរស័ព្ទ 911 យប់មិញ ដោយក្រើនរំឭកពួកគេពីការជម្លៀសជាចាំបាច់។
  - HYP: ពលរដ្ឋ នៅ Leona Valley, Lake Elizabeth, Ritter Ranch, Rancho Vista, Ana Verde និង Palmdale បាន ទទួល ទូរស័ព្ទ Reverse 911 កាល ពី យប់ មិញ ព្រមាន ពួក គេ អំពី ការ ជម្លៀស បង្ខំ។


## repetition_hallucination (39 sentences)

- **chrF++ 33.2** · `repetition_hallucination`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: ត្រូវ បាន បញ្ជាក់ ថា សេះ ប្រណាំង ប្រណាំង ពូជ ស្រស់ ៨ នាក់ នៅ Randwick Racecourse នៅ ក្នុង ទីក្រុង ស៊ីដនី បាន ឆ្លង ជំងឺ ផ្តាសាយ សត្វ សត្វ សត្វ ស្លាប។

- **chrF++ 6.6** · `repetition_hallucination`
  - EN: Had any civilization existed on the frozen ice cap, the USGS says that damage could be "light to moderate."
  - REF: បើមានពពួកមានជីវិតនៅលើផ្ទាំងទឹកកក USGSនិយាយថាការខូចខាតអាចពី "ស្រាលទៅមធ្យម។"
  - HYP: ប្រសិន បើ មាន វប្បធម៌ ណា មួយ កើត មាន នៅ លើ ក្រពះ កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត កម្រិត ក

- **chrF++ 4.8** · `repetition_hallucination`
  - EN: Shenouda spent 40 years as pope to the Coptics, who make up the majority of the nation's estimated ten million Christians.
  - REF: សេននូដា បានចំណាយពេល40ឆ្នាំ បម្រើការជាសម្តេចប៉ាបនៅខូបស្ទីក មានអ្នកកាន់គ្រិស្តសាសនាភាគច្រើនក្នុងប្រទេសនេះដែលប៉ាន់ស្មានថាមានរហូតដល់ដប់លាននាក់។
  - HYP: ព្រះមហាក្សត្រ នៃ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះរាជាណាចក្រ ព្រះ

- **chrF++ 12.8** · `repetition_hallucination`
  - EN: Shenouda was dressed in full regalia, complete with a gold crown.
  - REF: សេននូដា ត្រូវបានគេស្លៀកពាក់អោយក្នុងសំលៀកបំពាក់រាជា ជាមួយនឹងម្កុជមាស។
  - HYP: លោក Shenouda មាន សម្លៀកបំពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ស្លៀកពាក់ ម

- **chrF++ 27.8** · `repetition_hallucination`
  - EN: This visit would make the first Papal visit to the UK since Pope John Paul II's visit in 1982.
  - REF: ការទស្សនកិច្ចធ្វើអោយមេដឹកនាំវិហារកាតូលិក រ៉ូមែនទស្សនាចក្រភពអង់គ្លេសលើកទីមួយ ចាប់តាំងពីទស្សនកិច្ចរបស់ផូប ចន ភលទីពីរ ក្នុងឆ្នាំ1982។
  - HYP: ដំណើរ ទស្សនកិច្ច នេះ នឹង ក្លាយ ជា ដំណើរ ទស្សនកិច្ច របស់ ប៉ា ប៉ា ប៉ា ដំបូង មក កាន់ ប្រទេស អង់គ្លេស ចាប់ តាំង ពី ដំណើរ ទស្សនកិច្ច របស់ ប៉ា ប៉ា យ៉ូ ន ប៉ុល ទី ២ នៅ ឆ្នាំ ១៩៨២។


## omission (8 sentences)

- **chrF++ 23.7** · `omission`
  - EN: His funeral was held at a packed in Cairo today.
  - REF: ពិធីបុណ្យសពរបស់គាត់ត្រូវបានប្រារព្ធឡើងនៅកន្លែងមួយដែលមានការចូលរួមពីមនុស្សយ៉ាងច្រើនកុះករ នៅទីក្រុងខារ៉ូ ក្នុងថ្ងៃនេះ។
  - HYP: សព របស់ គាត់ ត្រូវ បាន រៀបចំ ឡើង នៅ ទីក្រុង កាហ្វេ នៅ ថ្ងៃ នេះ។

- **chrF++ 2.5** · `omission`
  - EN: A large police presence watched over the scenes as mourners wept.
  - REF: ប៉ូលីសជាច្រើនបានមានវត្តមាននៅកន្លែងផ្ទាល់ ដើម្បីមើលការខុសត្រូវដល់អ្នកកាន់ទុក្ខដែលបានយំ។
  - HYP: ការ សោក ស្តាយ

- **chrF++ 26.2** · `omission`
  - EN: "He left us an example of leadership that we should all follow," a cleric told the congregation at the fourth-century cathedral.
  - REF: "គាត់បានបន្សល់ទុកនូវគំរូនៃភាពជាអ្នកដឹកនាំដែលយើងទាំងអស់គួរតែអនុវត្តតាម" បរិស័ទម្នាក់បានប្រាប់ទៅអង្គជំនុំសាសនានៅព្រះវិហារសតវត្សរ៍ទីបួន។
  - HYP: "គាត់ បាន ទុក គំរូ នៃ ការ ដឹកនាំ ដែល យើង ទាំងអស់ គ្នា គួរ តែ ធ្វើ តាម"

- **chrF++ 13.0** · `omission`
  - EN: However, other records from the former Soviet Union place his age at 70.
  - REF: ទោះជាយ៉ាងណាក៏ដោយ ការផ្សាយផ្សេងៗពីអតីតសហភាពសូវៀតបានដាក់ថាគាត់មានអាយុ 70 ឆ្នាំ។
  - HYP: ១៧. តើ លោក មាន អាយុ ៧០ ឆ្នាំ ឬ យ៉ាង ណា?

- **chrF++ 3.9** · `omission`
  - EN: After he had repeated this publicly, he was arrested and charged with apostasy.
  - REF: បន្ទាប់ពីលោកបានប្រព្រឹត្តដូច្នេះម្តងហើយម្តងទៀតជាសាធារណៈ លោកត្រូវបានចាប់ខ្លួន និងចោទប្រកាន់ពីបទក្បត់សាសនា។
  - HYP: ១៧ . តើ ព្រះ យេហូវ៉ា បាន ធ្វើ អ្វី?


## number_mismatch (97 sentences)

- **chrF++ 15.5** · `number_mismatch`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: Randwick ត្រូវ បាន បិទ បញ្ចប់ ហើយ គេ រំពឹង ថា នឹង នៅ តែ ដូច្នោះ រហូត ដល់ ២ ខែ។

- **chrF++ 32.7** · `number_mismatch`
  - EN: He said that $100 dollars per barrel was a "fair" price and remembered that when he assumed presidency of Venezuela in 1999, the price went up to about ten dollars.
  - REF: គាត់បាននិយាយថា 100ដុល្លារក្នុងមួយធុងគឺជាតំលៃមួយ"សមរម្យ" ហើយបានចងចាំថា នៅពេលគាត់ត្រលប់មើលទៅសម័យប្រធានាធិបតីនៃវ៉េណាសួអេឡានៅក្នុងឆ្នាំ1999 តំលៃគឺឡើងទៅដល់ប្រហែលដប់ដុល្លារ។
  - HYP: លោក បាន និយាយ ថា ដុល្លារ ១០០ ដុល្លារ ក្នុង មួយ ដុំ ជា តម្លៃ "ត្រឹមត្រូវ" ហើយ បាន រំលឹក ថា នៅ ពេល ដែល លោក បាន ចូល កាន់ តំណែង ជា ប្រធានាធិបតី នៃ ប្រទេស វេណេស៊ុយអេឡា នៅ ឆ្នាំ ១៩៩៩ តម្លៃ បាន កើន ឡើង ដល់ ប្រមាណ ១០ ដុល្លារ។

- **chrF++ 29.4** · `number_mismatch`
  - EN: "In the past eight days alone we have received reports on the killing of one journalist, Munir Shakir, in Balochistan on August 14 2011, and the disappearance of another journalist, Rehmatullah Daparkhel, three days earlier in North Waziristan on August 11," said spokesperson for the United Nations High Commissioner for Human Rights, Rupert Colville.
  - REF: ត្រឹមតែ8ថ្ងៃចុងក្រោយនេះ យើងបានទទួលរបាយការណ៍អំពីការសំលាប់អ្នកសារព័តិមានម្នាក់ឈ្មោះមុនាសាគា នៅប្រទេសបាឡូគីស្ថាននៅថ្ងៃទី14ខែសីហាឆ្នាំ2011 និងការបាត់ខ្លួនរបស់អ្នកសារព័តិមានម្នាក់ទៀតឈ្មោះរេម៉ាទុឡា ដាប៉ាខេល 3ថ្ងៃមុននោះនៅភាគខាងជើងនៃតំបន់វ៉ាហ្ស៊ីរីស្ថាននៅថ្ងៃទី11ខែសីហា នេះបើយោងតាមអ្នកនាំពាក្យនៃអង្គការត្រួតពិនិត្យសិទិ្ធមនុស្សជាន់ខ្ពស់នៃអង្គការសហប្រជាជាតិ លោករូភើត ខូវីល។
  - HYP: "ក្នុង រយៈ ពេល ៨ ថ្ងៃ ចុង ក្រោយ នេះ យើង បាន ទទួល របាយការណ៍ អំពី ការ សម្លាប់ អ្នក កាសែត ម្នាក់ ឈ្មោះ Munir Shakir នៅ ក្នុង ប្រទេស បាឡូឈីស្ថាន កាល ពី ថ្ងៃ ទី ១៤ ខែ សីហា ឆ្នាំ ២០១១ និង ការ បាត់ ខ្លួន អ្នក កាសែត ម្នាក់ ទៀត ឈ្មោះ Rehmatullah Daparkhel កាល ពី បី ថ្ងៃ មុន នៅ ក្នុង រដ្ឋ Waziristan ភាគ ខាង ជើង កាល ពី ថ្ងៃ ទី ១១ ខែ សីហា"។

- **chrF++ 32.8** · `number_mismatch`
  - EN: According to officials, no injuries have been reported but sea water levels have risen up to four meters in areas.
  - REF: បើយោងតាមមន្ត្រីនានា មិនមានអ្នកណាត្រូវរបួសឡើយ ប៉ុន្តែកំរិតទឹកបានកើនឡើងរហូតដល់បួនម៉ែតនៅតំបន់នោះ។
  - HYP: យោង តាម មន្ត្រី រដ្ឋាភិបាល មិន មាន ការ រង របួស ទេ ប៉ុន្តែ កម្រិត ទឹក សមុទ្រ បាន កើន ឡើង ដល់ ៤ ម៉ែត្រ នៅ ក្នុង តំបន់។

- **chrF++ 32.3** · `number_mismatch`
  - EN: Now for the first time since her affair, with Tie Domi, she sat down with CBC's George Stroumboulopoulos on his show The Hour to answer his questions about the affair, politics, and other topics during the nine minute chat, on October 9th.
  - REF: ឥឡូវនេះជាលើកទីមួយតាំងពីការលួចសេពគប់របស់គាត់ ជាមួយធី ឌុមី គាត់បានចេញមុខកម្មវិធីទូរទស្សស៊ីប៊ីស៊ីរបស់ ចក ស្តម់ប៊ូលុពូលេសនៃម៉ោងសំនួររបស់គាត់ពីការលួចសេពគប់ នយោបាយ និងប្រធានបទផ្សេងទៀតក្នុងរយពេល9នាទី នៅខែតុលាថ្ងៃទី9។
  - HYP: ឥឡូវ នេះ ជា លើក ទី មួយ ចាប់ តាំង ពី រឿងរ៉ាវ របស់ នាង ជាមួយ នឹង Tie Domi នាង បាន អង្គុយ ជាមួយ នឹង George Stroumboulopoulos របស់ CBC នៅ ក្នុង កម្មវិធី របស់ គាត់ The Hour ដើម្បី ឆ្លើយ តប ទៅ នឹង សំណួរ របស់ គាត់ អំពី រឿងរ៉ាវ នយោបាយ និង ប្រធានបទ ផ្សេង ទៀត នៅ ក្នុង ការ សន្ទនា ៩ នាទី កាល ពី ថ្ងៃ ទី ៩ ខែ តុលា។


## unseen_source_word (320 sentences)

- **chrF++ 17.7** · `unseen_source_word`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: គេ រំពឹង ថា ជំងឺ ផ្តាសាយ នឹង ប៉ះពាល់ ដល់ ភាគ ច្រើន នៃ សេះ ៧០០ នាក់ ដែល ត្រូវ បាន គេ សាងសង់ នៅ Randwick។

- **chrF++ 34.4** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្ត្រី ក្រសួង ឧស្សាហកម្ម អប្បបរមា នៃ រដ្ឋ NSW បាន និយាយ ថា រោងចក្រ នេះ នឹង ត្រូវ ដាក់ គាំង រហូត ដល់ ៣០ ថ្ងៃ បន្ទាប់ ពី សញ្ញា ចុង ក្រោយ នៃ ជំងឺ ផ្តាសាយ។

- **chrF++ 33.0** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណី នេះ គឺ ជា ការ ឆ្លង ដំបូង របស់ សេះ ប្រណាំង ទោះ បី ជា មាន សេះ សំរាប់ កម្សាន្ត រាប់សិប នាក់ នៅ ទូទាំង រដ្ឋ NSW និង រដ្ឋ Queensland ក៏ដោយ។

- **chrF++ 26.5** · `unseen_source_word`
  - EN: Chief Executive of Racing NSW, Peter V'Landys said while racing had been disrupted since a ban on horse movements last weekend today was a "grim, black day" for the racing industry in NSW.
  - REF: ប្រធានទីលានប្រណាំងញូវសោវែលប៊ីតទ័រ វ៉ាឡង់ឌីលើកឡើងថាការប្រកួត ត្រូវផ្អាក់តាំងពីការហាមនូវការចរាចររបស់សត្វសេះនៅចុងសប្តាហ៍មុនគឺជា"ធ្ងន់ធ្ងរ ថ្ងៃខ្មៅ"សំរាប់វិស័យឧស្សាហកម្មប្រណាំងនៅញូវសោវែល។
  - HYP: ប្រធាន នាយក ប្រតិបត្តិ Racing NSW លោក Peter V'Landys បាន និយាយ ថា ខណៈ ដែល ការ ប្រណាំង បាន រំខាន ចាប់ តាំង ពី ការ ហាមឃាត់ ការ ចលនា សេះ កាល ពី ចុង សប្តាហ៍ កន្លង ទៅ នេះ នៅ ថ្ងៃ នេះ គឺ ជា "ថ្ងៃ ខ្មៅ ខ្មៅ" សម្រាប់ វិស័យ ប្រណាំង ក្នុង រដ្ឋ NSW។

- **chrF++ 17.1** · `unseen_source_word`
  - EN: While Sydney's spring racing carnival has been canceled, Melbourne's is expected to kick off this weekend with the Caufield Cup.
  - REF: ក្នុងពេលក្បូនហែរសំរាប់ប្រណាំងរដូវផ្ការីកនៅស៊ីតនីត្រូវលប់ចោល នៅមែលប៊ិន គេពិចារណាពីបើកឡើងវិញនៅចុងសប្តាហ៍នូវកម្មវិធីពាន់រង្វាន់ ឃូហ្វៀលខាប់។
  - HYP: ខណៈពេល ដែល Carnival រត់ រដូវក្តៅ នៅ ស៊ីដនី ត្រូវបាន លុបចោល Melbourne រំពឹង ថា នឹង ចាប់ផ្តើម នៅ ចុង សប្តាហ៍ នេះ ជាមួយ នឹង Caufield Cup ។


## lexical_semantic (207 sentences)

- **chrF++ 23.7** · `lexical_semantic`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: ជំងឺ ផ្តាសាយ មាន ជំងឺ ឆ្លង ច្រើន តែ មិន អាច ឆ្លង ទៅ មនុស្ស បាន ទេ។

- **chrF++ 33.9** · `lexical_semantic`
  - EN: Racing is expected to resume in all Australian states except NSW and Queensland on the weekend.
  - REF: កម្មវិធីប្រណាំងត្រូវបានរំពឹងថានឹងប្រព្រឹត្តទូទាំងរដ្ឋនៅប្រទេសអូស្រ្តាលីលើកលែងតែញូវសោវែលនិងឃ្ខីនសាឡេននៅចុងសប្តាហ៍។
  - HYP: ការ ប្រកួត ប្រជែង ត្រូវ បាន គេ រំពឹង ថា នឹង បន្ត នៅ ក្នុង រដ្ឋ អូស្ត្រាលី ទាំង អស់ លើក លែង តែ រដ្ឋ NSW និង រដ្ឋ Queensland នៅ ចុង សប្តាហ៍ នេះ។

- **chrF++ 22.7** · `lexical_semantic`
  - EN: The cup will be ran with special precautions in place to attempt to keep the state free of the virus.
  - REF: ពាន់រង្វាន់នោះត្រូវអនុវត្តដោយប្រុងប្រយ័ត្នបំផុតជាងមុន ធ្វើយ៉ាងណារក្សាស្ថានភាពគ្មានមេរោគ។
  - HYP: ក្របខ័ណ្ឌ នេះ នឹង ត្រូវ ធ្វើ ដំណើរ ដោយ មាន ការ ប្រុង ប្រយ័ត្ន ពិសេស ដើម្បី ព្យាយាម រក្សា រដ្ឋ នេះ ដោយ គ្មាន វីរុស នោះ ទេ។

- **chrF++ 38.5** · `lexical_semantic`
  - EN: The blast happened at 7:18PM, around the time workers change shifts.
  - REF: ការផ្ទុះបានកើតឡើងនៅម៉ោង7:18ល្ងាច ជាពេលវេលាកម្មករប្តូរវេន។
  - HYP: ការ ផ្ទុះ បាន កើត ឡើង នៅ ម៉ោង ៧ និង ១៨ នាទី រសៀល នៅ ពេល ដែល កម្មករ ផ្លាស់ ប្តូរ កម្លាំង។

- **chrF++ 38.6** · `lexical_semantic`
  - EN: "All other production operations in our facilities in China continue operating normally."
  - REF: "ប្រតិបត្តិការផលិតកម្មទាំងអស់នៅស្ថាប័នផ្សេងនៅទូទាំងប្រទេសចិននៅបន្តប្រតិបត្តិការដូចធម្មដា។"
  - HYP: "ការ ប្រតិបត្តិការ ផលិតកម្ម ផ្សេង ទៀត នៅ ក្នុង រោងចក្រ របស់ យើង នៅ ក្នុង ប្រទេស ចិន នៅ តែ បន្ត ដំណើរការ ជា ធម្មតា"។
