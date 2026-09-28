# Error analysis: C: NLLB full fine-tuning

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 5.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហឹរផង។

- **chrF++ 13.1** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានកាបូបអត់?

- **chrF++ 13.9** · `lexical_semantic`
  - EN: I need to finish moving furniture.
  - REF: ញុមត្រូវធ្វើរើអីវ៉ាន់ឲ្យហើយ។
  - HYP: ខ្ញុំត្រូវបញ្ចប់ រើ គ្រឿងអលង្ការ។

- **chrF++ 14.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សុំទោសចំពោះការ មិនសកម្ម ថ្មីៗនេះ។

- **chrF++ 19.8** · `lexical_semantic`
  - EN: I am shocked now.
  - REF: ឥឡូវញុមតក់ស្លុត។
  - HYP: ញុមភ្ញាក់ផ្អើលឥឡូវ។

- **chrF++ 20.1** · `lexical_semantic`
  - EN: Stop studying and come here.
  - REF: ឈប់រៀនសិន មកនេះ។
  - HYP: ឈប់សិក្សាទៅនេះ។

- **chrF++ 20.4** · `lexical_semantic`
  - EN: The alpha is relaxed.
  - REF: Alpha គឺ ធូរស្រាល។
  - HYP: Alpha កំពុងស្ងប់ស្ងាត់។

- **chrF++ 21.2** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ធ្វើឱ្យម៉ាក់ភ្ញាក់ផ្អើលជាមួយកាដូ។

- **chrF++ 24.0** · `lexical_semantic`
  - EN: I do camping now.
  - REF: ញុមបោះតង់ឥឡូវ។
  - HYP: ញុមជំរប់កម្សាន្តឥឡូវ។

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 24.5** · `lexical_semantic`
  - EN: I broke the brush.
  - REF: ញុមធ្វើឲ្យបែកច្រាស។
  - HYP: ញុមបំផ្លាញច្រាស។

- **chrF++ 25.0** · `lexical_semantic`
  - EN: My uncle is relaxed.
  - REF: ពូកំពុងធូរអារម្មណ៍។
  - HYP: ពូកំពុងស្ងប់ស្ងាត់។

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 25.1** · `lexical_semantic`
  - EN: The gas station is closed today.
  - REF: ថ្ងៃនេះកន្លែងចាក់សាំងបិទ។
  - HYP: ថ្ងៃនេះស្ថានីយ៍ប្រេងឥន្ធនៈបិទ។

- **chrF++ 25.4** · `lexical_semantic`
  - EN: Stop camping and come here.
  - REF: ឈប់បោះតង់សិន មកនេះ។
  - HYP: ឈប់ជំរប់ហើយមកនេះ។


## spacing_only (10 sentences)

- **chrF++ 85.7** · `spacing_only`
  - EN: I bought gel from the hospital.
  - REF: ខ្ញុំបានទិញជែលពីមន្ទីរពេទ្យ។
  - HYP: ខ្ញុំបានទិញ ជែល ពី មន្ទីរពេទ្យ។

- **chrF++ 79.6** · `spacing_only`
  - EN: This equipment is subject to the jurisdiction of the committee.
  - REF: ឧបករណ៍ នេះស្ថិតនៅក្រោមដែនសមត្ថកិច្ចរបស់ គណៈកម្មាធិការ។
  - HYP: ឧបករណ៍នេះស្ថិតនៅក្រោមដែនសមត្ថកិច្ចរបស់ គណៈកម្មាធិការ។

- **chrF++ 90.7** · `spacing_only`
  - EN: Why is the truth so white?
  - REF: ហេតុអីបានជា ការពិត ពណ៌ស ម៉េស?
  - HYP: ហេតុអីបានជា ការពិត ពណ៌ ស ម៉េស?

- **chrF++ 86.2** · `spacing_only`
  - EN: Hello Neth, how are you?
  - REF: សួស្តី ណេត សុខសប្បាយអត់?
  - HYP: សួស្តីណេត សុខសប្បាយអត់?

- **chrF++ 79.6** · `spacing_only`
  - EN: The none is red.
  - REF: គ្មាន គឺ ពណ៌ក្រហម។
  - HYP: គ្មាន គឺពណ៌ក្រហម។


## wrong_script (1 sentences)

- **chrF++ 38.7** · `wrong_script`
  - EN: The mod installs the fruit.
  - REF: Mod ដំឡើង ផ្លែឈើ។
  - HYP: Mod Install ផ្លែឈើ។


## repetition_hallucination (2 sentences)

- **chrF++ 25.0** · `repetition_hallucination`
  - EN: It is raining.
  - REF: ភ្លៀងហើយ។
  - HYP: ភ្លៀងកំពុងធ្លាក់។

- **chrF++ 37.0** · `repetition_hallucination`
  - EN: I am allergic to fish soup.
  - REF: ញុមចាញ់ស៊ុបត្រី។
  - HYP: ខ្ញុំមានប្រតិកម្មជាមួយស៊ុបត្រី។


## unseen_source_word (4 sentences)

- **chrF++ 27.8** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: នោះជារឿងធំណាស់សម្រាប់ញុម។

- **chrF++ 36.6** · `unseen_source_word`
  - EN: The contract is binding upon the successors and assigns of the parties.
  - REF: កិច្ចសន្យានេះមានកាតព្វកិច្ចអនុវត្តចំពោះអ្នកបន្តវេន និងអ្នកទទួលសិទ្ធិរបស់ភាគី។
  - HYP: កិច្ចសន្យា គឺ មានកាតព្វកិច្ចលើ អ្នកបន្តវេន និង ចាត់តាំង ភាគី។

- **chrF++ 21.2** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ធ្វើឱ្យម៉ាក់ភ្ញាក់ផ្អើលជាមួយកាដូ។

- **chrF++ 14.1** · `unseen_source_word`
  - EN: Sorry for being inactive lately.
  - REF: សុំទោសផងដែលមួយរយៈនេះញុមអត់សូវបានផុសអី។
  - HYP: សុំទោសចំពោះការ មិនសកម្ម ថ្មីៗនេះ។


## lexical_semantic (32 sentences)

- **chrF++ 35.8** · `lexical_semantic`
  - EN: My boyfriend is angry.
  - REF: សង្សារកំពុងខឹង។
  - HYP: សង្សារខឹង។

- **chrF++ 13.1** · `lexical_semantic`
  - EN: Do you have luggage?
  - REF: តើអ្នកមាន វ៉ាលី ទេ?
  - HYP: មានកាបូបអត់?

- **chrF++ 20.1** · `lexical_semantic`
  - EN: Stop studying and come here.
  - REF: ឈប់រៀនសិន មកនេះ។
  - HYP: ឈប់សិក្សាទៅនេះ។

- **chrF++ 24.3** · `lexical_semantic`
  - EN: Do you prefer lime or lime?
  - REF: ចូលចិត្តពណ៌បៃតងខ្ចីឬបៃតងខ្ចី?
  - HYP: ចូលចិត្តក្រូចឆ្មាឬក្រូចឆ្មា?

- **chrF++ 5.4** · `lexical_semantic`
  - EN: No spicy please.
  - REF: អត់យកហិរទេ។
  - HYP: កុំហឹរផង។
