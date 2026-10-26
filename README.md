# parasite-case-mcq

An Agent Skill that writes clinical case-based, five-option one-best-answer
multiple-choice questions (MCQs) in parasitology, following medical-education
item-writing principles. Items are written in Korean with English technical
terms in parentheses.

의학교육의 선다형 문항 제작 원칙에 따라 기생충학 임상 증례형 5지선다
최선답형 문항을 만드는 Agent Skill입니다. 문항은 한국어로 작성하며,
전문용어에는 괄호 안에 영문을 병기합니다.

## What it does

| Input | Mode | Default output |
|---|---|---|
| Parasite name or topic (e.g., "간흡충 4문항") | Mode A | The number of items requested (3 if not stated) |
| One article (PDF, DOCX, Markdown, DOI, or PMID) | Mode B | 3 items on 3 different physician tasks, plus article notes |
| Optional image file uploaded by the user | Either | Image placed in the vignette (stem) |

Each item file contains, in order:

1. 증례 (clinical vignette), with a figure if available
2. 질문 (lead-in)
3. 답가지 (options 1–5)
4. 정답과 근거 (answer, explanation of the key and two distractors, a
   verbatim evidence passage from the supplied article, and a verifiable
   reference)
5. 문항분류 (parasite or topic; item level: 암기형, 판단형, or 문제해결형;
   learning objective; difficulty)
6. Physician task 분류: 예방·건강유지 (health and health maintenance),
   병태생리·기전 (mechanisms of disease), 진단 (diagnosis), or 치료·관리
   (management)
7. 품질 점검 (quality check)

Key rules:

- Item-writing flaws are checked explicitly: cover-the-options rule,
  testwiseness cues (grammatical, logical, absolute terms, longest option,
  clang clues, convergence), and irrelevant difficulty (vague frequency
  terms, overlapping numbers, "all/none of the above", negative stems,
  K-type formats).
- Cases are always fictionalized; patients in uploaded case reports are not
  reproduced.
- Correct answers are keyed to established knowledge. Items that depend on
  a single article's finding are labelled 논문 의존 (article-dependent).
- In Mode B, the most suitable article figure (microscopy, pathology,
  imaging, or clinical photograph) is cropped to PNG with labels and
  answer-revealing marks removed, and placed in the vignette.
- No source, quotation, page number, or link is invented; unverifiable
  sources are marked 출처 확인 필요 (source verification required).

## Install

With the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/huhsoleil/parasite-case-mcq --skill parasite-case-mcq
```

As a Claude Code plugin marketplace:

```bash
/plugin marketplace add huhsoleil/parasite-case-mcq
/plugin install parasite-case-mcq@parasite-case-mcq
```

Manually: copy `skills/parasite-case-mcq/` into `~/.claude/skills/`
(Claude Code) or `.agents/skills/` (Antigravity), or zip that folder and
upload it under Settings → Capabilities → Skills (Claude apps).

## Usage

Mode A (parasite name):

```
간흡충(Clonorchis sinensis) 문항 4개 만들어 주세요.
```

Mode B (one article; attach the file):

```
/parasite-case-mcq 첨부한 case.pdf 논문을 바탕으로 시험 문항을 만들어 주세요.
```

With your own image (attach the image):

```
첨부한 충란 사진을 증례에 넣어 회충 진단 문항을 1개 만들어 주세요.
```

Items are saved as `items/<topic>_<number>.md`, figures as
`items/images/<topic>_<number>_fig.png`, and the response ends with a
summary table by topic and physician task.

## Example

[`examples/neurocysticercosis-case/`](examples/neurocysticercosis-case/)
shows a full Mode B run on an open-access case report (giant
neurocysticercosis): the prompt, the article notes, three items, and the
MRI figure cropped from the article, with a script that reproduces the
crop.

## Repository layout

```
.
├── .claude-plugin/marketplace.json     # Claude Code plugin marketplace manifest
├── skills/
│   └── parasite-case-mcq/
│       ├── SKILL.md                    # Instructions (frontmatter: name, description)
│       ├── LICENSE.txt
│       └── evals/evals.json            # Test prompts (skill-creator format)
├── examples/
│   └── neurocysticercosis-case/
│       ├── README.md                   # Prompt and walkthrough
│       ├── case.pdf                    # Source article (CC BY-NC 4.0)
│       ├── crop_figure.py              # Reproduces the figure crop
│       └── items/                      # Notes, three items, and images/
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── README.md
```

## Validate and test

```bash
# Frontmatter and structure (skill-creator validator)
python path/to/skill-creator/scripts/quick_validate.py skills/parasite-case-mcq
```

`skills/parasite-case-mcq/evals/evals.json` contains two test cases in the
[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
format: Mode B with the example article and Mode A with a parasite name.

## Limitations

- Generated items are drafts. A content expert must review every item,
  including facts, drug choices, and doses, before use in an examination.
- Item difficulty is an estimate; confirm it with item analysis after
  administration.
- Check the licence of any article figure before distributing items
  outside your institution.

## License

Skill instructions: Apache License 2.0 (see `LICENSE`). The example
article and the files derived from it in `examples/neurocysticercosis-case/`
are CC BY-NC 4.0; see `THIRD_PARTY_NOTICES.md`.

## Skill.sh   search
[![skills.sh](https://skills.sh/b/huhsoleil/parasite-case-mcq)](https://skills.sh/huhsoleil/parasite-case-mcq)
