# Qualitative probe (augmented experiment)

Everyday sentences unlike the training templates, translated by every model with beam search (4 beams). Fill in the last column: ✅ correct, ⚠️ understandable but wrong register or word, ❌ wrong or nonsense.


**1. i want to hug you**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ជ្រោមជ្រែង អ្នក | |
| A: Transformer from scratch | ខ្ញុំចង់ហ្ស័ង។ | |
| B: NLLB frozen backbone | ញុមចង់យកចិត្តទុកដាក់ឯង | |

**2. i want to kiss you**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ថើប អ្នក | |
| A: Transformer from scratch | ខ្ញុំចង់អរគុណ។ | |
| B: NLLB frozen backbone | ញុមចង់បានអ្នក | |

**3. i want to study english in my parents school**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ រៀន ភាសា អង់គ្លេស នៅ សាលា របស់ ឪពុក ម្តាយ ខ្ញុំ | |
| A: Transformer from scratch | ខ្ញុំចង់រៀនសូត្រក្នុងឪពុកម្តាយរបស់ខ្ញុំ។ | |
| B: NLLB frozen backbone | ខ្ញុំចង់សិក្សា ភាសាអង់គ្លេស នៅ សាលារៀនរបស់ឪពុកម្តាយរបស់ខ្ញុំ | |

**4. i want you to believe in me, i know i can do it**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ឲ្យ អ្នក ជឿ លើ ខ្ញុំ ខ្ញុំ ដឹង ថា ខ្ញុំ អាច ធ្វើ បាន | |
| A: Transformer from scratch | អ្នកចង់ជឿថានៅត្រង់ខ្ញុំ i ស្គាល់អាចធ្វើវាបាន។ | |
| B: NLLB frozen backbone | ញុមចង់ឲ្យអ្នកជឿលើខ្ញុំ ញុមដឹងថាញុមអាចធ្វើបាន។ | |

**5. can you start the project? i want to see what you can do.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ អ្នក អាច ចាប់ផ្តើម គម្រោង នេះ បាន ទេ? ខ្ញុំ ចង់ ឃើញ ថា អ្នក អាច ធ្វើ អ្វី បាន។ | |
| A: Transformer from scratch | អ្នកអាចចាប់ផ្តើមគម្រោងរបស់អ្នកចង់មើលនូវអ្វីដែលអ្នកអាចធ្វើបាន។ | |
| B: NLLB frozen backbone | តើអ្នកអាចចាប់ផ្តើម គម្រោង បានទេ? ញុមចង់មើល អ្វីដែលអ្នកអាចធ្វើបាន។ | |

**6. I love you.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ស្រឡាញ់ អ្នក។ | |
| A: Transformer from scratch | ញុមស្រលាញ់។ | |
| B: NLLB frozen backbone | ញុមស្រលាញ់ឯង។ | |

**7. I love my mother.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ស្រឡាញ់ ម្តាយ ខ្ញុំ។ | |
| A: Transformer from scratch | ញុមស្រលាញ់ម្តាយ។ | |
| B: NLLB frozen backbone | ញុមស្រលាញ់ម៉ាក់។ | |

**8. The weather is very hot today.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | អាកាសធាតុ នៅថ្ងៃនេះ ក្តៅ ខ្លាំងណាស់ ។ | |
| A: Transformer from scratch | ថ្ងៃនេះ អាកាសធាតុនៅក្នុងខែ ក្តៅ ណាស់។ | |
| B: NLLB frozen backbone | ថ្ងៃនេះអាកាសធាតុក្តៅណាស់។ | |

**9. Where is the nearest hospital?**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ មន្ទីរពេទ្យ ជិត បំផុត នៅ ទីណា? | |
| A: Transformer from scratch | តើមន្ទីរពេទ្យដែលនៅជិតបំផុតនៅឯណា? | |
| B: NLLB frozen backbone | មន្ទីរពេទ្យជិតបំផុតនៅណា? | |

**10. I am a student at Kirirom Institute of Technology.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ជា និស្សិត នៅ វិទ្យាស្ថាន បច្ចេកវិទ្យា Kirirom។ | |
| A: Transformer from scratch | សិស្សនៅវិទ្យាស្ថានគីរូមប្រូត្រូនៃបច្ចេកវិទ្យា។ | |
| B: NLLB frozen backbone | ញុមជាសិស្សនៅវិទ្យាស្ថានបច្ចេកវិទ្យាគីរ៉ូម។ | |

**11. Can you help me find my phone?**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ អ្នក អាច ជួយ ខ្ញុំ រក ទូរស័ព្ទ របស់ ខ្ញុំ បាន ទេ? | |
| A: Transformer from scratch | ជួយទូរស័ព្ទញុមបានអត់? | |
| B: NLLB frozen backbone | ជួយរកទូរស័ព្ទញុមបានអត់? | |

**12. I have 3 brothers and 2 sisters.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ មាន បងប្រុស ៣ នាក់ និង ប្អូនស្រី ២ នាក់។ | |
| A: Transformer from scratch | ខ្ញុំមានបងប្អូនប្រុសចំនួន២និងបងប្អូនស្រី។ | |
| B: NLLB frozen backbone | ញុមមានបងប្អូនប្រុសបីនាក់ និងបងប្អូនស្រីពីរនាក់។ | |

**13. Machine learning is changing the world.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ការ សិក្សា ដោយ ម៉ាស៊ីន កំពុង ផ្លាស់ ប្តូរ ពិភពលោក។ | |
| A: Transformer from scratch | Machine រៀនសូត្រគឺជាការផ្លាស់ប្តូរពិភពលោក។ | |
| B: NLLB frozen backbone | ការរៀនរបស់ម៉ាស៊ីនកំពុងផ្លាស់ប្តូរពិភពលោក។ | |

**14. Please call me when you arrive at the airport.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | សូម ទូរស័ព្ទ មក ខ្ញុំ នៅ ពេល ដែល អ្នក មក ដល់ អាកាសយានដ្ឋាន។ | |
| A: Transformer from scratch | សូមហៅអ្នកមកដល់ព្រលានយន្តហោះ។ | |
| B: NLLB frozen backbone | សូមហៅញុមនៅពេលអ្នកមកដល់ព្រលានយន្តហោះ។ | |
