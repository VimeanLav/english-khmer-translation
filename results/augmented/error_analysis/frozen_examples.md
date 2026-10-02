# Error analysis: B: NLLB frozen backbone

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 5.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហឹរផង។

- **chrF++ 10.0** · `lexical_semantic`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សូមអភ័យទោសចំពោះភាពមិនសកម្ម ថ្មីៗនេះ។

- **chrF++ 15.2** · `lexical_semantic`
  - EN: The bot loses the time.
  - REF: Bot បាត់ ម៉ោង។
  - HYP: Bot ខាតពេលវេលា។

- **chrF++ 20.8** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: សម្រាប់ខ្ញុំវាជារឿងធំមួយ។

- **chrF++ 20.8** · `lexical_semantic`
  - EN: I spilled my latte.
  - REF: ញុមកំពប់ឡាតេ។
  - HYP: ញុមលាបឡាតេហើយ។

- **chrF++ 22.4** · `lexical_semantic`
  - EN: I passed the problem.
  - REF: ញុមជាប់បញ្ហាហ្នឹង។
  - HYP: ញុមឈ្នះបញ្ហា។

- **chrF++ 23.2** · `lexical_semantic`
  - EN: School is crowded.
  - REF: សាលាមនុស្សច្រើនណាស់។
  - HYP: សាលារៀនកកស្ទះណាស់។

- **chrF++ 24.0** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មារឬក្រូចឆ្មារ?

- **chrF++ 24.0** · `lexical_semantic`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ញុមភ្ញាក់ផ្អើលម៉ាក់ជាមួយកាដូ។

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 25.2** · `lexical_semantic`
  - EN: The river is crowded.
  - REF: ទន្លេមនុស្សច្រើនណាស់។
  - HYP: ទន្លេកកស្ទះណាស់។

- **chrF++ 25.3** · `lexical_semantic`
  - EN: The gas station is closed today.
  - REF: ថ្ងៃនេះកន្លែងចាក់សាំងបិទ។
  - HYP: ថ្ងៃនេះស្ថានីយប្រេងឥន្ធនៈបិទ។

- **chrF++ 26.8** · `lexical_semantic`
  - EN: This bread looks delicious.
  - REF: នំប៉័ងហ្នឹងទំនងឆ្ងាញ់។
  - HYP: នំបុ័ងនេះមើលទៅឆ្ងាញ់។

- **chrF++ 27.5** · `lexical_semantic`
  - EN: There is the router.
  - REF: រ៉ោតទ័រនៅនោះ។
  - HYP: Routerនៅនោះ។

- **chrF++ 27.5** · `repetition_hallucination`
  - EN: My grandma is sick.
  - REF: យាយឈឺ។
  - HYP: យាយកំពុងឈឺ។


## spacing_only (4 sentences)

- **chrF++ 85.7** · `spacing_only`
  - EN: He has been feeling sneezing since last night.
  - REF: គាត់មានអារម្មណ៍កណ្តាស់ តាំងពីយប់មិញ។
  - HYP: គាត់មានអារម្មណ៍កណ្តាស់តាំងពីយប់មិញ។

- **chrF++ 88.7** · `spacing_only`
  - EN: The none is red.
  - REF: គ្មាន គឺ ពណ៌ក្រហម។
  - HYP: គ្មាន គឺ ពណ៌ ក្រហម។

- **chrF++ 88.7** · `spacing_only`
  - EN: The winner is red.
  - REF: អ្នកឈ្នះ គឺ ពណ៌ក្រហម។
  - HYP: អ្នកឈ្នះ គឺ ពណ៌ ក្រហម។

- **chrF++ 88.7** · `spacing_only`
  - EN: The documentary is brown.
  - REF: ភាពយន្តឯកសារ គឺ ពណ៌ត្នោត។
  - HYP: ភាពយន្តឯកសារ គឺ ពណ៌ ត្នោត។


## repetition_hallucination (2 sentences)

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 27.5** · `repetition_hallucination`
  - EN: My grandma is sick.
  - REF: យាយឈឺ។
  - HYP: យាយកំពុងឈឺ។


## unseen_source_word (1 sentences)

- **chrF++ 20.8** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: សម្រាប់ខ្ញុំវាជារឿងធំមួយ។


## lexical_semantic (33 sentences)

- **chrF++ 37.1** · `lexical_semantic`
  - EN: Keep relaxing.
  - REF: សម្រាកទៀតទៅ។
  - HYP: ធូរស្រាលទៀតទៅ។

- **chrF++ 34.4** · `lexical_semantic`
  - EN: The farm is crowded.
  - REF: កសិដ្ឋានមនុស្សច្រើនណាស់។
  - HYP: កសិដ្ឋានកកស្ទះណាស់។

- **chrF++ 35.7** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានវ៉ាលីអត់?

- **chrF++ 36.6** · `lexical_semantic`
  - EN: The factory is near.
  - REF: រោងចក្រជិតហ្នឹង។
  - HYP: រោងចក្រនៅជិត។

- **chrF++ 24.0** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មារឬក្រូចឆ្មារ?
