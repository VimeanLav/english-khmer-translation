# Error analysis: C: NLLB full fine-tuning

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 6.7** · `repetition_hallucination`
  - EN: The second fire, the "Briggs Fire", began shortly after 2:00 pm near 8334 Soledad Canyon Road and Briggs Road, south of the freeway.
  - REF: អគ្គិភ័យទីពីរឈ្មោះថា "ព្រីក ហ្វៃអើ" បានចាប់ផ្ដើមឆាបឆេះរយៈពេលខ្លី​ក្រោយម៉ោង 2:00 រសៀលជិត 8334 សូលីដាត ខេនយ៉ុន រ៉ូត និងព្រីក រ៉ូត ភាគខាងត្បូងផ្លូវហ្រ្វីវ៉េ។
  - HYP: អគ្គីភ័យទីពីរ គឺ"អគ្គីភ័យខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ

- **chrF++ 10.1** · `omission`
  - EN: "There is a growing sense of insecurity among media persons who increasingly interpret each attack on journalists as a warning to ‘behave,’" the HRCP said last Monday.
  - REF: អង្គការអេចអាលស៊ីភីបាននិយាយនៅថ្ងៃច័ន្ទមុននេះថា៖ "មានការកើនឡើងនៃអសុវត្ថិភាពក្នុងចំណោមក្រុមអ្នកផ្សព្វផ្សាយដែលបានចាត់ទុករាល់ការវាយប្រហារទៅលើអ្នកសារព័ត៌មានថាជាការព្រមានទៅលើ‘អាកប្បកិរិយា‘។"
  - HYP: មជ្ឈត្តកម្មមនុស្សធម៌បាននិយាយថា កាលពីថ្ងៃច័ន្ទមុន។

- **chrF++ 11.4** · `unseen_source_word`
  - EN: A large police presence watched over the scenes as mourners wept.
  - REF: ប៉ូលីសជាច្រើនបានមានវត្តមាននៅកន្លែងផ្ទាល់ ដើម្បីមើលការខុសត្រូវដល់អ្នកកាន់ទុក្ខដែលបានយំ។
  - HYP: មានសមត្ថភាពនគរបាល ដ៏ធំមួយ បានសង្កេត ជាង វេទិកា ខណៈដែល អ្នកពិបាកចិត្ត ស្រែក។

- **chrF++ 11.7** · `unseen_source_word`
  - EN: In addition to transport disruption, a number of sports have been affected.
  - REF: បន្ថែម​លើស​ពី​ការ​អាក់​ខាន​នៃ​មធ្យោបាយ​ធ្វើ​ដំណើរ​ កីឡា​ជា​ច្រើន​ប្រភេទ​បានរងផល​ប៉ះពាល់ផងដែរ​។
  - HYP: ក្រៅពី ការរំខានដឹកជញ្ជូន មួយចំនួន កីឡា ត្រូវបានប៉ះពាល់។

- **chrF++ 11.8** · `unseen_source_word`
  - EN: New Zealand's Kyle Mills led the bowling attack with 3 for 44.
  - REF: ឃីឡេ មៀលស៍នៃប្រទេសញ៉ូវហ្សេឡង់បាននាំមុខក្នុងការគប់បាល់ 3 ដោយទទួលបាន 44 ពិន្ទុ។
  - HYP: កីឡាការិនីកម្ពុជា កៃល ម៉ីលស បានដឹកនាំ ការវាយប្រហារប៊ូឡីង ដោយបាន ៣ សម្រាប់ ៤៤។

- **chrF++ 12.0** · `unseen_source_word`
  - EN: Shenouda was dressed in full regalia, complete with a gold crown.
  - REF: សេននូដា ត្រូវបានគេស្លៀកពាក់អោយក្នុងសំលៀកបំពាក់រាជា ជាមួយនឹងម្កុជមាស។
  - HYP: ស្រីណុដាពាក់ខោអាវធំ, ពេញជាមួយមួកសុវត្ថិភាពពណ៌មាស។

- **chrF++ 12.1** · `unseen_source_word`
  - EN: Dannie Abse is well-known for being a poet and a medical doctor.
  - REF: លោកដានី អាប់សេ ល្បីឈ្មោះជាកវី​តែងកំណាព្យ និង​ជាវេជ្ជបណ្ឌិត​ផ្នែកវេជ្ជសាស្រ្ត​។
  - HYP: Dannie Abseល្បីល្បាញដោយសារតែជាកំណាព្យករនិងគ្រូពេទ្យ។

- **chrF++ 12.1** · `repetition_hallucination`
  - EN: In the 2007 Rugby World Cup, New Zealand overwhelmed tournament newcomers Portugal.
  - REF: នៅក្នុងប្រកួត រ៉ាប់ប៊ី វើលដ៍ ខាប់ ឆ្នាំ2007 ក្រុមញូហ្ស៊េលែនបានសម្លុតក្រុមកីឡាករថ្មីនៃប៉ទុយហ្គាល់ជាច្រើននៅក្នុងការប្រកួតនោះ។
  - HYP: នៅក្នុងការប្រកួតពូលពិភពលោកឆ្នាំ ២០០៧ កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាបាល់ទាត់កីឡាប

- **chrF++ 12.5** · `number_mismatch`
  - EN: New Zealand are top of Pool C with ten points, ahead of Scotland with 5 and Italy with 4.
  - REF: ក្រុមញូហ្ស៊េលែនឈរលើកំពូលតារាងក្នុងពូលដោយមានដប់ពិន្ទុមុនក្រុមស្កុតឡេនដែលមាន5ពិន្ទុ និងក្រុមអ៊ីតាលីដែលមាន4ពិន្ទុ។
  - HYP: កម្ពុជានៅលើពូជ Cមាន១០ពិន្ទុ, នៅមុខសក្កដាមាន៥ និងអ៊ីតាលីមាន៤។

- **chrF++ 13.1** · `unseen_source_word`
  - EN: During rush hours, the 9 is a skip-stop supplement to the 1, running the same route but skipping some stops in Upper Manhattan and the Bronx.
  - REF: ក្នុងម៉ោងមមាញឹក រថភ្លើងទាំង​ 9 ​គ្រឿង ធ្វើជារថភ្លើងជំនួយចំពោះរថភ្លើង 1 គ្រឿង ដោយរត់បង្ហួសចំណត ពោលគឺរត់តាមផ្លូវតែមួយ ប៉ុន្តែបង្ហួសចំណតមួយចំនួននៅ អាប់ភើ មេនហាតធេន និង ឌឹ ប៊្រុនស៍។
  - HYP: ក្នុងអំឡុងពេលម៉ោងសក្ដានុពល ៩ គឺជាថ្នាំបន្ថែម skip-stop ទៅនឹង ១, បើកផ្លូវដដែល តែច្រានចោលមួយចំនួនឈប់នៅម៉ាតណាថនខាងលើ និងប្រ៊ុងកស។

- **chrF++ 13.2** · `unseen_source_word`
  - EN: Chicago Fire plays the winner of the New England Revolution/New York Red Bulls 2 Leg affair which is currently tied 0-0.
  - REF: ក្រុមឈីខាហ្គូនឹងជួបក្រុមឈ្នះរវាងក្រុមញូ អ៊ីនឡេន រីវ៉ូលូសុន/ញូយ៉ក រេត ប៊ូល 2ជើងដែលបច្ចុប្បន្នមានពន្ទុស្មើ 0-0។
  - HYP: ចិញ្ចៀនអំពូលលេងអ្នកឈ្នះរឿងកំណែទម្រង់នីយូអង់គ្លេស / រឿងក្រហមគោទីក្រុងញូវយ៉ក 2 Leg ដែលជាស្មើឥឡូវនេះគឺ០-០។

- **chrF++ 13.4** · `unseen_source_word`
  - EN: The ship missed a course change and ran agroung off Gil Island.
  - REF: នាវានេះបានខកខានការចតចូលច្រាំង និងជាប់កឿងនៅក្បែរកោះហ្គីលអាយឡេន។
  - HYP: ទូកបាត់ការផ្លាស់ប្តូរវគ្គនានាហើយរត់ខូចខាតនៅឆ្នេរសមុទ្រកោះគិល។

- **chrF++ 13.8** · `unseen_source_word`
  - EN: The Senators will play against Frolunda of Sweden's elite league.
  - REF: ក្រុម Senators នឹងប្រកួតជាមួយក្រុម Frolunda នៃសហព័ន្ធដ៏ខ្លាំងខ្លារបស់ប្រទេសស៊ុយអែត។
  - HYP: ព្រឹទ្ធបុរស នឹងលេងប្រឆាំងជាមួយស្រីល័ក្ខនៃជម្រើសជាតិខ្ពង់ខ្ពស់របស់ស្វ៊ីស។

- **chrF++ 14.5** · `omission`
  - EN: Eleven of those killed were in Paisley and three were in Lady Lake.
  - REF: ក្នុងនោះមនុស្សដប់មួយនាក់ដែលត្រូវបានសម្លាប់នោះគឺនៅក្រុងផាយស្លេ និងបីនាក់ទៀតនៅក្នុងក្រុងឡេឌី ឡេក។
  - HYP: ម្នាក់រយនៃអ្នកស្លាប់នៅប៉ៃលិននិងបីនៅបឹងស្រី។

- **chrF++ 14.5** · `repetition_hallucination`
  - EN: Mayon secured the title of Belgian 1/4 Triathlon champion, in addition to the previously won Sprint Triathlon and Long Distance championships.
  - REF: ម៉ាយ៉ុនរក្សាជើងឯកនៃប៊ែលហ្សិកម្ចាស់ជើងឯក 1/4 កីឡាទ្រីយ៉ាថ្លុន ក្រៅពីឈ្នះការប្រកួតជើងឯករត់ប្រណាំងទ្រីយ៉ាថ្លុន និងចម្ងាយឆ្ងាយកាលពីមុន។
  - HYP: ម៉ៃន បានធានាសុវត្ថិភាព ពានរង្វាន់បែលហ្ស៊ិក 1/4 Triathlon, ក្រៅពីបានឈ្នះមុនពេលនេះពានរង្វាន់ប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រណាំងប្រ


## repetition_hallucination (8 sentences)

- **chrF++ 39.7** · `repetition_hallucination`
  - EN: According to the Committee to Protect Journalists, nine journalists have been killed in Pakistan this year, and at least 16 were killed in 2010.
  - REF: យោងតាមគណៈកម្មការការពារអ្នកសារព័ត៌មានបានអោយដឹងថា នៅក្នុងឆ្នាំនេះ មានអ្នកសារព័ត៌មានចំនួន៩នាក់ហើយត្រូវបានសំលាប់ នៅក្នុងប្រទេសប៉ាគីស្ថាន ហើយយ៉ាងហោចណាស់ចំនួន16នាក់ត្រូវបានសំលាប់ ក្នុងឆ្នាំ2010។
  - HYP: យោងតាម គណៈកម្មាធិការការការពារអ្នកសារព័ត៌មាន ៩ អ្នកសារព័ត៌មាន ត្រូវបានសម្លាប់នៅប៉ាគីស្ថាន ឆ្នាំនេះ ហើយយ៉ាងតិច ១៦ ត្រូវបានសម្លាប់នៅក្នុងឆ្នាំ២០១០។

- **chrF++ 6.7** · `repetition_hallucination`
  - EN: The second fire, the "Briggs Fire", began shortly after 2:00 pm near 8334 Soledad Canyon Road and Briggs Road, south of the freeway.
  - REF: អគ្គិភ័យទីពីរឈ្មោះថា "ព្រីក ហ្វៃអើ" បានចាប់ផ្ដើមឆាបឆេះរយៈពេលខ្លី​ក្រោយម៉ោង 2:00 រសៀលជិត 8334 សូលីដាត ខេនយ៉ុន រ៉ូត និងព្រីក រ៉ូត ភាគខាងត្បូងផ្លូវហ្រ្វីវ៉េ។
  - HYP: អគ្គីភ័យទីពីរ គឺ"អគ្គីភ័យខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ្នុរខ

- **chrF++ 37.8** · `repetition_hallucination`
  - EN: A package of six media reform bills introduced last week before Australia's Parliament — including one proposing appointing a Public Interest Media Advocate (PIMA) to monitor print and online sectors — was shelved yesterday by the Australian Labor Party, with only two passed before a seven week break for the country's legislative body.
  - REF: កញ្ចប់សេចក្តីព្រាងច្បាប់ស្ដីពីកំណែទម្រង់ប្រព័ន្ធផ្សព្វផ្សាយចំនួនប្រាំមួយដែលបានដាក់ចេញនៅសប្តាហ៍ចុងក្រោយចំពោះមុខសភាអូស្រ្តាលី ដោយរួមបញ្ចូលទាំងសំណើសុំតែងតាំងអ្នកតស៊ូមតិប្រព័ន្ធផ្សព្វផ្សាយសម្រាប់អត្ថប្រយោជន៍សាធារណៈ (PIMA) មួយ ដើម្បីតាមដានផ្នែកបោះពុម្ព និងអនឡាញ ត្រូវបានទុកចោលកាលពីម្សិលមិញ ដោយគណបក្សការងារអូស្រ្តាលី ដោយមានច្បាប់តែពីរប៉ុណ្ណោះដែលត្រូវបានអនុម័តមុនពេលសម្រាកចំនួនប្រាំពីរសប្តាហ៍សម្រាប់អង្គការនីតិប្បញ្ញត្តិរបស់ប្រទេសនេះ។
  - HYP: កញ្ចប់នៃសំណើកំណែទម្រង់សារព័ត៌មានប្រាំពីរ ត្រូវបានដាក់ឱ្យដំណើរការសប្តាហ៍មុនមុនមុនពេលសភាអូស្ត្រាលី  ក្នុងនោះមានមួយដែលស្នើតែងតាំង អ្នកគាំទ្រសារព័ត៌មានសាធារណៈប្រយោជន៍ (PIMA) ដើម្បីតាមដានវិស័យបោះពុម្ពផ្សាយនិងអ៊ីនធឺណិត  ត្រូវបានដាក់ក្នុងឃ្លាំងម្សិលមិញ ដោយគណបក្សការងារអូស្ត្រាលី ដោយមានតែពីរ ត្រូវបានអនុម័តមុនពេលឈប់សម្រាកប្រាំពីរសប្តាហ៍សម្រាប់អាជ្ញាធរ

- **chrF++ 34.3** · `repetition_hallucination`
  - EN: The move is akin to the private sector's migration from defined benefit retirement plans to defined contribution benefit plans such as 401(k)s as almost half of a worker’s benefits will not be guaranteed by the year 2075.
  - REF: ដំណើរការនេះដូចគ្នាទៅនឹងជនចំណាកស្រុកនៅវិស័យឯកជនចាប់ពីផែនការអត្ថប្រយោជន៍ចូលនិវត្ត រហូតដល់ផែនការអត្ថប្រយោជន៍វិភាគទានដែលបានកំណត់ដូច 401(k) ដែលអត្ថប្រយោជន៍ស្ទើរជិតពាក់កណ្តាលរបស់បុគ្គលិកនឹងមិនទទួលបានការធានាឡើយនៅឆ្នាំ2075។
  - HYP: ការផ្លាស់ទី គឺស្រដៀងគ្នានឹង ការផ្លាស់ទីវិស័យឯកជនពី ផែនការចូលនិវត្តន៍អត្ថប្រយោជន៍កំណត់ ទៅនឹង ផែនការអត្ថប្រយោជន៍អត្ថប្រយោជន៍អត្ថប្រយោជន៍កំណត់ ដូចជា 401ks ដោយសារតែជិតពាក់កណ្តាលនៃអត្ថប្រយោជន៍របស់កម្មករ នឹងមិនត្រូវបានធានា នៅឆ្នាំ ២០៧៥។

- **chrF++ 26.5** · `repetition_hallucination`
  - EN: In the hills of Weiswampach, Luxembourg yesterday, the 12th International Wämper Triathlon became the setting for the national championship Olympic distance (1,5 km swimming, 40 km cycling, 10 km running) triathlon for both Belgium and Luxembourg.
  - REF: កាលពីម្សិលមិញ នៅលើភ្នំវេសវ៉មផាច លុចសំបួ ពានរង្វាន់វែមព័រទ្រីយ៉ាថ្លុនអន្ដរជាតិលើកទី12បានរកឃើញជើងឯកថ្នាក់ជាតិចម្ងាយអូឡាំពិក (ហែលទឹក 1.5km ជិះកង់ 40km រត់ចម្ងាយ 10 km) ប្រណាំងបីប្រភេទសម្រាប់ទាំងប្រទេសប៊ែលហ្ស៊ិក និងលុចសំបួ។
  - HYP: នៅកំពូលភ្នំនៅវៃស្វាយប៉ាក,ឡុយក្លេអ៊ែរម្សិលមិញ ការប្រកួតប្រជែងប្រជែងប្រជែងប្រដាប់អន្តរជាតិ លើកទី ១២ បានក្លាយជាទីតាំងសម្រាប់ ការប្រកួតប្រជែងប្រដាប់អូឡាំពិក ឆ្ងាយជាតិ (ការហែលទឹក ១,៥ គីឡូម៉ែត្រ, ជិះកង់ ៤០ គីឡូម៉ែត្រ, ការរត់១០ គីឡូម៉ែត្រ) សម្រាប់ទាំងបែលហ្ស៊ិកនិងឡុយក្លេអ


## omission (4 sentences)

- **chrF++ 10.1** · `omission`
  - EN: "There is a growing sense of insecurity among media persons who increasingly interpret each attack on journalists as a warning to ‘behave,’" the HRCP said last Monday.
  - REF: អង្គការអេចអាលស៊ីភីបាននិយាយនៅថ្ងៃច័ន្ទមុននេះថា៖ "មានការកើនឡើងនៃអសុវត្ថិភាពក្នុងចំណោមក្រុមអ្នកផ្សព្វផ្សាយដែលបានចាត់ទុករាល់ការវាយប្រហារទៅលើអ្នកសារព័ត៌មានថាជាការព្រមានទៅលើ‘អាកប្បកិរិយា‘។"
  - HYP: មជ្ឈត្តកម្មមនុស្សធម៌បាននិយាយថា កាលពីថ្ងៃច័ន្ទមុន។

- **chrF++ 26.1** · `omission`
  - EN: His funeral was held at a packed in Cairo today.
  - REF: ពិធីបុណ្យសពរបស់គាត់ត្រូវបានប្រារព្ធឡើងនៅកន្លែងមួយដែលមានការចូលរួមពីមនុស្សយ៉ាងច្រើនកុះករ នៅទីក្រុងខារ៉ូ ក្នុងថ្ងៃនេះ។
  - HYP: សពរបស់គាត់ត្រូវបានធ្វើនៅកន្លែងកកស្ទះនៅកៃរ៉ូថ្ងៃនេះ។

- **chrF++ 18.4** · `omission`
  - EN: "He left us an example of leadership that we should all follow," a cleric told the congregation at the fourth-century cathedral.
  - REF: "គាត់បានបន្សល់ទុកនូវគំរូនៃភាពជាអ្នកដឹកនាំដែលយើងទាំងអស់គួរតែអនុវត្តតាម" បរិស័ទម្នាក់បានប្រាប់ទៅអង្គជំនុំសាសនានៅព្រះវិហារសតវត្សរ៍ទីបួន។
  - HYP: សាស្ត្រាចារ្យ ម្នាក់ បានប្រាប់ ក្រុមជំនុំ នៅព្រះវិហារវេនទី៤។

- **chrF++ 14.5** · `omission`
  - EN: Eleven of those killed were in Paisley and three were in Lady Lake.
  - REF: ក្នុងនោះមនុស្សដប់មួយនាក់ដែលត្រូវបានសម្លាប់នោះគឺនៅក្រុងផាយស្លេ និងបីនាក់ទៀតនៅក្នុងក្រុងឡេឌី ឡេក។
  - HYP: ម្នាក់រយនៃអ្នកស្លាប់នៅប៉ៃលិននិងបីនៅបឹងស្រី។


## number_mismatch (59 sentences)

- **chrF++ 19.9** · `number_mismatch`
  - EN: Initial investigations now suggest the explosion was caused by poor ventilation, which lead to high concentrations of combustible dust.
  - REF: ការស្រាវជ្រាវដំបូងបានសង្ស័យថាការផ្ទុះបានកើតឡើងដោយខ្វះខ្យល់ចេញចូល ដែលនាំអោយប្រមូលផ្តុំនូវសារធាតុដែលងាយឆេះ។
  - HYP: ការស៊ើបអង្កេតទី១ ឥឡូវនេះបង្ហាញថា ការផ្ទុះ ត្រូវបានបណ្តាលឱ្យដោយការខ្យល់ខ្យល់ខ្វះខាត, ដែលបណ្តាលឱ្យមានការយកចិត្តទុកដាក់ខ្ពស់នៃគ្រាប់ធូលីផ្ទុះ។

- **chrF++ 32.4** · `number_mismatch`
  - EN: Research group IHS iSuppli said the explosion may cause loss of production of 500,000 iPads during this quarter of the year.
  - REF: ក្រុមស្រាវជ្រាវអាយអេកអេស អាយសាប់ព្លីបាននិយាយថាការផ្ទុះអាចធ្វើឲ្យខាតបង់ផលិតផលរបស់ អាយផេត 500,000ក្នុងឆមាសនៃឆ្នាំនេះ។
  - HYP: ក្រុមស្រាវជ្រាវ IHS iSuppli បាននិយាយថា ការផ្ទុះ អាចបណ្តាលឱ្យមាន ការបាត់បង់ការផលិតរបស់ iPad ចំនួន ៥០,០០០,០០០ ក្នុងត្រីមាសនេះនៃឆ្នាំ។

- **chrF++ 32.2** · `number_mismatch`
  - EN: According to the United States Geological Survey (USGS), at 3:35 p.m (eastern time) the 5.8 quake struck in Antarctica, 105 kilometers (65 miles) south, southeast of Casey Station or 2565 kilometers (1590 miles) north of the South Pole.
  - REF: យោងតាមពិនិត្យលើស្ថានភាពភូគព្ភសាស្ដ្ររបស់សហរដ្ឋអាមេរិក (USGS) នៅវេលាម៉ោង3:35ល្ងាច (ម៉ោងនៅភាគខាងកើត) ការរញ្ជួយទំហំ5.8 បានកើតឡើងនៅ Antarctica ចំងាយ105គីឡូម៉ែត្រ (65ម៉ែល៍)ខាងត្បូង ភាគអាគ្នេយ៍នៃ ស្ថានីយ Casey ឬ​ 2565គីឡូម៉ែត្រ (1590ម៉ែល៍) ខាងជើងនៃប៉ូលខាងត្បូង។
  - HYP: យោងតាមការស្ទង់មតិភូមិសាស្ត្រសហរដ្ឋអាមេរិក (USGS) នៅម៉ោង៣និង៣៥ថ្ងៃត្រង់ម៉ោងកើតហេតុ រញ្ជួយដី ៥.៨ បានកើតឡើងនៅអង់តារិកា, ១០៥ គីឡូម៉ែត្រ ភាគខាងត្បូង, ភាគខាងត្បូងនៃស្ថានីយ៍កាសី ឬ ២៥៦៥ គីឡូម៉ែត្រ ភាគខាងជើងនៃពូលទីត្បូង។

- **chrF++ 26.0** · `number_mismatch`
  - EN: The quake was reported at a depth of 7.5 k.m. (4.7 miles), but the USGS says it was "poorly constrained."
  - REF: ការរញ្ជួយនេះ ត្រូវបានគេរាយការណ៍ថាមានជំរៅដល់ទៅ 7.5គីឡូម៉ែត្រ (4.7ម៉ែល៍) ប៉ុន្តែ USGSនិយាយថា "វាមានផលប៉ះពាល់តិច។"
  - HYP: ការរញ្ជួយដី ត្រូវបានរាយការណ៍នៅកម្រិតដីកាប្រមាណជា ៧,៥ គីឡូម៉ែត្រ, តែទីភ្នាក់ងារទេសចរណ៍សហរដ្ឋអាមេរិក និយាយថាវាមានកម្រិតខ្វះខាត។

- **chrF++ 34.0** · `number_mismatch`
  - EN: The prices of raw oil approached $100 last week before settling down again.
  - REF: តំលៃនៃប្រេងឆៅជិតទៅដល់100ដុល្លារកាលពីសប្តាហ៍មុន មុនពេលដែលនៅនឹងម្តងទៀត។
  - HYP: តម្លៃប្រេងឥន្ធនៈបានជិត១០០០ដុល្លារសប្តាហ៍មុន មុនពេលកំណត់ខ្លួនម្តងទៀត។


## unseen_source_word (693 sentences)

- **chrF++ 27.1** · `unseen_source_word`
  - EN: It has been confirmed that eight thoroughbred race horses at Randwick Racecourse in Sydney have been infected with equine influenza.
  - REF: គេបានបញ្ចាក់ថាសេះពូជប្រណាំងទាំង៨នៅទីលានប្រណាំងសេះរង់វីក ​ទីក្រុងស៊ីដនីបានឆ្លងរោគផ្ដាសាយធំរបស់សត្វសេះ។
  - HYP: ត្រូវបានបញ្ជាក់ថាសេះប្រណាំងពូជផ្ទៃក្នុងប្រាំបីនៅទីតាំងរណសិរ្សរណបនៅស៊ីដនី ត្រូវបានឆ្លងមេរោគផ្តាសាយស្វា។

- **chrF++ 23.1** · `unseen_source_word`
  - EN: Randwick has been locked down, and is expected to remain so for up to two months.
  - REF: រង់វីកត្រូវបិទ ហើយយ៉ាងហោចណាស់ក៏ត្រូវរក្សារហូត២ខែដែរ។
  - HYP: រ៉ង់ដាវីក ត្រូវបានដាក់សោ, ហើយត្រូវបានរំពឹងថានឹងស្នាក់នៅយ៉ាងនោះ រហូតដល់ពីរខែ។

- **chrF++ 25.5** · `unseen_source_word`
  - EN: It is expected that the virulent flu will affect the majority of the 700 horses stabled at Randwick.
  - REF: គេប៉ាន់ស្មានថានឹងមានឥទិ្ធពលរីករាលដាលភាគច្រើនដល់សេះចំនួន700ក្បាលដែលស្ថិតនៅរង់វីក។
  - HYP: ត្រូវបានរំពឹងថាការផ្តាសាយធំៗ នឹងប៉ះពាល់ភាគច្រើននៃសេះ ៧០០ ដែលស្ថិតនៅរង្វង់មូល។

- **chrF++ 28.8** · `unseen_source_word`
  - EN: NSW Minister for Primary Industries said the facility would be quarantined until 30 days after the last sign of the flu.
  - REF: រដ្ឋមន្ត្រីញូវសោវែលទទួលបន្ទុកស្សាហកម្មចម្បងៗបានមានប្រសាសន៍ថាទីកន្លែងនេះនឹងត្រូវធ្វើចត្តាលីស័ករហូត30ថ្ងៃក្រោយពីសញ្ញាចុងក្រោយនៃជម្ងឺគ្រុនផ្ដាសាយធំ។
  - HYP: រដ្ឋមន្ត្រីក្រសួងឧស្សាហកម្មអប្បបរមានៃខេត្តព្រះសីហនុបាននិយាយថា អចលនទ្រព្យ នឹងស្ថិតនៅក្នុងការសម្របសម្រួល រហូតដល់រយៈពេល ៣០ ថ្ងៃបន្ទាប់ពីការបង្ហាញចុងក្រោយនៃផ្តាសាយធំ។

- **chrF++ 20.7** · `unseen_source_word`
  - EN: The cases are the first infections of race horses, despite infecting dozens of recreational horses across NSW and Queensland.
  - REF: ករណីនេះគឺជាការឆ្លងកាត់លើកទី១សំរាប់សត្វសេះប្រណាំង ទោះបីឆ្លងលើសេះសម្រាប់កំសាន្តរាប់សិបក្បាលនៅអិនអេសដាប់ប័រយូនិងឃ្ខីនសាឡេនក៏ដោយ។
  - HYP: ករណីនេះគឺការឆ្លងមេរោគទីមួយនៃសេះរត់, ទោះបីជាឆ្លងមេរោគ រាប់សិបសេះសំណាញ់នៅទូទាំងខេត្តណេស៊ុយលង់ដានិងគិលានដា។


## lexical_semantic (2 sentences)

- **chrF++ 23.4** · `lexical_semantic`
  - EN: "We have no idea what the result of that would be."
  - REF: "យើងពុំដឹងថានឹងទទួលបានលទ្ធផលយ៉ាងដូចម្តេចឡើយ។"
  - HYP: យើងអត់ដឹងថា លទ្ធផលនៃរឿងនោះនឹងមានអីទេ។"

- **chrF++ 17.3** · `lexical_semantic`
  - EN: The teams now go on to play a one-day series followed by a test match series.
  - REF: បច្ចុប្បន្នក្រុមជាច្រើនបន្តការប្រកួតក្នុងស៊េរីរយៈពេលមួយថ្ងៃក្រោយពីការប្រកួតស៊េរីសាកល្បងមួយ។
  - HYP: ក្រុមការងារឥឡូវបន្តលេងខ្សែក្រវ៉ាត់មួយថ្ងៃបន្ទាប់ពីនោះមានខ្សែក្រវ៉ាត់ប្រឡង។
