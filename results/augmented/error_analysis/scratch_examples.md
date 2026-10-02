# Error analysis: A: Transformer from scratch

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 5.4** · `lexical_semantic`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: ស៊ីរីសម្រាប់គណៈកម្មាធិការសកម្មយឺត។

- **chrF++ 14.9** · `lexical_semantic`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ជំរុញឲ្យម៉ាក់ ដោយ កាដូ។

- **chrF++ 16.2** · `lexical_semantic`
  - EN: What is wrong?
  - REF: មានរឿងអី?
  - HYP: ខុសអី?

- **chrF++ 16.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: សុំហឹរទេ។

- **chrF++ 21.5** · `lexical_semantic`
  - EN: If you go, I will go too.
  - REF: បើឯងទៅ ញុមទៅដែរ។
  - HYP: បើទៅទៅ ញុមនឹងទៅពេក។

- **chrF++ 22.5** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: នោះគឺកចម្បងសម្រាប់ខ្ញុំ។

- **chrF++ 23.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: វា កំពុងតែ ភ្លៀងធ្លាក់។

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 26.2** · `lexical_semantic`
  - EN: Keep watering the flowers.
  - REF: ស្រោចផ្កាទៀតទៅ។
  - HYP: ទឹកទៀតទៅ។

- **chrF++ 28.5** · `lexical_semantic`
  - EN: If it rains, I will stay home.
  - REF: បើភ្លៀង ញុមនៅផ្ទះ។
  - HYP: បើ ភ្លៀងធ្លាក់ ញុមនឹង ស្នាក់នៅ វា។

- **chrF++ 36.6** · `unseen_source_word`
  - EN: The contract is binding upon the successors and assigns of the parties.
  - REF: កិច្ចសន្យានេះមានកាតព្វកិច្ចអនុវត្តចំពោះអ្នកបន្តវេន និងអ្នកទទួលសិទ្ធិរបស់ភាគី។
  - HYP: កិច្ចសន្យា គឺ មានកាតព្វកិច្ច លើ អ្នកបន្តវេន និង ចាត់តាំងភាគី។

- **chrF++ 39.1** · `lexical_semantic`
  - EN: Go straight ahead.
  - REF: ទៅត្រង់ទៅមុខ។
  - HYP: ទៅត្រង់ដល់មុន។

- **chrF++ 43.8** · `partially_correct`
  - EN: It is too cold outside.
  - REF: នៅខាងក្រៅត្រជាក់ណាស់។
  - HYP: នៅខាងក្រៅរងាណាស់។

- **chrF++ 49.3** · `partially_correct`
  - EN: Don't sleep the coupon!
  - REF: កុំ ដេក Coupon!
  - HYP: កុំ Sleep Coupon!

- **chrF++ 50.2** · `partially_correct`
  - EN: I have a stomach ache.
  - REF: ខ្ញុំឈឺពោះ។
  - HYP: ខ្ញុំមានឈឺឈឺពោះ។


## spacing_only (1 sentences)

- **chrF++ 79.2** · `spacing_only`
  - EN: The none is red.
  - REF: គ្មាន គឺ ពណ៌ក្រហម។
  - HYP: គ្មាន គឺពណ៌ ក្រហម។


## repetition_hallucination (1 sentences)

- **chrF++ 23.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: វា កំពុងតែ ភ្លៀងធ្លាក់។


## unseen_source_word (2 sentences)

- **chrF++ 22.5** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: នោះគឺកចម្បងសម្រាប់ខ្ញុំ។

- **chrF++ 36.6** · `unseen_source_word`
  - EN: The contract is binding upon the successors and assigns of the parties.
  - REF: កិច្ចសន្យានេះមានកាតព្វកិច្ចអនុវត្តចំពោះអ្នកបន្តវេន និងអ្នកទទួលសិទ្ធិរបស់ភាគី។
  - HYP: កិច្ចសន្យា គឺ មានកាតព្វកិច្ច លើ អ្នកបន្តវេន និង ចាត់តាំងភាគី។


## lexical_semantic (9 sentences)

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 16.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: សុំហឹរទេ។

- **chrF++ 21.5** · `lexical_semantic`
  - EN: If you go, I will go too.
  - REF: បើឯងទៅ ញុមទៅដែរ។
  - HYP: បើទៅទៅ ញុមនឹងទៅពេក។

- **chrF++ 14.9** · `lexical_semantic`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ជំរុញឲ្យម៉ាក់ ដោយ កាដូ។

- **chrF++ 26.2** · `lexical_semantic`
  - EN: Keep watering the flowers.
  - REF: ស្រោចផ្កាទៀតទៅ។
  - HYP: ទឹកទៀតទៅ។
