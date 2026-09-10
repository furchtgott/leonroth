# Leon Roth digitization plan

Editorial standard, version 1 — accepted by the project owner on September 9, 2026, then amended at their request to omit inline editorial page numbers. New work-specific presentation choices remain subject to their own review.

## Scope and first milestone

Create faithful, readable HTML editions while preserving the scans, bibliography citations, and public PDF addresses. The project owner has reviewed and accepted the David Nieto pilot, its review record, and this editorial standard. The archive now contains thirty-six transcriptions (two unreadable words are explicitly marked in Boloney): David Nieto is accepted, and thirty-five works await their own editorial review. The latest owner-requested batch adds twenty works and fixes Hebrew quotation typography; see [the twenty-work review guide](batches/2026-09-09-twenty-works.md). All thirty-six remain unpublished and reading pages omit inline editorial page markers.

The initial bibliography inventory has 76 top-level English entries and 41 Hebrew entries. Of these, 67 English and 31 Hebrew entries already have local document links; the other 19 need source matching before assuming a scan is missing. These are bibliography-entry counts, not unique-work counts: reviews, multipart essays, and editions need reconciliation. The site's 209 preserved PDF URLs also include books and other resources, so that number is not the transcription backlog.

## Production boundaries

- Development happens on feature branches and draft PRs. No merge or deployment is authorized by this plan.
- `_works/` is registered only in `_config.works-preview.yml`. Normal production builds still omit the archive.
- `_config.yml` supplies `published: false` as the default for works. Local preview explicitly enables `unpublished: true`; production must never inherit that preview setting.
- The index shows drafts only when `works_preview: true`. Otherwise it requires both `published: true` and `digitization_status: verified`.
- Metadata validation rejects publication of an unverified work. The PR-only archive workflow tests default, preview, and simulated release behavior without Pages deployment permissions.
- GitHub source is public even when the Pages edition is unpublished. Do not put confidential notes or unpublished third-party material in the public branch.

## Work inventory and prioritization

Maintain one record per work in `_docs/digitization-catalog.yml`. The seed catalog currently records thirty-six transcribed works and eight deferred candidates. Expand it by matching the existing bibliographies and `migration/assets.json`; do not rewrite the bibliographies during inventory work. Catalog-only states such as `candidate` or `deferred_source_review` do not create pages and are separate from the four work front-matter statuses.

For each record retain a stable ID, title, language, bibliographic year, bibliography route, current PDF path(s), local original filename where available, scan page count, printed page range, extraction method, editorial status, reviewer, open issues, and priority rationale. Record uncertainty instead of inferring missing dates or page ranges from filenames. Separate multiple editions; group genuinely multipart essays under one work with ordered source parts.

Prioritize short, complete, legible, important works for which a reviewer is available. Ordinarily process batches of three to five works; the owner explicitly requested twenty in the latest batch. Keep long books for a later phase, once chapter navigation and the review process have proved themselves on essays. Do not produce large queues of unreviewed OCR.

## Editorial standard

| Element | Rule |
| --- | --- |
| Wording and spelling | Preserve the printed text, including historical spelling. Do not improve phrasing or silently correct apparent author/printer errors. |
| Typography | Normalize long s (`ſ`) and English historical ss ligatures to `s`/`ss`; retain original words. Use semantic headings rather than reproducing all capitals/small capitals. |
| Line endings | Reflow printed lines into paragraphs and join words split only by line endings. Preserve meaningful compound hyphens. Record ambiguous joins. |
| Punctuation | Preserve punctuation and quotation scope. Normalize typographic glyphs/spacing consistently without repairing unmatched quotation marks silently. |
| Paragraphs | Follow the source. Do not create a new paragraph at a page boundary inside a sentence. |
| Page boundaries | Do not insert editorial page numbers or page-break markers in the Markdown body. Reflow continuously across print pages while preserving paragraphs. Keep the publication page range in metadata and source-page checks in the internal review record. |
| Headings and ornaments | The layout supplies the title. Start substantive sections at `##`. A print ornament can become a horizontal rule; record the change. |
| Emphasis | Preserve meaningful italics and bold. Small-cap headings/signatures may become normal case; do not invent italics for book titles when the source does not use them. |
| Footnotes | Preserve every note, its attachment point, and order. Use stable Markdown labels such as `[^p12-1]` when numbering restarts by page. Check note text and return links. |
| Source brackets | Retain the author's/translator's bracketed explanations as source text. Do not use identical unlabelled brackets for new editorial commentary. |
| Illegibility | Use an explicitly labelled editorial marker, such as `[Editorial: illegible word]`, and record the location. Never reconstruct missing words from context without marking an editorial proposal. |
| Hebrew | Transcribe the actual letters, punctuation, vowel points, and final forms visible in the source. Do not transliterate, modernize spelling, or silently remove diacritics. |
| Mixed languages | Mark embedded text with `lang` and `dir`, for example `<span lang="he" dir="rtl">טבע</span>`. Review numbers and punctuation visually. |
| Editorial notes | Keep new commentary outside the transcription, labelled as editorial. Historical/source-critical corrections need their own supporting evidence; transcription checks alone do not establish historical accuracy. |

The project owner accepted these policy choices after reviewing the David Nieto pilot. The new English pilot proposes collecting source footnotes at the end with continuous HTML numbering and a source-page/number map in its review record. The new Hebrew pilot normalizes quotation/abbreviation glyphs while preserving spelling. Review these concrete applications before carrying them into a larger batch.

## Per-work procedure

1. **Identify the source.** Match title and opening/closing text, verify scan completeness and printed pagination, and check the bibliography against the scan. Compare the original download with the web PDF. Record hashes; never overwrite the scan.
2. **Assess extraction.** Run `pdfinfo` and `pdftotext -layout`. Check representative passages visually. If the text layer is unusable, benchmark available OCR tools on the same English/Hebrew sample pages before choosing one. Avoid rerunning OCR just because a text layer exists or assuming an existing layer is accurate.
3. **Prepare the first draft.** Use extraction as a proposal, correct it against page images, and structure the text in Markdown. Tag Hebrew spans and preserve source emphasis and quotation boundaries. Retain raw extraction in a local temporary directory; commit only the edition, provenance, and review notes.
4. **Check every page.** Compare the complete page against the draft, including the final words and first words across each page break. Separately check proper names, dates, numerals, quotations, Hebrew, and notes. Record each checked page and unresolved reading; do not substitute an OCR confidence score for this review.
5. **Render and inspect.** Build under both supported base paths. Check desktop and mobile; test original scan links and note/backlink navigation, RTL, and mixed-script punctuation. Run the existing route/PDF/link checker and the publication checks.
6. **Editorial review.** A named reviewer compares the full edition against the source and closes outstanding textual issues. Hebrew works or Hebrew quotations require a proficient Hebrew reader. Record reviewer, date, and the exact content commit reviewed. Substantive later changes require renewed review.
7. **Approve for release.** Set `digitization_status: verified` only after editorial review. Leave `published: false` until a separate release decision. Publication needs both flags, the review record, and successful checks.

## Status and review records

| Status | Meaning | Public eligibility |
| --- | --- | --- |
| `forthcoming` | Metadata only | No |
| `in_progress` | Extraction/correction underway | No |
| `scan_checked` | Complete draft checked against the scan; identify who or what checked it | No |
| `verified` | Named editorial reviewer has approved the text and recorded the reviewed revision | Only with an explicit `published: true` |

For each pilot create `_docs/pilots/<work-id>-review.md`: source hashes, extraction method, checks by page, corrections/normalizations, outstanding questions, and a human review section. An AI scan check must be attributed to the AI; it does not constitute an independent human review. David Nieto now has `verified` status following the owner's acceptance, with the scope of that review recorded precisely. The other thirty-five works remain `scan_checked`. All remain unpublished. Removing editorial page markers is an explicitly requested presentation change; it does not change Roth’s words or reset the acceptance of David Nieto.

For a verified work, front matter must also contain `reviewed_by`, `reviewed_on` (quoted ISO date), `reviewed_revision` (the full content commit SHA), and `review_record` (a repository-relative path to the review record). The reviewer approves the transcription at that revision; the subsequent metadata-only approval commit records it. Use `translator` separately from `author` where relevant.

## Pilot sequence and acceptance criteria

| Pilot | Purpose | Next action |
| --- | --- | --- |
| David Nieto (1921), 5 scan pages, printed pp. 278–282 | Long-s normalization, unreliable embedded OCR, Hebrew inside English, source pagination, translated letter | Accepted by the owner at revision `8d7853a73b86224c1e8bea1b3911d6b2cd2bf954`; retain unpublished status |
| Spinoza in Recent English Thought (1927), 6 scan pages, printed pp. 205–210 | Seven real notes, numbering restarted by source page, italics, German/Latin, paragraph joins | Review the completed scan-checked draft and source-note map |
| Introduction to Freedom and Government (1945), 2 text pages plus title page, printed ה–ו | Complete Hebrew prose, RTL, historical spelling, date/signature, original page labels | Proficient Hebrew reader to review the completed scan-checked draft |

The third batch now includes *Note on the Relationship between Locke and Descartes*, which has no footnotes. Its closing date says Jerusalem, May, 1935, supporting the bibliography's year despite the filename's 1937. Its ten numbered paragraphs and inline citations are retained as source text. *Yovel Spinoza* has dense newspaper columns, no text layer, and obscured words; defer it for source review. The other two additions are *Philosophical Classics in Hebrew: Building a Language* (1946), read from three page images, and the Hebrew review *צדק וצדקה בישראל* (1944), read from two shared journal pages. Their review records document the exact article boundaries so neighboring material is excluded. Neither bibliography was altered.

The pilot succeeds when every printed page has a matching transcription segment, all notes and quoted languages are checked, remaining uncertainties are explicit, the editor has approved the policy, and publication exclusion has passed. The first work can be technically complete while editorial sign-off remains pending; report those separately.

## Tooling and estimating the backlog

The first pilot used Poppler's existing-text extraction plus visual comparison of 250 dpi page renders and enlarged crops. Its OCR layer repeatedly confused long s with f, lost Hebrew, and misread centuries. The second English pilot also uses existing PDF text corrected visually; its OCR misread the year 1915 as 1916. The Hebrew introduction has no text layer and was manually read from two legible pages, with enlarged crops. Local Tesseract could not start because its linked `libarchive.13.dylib` was unavailable. No system installation was changed to fix it; selecting or repairing a general OCR tool belongs to the next extraction benchmark. These methods were not a controlled comparison and establish no OCR accuracy percentage.

For the next extraction benchmark, log active minutes separately for source preparation, extraction, text correction, script-specific review, and layout checks. The present pilots did not capture reliable active minutes per phase; do not use conversational wall time as editorial labor or a throughput estimate. Record corrected errors in a manually checked sample of equal size for each method, separating character errors, missing text, reading order, and note attachment. A second OCR tool may help locate disagreements, but agreement is not proof of correctness. Record tool/model version and settings; do not replace stable outputs by rerunning a different version without review.

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

### Hebrew quotation typography (September 9, 2026)

Use symmetric straight double quotation marks in Hebrew prose; write `&quot;` in Markdown so Kramdown does not convert them to English curly quotes. The visible result is an ordinary quotation mark on each side, in logical Hebrew reading order. Retain geresh (׳) and gershayim (״) for Hebrew abbreviations, and retain English quotation conventions within explicitly English passages. Do not reverse strings or introduce invisible direction overrides. See [W3C Hebrew Layout Requirements, quotations](https://www.w3.org/International/hlreq/#quotations).
