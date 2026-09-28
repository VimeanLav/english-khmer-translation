# Error analysis: Zero-shot NLLB-600M (reference)

Failure = sentence chrF++ < 40. Categories are defined in `src/error_analysis.py`.

## 15 worst translations

- **chrF++ 0.0** · `repetition_hallucination`
  - EN: The beta is more away than the tip.
  - REF: Beta គឺ មិននៅ ជាង Tip។
  - HYP: ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រភេទ ប្រ

- **chrF++ 0.7** · `repetition_hallucination`
  - EN: Is the sunglasses yellow?
  - REF: តើ វ៉ែនតាការពារកម្ដៅថ្ងៃ ពណ៌ លឿង ឬ?
  - HYP: អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អញ្ចឹង អ

- **chrF++ 1.1** · `repetition_hallucination`
  - EN: The sushi is gross.
  - REF: ស៊ូស៊ី គឺ អាក្រក់មើល។
  - HYP: អាហ្នឹង អាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹងអាហ្នឹង

- **chrF++ 1.2** · `repetition_hallucination`
  - EN: Wow, Can you lower the price for these books?
  - REF: វ៉ាវ ចុះថ្លៃសៀវភៅតិចបានអត់?
  - HYP: អាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអា

- **chrF++ 1.3** · `repetition_hallucination`
  - EN: Pass me the speaker.
  - REF: ហុចធុងបាសឲ្យញុម។
  - HYP: សូមផ្ទេរអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញអញ្ជើញ

- **chrF++ 1.4** · `repetition_hallucination`
  - EN: Wow, Can you lower the price for these pants?
  - REF: វ៉ាវ ចុះថ្លៃខោតិចបានអត់?
  - HYP: អាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអា

- **chrF++ 1.4** · `repetition_hallucination`
  - EN: The auditor agrees to supply the property upon termination of this agreement.
  - REF: សវនករ យល់ព្រម ផ្គត់ផ្គង់ អចលនទ្រព្យ នៅពេលបញ្ចប់កិច្ចព្រមព្រៀងនេះ។
  - HYP: ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធ

- **chrF++ 1.5** · `repetition_hallucination`
  - EN: Hey, This pizza smells good.
  - REF: នែ៎ ភីហ្សានេះឈ្ងុយណាស់។
  - HYP: ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី ហេី

- **chrF++ 1.6** · `repetition_hallucination`
  - EN: Is that your broom?
  - REF: នោះជាអំបោសឯងមែន?
  - HYP: តើវាជាថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ្នាំថ

- **chrF++ 1.7** · `repetition_hallucination`
  - EN: Wow, Can you lower the price for this tissue?
  - REF: វ៉ាវ ចុះថ្លៃក្រដាសជូតមាត់តិចបានអត់?
  - HYP: អាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអាអា

- **chrF++ 1.8** · `repetition_hallucination`
  - EN: the certification refers to the application.
  - REF: វិញ្ញាបនបត្រ សំដៅទៅលើ ពាក្យស្នើសុំ។
  - HYP: លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា លិខិតឆ្លងដែន (certification) មានន័យថា ល

- **chrF++ 1.8** · `repetition_hallucination`
  - EN: We fertilize date palm because of good weather.
  - REF: យើងដាក់ជីល្មើដោយសារតែអាកាសធាតុល្អ។
  - HYP: យើង បង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្កបង្ក

- **chrF++ 1.9** · `repetition_hallucination`
  - EN: Apply a thin layer of gel to the back on an empty stomach.
  - REF: លាបជែល មួយស្រទាប់ស្តើង ត្រង់ខ្នង នៅពេលពោះទទេ។
  - HYP: ដាក់ ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស ក្រដាស

- **chrF++ 1.9** · `repetition_hallucination`
  - EN: The auditor is authorized to rent the policy commencing on the effective date.
  - REF: សវនករ ត្រូវបានផ្តល់សិទ្ធិឱ្យ ជួល គោលនយោបាយ ចាប់ផ្តើមនៅថ្ងៃចូលជាធរមាន។
  - HYP: ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធនាគារ ធ

- **chrF++ 2.0** · `wrong_script`
  - EN: Hey, No pancakes left.
  - REF: នែ៎ អស់នំផេនខេកហើយ។
  - HYP: Hey, គ្មាន pancakes សល់.


## spacing_only (83 sentences)

- **chrF++ 75.0** · `spacing_only`
  - EN: the intellectual property is acknowledged publicly.
  - REF: កម្មសិទ្ធិបញ្ញា ត្រូវបានទទួលស្គាល់ ជាសាធារណៈ។
  - HYP: កម្មសិទ្ធិ បញ្ញា ត្រូវ បាន ទទួល ស្គាល់ ជា សាធារណៈ។

- **chrF++ 91.3** · `spacing_only`
  - EN: I bought map at the market.
  - REF: ខ្ញុំបានទិញ ផែនទី នៅ ផ្សារ។
  - HYP: ខ្ញុំ បាន ទិញ ផែនទី នៅ ផ្សារ។

- **chrF++ 93.6** · `spacing_only`
  - EN: I will drink water at the museum.
  - REF: ខ្ញុំនឹង ផឹក ទឹក នៅ សារមន្ទីរ។
  - HYP: ខ្ញុំ នឹង ផឹក ទឹក នៅ សារមន្ទីរ។

- **chrF++ 91.3** · `spacing_only`
  - EN: I bought ticket at the market.
  - REF: ខ្ញុំបានទិញ សំបុត្រ នៅ ផ្សារ។
  - HYP: ខ្ញុំ បាន ទិញ សំបុត្រ នៅ ផ្សារ។

- **chrF++ 91.9** · `spacing_only`
  - EN: The supplier agrees to approve the decision.
  - REF: អ្នកផ្គត់ផ្គង់ យល់ព្រម អនុម័ត សេចក្តីសម្រេច។
  - HYP: អ្នកផ្គត់ផ្គង់ យល់ព្រម អនុម័ត សេចក្តីសម្រេច ។


## wrong_script (7 sentences)

- **chrF++ 5.4** · `wrong_script`
  - EN: Steak is better than steak.
  - REF: សាច់អាំងឆ្ងាញ់ជាងសាច់អាំង។
  - HYP: Steak ល្អជាង steak ។

- **chrF++ 28.7** · `wrong_script`
  - EN: Vanny is taller than Vanny.
  - REF: វណ្ណីខ្ពស់ជាងវណ្ណី។
  - HYP: Vanny ខ្ពស់ ជាង Vanny។

- **chrF++ 21.5** · `wrong_script`
  - EN: Sreymom is taller than Sreymom.
  - REF: ស្រីម៉ុំខ្ពស់ជាងស្រីម៉ុំ។
  - HYP: Sreymom ខ្ពស់ ជាង Sreymom ។

- **chrF++ 8.7** · `wrong_script`
  - EN: SreyOun is taller than SreyOun.
  - REF: ស្រីអូនខ្ពស់ជាងស្រីអូន។
  - HYP: SreyOun មាន ទម្ងន់ ជាង SreyOun ។

- **chrF++ 21.3** · `wrong_script`
  - EN: Please tell Darith to buy papaya salad.
  - REF: ប្រាប់ដារិទ្ធឲ្យទិញបុកល្ហុងផង។
  - HYP: សូម ប្រាប់ Darith ឲ្យ ទិញ salad papaya។


## repetition_hallucination (287 sentences)

- **chrF++ 20.3** · `repetition_hallucination`
  - EN: I am bad at sports.
  - REF: ញុមអន់កីឡា។
  - HYP: ខ្ញុំ លំបាក ក្នុង ការ ប្រកួត កីឡា។

- **chrF++ 13.2** · `repetition_hallucination`
  - EN: My boyfriend is angry.
  - REF: សង្សារកំពុងខឹង។
  - HYP: មិត្ត ប្រុស របស់ ខ្ញុំ មាន កំហឹង។

- **chrF++ 5.2** · `repetition_hallucination`
  - EN: Graduates must identify project management collaboratively.
  - REF: និស្សិតបញ្ចប់ការសិក្សា ត្រូវតែកំណត់អត្តសញ្ញាណ ការគ្រប់គ្រងគម្រោង ដោយសហការគ្នា។
  - HYP: និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និស្សិត និ

- **chrF++ 5.3** · `repetition_hallucination`
  - EN: I wish I had a cute beat.
  - REF: ញុមចង់បាន Beat ដ៏ Cute។
  - HYP: ខ្ញុំ សង្ឃឹម ថា ខ្ញុំ មាន សម្រស់ ស្រស់ ស្អាត។

- **chrF++ 20.1** · `repetition_hallucination`
  - EN: Is it rainy now?
  - REF: ឥឡូវភ្លៀងអត់?
  - HYP: តើ ពេល នេះ ភ្លៀង ធ្លាក់ មែន ទេ?


## omission (10 sentences)

- **chrF++ 2.1** · `omission`
  - EN: the debt refers to the claim.
  - REF: បំណុល សំដៅទៅលើ ការទាមទារ។
  - HYP: កាតព្វកិច្ច

- **chrF++ 3.6** · `omission`
  - EN: Remember that everyone should analyze literature assignments.
  - REF: សូមចងចាំថា អ្នកទាំងអស់គ្នា គួរតែវិភាគ កិច្ចការអក្សរសិល្ប៍។
  - HYP: ១៧ . តើ យើង អាច ធ្វើ អ្វី បាន?

- **chrF++ 2.5** · `omission`
  - EN: the trademark was issued confidentially.
  - REF: ពាណិជ្ជសញ្ញា ត្រូវបានចេញ ជាសម្ងាត់។
  - HYP: លិខិតឆ្លងដែន

- **chrF++ 6.5** · `omission`
  - EN: Consider that students can improve leadership qualities.
  - REF: ពិចារណាថា សិស្សានុសិស្ស អាចកែលម្អ គុណសម្បត្តិអ្នកដឹកនាំ។
  - HYP: តើ អ្នក អាច ធ្វើ អ្វី បាន?

- **chrF++ 5.7** · `omission`
  - EN: Groups will master literature assignments at home.
  - REF: ក្រុម នឹងចេះស្ទាត់ កិច្ចការអក្សរសិល្ប៍ នៅផ្ទះ។
  - HYP: សិក្ខាសាលា សិក្សា


## number_mismatch (19 sentences)

- **chrF++ 30.2** · `number_mismatch`
  - EN: Apply a thin layer of lotion to the head three times a day.
  - REF: លាបឡេលាប មួយស្រទាប់ស្តើង ត្រង់ក្បាល បីដងក្នុងមួយថ្ងៃ។
  - HYP: ដាក់ ស្លាក សរសៃប្រសាទ មួយ ខ្សែ ទៅ លើ ក្បាល ៣ ដង ក្នុង មួយ ថ្ងៃ។

- **chrF++ 30.5** · `number_mismatch`
  - EN: I would like one hundred bracelets.
  - REF: ខ្ញុំចង់បាន ខ្សែដៃ មួយរយ។
  - HYP: ខ្ញុំ ចង់ បាន ស្លាក ស្នាម ១០០ ស្លាបព្រាបាយ។

- **chrF++ 16.9** · `number_mismatch`
  - EN: Please prescribe spray for my fatigue.
  - REF: សូមចេញវេជ្ជបញ្ជាថ្នាំបាញ់សម្រាប់អស់កម្លាំងរបស់ខ្ញុំ។
  - HYP: សូម លោក ណែនាំ ឲ្យ ខ្ញុំ ប្រើ ថ្នាំ ព្យាបាល ជំងឺ កូវីដ១៩ ដើម្បី ព្យាបាល ជំងឺ កូវីដ១៩។

- **chrF++ 39.2** · `number_mismatch`
  - EN: The successor is obligated to violate the information within seven days.
  - REF: អ្នកបន្តវេន មានកាតព្វកិច្ច រំលោភលើ ព័ត៌មាន ក្នុងរយៈពេលប្រាំពីរថ្ងៃ។
  - HYP: អ្នកជាប់ពាក់ព័ន្ធ ត្រូវតែ រំលោភ លើ ព័ត៌មាន ក្នុង រយៈពេល ៧ ថ្ងៃ ។

- **chrF++ 35.5** · `number_mismatch`
  - EN: Is alcohol bad for typhoid?
  - REF: តើគ្រឿងស្រវឹងមិនល្អសម្រាប់គ្រុនពោះវៀនដែរឬទេ?
  - HYP: តើ គ្រឿង ស្រវឹង មាន ផល ប៉ះពាល់ ដល់ ជំងឺ កូវីដ-១៩ ដែរ ឬទេ?


## unseen_source_word (6 sentences)

- **chrF++ 18.5** · `unseen_source_word`
  - EN: That's a major ick for me.
  - REF: សម្រាប់ញុមអាហ្នឹងគឺ Ick ខ្លាំង។
  - HYP: វា ជា រឿង ធ្ងន់ធ្ងរ សម្រាប់ ខ្ញុំ។

- **chrF++ 30.6** · `unseen_source_word`
  - EN: The contract is binding upon the successors and assigns of the parties.
  - REF: កិច្ចសន្យានេះមានកាតព្វកិច្ចអនុវត្តចំពោះអ្នកបន្តវេន និងអ្នកទទួលសិទ្ធិរបស់ភាគី។
  - HYP: កិច្ចសន្យា នេះ ជា ការពង្រឹង ដល់ អ្នកទទួលខុសត្រូវ និង អ្នកទទួលខុសត្រូវ របស់ ភាគី ។

- **chrF++ 7.0** · `unseen_source_word`
  - EN: Surprising my mom with a gift.
  - REF: Surprise ម៉ាក់របស់ញុមជាមួយនឹងកាដូ។
  - HYP: ធ្វើ ឲ្យ ម្តាយ ខ្ញុំ ភ្ញាក់ ផ្អើល ដោយ អំណោយ មួយ។

- **chrF++ 26.7** · `unseen_source_word`
  - EN: You are liking the class.
  - REF: អ្នក កំពុងតែ ចូលចិត្ត ថ្នាក់រៀន។
  - HYP: អ្នក ចូល ចិត្ត ការ សិក្សា។

- **chrF++ 22.2** · `unseen_source_word`
  - EN: Go straight ahead.
  - REF: ទៅត្រង់ទៅមុខ។
  - HYP: ទៅមុខដោយផ្ទាល់។


## lexical_semantic (2268 sentences)

- **chrF++ 10.2** · `lexical_semantic`
  - EN: I saw Piseth at the library.
  - REF: ញុមឃើញពិសិដ្ឋនៅបណ្ណាល័យ។
  - HYP: ខ្ញុំ បាន ឃើញ Piseth នៅ សៀវភៅ។

- **chrF++ 24.7** · `lexical_semantic`
  - EN: It is prohibited for the council to transfer the rule.
  - REF: វាត្រូវបានហាមឃាត់សម្រាប់ ក្រុមប្រឹក្សា ក្នុងការ ផ្ទេរ វិធាន។
  - HYP: វា ហាម មិន ឲ្យ ក្រុមប្រឹក្សា បញ្ជូន ច្បាប់ នេះ ទៅ។

- **chrF++ 22.3** · `lexical_semantic`
  - EN: Please ensure to take this antibiotic every hour.
  - REF: សូមធានាថាលេបថ្នាំអង់ទីប៊ីយោទិចនេះ រាល់ម៉ោង។
  - HYP: សូម ប្រាកដ ថា អ្នក ត្រូវ ទទួលទាន ថ្នាំ ប្រឆាំង នឹង ជំងឺ នេះ ជា រៀងរាល់ ម៉ោង។

- **chrF++ 39.9** · `lexical_semantic`
  - EN: I bought beer at the school.
  - REF: ខ្ញុំបានទិញ ស្រាបៀរ នៅ សាលារៀន។
  - HYP: ខ្ញុំ បាន ទិញ ភេសជ្ជៈ នៅ សាលា។

- **chrF++ 28.6** · `lexical_semantic`
  - EN: the bond refers to the order.
  - REF: សញ្ញាបណ្ណ សំដៅទៅលើ ដីកា។
  - HYP: កាតប័ណ្ណ នេះ សំដៅ ទៅ លើ បទបញ្ជា។
