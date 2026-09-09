# Introduction to Freedom and Government: source and review record

Work: Leon Roth, “הקדמה” [Introduction], in H. Merhavya's *Freedom and Government*, pp. 5–6 (ה–ו). Jerusalem: Goren, 1945. The English title/year follow the existing bibliography. The scanned title page describes Merhavya as the collector/editor (`אסף וערך`); the work therefore uses `editors`, not a claim that Roth wrote the whole book. The original heading is simply `הקדמה`; the English translated title is a descriptive catalog label.

Current state: **scan_checked; published: false**. Codex manually transcribed the two printed pages and checked them visually on September 9, 2026. Review by a proficient Hebrew reader remains pending. This pilot has no human acceptance yet.

## Sources and reproduction

| Source | Identifier |
| --- | --- |
| Original local download | `Site Files/herut umishtar.pdf` (1,690,295 bytes) |
| Original SHA-256 | `37783f9d8d604d4ad31e63cfdd11e5c96afed0125c1146c42c09c606f47b6aba` |
| Retained public scan | `/_files/ugd/01b672_83e04f6517bb436e9804cbbe1d31e503.pdf` (1,391,434 bytes) |
| Public scan SHA-256 | `383cfe9e660d65b6b92f6671ebd63d97df1221b5cf69784aebf2c276173fa630` |
| Edition source | `_works/1945-freedom-government-introduction.md` |
| Checked Markdown body SHA-256 | `3b9bdab6ec8d68ca8898165ec2fd148aed6d982fc3214c2dbedb6fda01461f9b` (UTF-8 body after front matter, leading blank lines removed) |
| Reader URL | `/works/freedom-government-introduction/` (preview only) |

All three original/public PDF page pairs render pixel-identically at 180 dpi. PDF page 1 is the title page; Roth's introduction is complete on PDF pages 2–3. The title page is source evidence, not part of his prose. No source PDF was modified.

There is no embedded text layer: `pdftotext -layout` returns three page-separator characters and no words. Given two legible, single-column text pages, this pilot used manual image reading, not a claimed OCR benchmark. Page images were inspected at 180 dpi, with 300 dpi renders/crops for disputed-looking letter shapes and the date. Rendering at a higher dpi does not add missing source detail. The general Hebrew OCR comparison is still outstanding; this transcription establishes no OCR accuracy or backlog throughput estimate.

```sh
mkdir -p /tmp/leonroth-digitization/freedom-government
pdftoppm -r 180 -png 'Site Files/herut umishtar.pdf' /tmp/leonroth-digitization/freedom-government/page
pdftoppm -f 2 -l 3 -r 300 -png 'Site Files/herut umishtar.pdf' /tmp/leonroth-digitization/freedom-government/check
```

## Page checks

| Printed / PDF page | Checks |
| --- | --- |
| Title page / 1 | Identified the book, editor/collector, Roth introduction credit, Jerusalem, and Goren imprint. Not transcribed as Roth's prose. |
| ה (5) / 2 | Five source paragraphs, charter names, `ביוני 1940`, quotation boundaries, parentheses, and final words `שתנתן לו הרשות לכך.` Checked historical spellings and paragraph breaks; did not modernize them. |
| ו (6) / 3 | Four prose paragraphs, Locke's name, quotation of the philosopher-kings passage, closing blessing, `ירושלים, כ״ב במרחשון תש״ו`, and `ח״י רות`. A second visual pass corrected a draft's doubled vav in `ויתר` to the printed single vav. |

No source footnotes occur in this introduction. The Hebrew reading direction, Arabic numerals within the prose, Hebrew abbreviation marks, parentheses, quotes, and page markers are the main layout checks. Numbered markers retain stable decimal anchors `page-5` and `page-6`, display the source labels ה and ו, and link to PDF pages 2 and 3.

## Editorial transformations and remaining review

- Reflowed lines and joined words divided at line endings, including the printed line-break divisions in `האידיאליות` and `הפילוסופים`. Preserved nine prose paragraphs and separate closing date/signature lines.
- Normalized quotation glyphs to typographic double quotes, abbreviation marks to geresh/gershayim, and the meaningful `מבני־האדם` hyphen to Hebrew maqaf. No vowel points occur in the transcribed prose; no points were added. Decorative pointed cover lettering is outside this introduction's body.
- Retained historical forms such as `פנה`, `באוירה`, `החפשית`, `המאזנים`, `דימוקראטיה`, `איפוא`, `תאור`, `בספור`, and `דוקה`. Do not silently change them to modern spellings.
- Preserved the Hebrew date exactly as printed. The scan has no Gregorian publication date; 1945 follows the bibliography. Do not infer an exact Gregorian publication day from the date of the introduction.
- The English shell and metadata labels remain LTR; the title/prose are Hebrew RTL. No translation or paraphrase replaces the source Hebrew.
- Before acceptance, a proficient Hebrew reader should compare every paragraph, final form, punctuation mark, and date against the scan, and confirm the typographic normalization choices. The manuscript is AI-assisted and may still contain transcription errors. Bibliographic year and full title can be checked against a complete book if available.

## Human review and release decision

Technical validation: the preview passes route/link/PDF checks at both `/leonroth/` and the domain-root base path. The real Hebrew work renders with `lang="he"`, RTL prose, and 18px mobile text; 390px and 320px checks found no horizontal overflow. The source page labels ה and ו point to PDF pages 2 and 3. Desktop and mobile prose/date rendering were inspected. The citation uses decimal `5–6` in its LTR metadata region, avoiding the reversed range observed when Hebrew labels were mixed into that value. These checks do not establish the accuracy of the Hebrew transcription.

| Field | Value |
| --- | --- |
| Proficient Hebrew reviewer / date | Pending |
| Exact content commit reviewed | Pending |
| Text and normalization accepted | Pending |
| Publication approved | No |

After review, record the reviewer, date, and exact content commit before moving to `verified`. Keep `published: false` until a separate release decision. The new pilot does not inherit the owner's approval of David Nieto.
