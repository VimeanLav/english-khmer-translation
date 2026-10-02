# Error analysis: A: Transformer from scratch

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 8.4** · `omission`
  - EN: Fabio Capello has emerged as the new favourite to succeed Steve McClaren as the England football team's new head coach after José Mourinho ruled himself out of taking the job.
  - REF: ហ្វាប៊ីអូ ខាភេឡូ បានក្លាយជាអ្នកដែលគេសំលឹងឃើញក្នុងការស្នងតំណែងពី ស្ទេវ ម៉ាកក្លារេន ជាមេគ្រូបង្វឹកថ្មីរបស់ក្រុមបាល់ទាត់អង់គ្លេស ក្រោយពីជូសេ ម៉ូរីនហូ បានបញ្ឈប់ខ្លួនឯងក្នុងការធ្វើការងារ។
  - HYP: ហ្វាប៊ីឡូបខេខេខេឡូបានចេញមុខជាកីឡាករថ្មី ដើម្បីទទួលបានជោគជ័យ។

- **chrF++ 10.6** · `unseen_source_word`
  - EN: Although Beast Loose in Paradise is more 'movie-esque' and 'horror-ish' on purpose.
  - REF: ទោះបីជាចម្រៀង Beast Loose in Paradise មាន 'លក្ខណៈភាពយន្ត'និង 'ដូចជារន្ធត់'ច្រើនក៏ដោយ។
  - HYP: ទោះបីជាលោកប៊ុសាស ខាងលើក្រុមបេរ៉ាគឺជា "សច្ចភាព" និង សុក្ររបស់ប៊័រ ខាងលើគោលបំណងរបស់ប៊័រ ។

- **chrF++ 11.0** · `lexical_semantic`
  - EN: The cup will be ran with special precautions in place to attempt to keep the state free of the virus.
  - REF: ពាន់រង្វាន់នោះត្រូវអនុវត្តដោយប្រុងប្រយ័ត្នបំផុតជាងមុន ធ្វើយ៉ាងណារក្សាស្ថានភាពគ្មានមេរោគ។
  - HYP: កែវនេះនឹងដំណើរការដោយមានជំនួយពិសេសដើម្បីព្យាយាមរក្សាភាពរដ្ឋ។

- **chrF++ 12.2** · `unseen_source_word`
  - EN: After one year the team split and Cade was tagged with another wrestler.
  - REF: មួយឆ្នាំក្រោយកុ្រមនេះបានបែកបាក់ កេដបានបង្កើតក្រុមជាមួយកីឡាករបោកចំបាប់ផ្សេងទៀត។
  - HYP: បន្ទាប់ពីបានបំបែកក្រុមហើយ Cade ហើយ Cade ទទួលបានសញ្ញាមួយឈុត។

- **chrF++ 13.0** · `unseen_source_word`
  - EN: It is caused by obstructed arteries, which causes heart pain in a person's body.
  - REF: ជំងឺនេះបង្កឡើងដោយការស្ទះសរសៃអាកទែ ដែលធ្វើឲ្យបេះដូងអ្នកជំងឺចុកចាប់នៅក្នុងខ្លួន។
  - HYP: បណ្តាលមកពីពង្រាយសរសៃឈាម បណ្តាលឱ្យមានការឈឺចាប់បេះដូងរបស់មនុស្សម្នាក់។

- **chrF++ 13.5** · `lexical_semantic`
  - EN: A dominant first half display from Australia saw them defeat Wales in Cardiff.
  - REF: ក្នុងការប្រកួតដែលបានត្រូវគ្រប់គ្រងទាំងស្រុងមាននៅតង់ទីមួយរបស់ក្រុមអូស្រ្តាលី ដែលផ្តួលក្រុមវែលនៅទីក្រុងខាឌីហ្វ។
  - HYP: វគ្គពាក់កណ្តាលលើកទីមួយដែលមកពីប្រទេសអូស្ត្រាលីបានឃើញពួកគេខេល វេលស៍នៅខាឌីហ៊្លី។

- **chrF++ 13.8** · `unseen_source_word`
  - EN: Last night, the California Aqueduct acted as a barrier to the fire.
  - REF: យប់មិញ ប្រព័ន្ធប្រឡាយកាលីហ្វរនៀ អាខ្វេដាក់បានធ្វើជារបាំងដើម្បីទប់អគ្គិភ័យនេះ។
  - HYP: យប់ម៉ិញនេះ កាលីហ្វ័រនីញ៉ាបានដើរតួជាកន្លែងឆេះភ្លើង។

- **chrF++ 13.9** · `lexical_semantic`
  - EN: In addition to transport disruption, a number of sports have been affected.
  - REF: បន្ថែម​លើស​ពី​ការ​អាក់​ខាន​នៃ​មធ្យោបាយ​ធ្វើ​ដំណើរ​ កីឡា​ជា​ច្រើន​ប្រភេទ​បានរងផល​ប៉ះពាល់ផងដែរ​។
  - HYP: បន្ថែមពីលើការដឹកជញ្ជូនឋានចោល ចំនួនកីឡា ត្រូវមានផលប៉ះពាល់។

- **chrF++ 14.0** · `lexical_semantic`
  - EN: The planet is relatively much closer to its star than Earth is to the Sun.
  - REF: ភពនេះទៅតារារបស់វាមានចម្ងាយជិតជាងពីផែនដីទៅព្រះអាទិត្យ។
  - HYP: ភពគឺជិតស្ដិតដែលជិតៗគ្នារបស់ខ្លួនគឺផែនដីគឺស្ថិតនៅស៊ូន។

- **chrF++ 14.1** · `lexical_semantic`
  - EN: It did indicate that acute care emergency patients would not be turned away.
  - REF: វាចង្អុលបង្ហាញថាអ្នកជំងឺសង្គ្រោះបន្ទាន់ធ្ងន់ធ្ងរមិនអាចត្រូវបដិសេធចោលនោះទេ។
  - HYP: មានការយកចិត្តទុកដាក់លើការថែទាំយ៉ាង ស្រួចស្រាវ នឹងមិនត្រូវបានប្រគល់ចោលឡើយ។

- **chrF++ 14.3** · `omission`
  - EN: Friends of the Earth was cautiously cheered by the committee's commitment to energy efficiency, and support of reduced emissions.
  - REF: អង្គការផ្នែកបរិស្ថាន មិត្តភក្ដិភពផែនដី ត្រូវបានសាទរយ៉ាងប្រយ័ត្នប្រយែងដោយការប្ដេជ្ញារបស់គណៈកម្មធិការដើម្បីទទួលបានប្រសិទ្ធិភាពផ្នែកថាមពល និងការគាំទ្រការកាត់បន្ថយការបំភាយឧស្ម័ន។
  - HYP: ចំណុចនៃផែនដីផែនដីគឺជាធាតុសំខាន់ដែលរៀបចំដោយគណៈកម្មាធិការថាមពល ដើម្បីបង្កើនប្រសិទ្ធភាព។

- **chrF++ 14.6** · `unseen_source_word`
  - EN: Before Pujols' mammoth homer, Lidge had saved three straight NLCS games and dominated the Cardinals over a two-year stretch.
  - REF: មុនទទួលបានពិន្ទុរត់ទៅទីដោយកីឡាមាឌធំរបស់លោកភូជូល លិជ្ចបានយកឈ្នះការប្រកូតNLCS បីដងជាប់ៗគ្នា និងមានប្រៀបជាងក្រុមកាឌីណល ក្នុងរយៈពេលពីរឆ្នាំនេះ។
  - HYP: មុនពេលគាត់ពុកលីមូដែលជាផ្ទះ លីមូដ លីដបានសង្គ្រោះជាប់លេខបីរបស់ NLCS និងប្រៀឡង់ Cardald លើសពីរឆ្នាំមកហើយ។

- **chrF++ 15.0** · `repetition_hallucination`
  - EN: Finnish theatrical hard rock band Lordi have released Beast Loose in Paradise - which will be the soundtrack to the band's upcoming horror movie Dark Floors - as a downloadable single.
  - REF: ក្រុមសម្តែងហាដរ៉ក់ហ្វាំងឡង់ឈ្មោះថា Lordi បានចេញបទចម្រៀងមានឈ្មោះថា Beast Loose in Paradise - ដែលនឹងជាបទចម្រៀងនៅក្នុងភាពយន្តរន្ធត់ញាប់ញ័រដែលនឹងដាក់បញ្ចាំងនៅក្នុងពេលឆាប់ៗនេះឈ្មោះ Dark Floors ដែលជាចម្រៀងអាចដោនឡូតបាន។
  - HYP: ក្រុមជនជាតិហ្វាំងឡង់ដ៏លំបាកចិត្តរបស់ក្រុមតន្រ្តីរ៉ដឌី ឡាំងឌី ឡសសសេ នៅផាដឺ នៅប៉ារ៉ាដ ដែលនឹងក្លាយជារឿងភាគខាងលើខ្សែភាពយន្តថ្មីរបស់ក្រុមនេះ ដ័រ ហ័រ ហ័រ ហ័រ - ជារឿងដ៏គួរទាញយកតែមួយតែមួយ។

- **chrF++ 15.1** · `lexical_semantic`
  - EN: They should only adopt an ethical investment approach with specific justification and not on the grounds of individual moral views.
  - REF: ពួកគេត្រូវតែរើសយកតែវិធីសាស្រ្តវិនិយោគមួយប្រកបដោយសីលធម៌ ដោយមានយុត្តិកម្មជាក់លាក់ត្រឹមត្រូវប៉ុណ្ណោះ ហើយមិនមែននៅលើមូលដ្ឋាននៃទស្សនៈសីលធម៌បុគ្គលនោះទេ។
  - HYP: ពួកគេគួរតែទទួលយកការវិនិយោគលើក្រមសីលធម៌ នឹងបង្កើនការវិនិយោគទៅលើភាពងាយស្រួល និងការអត់ឃ្លានរបស់បុគ្គលម្នាក់ៗ។

- **chrF++ 15.1** · `lexical_semantic`
  - EN: Field Marshal , presently leader of Egypt, has made today a day of mourning.
  - REF: លោកសេនាប្រមុខដែលជាមេដឹកនាំរបស់ប្រទេសអេហ្ស៊ីបក្នុងពេលបច្ចុប្បន្ន បានកំណត់យកថ្ងៃនេះជាថ្ងៃសំរាប់កាន់ទុក្ខ។
  - HYP: ម៉ាហ្វីល ម៉ាលសល  នឹងធ្វើបទបង្ហាញរបស់អេហ្ស៊ីប នៅថ្ងៃនេះបានធ្វើថ្ងៃនៃជីវកាយ។


## repetition_hallucination (29 sentences)

- **chrF++ 24.8** · `repetition_hallucination`
  - EN: The Afghan government has not provided a copy of the text of the Shia Family Law to the UN or to other outside groups requesting it, citing "technical problems", however, the UN and opposition politicians say that the bill contains numerous provisions restricting the rights of women, such as giving their husbands priority in court; requiring the husband's permission to leave the house, obtain education or employment, or to see a doctor; and reserving the custody of children to male relatives.
  - REF: រដ្ឋាភិបាលអាហ្គានីស្ថានមិនបានផ្តល់នូវសំណៅឯកសារច្បាប់មួយនៃច្បាប់ស៊ីអាហ្វ៊េមីលីទៅកាន់ អង្គការសហប្រជាជាតិឬទៅកាន់ក្រុមខាងក្រៅផ្សេងទៀតដែលស្នើសុំវាឡើយ ដោយបាននិយាយថា"កំហុសបច្ចេកទេស" ប៉ុន្តែយ៉ាងណាក៏ដោយ អង្គការសហប្រជាជាតិ និងគណបក្សនយោបាយប្រឆាំងទាំងឡាយនិយាយថា ពង្រាងច្បាប់ផ្ទុកនូវការហាមឃាត់សិទ្ធិរបស់ស្ត្រីជាច្រើន ដូចជាផ្តល់សិទ្ធិអោយប្តីមានអាទិភាពក្នុងតុលាការ;តំរូវអោយសុំសិទ្ធិប្តីប្រសិនបើចង់ចេញពីផ្ទះ សុំសិទ្ធិដើម្បីការទៅរៀនឬទៅធ្វើការ ឬក៏ទៅជួបពិគ្រោះជាមួយវេជ្ជបណ្ឌិត;ហើយរក្សាទុកនូវសិទ្ធិមើលថែរក្សាកូនទៅសាច់ញាតិខាងបុរស។
  - HYP: រដ្ឋាភិបាលអាហ្វហ្គានីស្ថានមិនបានផ្តល់ការចម្លងចម្លងចម្លងនៃអត្ថបទនិន័យគ្រួសារលោកស៊ី ហ្វាយ រឺរឺទៅក្រុមច្បាប់ផ្សេងៗដែលលើកឡើងដោយលើកឡើងថា "បញ្ហាបច្ចេកទេស" ប៉ុន្តែអ្នកនយោបាយអាមេរិកនិងអ្នកនយោបាយគណបក្សប្រឆាំងបាននិយាយថា សេចក្តីព្រាងច្បាប់ដែលមានភាពស្របច្បាប់ដាក់ មិនឲ្យដាក់កំហិតដល់ស្រ្តីទាំងនោះជាប្តី ឬផ្តល់ការអនុញ្ញាតឲ្យកូនក្នុងតុលាការ។

- **chrF++ 31.7** · `repetition_hallucination`
  - EN: Tanks of oxygen, helium and acetylene began to explode after a connector used to join acetylene tanks during the filling process malfunctioned.
  - REF: បំពង់អុកស៊ីសែន អេលីយ៉ូមនិងអឹសាតធីលីនចាប់ផ្តើមផ្ទុះបន្ទាប់ពីខ្សែភ្ជាប់តំណរបំពង់អឹសាតធីលីនកំឡុងពេលចាក់បំពេញដំណើរការខុសប្រក្រតី។
  - HYP: តង់នៃអុកស៊ីសែនអុកស៊ីអេលម៉ាហើយសែសបានចាប់ផ្តើមបណ្ដើរចេញពីនាវាបន្ទាប់ពីតភ្ជាប់នឹងរថក្រណាត់យានរថម្រាំងក្នុងអំឡុងពេលដំណើរការដោយខ្លួនខ្លួនខ្លួនសល់។

- **chrF++ 18.0** · `repetition_hallucination`
  - EN: The mass featured hymns, prayers and incense-burning as crowds in and outside the cathedral paid their respects.
  - REF: មានមនុស្សជាច្រើនបានមកជួបជុំគ្នាដោយ​សម្តែង​នូវការគោរពរបស់ពួកគេតាមរយៈការអុជធូប និងច្រៀងចម្រៀងអធិដ្ឋាននៅក្នុងនិងក្រៅសាលធំនៃព្រះវិហារ។
  - HYP: រូបកាយសម្បង្គង្គង្គន់ បួងសួងនិងនៅក្នុងហ្វូងមនុស្សដែលស្រែកនៅខាងក្រៅនិងនៅក្រៅសត្វចិញ្ចឹមរបស់ពួកគេគិតថ្លៃ។

- **chrF++ 22.6** · `repetition_hallucination`
  - EN: Clashes began last night after Estonian authorities removed a controversial Soviet monument, the Bronze Soldier of Tallinn, which Russian-speaking Estonians see as a symbol of the liberation of Eastern Europe from Nazism, while Estonian nationalists view it as a reminder of Soviet occupation.
  - REF: ការប៉ះទង្គិចគ្នាបានចាប់ផ្ដើមកាលពីយប់មិញ បន្ទាប់ពីអាជ្ញាធរអេស្តូនីបានដករូបសំណាកសូវៀតដែលចម្រោងចម្រាស់មួយចេញ ជាទាហានសំរិទ្ធរបស់តាលីន ដែលជនជាតិអេស្តូនីនិយាភាសារុស្សីចាត់ទុកថាជានិមិត្តរូបនៃការរំដោះអឺរ៉ុបខាងកើតចេញពីរបបណាស៊ីស រីឯអ្នកជាតិនិយមអេស្តូនីចាត់ទុកវាថាជាការរំលឹកដល់ការកាន់កាប់របស់សូវៀតទៅវិញ។
  - HYP: លោក ឃើស បានចាប់ផ្តើមកាលពីយប់ម៉ិញ បន្ទាប់ពីអាជ្ញាធរអេស្តូនី បានលុបចេញដោយចំណាត់ការបូស សូនី នៃ សូឡេ សូណា នៃ សូលីព័រ សូណា នៃ រុស្ស៊ី ដែល មើលឃើញជាទិទិកិក ទិកិកិកមិត្តសញ្ញាសញ្ញាសញ្ញា របស់អឺរ៉ុប សាធារណរដ្ឋអ៊ឺរ៉ុប ខណៈដែលកំពុង រំខាន រំលំ ដោយ រំខាន រំខាន រំលំ ដោយ រំលំ ដោយ រំលំ ដោយ រំលំ រំលំ រំលំ រំលំ រំលាស់ រំលំ រំលំ ដោយ រំលំ រំលំ ដោយ រំលំ

- **chrF++ 26.9** · `repetition_hallucination`
  - EN: It became the first ever UK visit from the Pope, which will make Pope Benedict's visit the second papal one.
  - REF: វាជាទស្សនកិច្ចចក្រភពអង់គ្លេសលើកទីមួយបំផុតពីផូប ដែលធ្វើឱ្យទស្សនកិច្ចរបស់ផូប ប៉ែនើឌិក ជាទស្សនកិច្ចលើកទីពីររបស់មេដឹកនាំវិហារកាតូលិក រ៉ូមែន។
  - HYP: វាគឺជាដំណើរទស្សនកិច្ចដំបូងរបស់ចក្រភពអង់គ្លេសដែលនឹងធ្វើទៅទស្សនាផូប ប៉ូប ដែលធ្វើឲ្យលោកប៉ប ប៊ែ្ឆកាទស្សនាទស្សនាទស្សនាកំសាន្តនៀទីពីរ។


## omission (5 sentences)

- **chrF++ 8.4** · `omission`
  - EN: Fabio Capello has emerged as the new favourite to succeed Steve McClaren as the England football team's new head coach after José Mourinho ruled himself out of taking the job.
  - REF: ហ្វាប៊ីអូ ខាភេឡូ បានក្លាយជាអ្នកដែលគេសំលឹងឃើញក្នុងការស្នងតំណែងពី ស្ទេវ ម៉ាកក្លារេន ជាមេគ្រូបង្វឹកថ្មីរបស់ក្រុមបាល់ទាត់អង់គ្លេស ក្រោយពីជូសេ ម៉ូរីនហូ បានបញ្ឈប់ខ្លួនឯងក្នុងការធ្វើការងារ។
  - HYP: ហ្វាប៊ីឡូបខេខេខេឡូបានចេញមុខជាកីឡាករថ្មី ដើម្បីទទួលបានជោគជ័យ។

- **chrF++ 16.8** · `omission`
  - EN: But most observers believe that the portraits were taken down by the order of Kim Jong Il himself, who might be trying to downsize his own personality cult.
  - REF: ប៉ុន្តែ ក្រុមអ្នកសង្កេតការណ៍ភាគច្រើនជឿជាក់ថា រូបថតនេះ ត្រូវបានដកចេញដោយការបញ្ជារបស់លោកគីម ជុងអ៊ីល ខ្លួនឯងផ្ទាល់ ដែលអាចនឹងកំពុងព្យាយាមកាត់បន្ថយការគោរពបុគ្គលផ្ទាល់ខ្លួនរបស់គាត់។
  - HYP: ប៉ុន្តែអ្នកសង្កេតភាគច្រើនជឿថាកំពង់ផែត្រូវបានបិទ។

- **chrF++ 20.9** · `omission`
  - EN: In a speech on Sunday in Abu Dhabi, the president also urged Gulf states to join Washington in confronting Iran, which he called "the world's leading state sponsor of terror."
  - REF: នៅក្នុងសុន្ទរកថាកាលពីថ្ងៃអាទិត្យនៅ អាប៊ូ ដាប៊ី លោកប្រធានាធិបតីក៏ទទូចឲ្យរដ្ឋនៅឈូង​សមុទ្រចូលរួមជាមួយវ៉ាស៊ីងតោនក្នុងការប្រឈមមុខជាមួយប្រទេសអឺរ៉ង់ ដែលលោកហៅថា "រដ្ឋគាំទ្រភេរវករនាំមុខគេក្នុងពិភពលោក។"
  - HYP: ក្នុងសុន្ទរកថានៅថ្ងៃអាទិត្យនៅទីក្រុងអាប៊ូដាបី ប្រធានាធិបតីក៏បានជំរុញរដ្ឋផងដែរ។

- **chrF++ 22.1** · `omission`
  - EN: The ICRC rarely discloses publicly the contents of the confidential reports it gives to governments.
  - REF: ICRC កម្របង្ហាញជាសាធារណៈអំពីមាតិកានៃសេចក្តីរាយការណ៍សម្ងាត់ ដែលខ្លួនបានផ្តល់ឲ្យរដ្ឋាភិបាល។
  - HYP: ICRC កម្រ បញ្ចេញមាតិកា ជាសាធារណៈ។

- **chrF++ 14.3** · `omission`
  - EN: Friends of the Earth was cautiously cheered by the committee's commitment to energy efficiency, and support of reduced emissions.
  - REF: អង្គការផ្នែកបរិស្ថាន មិត្តភក្ដិភពផែនដី ត្រូវបានសាទរយ៉ាងប្រយ័ត្នប្រយែងដោយការប្ដេជ្ញារបស់គណៈកម្មធិការដើម្បីទទួលបានប្រសិទ្ធិភាពផ្នែកថាមពល និងការគាំទ្រការកាត់បន្ថយការបំភាយឧស្ម័ន។
  - HYP: ចំណុចនៃផែនដីផែនដីគឺជាធាតុសំខាន់ដែលរៀបចំដោយគណៈកម្មាធិការថាមពល ដើម្បីបង្កើនប្រសិទ្ធភាព។


## number_mismatch (79 sentences)

- **chrF++ 30.7** · `number_mismatch`
  - EN: Research group IHS iSuppli said the explosion may cause loss of production of 500,000 iPads during this quarter of the year.
  - REF: ក្រុមស្រាវជ្រាវអាយអេកអេស អាយសាប់ព្លីបាននិយាយថាការផ្ទុះអាចធ្វើឲ្យខាតបង់ផលិតផលរបស់ អាយផេត 500,000ក្នុងឆមាសនៃឆ្នាំនេះ។
  - HYP: ក្រុមស្រាវជ្រាវឈ្មោះ IHS បានឲ្យដឹងថា ការផ្ទុះនេះ អាចបាត់បង់ចំនួន 500,000 ក្បាល នៃចំនួន 500,000 អំឡុងត្រីមាសនេះ ក្នុងឆ្នាំនេះ។

- **chrF++ 35.4** · `number_mismatch`
  - EN: The Moldovan leader noted that he has sent a package of documents to Russia regarding the activity of 13 Transnistrian military companies.
  - REF: អ្នកដឹកនាំម៉ូដូវ៉ានបានកត់សំគាល់ថាគាត់បានផ្ញើរកញ្ចប់មួយនៃឯកសារទៅរុស្សីចំពោះសកម្មភាពនៃក្រុមហ៊ុនយោធាត្រេនស្នីស្រ្ថីនចំនួន13។
  - HYP: មេដឹកនាំជាន់ខ្ពស់លោកមឺនៀ បានកត់សម្គាល់ថាគាត់បានបញ្ជូនឯកសារមួយទៅកាន់ប្រទេសរុស្ស៊ីទាក់ទងនឹងសកម្មភាពនៃក្រុមហ៊ុន ត្រានស្តេន។

- **chrF++ 35.6** · `number_mismatch`
  - EN: During the trading session following this two-day summit, that is expected to result in the "Declaration of Riyadh", the price of petroleum rose $0.80 in the New York market and $0.66 in London.
  - REF: ក្នុងអំឡុងពេលជួញដូរ បន្ទាប់ពីកិច្ចប្រជុំកំពូលរយៈពេលពីរថ្ងៃនេះ នោះត្រូវបានរំពឹងថាចេញជាលទ្ធផលនៅក្នុង"ការប្រកាសនៃរីយ៉ាត" តំលៃនៃប្រេងសាំងបានឡើង0.80ដុល្លារនៅទីផ្សារញ៉ូវយ៉កនិង0.66ដុល្លារនៅឡុនដុន។
  - HYP: ក្នុងពេលធ្វើជំនួញនៃកិច្ចប្រជុំរយៈពេលពីរថ្ងៃនេះ ដែលនឹងត្រូវរំពឹងថាជាលទ្ធផលនៅ "Donlaad" តម្លៃនៃតម្លៃប្រេងសាំងបានកើនឡើងដល់ $0.80 នៅទីផ្សារនៅញូវយ៉ក និង $66.066 ក្នុងទីក្រុងឡុងដ៍។

- **chrF++ 26.4** · `number_mismatch`
  - EN: "In the past eight days alone we have received reports on the killing of one journalist, Munir Shakir, in Balochistan on August 14 2011, and the disappearance of another journalist, Rehmatullah Daparkhel, three days earlier in North Waziristan on August 11," said spokesperson for the United Nations High Commissioner for Human Rights, Rupert Colville.
  - REF: ត្រឹមតែ8ថ្ងៃចុងក្រោយនេះ យើងបានទទួលរបាយការណ៍អំពីការសំលាប់អ្នកសារព័តិមានម្នាក់ឈ្មោះមុនាសាគា នៅប្រទេសបាឡូគីស្ថាននៅថ្ងៃទី14ខែសីហាឆ្នាំ2011 និងការបាត់ខ្លួនរបស់អ្នកសារព័តិមានម្នាក់ទៀតឈ្មោះរេម៉ាទុឡា ដាប៉ាខេល 3ថ្ងៃមុននោះនៅភាគខាងជើងនៃតំបន់វ៉ាហ្ស៊ីរីស្ថាននៅថ្ងៃទី11ខែសីហា នេះបើយោងតាមអ្នកនាំពាក្យនៃអង្គការត្រួតពិនិត្យសិទិ្ធមនុស្សជាន់ខ្ពស់នៃអង្គការសហប្រជាជាតិ លោករូភើត ខូវីល។
  - HYP: "ក្នុងរយៈពេលប្រាំបីថ្ងៃទៀត យើងបានទទួលសេចក្តីរាយការណ៍លើអ្នកកាសែតរបស់អ្នកកាសែតអ្នកកាសែតម្នាក់ លោក Munirkirkir នៅបាលី ខែសីហា ឆ្នាំ2011 និងប្បយភាពមិនពេញចិត្តចំពោះអ្នកកាសែតម្នាក់ទៀត ចូរែល រីយ៉ាផាស ដែលបាននិយាយកាលពីបីថ្ងៃមុនថា "ថ្ងៃនេះយើងបានទទួលសេចក្តីរាយការណ៍ជាន់ខ្ពស់នៃអង្គការសហប្រជាជាតិទី11 ខែសីហា។"

- **chrF++ 28.7** · `number_mismatch`
  - EN: The tremor, lasting about 2 minutes, sparked panic in numerous seaside communities on the island.
  - REF: ការញ័រកើតឡើងប្រហែល2នាទី បង្កអោយមានការភិតភ័យពីសហគមនៅតាមឆ្នេរជាច្រើននៅលើកោះនេះ។
  - HYP: លំអច្ចរណ៍ចុងក្រោយ ថ្មីៗនេះបានបង្កឲ្យមានការព្រួយបារម្ភជាច្រើននៅក្នុងសហគមន៍ជាច្រើននៅលើកោះនេះ។


## unseen_source_word (388 sentences)

- **chrF++ 26.2** · `unseen_source_word`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: វាត្រូវបានគេបញ្ជាក់ថា សេះចំនួនប្រាំបីរូប បានចប់ប្រណាំងនៅឯ Randick Rawickce ក្នុង ទីក្រុងស៊ីដនីត្រូវបានឆ្លងដោយសាហ្វេន ក្នុងក្រុងប្រ៊ីនហ្សា។

- **chrF++ 23.9** · `unseen_source_word`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: រ៉ាដវិកត្រូវបិទ ហើយត្រូវគេរំពឹងថានៅតែចង់បន្តរយៈពេលពីរខែ។

- **chrF++ 19.8** · `unseen_source_word`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: មានការរំពឹងថា អាស្រ័យលើជំងឺផ្តាសាយនេះនឹងប៉ះពាល់ដល់ភាគច្រើនរបស់គណបក្សដែលមានទំហំ 700 នាក់ នៅ Randwick។

- **chrF++ 23.3** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្រ្តី NSW សំរាប់តំបន់បាននិយាយថា កន្លែងនឹងត្រូវបញ្ចប់រហូតដល់ 30 ថ្ងៃបន្ទាប់ពីសញ្ញានៃជំងឺផ្តាសាយជ្រូក។

- **chrF++ 17.0** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណីគឺចំលងលើកដំបូងនៃការប្រណាំងផូស្វ័រ ទោះបីជាមានការឆ្លងថ្មីជាច្រើននៅពាសពេញS NSW និងឃ្វីនស៍លែនដ៍។


## lexical_semantic (280 sentences)

- **chrF++ 19.9** · `lexical_semantic`
  - EN: The flu is highly contagious but cannot be transmitted to humans.
  - REF: មេរោគនេះងាយឆ្លង​តែមិនឆ្លងដល់មនុស្សឡើយ។
  - HYP: ជំងឺផ្តាសាយគឺខ្ពស់ ប៉ុន្តែមិនអាចបញ្ជូនទៅមនុស្សបានឡើយ។

- **chrF++ 39.4** · `lexical_semantic`
  - EN: The national racing shutdown was costing the industry tens of millions of dollars every day.
  - REF: ការបិទការប្រណាំងថ្នាក់ជាតិ បានធ្វើឲ្យវិស័យនេះខាតបង់រាប់លានដុល្លាក្នុងមួយថ្ងៃៗ។
  - HYP: ការប្រណាំងប្រជែងជាតិមានការបិទឧស្សាហកម្មចំនួនដប់លានដុល្លារក្នុងមួយថ្ងៃៗរៀងរាល់ថ្ងៃ។

- **chrF++ 39.5** · `lexical_semantic`
  - EN: Racing is expected to resume in all Australian states except NSW and Queensland on the weekend.
  - REF: កម្មវិធីប្រណាំងត្រូវបានរំពឹងថានឹងប្រព្រឹត្តទូទាំងរដ្ឋនៅប្រទេសអូស្រ្តាលីលើកលែងតែញូវសោវែលនិងឃ្ខីនសាឡេននៅចុងសប្តាហ៍។
  - HYP: ការប្រណាំងត្រូវរំពឹងថាអាចបន្តបាននៅក្នុងរដ្ឋអូស្រ្តាលី លើកលែងតែ NSW និងឃ្វីនស៍លែនដ៍ នៅចុងសប្តាហ៍នេះ។

- **chrF++ 11.0** · `lexical_semantic`
  - EN: The cup will be ran with special precautions in place to attempt to keep the state free of the virus.
  - REF: ពាន់រង្វាន់នោះត្រូវអនុវត្តដោយប្រុងប្រយ័ត្នបំផុតជាងមុន ធ្វើយ៉ាងណារក្សាស្ថានភាពគ្មានមេរោគ។
  - HYP: កែវនេះនឹងដំណើរការដោយមានជំនួយពិសេសដើម្បីព្យាយាមរក្សាភាពរដ្ឋ។

- **chrF++ 36.3** · `lexical_semantic`
  - EN: Foxconn halted production to investigate, saying "All operations at the affected workshop remain suspended and production at all other workshops that carry out similar processing functions have also been halted pending the results of the investigation. "
  - REF: ហ្វកកនបានផ្អាកផលិតកម្មសំរាប់ការស៊ើបអង្កេតបាននិយាយថា"ប្រតិបត្តិការទាំងអស់ក្នុងការដ្ឋានការងារនៅសល់ត្រូវព្យូរហើយផលិតកម្មដែលមានមុខងារប្រហែលក្នុងការដ្ឋានទាំងអស់ក៏ត្រូវផ្អាករហូតដល់លទ្ធផលនៃការស៊ើបអង្កេត។"
  - HYP: ក្រុមហ៊ុនហ្វូខខូនបានផ្អាកដំណើរការមួយដើម្បីស៊ើបអង្កេតដោយនិយាយថា "ប្រតិបត្តិការនៅរោងជាងនេះនៅតែមានដំណើរការនិងការផលិតនៅរោងជាងផ្សេងទៀតដែលផ្ទុកនូវដំណើរការដ៏ស្រដៀងគ្នានេះក៏ត្រូវបានគេផ្អាកនូវលទ្ធផល" ក្នុងការស៊ើបអង្កេតនោះ។
