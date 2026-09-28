# Error analysis: A: Transformer from scratch

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 2.8** · `repetition_hallucination`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ការចេញ្ញ្ញ្ញ្ញ្ញ្ត្ញ្ញ។

- **chrF++ 4.3** · `omission`
  - EN: Physics is difficult.
  - REF: រូបវិទ្យាពិបាក។
  - HYP: សិល្បៈ។

- **chrF++ 5.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: ត្រៀមខ្លួនសម្រាប់បអិតិតិតិតិត។

- **chrF++ 5.3** · `lexical_semantic`
  - EN: If you go, I will go too.
  - REF: បើឯងទៅ ញុមទៅដែរ។
  - HYP: ប្រសិនបើអ្នកមានហើយពេក។

- **chrF++ 7.8** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: ផូល់ខ្រេញុមកណី។

- **chrF++ 9.2** · `lexical_semantic`
  - EN: What is wrong?
  - REF: មានរឿងអី?
  - HYP: ខុសអត់?

- **chrF++ 14.3** · `lexical_semantic`
  - EN: I eat pizza now.
  - REF: ញុមញ៉ាំភីហ្សាឥឡូវ។
  - HYP: Pizzaឥឡូវ។

- **chrF++ 14.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: អត់មាន ហឹរទៀត។

- **chrF++ 16.2** · `omission`
  - EN: I drink coconut water.
  - REF: ញុមផឹកទឹកដូង។
  - HYP: ដូង។។

- **chrF++ 17.9** · `lexical_semantic`
  - EN: The dermatology clinic is open on weekends.
  - REF: គ្លីនិកសើស្បែកបើកនៅចុងសប្តាហ៍។
  - HYP: គ្លីនិកកុមារបណេត

- **chrF++ 18.3** · `lexical_semantic`
  - EN: I want to buy book for Samnang.
  - REF: ញុមចង់ទិញសៀវភៅឲ្យសំណាង។
  - HYP: ញុមចេញ ញុមគិតថាសំណាង

- **chrF++ 19.7** · `lexical_semantic`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: នៅហើយ។

- **chrF++ 21.0** · `omission`
  - EN: Please tell Narith to go to the hall.
  - REF: ប្រាប់ណារិទ្ធឲ្យទៅសាលផង។
  - HYP: បីៅសាលផង។

- **chrF++ 21.6** · `lexical_semantic`
  - EN: I want to buy glass for Sreyka.
  - REF: ញុមចង់ទិញកែវឲ្យស្រីកា។
  - HYP: កុំភ្លេចលេបថ្នាំស្រីកា។

- **chrF++ 21.6** · `lexical_semantic`
  - EN: I want to buy cup for Vuthy.
  - REF: ញុមចង់ទិញកែវឲ្យវុទ្ធី។
  - HYP: កុំភ្លេចលេបថ្នាំវុទ្ធី។


## spacing_only (3 sentences)

- **chrF++ 85.7** · `spacing_only`
  - EN: I trust my roommate.
  - REF: ញុមទុកចិត្តមិត្តរួមបន្ទប់។
  - HYP: ញុមទុកចិត្ត មិត្តរួមបន្ទប់។

- **chrF++ 85.7** · `spacing_only`
  - EN: I am going with my roommate.
  - REF: ញុមទៅជាមួយមិត្តរួមបន្ទប់។
  - HYP: ញុមទៅជាមួយ មិត្តរួមបន្ទប់។

- **chrF++ 79.2** · `spacing_only`
  - EN: The documentary is brown.
  - REF: ភាពយន្តឯកសារ គឺ ពណ៌ត្នោត។
  - HYP: ភាពយន្តឯកសារ គឺពណ៌ ត្នោត។


## repetition_hallucination (1 sentences)

- **chrF++ 2.8** · `repetition_hallucination`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ការចេញ្ញ្ញ្ញ្ញ្ញ្ត្ញ្ញ។


## omission (5 sentences)

- **chrF++ 16.2** · `omission`
  - EN: I drink coconut water.
  - REF: ញុមផឹកទឹកដូង។
  - HYP: ដូង។។

- **chrF++ 21.0** · `omission`
  - EN: Please tell Narith to go to the hall.
  - REF: ប្រាប់ណារិទ្ធឲ្យទៅសាលផង។
  - HYP: បីៅសាលផង។

- **chrF++ 4.3** · `omission`
  - EN: Physics is difficult.
  - REF: រូបវិទ្យាពិបាក។
  - HYP: សិល្បៈ។

- **chrF++ 23.6** · `omission`
  - EN: Why is Sokunthea angry?
  - REF: ម៉េចបានសុគន្ធាខឹង?
  - HYP: ាខឹង?

- **chrF++ 25.1** · `omission`
  - EN: Please tell Samnang to go to the hospital.
  - REF: ប្រាប់សំណាងឲ្យទៅពេទ្យផង។
  - HYP: បិញពេទ្យផង។


## unseen_source_word (5 sentences)

- **chrF++ 7.8** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: ផូល់ខ្រេញុមកណី។

- **chrF++ 24.6** · `unseen_source_word`
  - EN: The contract is binding upon the successors and assigns of the parties.
  - REF: កិច្ចសន្យានេះមានកាតព្វកិច្ចអនុវត្តចំពោះអ្នកបន្តវេន និងអ្នកទទួលសិទ្ធិរបស់ភាគី។
  - HYP: កិច្ចសន្យា គឺ មានកាតព្វកិច្ច ចាត់តាំងិច្ចព្រមព្រៀងនេះ។

- **chrF++ 37.9** · `unseen_source_word`
  - EN: Go straight ahead.
  - REF: ទៅត្រង់ទៅមុខ។
  - HYP: ទៅត្រង់ដល់។

- **chrF++ 28.5** · `unseen_source_word`
  - EN: If it rains, I will stay home.
  - REF: បើភ្លៀង ញុមនៅផ្ទះ។
  - HYP: បើភ្លៀងធ្លាក់ ឆ្ងាញ់ ញុមនឹង នៅ វា។

- **chrF++ 5.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: ត្រៀមខ្លួនសម្រាប់បអិតិតិតិតិត។


## lexical_semantic (33 sentences)

- **chrF++ 18.3** · `lexical_semantic`
  - EN: I want to buy book for Samnang.
  - REF: ញុមចង់ទិញសៀវភៅឲ្យសំណាង។
  - HYP: ញុមចេញ ញុមគិតថាសំណាង

- **chrF++ 35.3** · `lexical_semantic`
  - EN: This cable is for Ry.
  - REF: ខ្សែភ្លើងនេះសម្រាប់រី។
  - HYP: ខ្សែភ្លើងឲ្យរី។

- **chrF++ 27.2** · `lexical_semantic`
  - EN: Is it rainy now?
  - REF: ឥឡូវភ្លៀងអត់?
  - HYP: ឥឡូវមានពកអត់?

- **chrF++ 39.2** · `lexical_semantic`
  - EN: I love my friend.
  - REF: ញុមស្រលាញ់មិត្តភក្តិ។
  - HYP: ញុមស្រលាញ់ក្នុង។

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?
