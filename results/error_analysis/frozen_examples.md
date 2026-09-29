# Error analysis: B: NLLB frozen backbone

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 7.7** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: អធ្យាស្រ័យចំពោះការមិនសកម្មថ្មីៗនេះ។

- **chrF++ 11.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហិរផង។

- **chrF++ 15.2** · `lexical_semantic`
  - EN: Don't be fine.
  - REF: កុំសុខសប្បាយអី។
  - HYP: កុំមានសុខភាពល្អទេ។

- **chrF++ 15.3** · `lexical_semantic`
  - EN: I lost my menu.
  - REF: ខ្ញុំបានបាត់ មីនុយ របស់ខ្ញុំ។
  - HYP: ញុមបាត់ម៉ឺនុយ។

- **chrF++ 18.5** · `lexical_semantic`
  - EN: What is wrong?
  - REF: មានរឿងអី?
  - HYP: តើមានអ្វីខុស?

- **chrF++ 24.0** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ញុមភ្ញាក់ផ្អើលម៉ាក់ជាមួយកាដូ។

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 28.1** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: សម្រាប់ញុមវាធំណាស់។

- **chrF++ 29.1** · `lexical_semantic`
  - EN: My mom is younger than me.
  - REF: ម៉ាក់ប្អូនញុម។
  - HYP: ម៉ាក់ញុមញុម។

- **chrF++ 32.6** · `lexical_semantic`
  - EN: Keep relaxing.
  - REF: សម្រាកទៀតទៅ។
  - HYP: ធូរអារម្មណ៍ទៀតទៅ។

- **chrF++ 33.3** · `lexical_semantic`
  - EN: My dad is scared.
  - REF: ប៉ាកំពុងខ្លាច។
  - HYP: ប៉ាញុមខ្លាច។

- **chrF++ 35.7** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានវ៉ាលីអត់?

- **chrF++ 35.7** · `lexical_semantic`
  - EN: Come back to change the bandage next week.
  - REF: ត្រឡប់មកផ្លាស់ប្តូរត្រនាប់របួសវិញនៅសប្តាហ៍ក្រោយ។
  - HYP: ត្រឡប់មកដូរវ៉ាក់សាំងវិញសប្តាហ៍ក្រោយ។

- **chrF++ 38.8** · `lexical_semantic`
  - EN: It is too stormy outside.
  - REF: នៅខាងក្រៅមានព្យុះណាស់។
  - HYP: នៅខាងក្រៅគឺព្យុះពេកហើយ។


## spacing_only (3 sentences)

- **chrF++ 88.7** · `spacing_only`
  - EN: The none is red.
  - REF: គ្មាន គឺ ពណ៌ក្រហម។
  - HYP: គ្មាន គឺ ពណ៌ ក្រហម។

- **chrF++ 79.2** · `spacing_only`
  - EN: The winner is red.
  - REF: អ្នកឈ្នះ គឺ ពណ៌ក្រហម។
  - HYP: អ្នកឈ្នះ គឺពណ៌ ក្រហម។

- **chrF++ 79.2** · `spacing_only`
  - EN: The documentary is brown.
  - REF: ភាពយន្តឯកសារ គឺ ពណ៌ត្នោត។
  - HYP: ភាពយន្តឯកសារ គឺពណ៌ ត្នោត។


## repetition_hallucination (1 sentences)

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។


## unseen_source_word (3 sentences)

- **chrF++ 28.1** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: សម្រាប់ញុមវាធំណាស់។

- **chrF++ 24.0** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ញុមភ្ញាក់ផ្អើលម៉ាក់ជាមួយកាដូ។

- **chrF++ 7.7** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: អធ្យាស្រ័យចំពោះការមិនសកម្មថ្មីៗនេះ។


## lexical_semantic (12 sentences)

- **chrF++ 32.6** · `lexical_semantic`
  - EN: Keep relaxing.
  - REF: សម្រាកទៀតទៅ។
  - HYP: ធូរអារម្មណ៍ទៀតទៅ។

- **chrF++ 35.7** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានវ៉ាលីអត់?

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 11.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហិរផង។

- **chrF++ 38.8** · `lexical_semantic`
  - EN: It is too stormy outside.
  - REF: នៅខាងក្រៅមានព្យុះណាស់។
  - HYP: នៅខាងក្រៅគឺព្យុះពេកហើយ។
