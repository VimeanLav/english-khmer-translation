# Qualitative probe (base experiment)

Everyday sentences unlike the training templates, translated by every model with beam search (4 beams). Fill in the last column: ✅ correct, ⚠️ understandable but wrong register or word, ❌ wrong or nonsense.


**1. i want to hug you**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ជ្រោមជ្រែង អ្នក | |
| A: Transformer from scratch | កូរាមេញាមេញ។ | |
| B: NLLB frozen backbone | ញុមចង់យកចិត្តទុកដាក់ឯង | |

**2. i want to kiss you**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ថើប អ្នក | |
| A: Transformer from scratch | ចង់ទៅទំពិត្រប់ស្ល់។ | |
| B: NLLB frozen backbone | ញុមចង់ផ្កាឯង។ | |

**3. i want to study english in my parents school**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ រៀន ភាសា អង់គ្លេស នៅ សាលា របស់ ឪពុក ម្តាយ ខ្ញុំ | |
| A: Transformer from scratch | ឪពុកម្តាយក្រុមទាមទាញុម។ | |
| B: NLLB frozen backbone | ខ្ញុំចង់សិក្សា ភាសាអង់គ្លេស នៅ សាលារៀន ឪពុកម្តាយរបស់ខ្ញុំ | |

**4. i want you to believe in me, i know i can do it**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ចង់ ឲ្យ អ្នក ជឿ លើ ខ្ញុំ ខ្ញុំ ដឹង ថា ខ្ញុំ អាច ធ្វើ បាន | |
| A: Transformer from scratch | បានចុំក់ខ្រុំណ្ញុំណ្រណ្ញុំណី។ | |
| B: NLLB frozen backbone | ញុមចង់បានអ្នកជឿលើញុមញុមដឹងថាញុមអាចធ្វើវាបាន | |

**5. can you start the project? i want to see what you can do.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ អ្នក អាច ចាប់ផ្តើម គម្រោង នេះ បាន ទេ? ខ្ញុំ ចង់ ឃើញ ថា អ្នក អាច ធ្វើ អ្វី បាន។ | |
| A: Transformer from scratch | ចាប់ផ្តើមពិញ្រណ្ញ្ញ្ញុមាំណី។ | |
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
| A: Transformer from scratch | ញុមស្រលាញ់មេ។ | |
| B: NLLB frozen backbone | ញុមស្រលាញ់ម៉ាក់។ | |

**8. The weather is very hot today.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | អាកាសធាតុ នៅថ្ងៃនេះ ក្តៅ ខ្លាំងណាស់ ។ | |
| A: Transformer from scratch | អាកាសធាតុនៅក្នុងខែ ក្តៅ គឺ ក្តៅ ណាស់។ | |
| B: NLLB frozen backbone | ថ្ងៃនេះអាកាសធាតុក្តៅណាស់។ | |

**9. Where is the nearest hospital?**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ មន្ទីរពេទ្យ ជិត បំផុត នៅ ទីណា? | |
| A: Transformer from scratch | តើមន្រពេទ្យដែលនៅជិតនៅឯណា? | |
| B: NLLB frozen backbone | តើមន្ទីរពេទ្យដែលជិតគេនៅណា? | |

**10. I am a student at Kirirom Institute of Technology.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ ជា និស្សិត នៅ វិទ្យាស្ថាន បច្ចេកវិទ្យា Kirirom។ | |
| A: Transformer from scratch | សិស្សធាញុមទាន។ | |
| B: NLLB frozen backbone | ញុមសិស្សនៅវិទ្យាល័យបច្ចេកវិទ្យាកិរីរ៉ូម។ | |

**11. Can you help me find my phone?**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | តើ អ្នក អាច ជួយ ខ្ញុំ រក ទូរស័ព្ទ របស់ ខ្ញុំ បាន ទេ? | |
| A: Transformer from scratch | ជួយទូរស័ព្ទរបស់ខ្ញុំបានទេ? | |
| B: NLLB frozen backbone | ជួយរកទូរស័ព្ទញុមបានអត់? | |

**12. I have 3 brothers and 2 sisters.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ខ្ញុំ មាន បងប្រុស ៣ នាក់ និង ប្អូនស្រី ២ នាក់។ | |
| A: Transformer from scratch | បងប្រុសរបស់ខ្ញុំហើយទិញ បងស្រីរបស់ខ្ញុំ។ | |
| B: NLLB frozen backbone | ញុមមានបងប្អូនប្រុស៣នាក់ និងបងប្អូនស្រី២នាក់។ | |

**13. Machine learning is changing the world.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | ការ សិក្សា ដោយ ម៉ាស៊ីន កំពុង ផ្លាស់ ប្តូរ ពិភពលោក។ | |
| A: Transformer from scratch | សូមអីនាលាល់នៅ។ | |
| B: NLLB frozen backbone | ការរៀនរបស់ម៉ាស៊ីន កំពុងតែផ្លាស់ប្តូរ ពិភពលោក។ | |

**14. Please call me when you arrive at the airport.**

| Model | Khmer output | Judgement |
|---|---|---|
| Zero-shot NLLB-600M (reference) | សូម ទូរស័ព្ទ មក ខ្ញុំ នៅ ពេល ដែល អ្នក មក ដល់ អាកាសយានដ្ឋាន។ | |
| A: Transformer from scratch | សូមហុំនៅព្រលានយន្តហោះ។ | |
| B: NLLB frozen backbone | សូមតេមកញុមនៅពេលអ្នកមកដល់ព្រលានយន្តហោះ។ | |
