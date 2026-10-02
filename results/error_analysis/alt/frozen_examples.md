# Error analysis: B: NLLB frozen backbone

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 9.1** · `unseen_source_word`
  - EN: A large police presence watched over the scenes as mourners wept.
  - REF: ប៉ូលីសជាច្រើនបានមានវត្តមាននៅកន្លែងផ្ទាល់ ដើម្បីមើលការខុសត្រូវដល់អ្នកកាន់ទុក្ខដែលបានយំ។
  - HYP: មាននគរបាលធំ បានសង្កេត លើ វីដេអូ នៅពេលអ្នកពួងសួងកំពុងស្រែក។

- **chrF++ 10.2** · `unseen_source_word`
  - EN: Chicago Fire plays the winner of the New England Revolution/New York Red Bulls 2 Leg affair which is currently tied 0-0.
  - REF: ក្រុមឈីខាហ្គូនឹងជួបក្រុមឈ្នះរវាងក្រុមញូ អ៊ីនឡេន រីវ៉ូលូសុន/ញូយ៉ក រេត ប៊ូល 2ជើងដែលបច្ចុប្បន្នមានពន្ទុស្មើ 0-0។
  - HYP: Chicago Fire លេងជាអ្នកឈ្នះនៃ រឿងកំណែទម្រង់ប្រទេសថ្មី / New York Red Bulls 2 Leg ដែលកំពុងស្មើ 0-0.

- **chrF++ 10.5** · `unseen_source_word`
  - EN: It is a direct tribute to the KISS album Creatures of the Night.
  - REF: វាជាលក្ខណៈផ្ទាល់របស់អាល់ប៊ុម KISS ដែលមានឈ្មោះថា Creatures of the Night។
  - HYP: វាជាការ សប្បុរសធម៌ផ្ទាល់ដល់ Album កញ្ញាស្រស់នៃយប់។

- **chrF++ 10.7** · `unseen_source_word`
  - EN: He also published The Andromeda Strain, Congo, Rising Sun, Timeline, Eaters of the Dead, all of which became major motion pictures.
  - REF: លោកក៏បានបោះពុម្ពរឿងអេដ្រូមាដា ស្ត្រេន រឿងកុងហ្គូ រឿងរាយស៊ីង សាន់ រឿងថាមឡាញ រឿងអ៊ីស្ទឺ អហ្វ ដឹ ដេដថ៍ ដែលរឿងទាំងនេះបានក្លាយជាគំនូរជីវចលដ៏សំខាន់។
  - HYP: គាត់បានបោះពុម្ពផ្សាយ The Andromeda Strain, Congo, Rising Sun, Timeline, Eaters of the Dead ផងដែរ ដែលទាំងអស់គ្នាក្នុងរឿងរ៉ាវធំៗ។

- **chrF++ 11.2** · `unseen_source_word`
  - EN: Shenouda was dressed in full regalia, complete with a gold crown.
  - REF: សេននូដា ត្រូវបានគេស្លៀកពាក់អោយក្នុងសំលៀកបំពាក់រាជា ជាមួយនឹងម្កុជមាស។
  - HYP: សែនុធាពាក់ខោអាវធំៗ, ពេញជាមួយមួកសុវត្ថិភាពពណ៌មាស។

- **chrF++ 11.9** · `unseen_source_word`
  - EN: In addition to transport disruption, a number of sports have been affected.
  - REF: បន្ថែម​លើស​ពី​ការ​អាក់​ខាន​នៃ​មធ្យោបាយ​ធ្វើ​ដំណើរ​ កីឡា​ជា​ច្រើន​ប្រភេទ​បានរងផល​ប៉ះពាល់ផងដែរ​។
  - HYP: ក្រៅពី ការរំខានដឹកជញ្ជូន, មួយចំនួននៃកីឡា ត្រូវបានប៉ះពាល់។

- **chrF++ 12.3** · `number_mismatch`
  - EN: New Zealand are top of Pool C with ten points, ahead of Scotland with 5 and Italy with 4.
  - REF: ក្រុមញូហ្ស៊េលែនឈរលើកំពូលតារាងក្នុងពូលដោយមានដប់ពិន្ទុមុនក្រុមស្កុតឡេនដែលមាន5ពិន្ទុ និងក្រុមអ៊ីតាលីដែលមាន4ពិន្ទុ។
  - HYP: ប្រទេសញូវយ៉កឈរនៅខាងលើនៃពូជ C ជាមួយនឹង១០ពិន្ទុ, នៅមុខសក្កដាជាមួយ ៥ និងអ៊ីតាលីជាមួយ ៤។

- **chrF++ 12.7** · `unseen_source_word`
  - EN: The Senators will play against Frolunda of Sweden's elite league.
  - REF: ក្រុម Senators នឹងប្រកួតជាមួយក្រុម Frolunda នៃសហព័ន្ធដ៏ខ្លាំងខ្លារបស់ប្រទេសស៊ុយអែត។
  - HYP: អ្នកតំណាងរាស្ត្រ នឹងលេងប្រឆាំងនឹងស្រីល័ក្ខពីសម្ព័ន្ធអéliteរបស់ស្វីស។

- **chrF++ 13.0** · `unseen_source_word`
  - EN: "I'm pretty tired, actually," said Kevin Vallely, calling from Patriot Hills, Antarctica.
  - REF: ខេវីន វ៉ាល់លេលី ដោយបាននិយាយទូរស័ព្ទពីប៉ាទ្រីយ៉ូហ៊ីលស៍ អង់តាក់ទិក បានឱ្យដឹងថា "តាមពិតទៅ ខ្ញុំពិតជានឿយហត់ខ្លាំងណាស់។"
  - HYP: "ញុមហត់នឿយមែនទែន", កែវ វាលីបាននិយាយថា, តេមកុំពីភ្នំប្រាសាទព្រះសីហនុ,អន្តរជាតិ។

- **chrF++ 13.1** · `unseen_source_word`
  - EN: Now, Lidge is ready to pitch again after the needed rest.
  - REF: បច្ចុប្បន្ននេះ លិជ្ចត្រៀមខ្លួនរួចជាស្រេច ដើម្បីបោះបាល់ម្តងទៀត ក្រោយពីតម្រូវការនៃការសម្រាក។
  - HYP: ឥឡូវនេះ លីកត្រៀមសម្លាញ់ឡើងវិញបន្ទាប់ពីសម្រាកដែលចាំបាច់។

- **chrF++ 13.7** · `unseen_source_word`
  - EN: And Studs and Leather is basically Heaven's on Fire (KISS song) meets Balls To The Wall (Accept song).
  - REF: ហើយបទ Studs and Leather មានមូលដ្ឋានជាបទ Heaven's on Fire (ចម្រៀង KISS) ជួបជាមួយ​បទ Balls To The Wall (ចម្រៀង Accept)។
  - HYP: និងស្លាបព្រា និងសើស្បែកគឺសុទ្ធសឹងតែសួគ៌នៅលើកេះ (បទចម្រៀងកISS) ជួបបាល់ដល់វែង (បទចម្រៀងទទួល)។

- **chrF++ 14.4** · `unseen_source_word`
  - EN: New Zealand's Kyle Mills led the bowling attack with 3 for 44.
  - REF: ឃីឡេ មៀលស៍នៃប្រទេសញ៉ូវហ្សេឡង់បាននាំមុខក្នុងការគប់បាល់ 3 ដោយទទួលបាន 44 ពិន្ទុ។
  - HYP: កីឡាករថៃម៉ិលស៍របស់ប្រទេសញូវយ៉ក បានដឹកនាំការវាយប្រហារប៊ូលីងជាមួយ ៣ សម្រាប់ ៤៤។

- **chrF++ 14.6** · `unseen_source_word`
  - EN: And hard-throwing closer Brad Lidge will be refreshed physically and mentally after an exhausting stretch.
  - REF: ហើយលោកប្រេត លិច្ច ដែលជាអ្នកគប់បាល់ដ៏ប៉ិនប្រសប់ នឹងត្រូវមានអារម្មណ៍ស្រស់ថ្លាទាំងរាងកាយ និងផ្លូវចិត្តក្រោយពីការហាត់ប្រាណឱ្យយឺតសសៃ។
  - HYP: ហើយប្រដាល់ពិបាកជាងបារ៉ាត់លក្ខិណា នឹងសម្រស់ ដោយចលនា និងរូបកាយ បន្ទាប់ពីការខិតខំប្រឹងប្រែង។

- **chrF++ 14.6** · `unseen_source_word`
  - EN: A dominant first half display from Australia saw them defeat Wales in Cardiff.
  - REF: ក្នុងការប្រកួតដែលបានត្រូវគ្រប់គ្រងទាំងស្រុងមាននៅតង់ទីមួយរបស់ក្រុមអូស្រ្តាលី ដែលផ្តួលក្រុមវែលនៅទីក្រុងខាឌីហ្វ។
  - HYP: ការបង្ហាញផ្តាច់មុខឆមាសទីមួយពីអូស្ត្រាលី បានឃើញពួកគេចាញ់វែលសនៅកាឌីហ្វ។

- **chrF++ 14.7** · `number_mismatch`
  - EN: According to Gen Iinuma, Maui County Civil Defense administrator, the CH-47s carry 2000-gallon buckets of water, whereas the smaller helicopters only have 100-gallon buckets.
  - REF: យោងតាម ជីន អ៊ីនូម៉ា មន្រ្តីរដ្ឋបាលការពារស៊ីវិលតំបន់មូអៃ ឧទ្ធម្ភាគចក្រ CH-47s អាចដឹកទឹកបាន 2000-gallon ចំណែកឧទ្ធម្ភាគចក្រតូចអាចដឹកទឹកបានតែ 100-gallon ប៉ុណ្ណោះ។
  - HYP: យោងតាមលោកឧត្តមសេនីយ៍អ៊ិនមា អ្នកគ្រប់គ្រងការពារពលរដ្ឋខេត្តម៉ាវី, ចរន្តគីរី-47 ដឹកនាំធុងទឹក ២២០០ ហ្គាលីទ័រ, ខណៈពេលដែលម៉ាស៊ីនកាំជ្រួចតូចជាងនេះមានធុងទឹកតែ១០០ ហ្គាលីទ័រ។


## repetition_hallucination (12 sentences)

- **chrF++ 33.4** · `repetition_hallucination`
  - EN: Had any civilization existed on the frozen ice cap, the USGS says that damage could be "light to moderate."
  - REF: បើមានពពួកមានជីវិតនៅលើផ្ទាំងទឹកកក USGSនិយាយថាការខូចខាតអាចពី "ស្រាលទៅមធ្យម។"
  - HYP: ប្រសិនបើអរិយធម៌ណាមួយបានអវត្តមាននៅលើ ការកកកកកកកកកកកក, USGS និយាយថា ការខូចខាតអាច"ស្រាលដល់មធ្យម"។

- **chrF++ 16.5** · `repetition_hallucination`
  - EN: "If you took a cloud, wrapped it around your head and then duct-taped it, that's what a white-out is like," Mr Zahab, explained.
  - REF: "ប្រសិនបើអ្នកបានយកពពក គ្របព័ទ្ធក្បាលរបស់អ្នកហើយបន្ទាប់មករុំវាជុំវិញ នោះហើយគឺសស្លុប" លោក ហ្សាហាប់ បានពន្យល់។
  - HYP: "ប្រសិនបើអ្នកយកពពក, បំពងវានៅក្បាលរបស់អ្នក រួចដកកញ្ចក់អញ្ចាញវ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់វ៉ាក់

- **chrF++ 34.4** · `repetition_hallucination`
  - EN: Among the alleged offences are a first-degree murder charge in the shooting death of Constable Daniel Tessier, attempted murder in the wounding of Tessier's partner, Stephane Forbes, and several weapons offences.
  - REF: ក្នុងចំណោមបទល្មើសត្រូវបានចោទប្រកាន់មានការចោទប្រកាន់ពីបទឃាតកម្មកម្រិតទីមួយនៅក្នុងការបាញ់សម្លាប់តម្រួត Daniel Tessier ឃាតកម្មប៉ុនប៉ងក្នុងការធ្វើឱ្យរបួសនៃដៃគូរបស់ Tessier គឺ Stephane Forbes និងបទល្មើសប្រដាប់អាវុធជាច្រើនទៀត។
  - HYP: ក្នុងចំណោមបទល្មើសចោទប្រកាន់រួមមានការចោទប្រកាន់ពីបទល្មើសឃាតកម្មថ្នាក់ទី១ ក្នុងការបាញ់សម្លាប់ស្ទាវដាវដាវដាវដាវដាវដាវដាវដាវដាវដាវដាវ, ការប៉ុនប៉ងឃាតកម្មក្នុងការរងរបួសដៃគូរបស់តេជោដាវដាវដាវដាវដាវដាវដាវដាវដាវដាវជាច្រើន។

- **chrF++ 33.2** · `repetition_hallucination`
  - EN: Since completion of the surgery, the patient has been on immuno-suppressant drugs to prevent rejection of the new limbs.
  - REF: ចាប់តាំងពីការបញ្ចប់នៃការវះកាត់ អ្នកជំងឺត្រូវបានគេប្រើ​ បង្រ្កាប ផ្ស៊ាំ ដើម្បីបង្ការពីការបដិសេធន៍នូវអវយវៈថ្មី។
  - HYP: តាំងពីការបញ្ចប់ការវះកាត់ អ្នកជំងឺត្រូវបានលេបថ្នាំប្រឆាំងនឹងប្រព័ន្ធប្រឆាំងនឹងប្រព័ន្ធប្រឆាំងនឹងប្រព័ន្ធប្រឆាំងនឹងប្រព័ន្ធប្រឆាំងនឹងប្រព័ន្ធប្រឆាំងនឹងការបដិសេធនៃជើងថ្មី។

- **chrF++ 23.8** · `repetition_hallucination`
  - EN: Residents of Leona Valley, Lake Elizabeth, Ritter Ranch, Rancho Vista, Ana Verde and Palmdale received Reverse 911 telephone calls last night alerting them of mandatory evacuations.
  - REF: ប្រជាជនតំបន់លីអូណា វ៉ាឡេ, ឡេក អ៊ីលីហ្សាប៊េត, រីធើ រ៉ាន, រ៉េនចូ វីស្តា, អាណា វែត និងផាមដាល់ បានទទួលការហៅទូរស័ព្ទ 911 យប់មិញ ដោយក្រើនរំឭកពួកគេពីការជម្លៀសជាចាំបាច់។
  - HYP: អ្នករស់នៅសង្កាត់លំផាត់ Lake Elizabeth រោងចក្រក្រក្រពើ Ritter រាជធានីភ្នំពេញ អាណានិគរ និងប៉ាលម៉ាដេល បានទទួលការហៅទូរស័ព្ទ Reverse 911 កាលពីយប់មិញ ដែលព្រមានពួកគេអំពីការបណ្តេញចេញជាកាតព្វកិច្ច។


## omission (2 sentences)

- **chrF++ 25.9** · `omission`
  - EN: His funeral was held at a packed in Cairo today.
  - REF: ពិធីបុណ្យសពរបស់គាត់ត្រូវបានប្រារព្ធឡើងនៅកន្លែងមួយដែលមានការចូលរួមពីមនុស្សយ៉ាងច្រើនកុះករ នៅទីក្រុងខារ៉ូ ក្នុងថ្ងៃនេះ។
  - HYP: សពរបស់គាត់ត្រូវបានរៀបចំនៅកន្លែងកកស្ទះនៅកៃរ៉ូថ្ងៃនេះ។

- **chrF++ 15.7** · `omission`
  - EN: Eleven of those killed were in Paisley and three were in Lady Lake.
  - REF: ក្នុងនោះមនុស្សដប់មួយនាក់ដែលត្រូវបានសម្លាប់នោះគឺនៅក្រុងផាយស្លេ និងបីនាក់ទៀតនៅក្នុងក្រុងឡេឌី ឡេក។
  - HYP: អ្នកស្លាប់ប្រាំមួយនាក់នៅប៉ៃលិនិងបីនៅលេដីបឹង។


## number_mismatch (71 sentences)

- **chrF++ 17.8** · `number_mismatch`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: វាត្រូវបានរំពឹងថាការផ្តាសាយធំនឹងប៉ះពាល់ភាគច្រើននៃសេះ៧០ ដែលត្រូវបានសាងសង់នៅរណប។

- **chrF++ 32.0** · `number_mismatch`
  - EN: At least 11 people were killed Dec. 26 and 27 in neighborhood gang turf fights between drug dealers at shantytown "morro da Mineira" (Miner Hill) in the Catumbi neighborhood of Rio de Janeiro, Brazil.
  - REF: យ៉ាងហោយណាស់មនុស្ស11នាគ់ត្រូវសម្លាប់នៅថ្ងៃទី26និង27ខែធ្នូ នៅជិតខាងរបស់ក្រុមបងធំដែលប្រយុទ្ថជាមួយអ្នកចែកចាយគ្រឿងញៀននៅតំបន់អនាធិបតេយ្យ "morro da Mineira"(ខ្ពង់រាបរ៉ែ)ដែលជិតនៅរីអូដឺហ្សានេរូ ប្រទេសប្រេស៊ីល។
  - HYP: យ៉ាងហោចណាស់មនុស្ស១១នាក់ត្រូវបានសម្លាប់នៅថ្ងៃទី២៦ និង២៧ ខែ ធ្នូ នៅក្នុងការតវ៉ានៅក្នុងសួនច្បារជិតខាង រវាងអ្នកជួញដូរគ្រឿងញៀននៅឃ្លាំងទី១"morro da Mineira" (Miner Hill) នៅក្នុងឃុំកាតូប៊ីទីក្រុងរុស្ស៊ី។

- **chrF++ 34.9** · `number_mismatch`
  - EN: Research group IHS iSuppli said the explosion may cause loss of production of 500,000 iPads during this quarter of the year.
  - REF: ក្រុមស្រាវជ្រាវអាយអេកអេស អាយសាប់ព្លីបាននិយាយថាការផ្ទុះអាចធ្វើឲ្យខាតបង់ផលិតផលរបស់ អាយផេត 500,000ក្នុងឆមាសនៃឆ្នាំនេះ។
  - HYP: ក្រុមស្រាវជ្រាវ IHS iSuppli បាននិយាយថា ការផ្ទុះ អាចបណ្តាលឱ្យបាត់បង់ការផលិតរបស់ iPad ចំនួន ៥០០០,០០០ ក្នុងឆមាសនេះនៃឆ្នាំ។

- **chrF++ 30.9** · `number_mismatch`
  - EN: Now for the first time since her affair, with Tie Domi, she sat down with CBC's George Stroumboulopoulos on his show The Hour to answer his questions about the affair, politics, and other topics during the nine minute chat, on October 9th.
  - REF: ឥឡូវនេះជាលើកទីមួយតាំងពីការលួចសេពគប់របស់គាត់ ជាមួយធី ឌុមី គាត់បានចេញមុខកម្មវិធីទូរទស្សស៊ីប៊ីស៊ីរបស់ ចក ស្តម់ប៊ូលុពូលេសនៃម៉ោងសំនួររបស់គាត់ពីការលួចសេពគប់ នយោបាយ និងប្រធានបទផ្សេងទៀតក្នុងរយពេល9នាទី នៅខែតុលាថ្ងៃទី9។
  - HYP: ឥឡូវនេះជាលើកដំបូងតាំងពីទំនាក់ទំនងរបស់នាង ជាមួយតាយដុំ, នាងបានអង្គុយជាមួយអ្នកសារព័ត៌មានកូរ៉េខាងត្បូង George Stroumboulopoulosនៅក្នុងកម្មវិធីរបស់គាត់ The Hour ដើម្បីឆ្លើយសំណួររបស់គាត់អំពីទំនាក់ទំនងនយោបាយ និង ប្រធានបទផ្សេងទៀតក្នុងអំឡុងពេលនិយាយរយៈពេល៩ នាទី, នៅថ្ងៃទី៩ ខែតុលា។

- **chrF++ 27.0** · `number_mismatch`
  - EN: The problem began around 9:30 a.m CDT (UTC-5) at a loading dock, according to Dallas Fire Department Lt. Joel Lavender, and then spread to a trailer housing some 100,000 cubic feet (approximately 28,300 cubic metres) of gas.
  - REF: បញ្ហានេះបានចាប់ផ្តើមប្រហែលនៅម៉ោង9:30a.m​ CDT(UT-5)នៅផែទំនិញ យោងទៅតាមនាយកដ្ឋានអគ្គីភ័យដាឡាស Lt. ចូឡាវិនដឺ ហើយក៏បានរាលដាលទៅផ្ទះសណ្តោងប្រមាណ100,000​ cubic feet(ប្រហែល28,300 ម៉ែត្រគូប)នៃហ្គាស។
  - HYP: បញ្ហាបានចាប់ផ្តើមប្រហែលម៉ោង៩កន្លះព្រឹក (UTC-5) នៅចំណុចដឹកទំនិញ, យោងតាមទីភ្នាក់ងារពន្លត់អគ្គីភ័យដាល់ស៍ Lt.ជូអែល ឡាវង់ដារ, ហើយបន្ទាប់មករីកសាយទៅលើរថយន្តដឹកទំនិញដែលមានផ្ទះសំណាក់ប្រហែល១០០,០០០ feet cubic (ប្រហែល ២៨,៣០០ ម៉ែត្រ cubic) នៃអគ្គិសនី។


## unseen_source_word (660 sentences)

- **chrF++ 22.4** · `unseen_source_word`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: ត្រូវបានបញ្ជាក់ថាសេះរត់ពូជស្រស់ប្រាំបីនៅរោងចក្ររត់រណបនៅសៀមរាប ត្រូវបានឆ្លងមេរោគជាមួយផ្តាសាយធំនៃសេះ។

- **chrF++ 24.0** · `unseen_source_word`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: រង់វីកត្រូវបានសោនៅខាងក្រៅ, និងត្រូវបានរំពឹងថានឹងស្នាក់នៅដូច្នេះរហូតដល់ពីរខែ។

- **chrF++ 30.3** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្ត្រីក្រសួងឧស្សាហកម្មបុគ្គលិក បាននិយាយថា រោងចក្រ នឹងត្រូវបានដាក់កុងត្រារហូតដល់ ៣០ ថ្ងៃបន្ទាប់ពីមានសញ្ញានៃផ្តាសាយធំចុងក្រោយ។

- **chrF++ 26.4** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណីនេះគឺជាការឆ្លងមេរោគដំបូងនៃសេះរត់, ទោះបីជាឆ្លងមេរោគ រាប់សិបនៃសេះសំរាប់សម្រាក នៅទូទាំងខេត្តសៀមរាប និងខេត្តគីនសែល។

- **chrF++ 23.8** · `unseen_source_word`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: ផ្តាសាយធំគឺឆ្លងខ្លាំង ប៉ុន្តែមិនអាចឆ្លងទៅមនុស្សទេ។


## lexical_semantic (2 sentences)

- **chrF++ 20.8** · `lexical_semantic`
  - EN: "We have no idea what the result of that would be."
  - REF: "យើងពុំដឹងថានឹងទទួលបានលទ្ធផលយ៉ាងដូចម្តេចឡើយ។"
  - HYP: "យើងគ្មានគំនិតថា លទ្ធផលនៃរឿងនោះនឹងមានអ្វី"។

- **chrF++ 23.1** · `lexical_semantic`
  - EN: The teams now go on to play a one-day series followed by a test match series.
  - REF: បច្ចុប្បន្នក្រុមជាច្រើនបន្តការប្រកួតក្នុងស៊េរីរយៈពេលមួយថ្ងៃក្រោយពីការប្រកួតស៊េរីសាកល្បងមួយ។
  - HYP: ក្រុមការងារ ឥឡូវបន្តលេង Series មួយថ្ងៃ ត្រូវបានបន្តដោយ Series ប្រកួតសាកល្បង។
