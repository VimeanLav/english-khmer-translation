# Error analysis: A: Transformer from scratch

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 0.9** · `omission`
  - EN: Guinness World Records spokesman, Damian Field, in London, however, said that "Guinness monitors a category for fastest unsupported trek to the South Pole, but it has no record currently listed."
  - REF: អ្នកនាំពាក្យរបស់កំណត់ត្រាពិភពលោក ហ្គិនណែស ដាមៀន ហ្វៀល នៅទីក្រុងឡុង បានឱ្យដឹងថា "ហ្គិនណែស គ្លាំមើលការធ្វើដំណើរដោយគ្មានការគាំទ្រយ៉ាងលឿនបំផុតទៅកាន់ប៉ូលខាងត្បូងមួយប្រភេទ ប៉ុន្តែវាមិនមានកំណត់ត្រាដែលបានចុះបញ្ជីថ្មីៗនោះទេ។"
  - HYP: េចេចេញ្ចេញ្ធាយ។

- **chrF++ 1.0** · `omission`
  - EN: Following the decision to nationalise Landsbanki, the Icelandic Prime Minister, Geir Haarde, who introduced and signed the emergency legislation into law, stated:"What we are doing here is saving a banking system - saving the domestic banking system - and making sure that it can function properly."
  - REF: បន្ទាប់ពីការសម្រេចចិត្តធ្វើសញ្ជាតូបនីយកម្ម ឡែនស៍បេងគី​ នាយករដ្ឋមន្រ្តីប្រទេសអ៊ីស្លង់ ហ្គែរ ហាដ ដែលណែនាំនិងចុះហត្ថលេខាបញ្ចូលបញ្ញត្តិបន្ទាន់ទៅក្នុងច្បាប់ដោយបានបញ្ជាក់ថា: "អ្វីដែលយើងកំពុងធ្វើនៅទីនេះគឺដើម្បីជួយសង្គ្រោះប្រព័ន្ធធនាគារ ពោលគឺការជួយសង្គ្រោះប្រព័ន្ធធនាគារក្នុងស្រុក និងធ្វើឲ្យប្រាកដថាវាអាចដំណើរការបានត្រឹមត្រូវ។"
  - HYP: េចេចេញាញាញាញាយ។

- **chrF++ 1.0** · `omission`
  - EN: It burned 500 acres south of the 14 Freeway, but the Los Angeles County Fire Department (LACFD) now has it contained, and firefighters are hopeful that it will burn itself out as it edges closer to the 160,577-acre burn area of last year's Station Fire.
  - REF: អគ្គិភ័យនេះ ឆេះព្រៃអស់ទំហំ 500 acres ភាគខាងត្បូងនៃ 14 ហ្វ្រីវ៉េ ប៉ុន្តែពេលនេះ នាយកដ្ធានអគ្គិភ័យតំបន់ឡូសអេនជើឡេស (LACFD) បានគ្រប់គ្រងអគ្គិភ័យនេះ ហើយអ្នកពន្លត់អគ្គិភ័យ សង្ឃឹមថាអគ្គិភ័យនេះនឹងរលត់ដោយខ្លួនឯង នៅពេលវាឆាបឆេះចូលជិតដល់កន្លែងឆេះដែលមាន ទំហំ 160,577 acre នៃស្ដេសិន ហ្វាយអើ កាលពីឆ្នាំមុន។
  - HYP: េចេញាលាមេញ្ញាលាយ។

- **chrF++ 1.1** · `omission`
  - EN: This recent development in North Korea has given rise to speculation among analysts, some of whom suspected that these may be a sign that Kim is losing power, or that a power struggle is going on among the top leaders of the totalitarian state.
  - REF: រឿងរ៉ាវថ្មីៗនេះ នៅកូរ៉េខាងជើង បានបង្កើននូវពាក្យចចាមអារាមក្នុងចំណោមអ្នកវិភាគទាំងអស់ ដែលអ្នកវិភាគមួយចំនួនបានសង្ស័យថា ទាំងនេះប្រហែលជាសញ្ញាបង្ហាញថា លោកគីមកំពុងបាត់បង់អំណាច ឬថា ការតស៊ូនៃអំណាច គឺកំពុងតែកើតឡើងនៅក្នុងចំណោមមេដឹកនាំកំពូលរបស់រដ្ឋ​ផ្តាច់ការនេះ។
  - HYP: េចេចេញ្ចេញ្ធាយ។

- **chrF++ 1.1** · `omission`
  - EN: The report continued, "Steve Yerrid, special counsel on the oil spill for Florida Gov. Charlie Crist, said the report clearly shows the company is attempting to spread blame for the well disaster, foreshadowing what will be a likely legal effort to force Halliburton and Transocean, and perhaps others, to share costs such as paying claims and government penalties."
  - REF: របាយការណ៍បានបន្តថា "ស្ទីវ យើរីដ ជាទីប្រឹក្សាពិសេសលើការ កំពប់ប្រេងរបស់អភិបាលក្រុងហ្ល័ររីដា ឆាលី គ្រីសបាននិយាយថា របាយការណ៍បង្ហាញយ៉ាងច្បាស់ថាក្រុមហ៊ុនប៉ុនប៉ងបង្កើតការស្តីបន្ទោសអំពីមហន្តរាយអណ្តូងប្រេង ព្រមានពីអ្វីដែលទាក់ទិននឹងច្បាប់ដើម្បីបង្ខំក្រុមហ៊ុនហាលីប៊ូតុន និងត្រានអូសិន ហើយប្រហែលក្រុមហ៊ុនផ្សេងៗទៀត ចែករំលែកនូវការចំណាយដូចជាការបង់ពាក្យបណ្តឹង និងការផាកពិន័យរបស់រដ្ឋាភិបាល។"
  - HYP: េចេញាមេញាញ្ញាមាមេញាមទាម។

- **chrF++ 1.1** · `omission`
  - EN: The fire burned down a Los Angeles County Sheriff Department communications tower, forcing Lancaster and Palmdale-based deputies to set up mobile operations bases and coordinate their efforts using cell phones and computers.
  - REF: អគ្គិភ័យនេះបានឆេះបង្គោលអង់តែនទូរគមនាគមន៍ការិយាល័យប្រធានតំបន់ឡូសអែនជើឡេស ដោយបានបង្ខំឲ្យអនុប្រធាននៅឡេនខេស្ទ័រ និងផាមដាល់រើទៅបង្កើតមូលដ្ឋានប្រតិបត្តិការទូរស័ព្ទ និងសម្របសម្រួលកិច្ចខិតខំប្រឹងប្រែងរបស់ខ្លួន​ដោយប្រើទូរស័ព្ទចល័ត និងកុំព្យូទ័រ។
  - HYP: េចេចេញាមេញ្លាយ។

- **chrF++ 1.1** · `omission`
  - EN: The report, the product of a four-month investigation conducted by BP's Head of Safety Operations, Mark Bly, criticizes the oil rig's fire prevention systems, the crew of the rig for failing to realize and act upon evidence that oil was leaking from the surface of the ocean, and describes how BP and Transocean "incorrectly accepted" negative pressure test results.
  - REF: របាយការណ៍ដែលជាលទ្ធភលនៃការស៊ើបអង្កេតរយៈពេល៤ខែដោយប្រធានប្រតិបត្តិការសុវត្ថិភាពរបស់ក្រុមហ៊ុនប៊ីភីលោក ម៉ាក ប្ល៊ី បានស្តីបន្ទោសទៅលើប្រព័ន្ឋការពាអគ្គិភ័យរបស់ឧបករណ៍ខួងប្រេង ក្រុមកម្មករដែលមើលការខុសត្រូវឧបករណ៍ខួងថាមិនបានដឹង និងមិនបានចាត់វិធានការចំពោះហេតុការណ៏ដែលប្រេងបានលេចធ្លាយប្រេងលើផ្ទៃសមុទ្រ និងបានពិព៌ណនាអំពីរបៀបដែលក្រុមហ៊ុនប៊ីភី និងត្រានអូសិន "ទទួលយកដោយមិនត្រឹមត្រូវ" នូវលទ្ឋផលតេស្តសម្ពាធអវិជ្ជមាន។
  - HYP: េចេញាមាបញ្ធាមេធាមាមម។

- **chrF++ 1.2** · `omission`
  - EN: Bourdin, who speaks at least five languages, told social workers and classmates that his name was Francisco Hernandez-Fernandez and that his parents had been killed in a car crash in 2000 and that he'd spent three months in a coma.
  - REF: ប៊ូឌិន ដែលអាចនិយាយបានយ៉ាងហោចណាស់ប្រាំភាសា បានប្រាប់បុគ្គលិកសង្គមកិច្ច និងសិស្សរួមថ្នាក់ថា ឈ្មោះរបស់គាត់គឺ ហ្រ្វង់ស៊ីសស្កូ ហឺណាឌីស ហ្វឺណានឌីស និងថាឪពុកម្តាយរបស់គាត់បានស្លាប់ក្នុងគ្រោះថ្នាក់រថយន្តកាលពី ឆ្នាំ2000 និងថាគាត់បានសន្លប់បាត់បង់ស្មារតី រយៈពេលបីខែ។
  - HYP: េចេចេញុមដោយផ្ទាលេធាយ។

- **chrF++ 1.2** · `omission`
  - EN: Speaking before a Senate committee about media reform, AAP chief Bruce Davidson said, "We simply do not believe that there is a problem with the conduct of the media in Australia, and certainly not that of AAP, that warrants further oversight by a minister-appointed body [...]"
  - REF: ដោយបាននិយាយនៅចំពោះមុខគណៈកម្មាធិព្រឹទ្ធសភាអំពីកំណែទម្រង់ប្រព័ន្ធផ្សព្វផ្សាយ ប្រធាន AAP លោក ប្រ៊ូស ដេវីដ បានប្រសាសន៍ថា "យើងគ្រាន់តែមិនជឿថាមានបញ្ហាពាក់ព័ន្ធនឹងការប្រព្រឹត្តរបស់ប្រព័ន្ធផ្សព្វផ្សាយនៅក្នុងប្រទេសអូស្រ្តាលី ហើយប្រាកដណាស់ AAP គ្មានអ្វីបញ្ហាឡើយ ដែលត្រូវទទួលការត្រួតពិនិត្យបន្ថែមទៀតដោយអង្គភាពដែលតែងតាំងដោយរដ្ឋមន្ត្រី នោះទេ[...]"
  - HYP: េចេចេញ្ធាមាមាយ។

- **chrF++ 1.2** · `omission`
  - EN: UDA spokesperson Frankie Gallagher spoke at a press conference in Belfast, stating that the group regrets the approximately 400 people, primarily Catholic civilians, that they were responsible for the murder of between 1971 and 2001.
  - REF: អ្នកនាំពាក្យ UDA ហ្វ៊ែ្រងឃី ហ្គាឡាហ្គ៊ើរបាននិយាយនៅក្នុងសន្និសីទកាសែតមួយនៅប៊ែលហ្វាសត៍ថា ក្រុមមានការសោកស្តាយចំពោះប្រជាជនប្រហែល400នាក់ ជាពិសេសជនស៊ីវិលកាតូលិក ដែលពួកគេទទួលខុសត្រូវចំពោះឃាតកម្មនៅចន្លោះឆ្នាំ1971 និងឆ្នាំ2001។
  - HYP: េចេញាម្ចេញ្ញ្ធាយ។

- **chrF++ 1.2** · `omission`
  - EN: The Afghan government has not provided a copy of the text of the Shia Family Law to the UN or to other outside groups requesting it, citing "technical problems", however, the UN and opposition politicians say that the bill contains numerous provisions restricting the rights of women, such as giving their husbands priority in court; requiring the husband's permission to leave the house, obtain education or employment, or to see a doctor; and reserving the custody of children to male relatives.
  - REF: រដ្ឋាភិបាលអាហ្គានីស្ថានមិនបានផ្តល់នូវសំណៅឯកសារច្បាប់មួយនៃច្បាប់ស៊ីអាហ្វ៊េមីលីទៅកាន់ អង្គការសហប្រជាជាតិឬទៅកាន់ក្រុមខាងក្រៅផ្សេងទៀតដែលស្នើសុំវាឡើយ ដោយបាននិយាយថា"កំហុសបច្ចេកទេស" ប៉ុន្តែយ៉ាងណាក៏ដោយ អង្គការសហប្រជាជាតិ និងគណបក្សនយោបាយប្រឆាំងទាំងឡាយនិយាយថា ពង្រាងច្បាប់ផ្ទុកនូវការហាមឃាត់សិទ្ធិរបស់ស្ត្រីជាច្រើន ដូចជាផ្តល់សិទ្ធិអោយប្តីមានអាទិភាពក្នុងតុលាការ;តំរូវអោយសុំសិទ្ធិប្តីប្រសិនបើចង់ចេញពីផ្ទះ សុំសិទ្ធិដើម្បីការទៅរៀនឬទៅធ្វើការ ឬក៏ទៅជួបពិគ្រោះជាមួយវេជ្ជបណ្ឌិត;ហើយរក្សាទុកនូវសិទ្ធិមើលថែរក្សាកូនទៅសាច់ញាតិខាងបុរស។
  - HYP: អ្នកចេញាមាបញ្ញ្មាមាមាមាម។

- **chrF++ 1.2** · `omission`
  - EN: Chisinau "holds official documents from the chancellery of Saddam Hussein, which show that Transnistria had supplied both arms, and entire weapon manufacturing lines to Iraq," Voronin told a group of Russian journalists, adding that an investigation on this case is under way.
  - REF: ឆីស៊ីនូ"កាន់ឯកសារផ្លូវការពីអធិការបតីស្ថាននៃសេដានហូសេនដែលបានបង្ហាញថាត្រេនស្នីស្រ្ថីនបានផ្គត់ផ្គង់ទាំងអាវុធនិងអាវុធផលិតជាខ្សែទាំងអស់ទៅកាន់អ៊ីរ៉ាក់"វ៉ូរ៉ូនីនបានប្រាប់ក្រុមមួយនៃអ្នកកាសែតរុស្សីដែលបានបន្ថែមថាការស៊ើបអង្កេតទៅលើក្ដីនេះគឺកំពុងកើតឡើង។
  - HYP: េចេញាលាមេញ្លេធាយ។

- **chrF++ 1.2** · `omission`
  - EN: He lives in Chelsea, Quebec, and is famous for his 4,300-mile (6,920-kilometer) epic run across the Sahara Desert in 2007, which was the subject of a documentary narrated by actor Matt Damon's "Running the Sahara."
  - REF: គាត់រស់នៅ ឆែលស៊ី កេបិច និងមានឈ្មោះល្បីល្បាញសម្រាប់វីរភាពរត់ឆ្លងកាត់វាលខ្សាច់សាហារ៉ារបស់គាត់ដែលមានចម្ងាយ 4,300-ម៉ាយ (6,920-គីឡូម៉ែត្រ) ក្នុង ឆ្នាំ2007 ដែលជាប្រធានបទនៃឯកសារនិទានដោយតារាសម្តែង ម៉ាត់ ដាម៉ុន ដែលមានចំណងជើងថា "ការរត់សាហារ៉ា។"
  - HYP: ហេចេញដីមេញ្ញាមាមេញ។

- **chrF++ 1.2** · `omission`
  - EN: Until now, they had been "too busy" to perform the act of marriage, due to various occurrences; according to The Daily Telegraph, this includes Ed's work in the 2010 UK general election, the birth of their son Daniel, and Ed's appearance at the 2009 United Nations Climate Change Conference.
  - REF: រហូតមកដល់ពេលនេះ ពួកគេមានការ "រវល់ពេក" មិនអាចធ្វើការរៀបអាពាហ៍ពិពាហ៍បានទេដោយសារតែមានព្រឹត្តិការណ៍ជាច្រើនបានកើតឡើង; នេះបើយោងតាមកាសែត ដេលី តេលេក្រាហ្វ រួមមានការងាររបស់លោក អេដ នៅក្នុងការបោះឆ្នោតទូទៅនៅប្រទេសអង់គ្លេសឆ្នាំ2010 ហើយនិង កំណើតរបស់កូនរបស់ពួកគេ ដានីអែល និងការចូលរួមរបស់លោកអេដ នៅឯសន្និសិទអង្គការសហប្រជាជាតិអំពីការផ្លាស់ប្តូរអាកាសធាតុក្នុងឆ្នាំ2009​។
  - HYP: េចេញាញាបញាញាមាមាមាមមម។

- **chrF++ 1.2** · `omission`
  - EN: Delta Airlines 1706—a domestic U.S. flight between Detroit and San Diego—diverted to Albuquerque International Sunport in Albuquerque, where the Boeing 737-800 aircraft was taken to a remote area of the airport.
  - REF: Delta Airlines 1706 ជាយន្តហោះដែលធ្វើការ ហោះហើរក្នុងស្រុករបស់អាមេរិច ហោះរវាង ដេត្រូយត៍ និង សាន់ ដេហ្គោ បានបង្វែរទិសចុះចតនៅ Albuquerque International Sunport ក្នុងទីក្រុង Albuquerque ដែលជាកន្លែងដែលយន្តហោះ Boeing 737-800​​ ត្រូវបានចុះចតនៅក្នុងកន្លែងដាច់ស្រយាលមួយនៅក្នុងប្រលានយន្តហោះ។
  - HYP: េចេញាញ្ចេញាបញាមាមាយ។


## repetition_hallucination (159 sentences)

- **chrF++ 9.7** · `repetition_hallucination`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: វាមានសារៈសំខាន់ដែល បានបញ្ជាក់ គំនិតផ្តួចផ្តើមបង្កើតការងារ្ចេញ្ញ្ញ្ញ្ញ្ញ្ញ្ចី។

- **chrF++ 4.7** · `repetition_hallucination`
  - EN: Comando Vermelho members started attacking the rival members of ADA to protect their turf.
  - REF: សមាជិកComando Vermelho បានចាប់ផ្តើមវាយចំពោះសមាជិកសត្រូវរបស់ អាដា ដើម្បីការពារដែនពូកវា។
  - HYP: ការបបញ្ញ្ត្ញ្ញ្ញានាបញ្ញ្ញ្នានានានានានានានានានានានានានានានានានានានានានានានានានានានាន្ន្នានានានានាន្ន្ន្ន្ន្នាន្

- **chrF++ 5.1** · `repetition_hallucination`
  - EN: Initial investigations now suggest the explosion was caused by poor ventilation, which lead to high concentrations of combustible dust.
  - REF: ការស្រាវជ្រាវដំបូងបានសង្ស័យថាការផ្ទុះបានកើតឡើងដោយខ្វះខ្យល់ចេញចូល ដែលនាំអោយប្រមូលផ្តុំនូវសារធាតុដែលងាយឆេះ។
  - HYP: ខ្ញុំបានទិញមាញុមទាន្ត្ត្ត្ត្ត្តី។

- **chrF++ 8.1** · `repetition_hallucination`
  - EN: "All other production operations in our facilities in China continue operating normally."
  - REF: "ប្រតិបត្តិការផលិតកម្មទាំងអស់នៅស្ថាប័នផ្សេងនៅទូទាំងប្រទេសចិននៅបន្តប្រតិបត្តិការដូចធម្មដា។"
  - HYP: ការបណ្ត្តិត្ញ្ញ្នាបញ្ញ្ញ្ញ្ញ្ញ្ត្នានានានានានានានាបញ្ត្ត្ញ្ញ្ញ្ញ្ញ្ញ្ញ្ញ្ញ្ញ្ញ្ញ្តន្តន្នានានានាន្ន្ន្ន្ន្ន្ន្ន្

- **chrF++ 2.3** · `repetition_hallucination`
  - EN: "When workers take off their cotton gloves, their hands are covered with aluminum dust."
  - REF: "នៅពេលកម្មករដកស្រោមដៃកម្បាស ដែរបស់ពួកគាត់ពោរពេញដោយធូលីអាលមីញ៉ូម។"
  - HYP: ការបណ្ត្ត្ត្ត្ត្ត្នានិច្ត្នាណ្ណ្ណ្ណ្ណ្ណ្នាន្ណ្ត្ត្ណ្ណ្ណ្ណ្ណ្ត្ត្ត្ត្ត្ត្ត្ត្ត្ត្ន្ន្ត្ច្ន្ន្ន្ន្ន្ច្ច្ច្ន្ន្ន្


## omission (830 sentences)

- **chrF++ 4.1** · `omission`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: ការសនុំខសនានាំខ្នាំខ្គី។

- **chrF++ 8.1** · `omission`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: វាមានសារៈសំខាន់ដែលាន្ញ្ធាញ្ញ្ធានី។

- **chrF++ 2.5** · `omission`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: ការបណ្តិតិត្ត្តិតិតិតិច្តិ។

- **chrF++ 4.6** · `omission`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: អ្នកសង្ានានានាញ្ញានានានាត់បាន។

- **chrF++ 4.4** · `omission`
  - EN: The national racing shutdown was costing the industry tens of millions of dollars every day.
  - REF: ការបិទការប្រណាំងថ្នាក់ជាតិ បានធ្វើឲ្យវិស័យនេះខាតបង់រាប់លានដុល្លាក្នុងមួយថ្ងៃៗ។
  - HYP: រដ្ឋសភាវិញុសនានុំនុម។


## number_mismatch (7 sentences)

- **chrF++ 18.4** · `number_mismatch`
  - EN: Some observers think it is possible that the $100 barrier may be broken.
  - REF: អ្នកអង្កេតខ្លះគិតថាវាគឹអាចទៅរួចដែលឧបសគ្គ100ដុល្លារអាចនឹងត្រូវបានបំបែក។
  - HYP: ដោយមានប្រព័ន្ធសង្កេតការណ៍បោះឆ្នោតអាចទៅរួចទេក្នុងការ គិតអាចទៅរួចទេក្នុងការ យកសនាយ។

- **chrF++ 3.9** · `number_mismatch`
  - EN: Portions of Interstate 35 and Interstate 30 were shut down.
  - REF: ផ្នែកខ្លះនៃអន្តររដ្ឋ35និងអន្តររដ្ឋ30ត្រូវបានបិទ។
  - HYP: អាជ្ញាធរកំពង់ផែប៉ុមទាកន ៥។

- **chrF++ 15.4** · `number_mismatch`
  - EN: The governor said that the fire was 20% contained and had burned 13,000 acres.
  - REF: លោកអភិបាលបាននិយាយថា ភ្លើង 20%​ ត្រូវបានគ្រប់គ្រង និងបានឆេះអស់ 13,000 acres។
  - HYP: ដោយជាប់លាប់បាននិយាយថាខ្ញុំត្រូវការស៊ុសន ២។

- **chrF++ 16.6** · `number_mismatch`
  - EN: Its 2007 annual convention, Wikimania, is set to take place in Taipei.
  - REF: សន្និបាតវីគីម៉ានា ប្រចាំឆ្នាំ 2007 នឹងប្រព្រឹត្តទៅនៅក្នុងទីក្រុងតៃប៉ិ។
  - HYP: វាបានស៊ុស ថវិកាប្រចាំឆ្នាំ តាមអេឡិចត្រូនិក។

- **chrF++ 7.4** · `number_mismatch`
  - EN: Scientists had a 1 in 2,000 chance of discovering the planet.
  - REF: អ្នកវិទ្យាសាស្រ្តមានឱកាស1លើ2,000ក្នុងការស្វែងរកភពនេះ។
  - HYP: ថ្ងៃត្រ ២ គ្រាប់ទៅសនាមកិសនានានាម។


## unseen_source_word (21 sentences)

- **chrF++ 8.6** · `unseen_source_word`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: ផ្តាសាយធំការប៉ុសនាញ្ញ្តិសនាកនេះ។

- **chrF++ 5.8** · `unseen_source_word`
  - EN: At least three people were killed, at least fifteen injured.
  - REF: យ៉ាងហោចណាស់មនុស្ស៣នាក់បានស្លាប់ យ៉ាងតិចណាស់១៥នាក់រងរបួស។
  - HYP: នៅក្នុងសន្និសីទស៊ុបបណ្ច្ញ្ត្ត្ត្ច្ចី។

- **chrF++ 7.2** · `unseen_source_word`
  - EN: On Monday, city officials gave the cause as combustible dust in the air at a polishing workshop.
  - REF: នៅថ្ងៃច័ន្ទ មន្ត្រីសាលាក្រុងបានប្រកាសពីមូលហេតុមកពីធូលីដែលងាយឆេះនៅក្នុងខ្យល់ក្នុងការដ្ឋានប៉ូលា។
  - HYP: នៅលើវេទិកាអនឡាញ ក្រុមសុខាភិបាលសាធារណៈុសនាសនាសុយ។

- **chrF++ 6.8** · `unseen_source_word`
  - EN: "In the process, there is lots of aluminum (aluminium) dust floating in the air. "
  - REF: "ក្នុងដំណើរការធូលីអាលមីញ៉ូមជាច្រើនអណ្តែតនៅក្នុងខ្យល់។"
  - HYP: ការចេញ្ញ្លាបញ្ញ្នាន្ញ្ញ្តី។

- **chrF++ 3.7** · `unseen_source_word`
  - EN: "Workers always breathe in aluminum dust even though they put on masks. "
  - REF: "កម្មករតែងតែបឺតធូលីអាលមីញ៉ូមទោះបីជាពាក់ម៉ាសក៏ដោយ។"
  - HYP: ការបទាញ្ចេញ្ញ្ញាបញ្ញ្ញ្ញ្ញ្តិ។


## lexical_semantic (1 sentences)

- **chrF++ 8.3** · `lexical_semantic`
  - EN: "We have no idea what the result of that would be."
  - REF: "យើងពុំដឹងថានឹងទទួលបានលទ្ធផលយ៉ាងដូចម្តេចឡើយ។"
  - HYP: ចងចាំក្នុងចិត្តថាស៊ុមទ្ធរុយ។
