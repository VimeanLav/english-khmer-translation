# Error analysis: B: NLLB frozen backbone

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 2.1** · `repetition_hallucination`
  - EN: Rambutan requires black soil to grow well.
  - REF: សាវម៉ាវត្រូវការដីខ្មៅដើម្បីលូតលាស់បានល្អ។
  - HYP: មន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរម

- **chrF++ 5.2** · `lexical_semantic`
  - EN: Pass me the speaker.
  - REF: ហុចធុងបាសឲ្យញុម។
  - HYP: ផ្ទេរ Speaker មកខ្ញុំ។

- **chrF++ 5.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហឹរផង។

- **chrF++ 6.5** · `lexical_semantic`
  - EN: I broke the router.
  - REF: ញុមធ្វើឲ្យបែករ៉ោតទ័រ។
  - HYP: ញុមបំផ្លាញ Router។

- **chrF++ 9.8** · `lexical_semantic`
  - EN: Don't be fine.
  - REF: កុំសុខសប្បាយអី។
  - HYP: កុំ មានរឿងល្អទេ។

- **chrF++ 11.8** · `repetition_hallucination`
  - EN: In Siem Reap produces the best broccoli in the country.
  - REF: នៅសៀមរាបផលិតផ្កាខាត់ណាខៀវល្អបំផុតនៅក្នុងប្រទេស។
  - HYP: នៅសៀមរាបផលិតខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខាត់ខ

- **chrF++ 12.9** · `lexical_semantic`
  - EN: What is wrong?
  - REF: មានរឿងអី?
  - HYP: ម៉េចបានលំបាក?

- **chrF++ 12.9** · `repetition_hallucination`
  - EN: Do you want ice with your beer?
  - REF: យកទឹកកកដាក់បៀរអត់?
  - HYP: ចង់បាន ការ៉េម ជាមួយ ស្រាបៀរ របស់ឯង ទេ?

- **chrF++ 13.9** · `unseen_source_word`
  - EN: Go straight ahead.
  - REF: ទៅត្រង់ទៅមុខ។
  - HYP: ទៅទៀងទាត់ទៅ។

- **chrF++ 14.0** · `lexical_semantic`
  - EN: My boss buys pancakes.
  - REF: មេទិញនំផេនខេក។
  - HYP: ចៅហ្វាយទិញនគុក។

- **chrF++ 14.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សុំទោសចំពោះការ មិនសកម្ម ថ្មីៗនេះ។

- **chrF++ 14.1** · `repetition_hallucination`
  - EN: I will take two laptops.
  - REF: ញុមយកឡេបថបពីរ។
  - HYP: ខ្ញុំនឹង យក កុំព្យូទ័រយួរដៃ ពីរ។

- **chrF++ 14.5** · `lexical_semantic`
  - EN: My teacher is lazy.
  - REF: គ្រូកំពុងខ្ជិល។
  - HYP: គ្រូគឺកន្សែង។

- **chrF++ 14.5** · `lexical_semantic`
  - EN: Is the hall near?
  - REF: សាលជិតអត់?
  - HYP: តើ រោងចក្រ ជិត ទេ?

- **chrF++ 14.7** · `lexical_semantic`
  - EN: The river is crowded.
  - REF: ទន្លេមនុស្សច្រើនណាស់។
  - HYP: ទន្លេ គឺ កកស្ទះ។


## spacing_only (34 sentences)

- **chrF++ 85.7** · `spacing_only`
  - EN: Eat the fork.
  - REF: ញ៉ាំ សម។
  - HYP: ញ៉ាំសម។

- **chrF++ 85.7** · `spacing_only`
  - EN: Take this gel as needed.
  - REF: លេបជែលនេះ តាមការចាំបាច់។
  - HYP: លេបជែលនេះតាមការចាំបាច់។

- **chrF++ 85.7** · `spacing_only`
  - EN: I went to the museum to see Ry.
  - REF: ញុមទៅសារមន្ទីរដើម្បីជួបរី។
  - HYP: ញុមទៅ សារមន្ទីរដើម្បីជួបរី។

- **chrF++ 86.2** · `spacing_only`
  - EN: This shoes is so special.
  - REF: ស្បែកជើង នេះគឺ ពិសេស ខ្លាំងណាស់។
  - HYP: ស្បែកជើងនេះគឺ ពិសេស ខ្លាំងណាស់។

- **chrF++ 85.7** · `spacing_only`
  - EN: I bought gel from the hospital.
  - REF: ខ្ញុំបានទិញជែលពីមន្ទីរពេទ្យ។
  - HYP: ខ្ញុំបានទិញ ជែល ពី មន្ទីរពេទ្យ។


## wrong_script (1 sentences)

- **chrF++ 17.8** · `wrong_script`
  - EN: Keyboard is more expensive than keyboard.
  - REF: ក្ដារចុចថ្លៃជាងក្ដារចុច។
  - HYP: Keyboard គឺ ថ្លៃ ជាង Keyboard។


## repetition_hallucination (23 sentences)

- **chrF++ 32.6** · `repetition_hallucination`
  - EN: If typhoon comes, protect rambutan with water pump.
  - REF: ប្រសិនបើព្យុះទីហ្វុងមកដល់ ការពារសាវម៉ាវជាមួយម៉ាស៊ីនបូមទឹក។
  - HYP: ប្រសិនបើព្យុះទីហ្វុងមកដល់ ការពារមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរមន្ទីរម

- **chrF++ 14.1** · `repetition_hallucination`
  - EN: I will take two laptops.
  - REF: ញុមយកឡេបថបពីរ។
  - HYP: ខ្ញុំនឹង យក កុំព្យូទ័រយួរដៃ ពីរ។

- **chrF++ 29.2** · `repetition_hallucination`
  - EN: Experts predict that tangerine prices will be scarce next year.
  - REF: អ្នកជំនាញព្យាករណ៍ថាតម្លៃក្រូចឃ្វិចនឹងខ្វះខាតនៅឆ្នាំក្រោយ។
  - HYP: អ្នកជំនាញព្យាករណ៍ថាតម្លៃក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្រូចក្របីនឹងខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះខ្វះ

- **chrF++ 36.1** · `repetition_hallucination`
  - EN: I like teal earphones.
  - REF: ញុមចូលចិត្តកាសពណ៌ស្លាបកំភេម។
  - HYP: ញុមចូលចិត្តកាសពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបកំភេពណ៌ស្លាបក

- **chrF++ 37.0** · `repetition_hallucination`
  - EN: I am allergic to fish soup.
  - REF: ញុមចាញ់ស៊ុបត្រី។
  - HYP: ខ្ញុំមានប្រតិកម្មជាមួយស៊ុបត្រី។


## omission (1 sentences)

- **chrF++ 22.1** · `omission`
  - EN: I am tired of gaming.
  - REF: ញុមហត់នឹងលេងហ្គេមណាស់។
  - HYP: ញុមហត់លេង។


## unseen_source_word (4 sentences)

- **chrF++ 18.4** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: សម្រាប់ខ្ញុំនោះគឺ ការខកខាន ដ៏ ធំ។

- **chrF++ 21.6** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ធ្វើការភ្ញាក់ផ្អើលម៉ាក់ជាមួយកាដូ។

- **chrF++ 13.9** · `unseen_source_word`
  - EN: Go straight ahead.
  - REF: ទៅត្រង់ទៅមុខ។
  - HYP: ទៅទៀងទាត់ទៅ។

- **chrF++ 14.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សុំទោសចំពោះការ មិនសកម្ម ថ្មីៗនេះ។


## lexical_semantic (137 sentences)

- **chrF++ 37.9** · `lexical_semantic`
  - EN: I have been suffering from mumps every day.
  - REF: ខ្ញុំបានរងទុក្ខពីស្រឡទែន រាល់ថ្ងៃ។
  - HYP: ខ្ញុំកំពុងរងទុក្ខពីអំបិល រៀងរាល់ថ្ងៃ។

- **chrF++ 32.8** · `lexical_semantic`
  - EN: Keep relaxing.
  - REF: សម្រាកទៀតទៅ។
  - HYP: សម្រាកបន្ត។

- **chrF++ 34.4** · `lexical_semantic`
  - EN: The farm is crowded.
  - REF: កសិដ្ឋានមនុស្សច្រើនណាស់។
  - HYP: កសិដ្ឋានកកស្ទះណាស់។

- **chrF++ 35.1** · `lexical_semantic`
  - EN: My boss likes pancakes.
  - REF: មេចូលចិត្តនំផេនខេក។
  - HYP: ចៅហ្វាយចូលចិត្តនគឹក។

- **chrF++ 22.8** · `lexical_semantic`
  - EN: More spring rolls please.
  - REF: សុំណែមទៀត។
  - HYP: សុំដុំពេជ្រទៀត។
