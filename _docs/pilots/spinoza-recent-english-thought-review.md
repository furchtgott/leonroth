# Spinoza in Recent English Thought: source and review record

Work: Leon Roth, “Spinoza in Recent English Thought,” *Mind* 36, no. 142 (1927), pp. 205–210. Volume, issue, and year follow the existing bibliography; the scan verifies the article title, signature, and continuous pagination. Its opening note dates the Hague lecture to February 1927. The scan does not include the journal issue's cover or contents page.

Current state: **scan_checked; published: false**. Codex prepared the transcription and compared it with all six scan pages on September 9, 2026. Human editorial review remains pending.

## Sources and reproduction

| Source | Identifier |
| --- | --- |
| Original local download | `Site Files/Spinoza in Recent English Thought Mind-1927-ROTH-205-10.pdf` (305,221 bytes) |
| Original SHA-256 | `2e1cbd942e6defe2e61a15617c6c53a048228ff5da104397641f75349878e10c` |
| Retained public scan | `/_files/ugd/01b672_e13163d3dffb4a108f6b88199f32cff7.pdf` (295,295 bytes) |
| Public scan SHA-256 | `9f8321a8d73adad2a228e6cf2bd974ecd2adb91240ec5d4d9a9dd2129c404129` |
| Edition source | `_works/1927-spinoza-recent-english-thought.md` |
| Checked Markdown body SHA-256 | `79852810e7b60d1a39369ebba17550657c3c124be10f2a7839ad7f58a446c716` (UTF-8 body after front matter, leading blank lines removed) |
| Reader URL | `/works/spinoza-recent-english-thought/` (preview only) |

The original and public PDFs render pixel-identically on all six pages at 180 dpi. No PDF was changed. Poppler's embedded-text extraction yielded 17,867 characters, including running heads and repeated download stamps. It supplied a draft, not authoritative text. All page images were read; enlarged crops clarified the mark over “interpretation” on p. 206 and the last footnote on p. 210.

```sh
mkdir -p /tmp/leonroth-digitization/recent-english-thought
pdftotext -layout '_files/ugd/01b672_e13163d3dffb4a108f6b88199f32cff7.pdf' /tmp/leonroth-digitization/recent-english-thought/source-text.txt
pdftoppm -r 180 -png '_files/ugd/01b672_e13163d3dffb4a108f6b88199f32cff7.pdf' /tmp/leonroth-digitization/recent-english-thought/page
```

## Page checks

| Printed / PDF page | Checks |
| --- | --- |
| 205 / 1 | Title; opening note; three introductory paragraphs; italic book titles; § 1 and its unfinished paragraph. Corrected OCR `REGENT`, `oast`, and `faotcrs` to the visible print. |
| 206 / 2 | Joined the paragraph from p. 205; printed “not of interpretation” retained despite a handwritten stroke across it; Hegel quotation, rationality/system argument, italics, and final sentence checked. OCR's `nationality` is printed `Rationality`. |
| 207 / 3 | Continued “precisely that levelled”; § 2; Bradley titles and quotation punctuation; German title/accent and Roman numeral in the note. |
| 208 / 4 | Two opening paragraphs; § 3; `Höffding`; note year **1915**, where OCR said 1916; paragraph continuing on p. 209. |
| 209 / 5 | Italic `Idealists` and `Realists`; § 4; all three note attachment points and texts; `I, 6` in the first note; quotation continuing to p. 210. |
| 210 / 6 | Completed Bradley quotation; § 5; Latin quotation; italic titles and `used`; `VITAE` and `HOMO LIBER`; final note and Roth signature. The unusual printed phrase `a barre's length` is retained. |

The six page markers map printed 205–210 to PDF 1–6. Markers at 206, 207, 209, and 210 fall inside continuing paragraphs. No paragraph break was added there. The initial journal rubric “IV.—DISCUSSIONS.” and running heads are not part of the essay's five section headings and are omitted.

## Footnote map

The source restarts numbering by page. Kramdown renders one continuous, linked sequence in reading order. Stable labels preserve the original page and number; all seven source notes are included. This presentation choice should be reviewed with the new pilot.

| HTML number | Markdown label | Printed page / note | Attachment |
| --- | --- | --- | --- |
| 1 | `p205-1` | 205 / 1 | “a great thinker” |
| 2 | `p207-1` | 207 / 1 | “as Hegel explained it himself,” |
| 3 | `p208-1` | 208 / 1 | “Höffding” |
| 4 | `p209-1` | 209 / 1 | “a democracy of things”. |
| 5 | `p209-2` | 209 / 2 | “no unity of the universe”, |
| 6 | `p209-3` | 209 / 3 | “his own philosophy would result.” |
| 7 | `p210-1` | 210 / 1 | “Ne judicate, ne judicemini,” |

## Editorial transformations and remaining review

- Reflowed print lines, joined line-end word divisions, normalized quotation glyphs and spacing, and changed title/signature casing as allowed by the accepted standard. Preserved British spelling, unusual phrasing, italics, and punctuation scope, including the nested single quotes in the Bradley quotation and the missing full stop after `Prof` on p. 209.
- Tagged the Latin quotation and terms and the German note title for language/direction. Retained `Ethics` in roman type where printed that way; did not invent italic book titles.
- Excluded publisher download stamps and handwritten marginal/stroke marks from the transcription. The original PDF still contains them.
- Preserved rather than interpreted the final note's `barre's length`. Its meaning and the correctness of historical claims/references have not been researched as part of transcription.
- Before acceptance, compare all prose and seven notes against the scan, paying particular attention to accents, the source's quotation punctuation, note numbering/presentation, the 1915 reference, and the final unusual phrase. Verify volume/issue against a full journal issue if available. No known unreadable word has been filled by an unlabelled reconstruction; the AI comparison can still contain errors.

## Human review and release decision

Technical validation: the preview passes the repository's route/link/PDF checks at both `/leonroth/` and the domain-root base path. Browser checks found seven notes and seven backlinks, with note text at 15px. The first note and its return link were clicked successfully. Desktop rendering and 390px/320px mobile widths were checked without horizontal overflow. A text-layer/rendered-text comparison found the documented OCR corrections and intentional running-head/note relocation, with no unexplained missing prose. These are technical/AI checks, not human editorial acceptance.

| Field | Value |
| --- | --- |
| Reviewer / date | Pending |
| Exact content commit reviewed | Pending |
| Text and note presentation accepted | Pending |
| Publication approved | No |

After review, record the reviewer, date, and exact content commit before moving to `verified`. Keep `published: false` until a separate release decision. The new pilot does not inherit the owner's approval of David Nieto.
