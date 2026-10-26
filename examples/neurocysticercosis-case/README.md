# Example: items from a case report (Mode B)

이 폴더는 논문 1편(증례보고)을 올려 문항을 만드는 예시입니다.
This folder shows the skill run in Mode B on one open-access case report.

## Source article

Lee CS, Lee YA, Koh HM, Chung YB. A giant neurocysticercosis diagnosed by
Western blotting. *Parasites Hosts Dis* 2026;64(2):190-193.
<https://doi.org/10.3347/PHD.26004> (PMID 41958280).
Licensed under CC BY-NC 4.0; see `../../THIRD_PARTY_NOTICES.md`.

## Prompt

Attach `case.pdf` and enter:

```
/parasite-case-mcq 첨부한 case.pdf 논문을 바탕으로 시험 문항을 만들어 주세요.
```

Without the slash command, a request such as
"case.pdf 논문으로 기생충학 증례 문항을 만들어 주세요" also triggers the skill.

## What the skill did

1. **Read the article and saved notes** grouped by physician task
   (`items/neurocysticercosis_article-notes.md`), separating established
   facts from article-specific findings (cyst-fluid Western blot).
2. **Chose three physician tasks** the article supports best (default for
   Mode B): health maintenance, mechanisms of disease, and management.
   Diagnosis was left out because the article's diagnostic method is not
   routine and a histology item would have been cued by the other items.
3. **Selected and cropped a figure.** Of the five figures (MRI, operative
   photos, SDS-PAGE, Western blot, histology), Fig. 1 panels C–D (T2 axial,
   T1 sagittal MRI) best support a vignette on hydrocephalus. The clean
   image embedded in the PDF has no asterisks or panel labels, so it was
   cropped directly (`crop_figure.py`) and saved as
   `items/images/neurocysticercosis_02_fig.png` (953 × 402 px).
4. **Wrote three fictionalized items** in Korean with English terms in
   parentheses, each with the answer, a verbatim evidence passage from the
   article, a guideline reference, item classification, and physician task.

| Item | Physician task | Item level | Answer | Figure |
|---|---|---|---|---|
| [neurocysticercosis_01](items/neurocysticercosis_01.md) | 예방·건강유지 (route of infection) | 판단형 | 4 | – |
| [neurocysticercosis_02](items/neurocysticercosis_02.md) | 병태생리·기전 (mechanism of hydrocephalus) | 판단형 | 5 | Fig. 1C–D |
| [neurocysticercosis_03](items/neurocysticercosis_03.md) | 치료·관리 (next step) | 문제해결형 | 2 | – |

## Reproduce the figure

```bash
python crop_figure.py case.pdf items/images/neurocysticercosis_02_fig.png
```

Requires `pdfimages` (poppler-utils) and Pillow.

## Notes for reviewers

- The cases are fictionalized; they do not reproduce the reported patient.
- Item 3 keys surgical cyst removal; the explanation notes that CSF
  diversion is an alternative first step, and only one of the two appears
  among the options to avoid two defensible answers.
- All items still require content-expert review before use in an
  examination.
