# Leon Roth digitization plan

Working editorial standard, version 1 — September 9, 2026.

## Scope and first milestone

Create faithful, readable HTML editions while preserving the scans, bibliography citations, and public PDF addresses. First complete the David Nieto pilot, review the editorial choices, then test an English work with footnotes and a short Hebrew work before scheduling larger batches. Only the David Nieto pilot is being transcribed in this PR.

The initial bibliography inventory has 76 top-level English entries and 41 Hebrew entries. Of these, 67 English and 31 Hebrew entries already have local document links; the other 19 need source matching before assuming a scan is missing. These are bibliography-entry counts, not unique-work counts: reviews, multipart essays, and editions need reconciliation. The site's 209 preserved PDF URLs also include books and other resources, so that number is not the transcription backlog.

## Production boundaries

- Development happens on feature branches and draft PRs. No merge or deployment is authorized by this plan.
- `_works/` is registered only in `_config.works-preview.yml`. Normal production builds still omit the archive.
- `_config.yml` supplies `published: false` as the default for works. Local preview explicitly enables `unpublished: true`; production must never inherit that preview setting.
- The index shows drafts only when `works_preview: true`. Otherwise it requires both `published: true` and `digitization_status: verified`.
- Metadata validation rejects publication of an unverified work. The PR-only archive workflow tests default, preview, and simulated release behavior without Pages deployment permissions.
- GitHub source is public even when the Pages edition is unpublished. Do not put confidential notes or unpublished third-party material in the public branch.

## Work inventory and prioritization

Maintain one record per work in `_docs/digitization-catalog.yml`. Start with the three pilot candidates. Expand the catalog by matching the existing bibliographies and `migration/assets.json`; do not rewrite the bibliographies during inventory work.

For each record retain a stable ID, title, language, bibliographic year, bibliography route, current PDF path(s), local original filename where available, scan page count, printed page range, extraction method, editorial status, reviewer, open issues, and priority rationale. Record uncertainty instead of inferring missing dates or page ranges from filenames. Separate multiple editions; group genuinely multipart essays under one work with ordered source parts.

Prioritize short, complete, legible, important works for which a reviewer is available. After the pilots, process batches of three to five works. Keep long books for a later phase, once chapter navigation, source pagination, and the review process have proved themselves on essays. Do not produce large queues of unreviewed OCR.

## Editorial standard

| Element | Rule |
| --- | --- |
| Wording and spelling | Preserve the printed text, including historical spelling. Do not improve phrasing or silently correct apparent author/printer errors. |
| Typography | Normalize long s (`ſ`) and English historical ss ligatures to `s`/`ss`; retain original words. Use semantic headings rather than reproducing all capitals/small capitals. |
| Line endings | Reflow printed lines into paragraphs and join words split only by line endings. Preserve meaningful compound hyphens. Record ambiguous joins. |
| Punctuation | Preserve punctuation and quotation scope. Normalize typographic glyphs/spacing consistently without repairing unmatched quotation marks silently. |
| Paragraphs | Follow the source. Do not create a new paragraph at a page boundary inside a sentence. |
| Page boundaries | Use `work-page.html` markers at the actual boundary; map printed page numbers to physical PDF pages. Keep stable `page-278`-style anchors. |
| Headings and ornaments | The layout supplies the title. Start substantive sections at `##`. A print ornament can become a horizontal rule; record the change. |
| Emphasis | Preserve meaningful italics and bold. Small-cap headings/signatures may become normal case; do not invent italics for book titles when the source does not use them. |
| Footnotes | Preserve every note, its attachment point, and order. Use stable Markdown labels such as `[^p12-1]` when numbering restarts by page. Check note text and return links. |
| Source brackets | Retain the author's/translator's bracketed explanations as source text. Do not use identical unlabelled brackets for new editorial commentary. |
| Illegibility | Use an explicitly labelled editorial marker, such as `[Editorial: illegible word]`, and record the location. Never reconstruct missing words from context without marking an editorial proposal. |
| Hebrew | Transcribe the actual letters, punctuation, vowel points, and final forms visible in the source. Do not transliterate, modernize spelling, or silently remove diacritics. |
| Mixed languages | Mark embedded text with `lang` and `dir`, for example `<span lang="he" dir="rtl">טבע</span>`. Review numbers and punctuation visually. |
| Editorial notes | Keep new commentary outside the transcription, labelled as editorial. Historical/source-critical corrections need their own supporting evidence; transcription checks alone do not establish historical accuracy. |

These are the policy choices used in the pilot. The Foundation's editor should approve or revise them before they become the standard for a larger batch.

## Per-work procedure

1. **Identify the source.** Match title and opening/closing text, verify scan completeness and printed pagination, and check the bibliography against the scan. Compare the original download with the web PDF. Record hashes; never overwrite the scan.
2. **Assess extraction.** Run `pdfinfo` and `pdftotext -layout`. Check representative passages visually. If the text layer is unusable, benchmark available OCR tools on the same English/Hebrew sample pages before choosing one. Avoid rerunning OCR just because a text layer exists or assuming an existing layer is accurate.
3. **Prepare the first draft.** Use extraction as a proposal, correct it against page images, and structure the text in Markdown. Tag Hebrew spans, add page markers, and preserve source emphasis and quotation boundaries. Retain raw extraction in a local temporary directory; commit only the edition, provenance, and review notes.
4. **Check every page.** Compare the complete page against the draft, including the final words and first words across each page break. Separately check proper names, dates, numerals, quotations, Hebrew, and notes. Record each checked page and unresolved reading; do not substitute an OCR confidence score for this review.
5. **Render and inspect.** Build under both supported base paths. Check desktop and mobile; test page links, note/backlink navigation, RTL, and mixed-script punctuation. Run the existing route/PDF/link checker and the publication checks.
6. **Editorial review.** A named reviewer compares the full edition against the source and closes outstanding textual issues. Hebrew works or Hebrew quotations require a proficient Hebrew reader. Record reviewer, date, and the exact content commit reviewed. Substantive later changes require renewed review.
7. **Approve for release.** Set `digitization_status: verified` only after editorial review. Leave `published: false` until a separate release decision. Publication needs both flags, the review record, and successful checks.

## Status and review records

| Status | Meaning | Public eligibility |
| --- | --- | --- |
| `forthcoming` | Metadata only | No |
| `in_progress` | Extraction/correction underway | No |
| `scan_checked` | Complete draft checked against the scan; identify who or what checked it | No |
| `verified` | Named editorial reviewer has approved the text and recorded the reviewed revision | Only with an explicit `published: true` |

For each pilot create `_docs/pilots/<work-id>-review.md`: source hashes, extraction method, checks by page, corrections/normalizations, outstanding questions, and a human review section. An AI scan check must be attributed to the AI; it does not constitute an independent human review. David Nieto currently has `scan_checked` status and remains unpublished.

For a verified work, front matter must also contain `reviewed_by`, `reviewed_on` (quoted ISO date), `reviewed_revision` (the full content commit SHA), and `review_record` (a repository-relative path to the review record). The reviewer approves the transcription at that revision; the subsequent metadata-only approval commit records it. Use `translator` separately from `author` where relevant.

## Pilot sequence and acceptance criteria

| Pilot | Purpose | Next action |
| --- | --- | --- |
| David Nieto (1921), 5 scan pages, printed pp. 278–282 | Long-s normalization, unreliable embedded OCR, Hebrew inside English, source pagination, translated letter | Review the completed scan-checked draft and this editorial standard |
| Note on the Relationship between Locke and Descartes (bibliography: 1935), 3 scan pages | Short English comparison case; inspect notes/citations and source metadata before selection | Inspect the scan; its original filename says 1937, so verify the discrepancy rather than copying the filename |
| Yovel Spinoza (1932), 2 scan pages | Hebrew layout and extraction/review workflow | Inspect completeness, columns, and typography; arrange a proficient Hebrew reviewer before transcription |

The latter two are candidates only. If the English candidate lacks representative footnotes, choose another short footnoted essay after inspection. Do not treat these titles as reviewed or create public placeholders for them.

The pilot succeeds when every printed page has a matching transcription segment, all notes and quoted languages are checked, remaining uncertainties are explicit, the editor has approved the policy, and publication exclusion has passed. The first work can be technically complete while editorial sign-off remains pending; report those separately.

## Tooling and estimating the backlog

The first pilot used Poppler's existing-text extraction plus visual comparison of 250 dpi page renders and enlarged crops. Its OCR layer repeatedly confused long s with f, lost Hebrew, and misread centuries. Local Tesseract could not start because its linked `libarchive.13.dylib` was unavailable. No system installation was changed to fix it; selecting or repairing a general OCR tool belongs to the next extraction benchmark. Do not infer comparative OCR accuracy from this single pilot.

For the next pilots, log active minutes separately for source preparation, extraction, text correction, script-specific review, and layout checks. Record corrected errors in a manually checked sample of equal size for each method, separating character errors, missing text, reading order, and note attachment. A second OCR tool may help locate disagreements, but agreement is not proof of correctness. Record tool/model version and settings; do not replace stable outputs by rerunning a different version without review.

Estimate remaining effort only after these pilots. Group works by language and complexity, then multiply observed correction/review time per page by the pages in that group and add source matching and final QA. Set throughput according to reviewer availability. No archive-wide completion date or unsupported accuracy percentage is promised here.

## Validation commands

```sh
BUNDLE_PATH=vendor/bundle bundle exec ruby tools/check_works.rb
BUNDLE_PATH=vendor/bundle bundle exec ruby tools/test_works_publication.rb
BUNDLE_PATH=vendor/bundle bundle exec jekyll build
python3 tools/check_site.py
BUNDLE_PATH=vendor/bundle bundle exec jekyll build --config _config.yml,_config.works-preview.yml --destination _site_test
python3 tools/check_site.py --site _site_test
```

The publication test uses temporary fixtures outside `_works/`. It verifies omitted flags default to unpublished, drafts appear in an explicit preview only, and a simulated release exposes only the explicitly published verified fixture in HTML, index, and sitemap. The new archive workflow runs these checks on PRs without deployment permissions.

## First public release, later and separately authorized

Choose a small set of verified editions. Register the collection in production; promote the index and stylesheet out of `_preview/`; remove preview notices and noindex only for eligible pages; enable sitemap entries for those pages. Keep `unpublished: false`, retain the per-work default, and incorporate the metadata/publication checks into the release build.

Update only the selected bibliography entries: link the title to the approved HTML edition and add a PDF link beside it. Everything else keeps its existing PDF or unlinked citation. Inspect all changed links and the normal production build before merging. Keep a record of the release commit; rollback by reverting the release change, which leaves the existing PDFs and bibliography routes intact. DNS/domain changes are unnecessary.
