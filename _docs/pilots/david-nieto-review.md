# David Nieto pilot: source and review record

Work: Leon Roth, "David Nieto and the Orthodoxy of Spinozism," *Chronicon Spinozanum* 1 (1921), pp. 278–282. The publication/year are inherited from the existing bibliography; the article scan itself verifies the title, signature, and printed pages but does not include the volume's title page.

Current state: **verified; published: false**. Codex compared the complete draft against the five printed pages on September 9, 2026. The project owner subsequently reported reviewing the text, this review record, and the editorial standard and accepted continued work. This records acceptance of the pilot, not authorization to publish it or a claim of independent scholarly certification.

## Sources and reproduction

| Source | Identifier |
| --- | --- |
| Original local download | `Site Files/David Nieto.pdf` (270,553 bytes) |
| Original SHA-256 | `edc50eb442846e5c4af920c4ff54ebba0f9a6685c80b56c27e5f73f1bb47a176` |
| Retained public scan | `/_files/ugd/01b672_c3b427c331294b0194fdc13ddab509d8.pdf` (258,541 bytes) |
| Public scan SHA-256 | `672fe1fb5ecaac9b1c6a244ba82c7ce95211d564ab0fda25cbd9087202578385` |
| Edition source | `_works/1921-david-nieto.md` |
| Checked Markdown body SHA-256 | `9a87551768a20502fc3e5ce2552305f41737f6676c7521ac09bc93f59b63e366` (UTF-8 body after front matter, leading blank lines removed) |
| Reader URL | `/works/david-nieto/` (preview only) |

Both PDFs contain five pages; their rendered page images are pixel-identical at 250 dpi. The original contains 300 dpi monochrome page images and an imperfect text layer. `pdftotext -layout` produced 10,587 bytes of text; extraction was used only as a starting point. All five original pages were rendered at 250 dpi and read visually; Hebrew passages and the accented heading were also inspected in enlarged crops. No original PDF was modified.

Reproduce the source extraction and rendering with Poppler:

```sh
mkdir -p /tmp/leonroth-digitization/david-nieto
pdftotext -layout 'Site Files/David Nieto.pdf' /tmp/leonroth-digitization/david-nieto/source-text.txt
pdftoppm -r 250 -png 'Site Files/David Nieto.pdf' /tmp/leonroth-digitization/david-nieto/page
```

The original download is not in Git. The public PDF is retained in Git and can be used for review; the edition's page markers link to its corresponding PDF pages. Tool outputs and page PNGs are temporary QA material and are not committed as site assets.

## Page-by-page check

| Printed / PDF page | Scope checked | Specific checks and corrections |
| --- | --- | --- |
| 278 / 1 | Title, introduction, question heading, sermon, start of defence | Long s normalized; `Shaaré` accent preserved; `טבע`, `השגחה`, and `טבעים פרטיים` read visually; Psalm quotation italics preserved; paragraph ends and quotation marks checked. |
| 279 / 2 | Continuation of defence through "with whom is the right" | No paragraph break introduced after "If what I had"; `טבע כולל` preserved; `natura naturans` and `natura naturata` left as printed; emphasis on Providence and Nature checked. |
| 280 / 3 | Answer through "on this count" | OCR's corrupted centuries corrected to printed `11th—12th` and `16th`; `מטבע`, `מטבעות`, `ההנהגה הכוללת`, and `האלוקות` read visually; quotation italics and dash/parenthesis structure checked. |
| 281 / 4 | Continuation through "because the" | Printed `misconstruktion` preserved; names/titles/dates checked; the Hebrew sentence `חפץ ורצון הבריאה היתה כי מטבע הטוב להיטיב` retained; page-boundary joins checked. |
| 282 / 5 | End of response, date, signatory, place, Roth signature | Joined the split word "providence"; `seventeenth day in Ab, 5465 [June 1705]` retained as printed; `Zevi Ashkenazi` preserved distinctly from introductory `Zevi Aschkenazi`; closing lines included. |

The essay has two substantive section headings and no numbered footnotes. Its square-bracketed explanations are already part of Roth's printing and remain inline. Footnote support was tested separately with temporary fixtures; this essay alone does not exercise a real footnote apparatus.

## Editorial transformations

- Normalized long s and historical English ss ligatures; corrected OCR substitutions and word spacing by reading the image, not by a global f-to-s replacement.
- Reflowed lines, joined line-end word splits, and retained source paragraphs. Printed page changes inside a paragraph are inline page markers.
- Replaced the three ornamental asterisks after the introduction with a horizontal rule. All-capital/small-cap headings and signatures use normal text casing. The layout supplies the title and author rather than duplicating running heads.
- Preserved source wording and spelling, including `Hhacham`, `Jehudah Hallevi`, `Cuzari`, `Moscato`, `Ezeckiel`, `mediaeval`, `centered`, `every one's`, and `misconstruktion`.
- Preserved the source's unusual quotation punctuation, including the closing quotation mark after "unbelievers" on p. 278. No unprinted opening quotation mark was invented.
- Preserved meaningful italics and source brackets. Hebrew spans have `lang="he" dir="rtl"`; no translation was substituted for the printed Hebrew.
- Added five labelled page markers, each pointing to the corresponding original PDF page. These markers are editorial navigation, not source prose.

## Review checklist supplied with the pilot

1. Compare the entire text, including all nine Hebrew passages, against the scan. No reading has been intentionally left as an unmarked guess, but the AI scan check is fallible and needs independent review.
2. Approve the normalization of long s/English ss ligatures, heading case, print ornaments, and line-end hyphenation. Confirm that preserving the source's quotation punctuation is the desired reading-edition policy.
3. Review the printed spelling `misconstruktion` and date `[June 1705]`. They are transcribed as printed; this work has not investigated or endorsed their historical correctness. Any correction/commentary must be separately identified and sourced.
4. Confirm the publication metadata against the volume's title/contents pages if a full volume is available. The existing bibliography is the current source for volume and year.

## Human review and release decision

Technical QA passed for the completed draft: normal builds preserve 18 HTML pages, 601 internal links, and 209 PDF URLs; preview builds contain 20 pages and pass 655 internal-link checks under both `/leonroth/` and the custom-domain root shape. Five page markers point to PDF pages 1–5, and all nine Hebrew spans have RTL direction. Desktop and 390px mobile rendering were inspected. Normal output matches the preceding architecture build byte for byte except for the generated feed timestamp. Temporary-fixture tests confirm omission of drafts from simulated release HTML, index, and sitemap; metadata validation rejects publication of unverified work.

| Field | Value |
| --- | --- |
| Reviewer | Project owner, through the current Codex task |
| Review date | September 9, 2026 |
| Exact content commit reviewed | `8d7853a73b86224c1e8bea1b3911d6b2cd2bf954` |
| Review outcome | Pilot accepted; no textual amendments requested |
| Editorial policy approved | Version 1 accepted for continued pilot work |
| Publication approved | No |

Approval evidence: the project owner wrote, “OK I reviewed the review, the david nieto piece, and the editorial standard. good job. keep going.” The revision above was the feature branch/PR head presented for that review. The body hash is unchanged by the subsequent approval metadata update.

The user did not describe their comparison method or claim an independent line-by-line collation, Hebrew proficiency, or external verification of the volume's title page. None of those claims is inferred here. The source/date observations above remain part of the edition's provenance. `verified` records the owner's acceptance of this pilot under the workflow; `published: false` remains in force. A future substantive text change needs renewed review.
