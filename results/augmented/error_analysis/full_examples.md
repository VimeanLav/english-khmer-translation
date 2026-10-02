# Error analysis: C: NLLB full fine-tuning

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 5.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហឹរផង។

- **chrF++ 8.0** · `lexical_semantic`
  - EN: The show is free.
  - REF: Show គឺ ទំនេរ។
  - HYP: កម្មវិធី គឺ ឥតគិតថ្លៃ។

- **chrF++ 8.8** · `repetition_hallucination`
  - EN: Study coding hard.
  - REF: ខំរៀនសរសេរកូដ។
  - HYP: រៀន Coding ដោយឧស្សាហ៍ព្យាយាម។

- **chrF++ 9.0** · `lexical_semantic`
  - EN: My dad is scared.
  - REF: ប៉ាកំពុងខ្លាច។
  - HYP: ប៉ាញុមភ័យ។

- **chrF++ 11.9** · `lexical_semantic`
  - EN: Make sure to bring fork.
  - REF: កុំភ្លេចយកសមមកផង។
  - HYP: ត្រូវប្រាកដថានាំសមមកជាមួយ។

- **chrF++ 12.4** · `lexical_semantic`
  - EN: I spilled my latte.
  - REF: ញុមកំពប់ឡាតេ។
  - HYP: ញុមលាបឡាទីហើយ។

- **chrF++ 12.7** · `repetition_hallucination`
  - EN: This broccoli variety is resistant to whiteflies.
  - REF: ពូជផ្កាខាត់ណាខៀវនេះធន់នឹងរុយស។
  - HYP: ពូជផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខាត់ផ្កាខ

- **chrF++ 13.1** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានកាបូបអត់?

- **chrF++ 14.1** · `lexical_semantic`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សុំទោសចំពោះការ មិនសកម្ម ថ្មីៗនេះ។

- **chrF++ 15.2** · `lexical_semantic`
  - EN: Pass me the speaker.
  - REF: ហុចធុងបាសឲ្យញុម។
  - HYP: ហុច Speaker មកញុម។

- **chrF++ 15.4** · `lexical_semantic`
  - EN: Make sure to bring mouse.
  - REF: កុំភ្លេចយកម៉ៅមកផង។
  - HYP: ត្រូវប្រាកដថានាំម៉ៅមក។

- **chrF++ 15.6** · `lexical_semantic`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ធ្វើអោយម៉ាក់ភ្ញាក់ផ្អើលជាមួយអំណោយ។

- **chrF++ 17.3** · `repetition_hallucination`
  - EN: Do you want ice with your beer?
  - REF: យកទឹកកកដាក់បៀរអត់?
  - HYP: ចង់បាន ការ៉េម ជាមួយ ស្រាបៀរ របស់ឯង អត់?

- **chrF++ 17.9** · `lexical_semantic`
  - EN: How does chicken soup taste?
  - REF: ស៊ុបមាន់រសជាតិម៉េចដែរ?
  - HYP: ស៊ុតមាន់ឆ្ងាញ់អត់?

- **chrF++ 18.5** · `lexical_semantic`
  - EN: Do you want ice with your whiskey?
  - REF: យកទឹកកកដាក់វិស្គីអត់?
  - HYP: ចង់បាន ការ៉េម ជាមួយ វីស្គី របស់ឯង អត់?


## spacing_only (19 sentences)

- **chrF++ 86.2** · `spacing_only`
  - EN: This shoes is so special.
  - REF: ស្បែកជើង នេះគឺ ពិសេស ខ្លាំងណាស់។
  - HYP: ស្បែកជើងនេះគឺ ពិសេស ខ្លាំងណាស់។

- **chrF++ 85.7** · `spacing_only`
  - EN: I bought gel from the hospital.
  - REF: ខ្ញុំបានទិញជែលពីមន្ទីរពេទ្យ។
  - HYP: ខ្ញុំបានទិញ ជែល ពី មន្ទីរពេទ្យ។

- **chrF++ 88.7** · `spacing_only`
  - EN: Please ensure to take this ear drops for 5 days.
  - REF: សូមធានាថាលេបថ្នាំបន្តក់ត្រចៀកនេះរយៈពេល ៥ ថ្ងៃ។
  - HYP: សូមធានាថាលេបថ្នាំបន្តក់ត្រចៀកនេះ រយៈពេល ៥ ថ្ងៃ។

- **chrF++ 90.7** · `spacing_only`
  - EN: The admin will stay the mask often.
  - REF: Admin នឹង ស្នាក់នៅ ម៉ាស់ ញឹកញាប់។
  - HYP: Admin នឹង ស្នាក់ នៅ ម៉ាស់ ញឹកញាប់។

- **chrF++ 87.9** · `spacing_only`
  - EN: Don't reply the battery!
  - REF: កុំ ឆ្លើយតប ថ្ម!
  - HYP: កុំ ឆ្លើយ តប ថ្ម!


## repetition_hallucination (7 sentences)

- **chrF++ 21.1** · `repetition_hallucination`
  - EN: More spring rolls please.
  - REF: សុំណែមទៀត។
  - HYP: សុំក្រដាសជូតទឹកទៀត។

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 8.8** · `repetition_hallucination`
  - EN: Study coding hard.
  - REF: ខំរៀនសរសេរកូដ។
  - HYP: រៀន Coding ដោយឧស្សាហ៍ព្យាយាម។

- **chrF++ 37.0** · `repetition_hallucination`
  - EN: I am allergic to fish soup.
  - REF: ញុមចាញ់ស៊ុបត្រី។
  - HYP: ខ្ញុំមានប្រតិកម្មជាមួយស៊ុបត្រី។

- **chrF++ 27.5** · `repetition_hallucination`
  - EN: My grandma is sick.
  - REF: យាយឈឺ។
  - HYP: យាយកំពុងឈឺ។


## unseen_source_word (1 sentences)

- **chrF++ 28.3** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: នោះជាអាពាហ៍ពិពាហ៍ធំសម្រាប់ញុម។


## lexical_semantic (61 sentences)

- **chrF++ 34.5** · `lexical_semantic`
  - EN: I have been suffering from mumps every day.
  - REF: ខ្ញុំបានរងទុក្ខពីស្រឡទែន រាល់ថ្ងៃ។
  - HYP: ញុមរងទុក្ខពីកញ្រ្ជិល រៀងរាល់ថ្ងៃ។

- **chrF++ 32.8** · `lexical_semantic`
  - EN: Keep relaxing.
  - REF: សម្រាកទៀតទៅ។
  - HYP: បន្តសម្រាក។

- **chrF++ 34.4** · `lexical_semantic`
  - EN: The farm is crowded.
  - REF: កសិដ្ឋានមនុស្សច្រើនណាស់។
  - HYP: កសិដ្ឋានកកស្ទះណាស់។

- **chrF++ 24.2** · `lexical_semantic`
  - EN: The sushi is gross.
  - REF: ស៊ូស៊ី គឺ អាក្រក់មើល។
  - HYP: ស៊ូស៊ី ស្អប់ខ្ពើម។

- **chrF++ 13.1** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានកាបូបអត់?
