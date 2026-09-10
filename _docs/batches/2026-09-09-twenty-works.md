# Twenty-work batch: September 9, 2026

The owner requested another twenty works and correction of Hebrew quotation typography. This batch adds nineteen English works and one Hebrew memorial essay, bringing the archive to thirty-six works (thirty-two English, four Hebrew). All twenty additions are `scan_checked` and `published: false`, pending human editorial review. Boloney has two explicitly marked unreadable words; those must be resolved from a clearer source before publication. David Nieto remains the only editorially accepted work, also unpublished.

No inline editorial page numbers are added. Printed citation ranges, source section numbers, and original notes remain. New pages appear only with the explicit archive preview configuration.

## Review queue

Each record identifies both PDF files and hashes, the exact Markdown body hash, page-by-page scope, editorial choices, and pending human acceptance. Reading links require the local server on port 4000.

| Work | Year | Reading page | Source record |
| --- | --- | --- | --- |
| The Jerusalem University: Some Personal Notes | 1930 | [Read](http://127.0.0.1:4000/leonroth/works/jerusalem-university/) | [Review record](../pilots/jerusalem-university-review.md) |
| Henri Bergson, In Memoriam | 1941 | [Read](http://127.0.0.1:4000/leonroth/works/henri-bergson-memoriam/) | [Review record](../pilots/henri-bergson-memoriam-review.md) |
| Ambassadors of English | 1942 | [Read](http://127.0.0.1:4000/leonroth/works/ambassadors-english/) | [Review record](../pilots/ambassadors-english-review.md) |
| I.A. and the Hebrew University | 1949 | [Read](http://127.0.0.1:4000/leonroth/works/abrahams-hebrew-university/) | [Review record](../pilots/abrahams-hebrew-university-review.md) |
| Judah L. Magnes and the Hebrew University | 1949 | [Read](http://127.0.0.1:4000/leonroth/works/magnes-hebrew-university/) | [Review record](../pilots/magnes-hebrew-university-review.md) |
| The General Humanities | 1950 | [Read](http://127.0.0.1:4000/leonroth/works/general-humanities/) | [Review record](../pilots/general-humanities-review.md) |
| Boloney | 1951 | [Read](http://127.0.0.1:4000/leonroth/works/boloney/) | [Review record](../pilots/boloney-review.md) |
| Right Is Might | 1953 | [Read](http://127.0.0.1:4000/leonroth/works/qibya-letter/) | [Review record](../pilots/qibya-letter-review.md) |
| Achad Ha’am’s Moral Outlook (April 16 letter) | 1954 | [Read](http://127.0.0.1:4000/leonroth/works/ahad-haam-letter-april-16/) | [Review record](../pilots/ahad-haam-letter-april-16-review.md) |
| Achad Ha’am’s Moral Outlook (April 30 letter) | 1954 | [Read](http://127.0.0.1:4000/leonroth/works/ahad-haam-letter-april-30/) | [Review record](../pilots/ahad-haam-letter-april-30-review.md) |
| St George for England | 1954 | [Read](http://127.0.0.1:4000/leonroth/works/st-george-england/) | [Review record](../pilots/st-george-england-review.md) |
| Biography of Judah Magnes | 1955 | [Read](http://127.0.0.1:4000/leonroth/works/magnes-letter/) | [Review record](../pilots/magnes-letter-review.md) |
| The ‘Cherem’ on Spinoza | 1956 | [Read](http://127.0.0.1:4000/leonroth/works/cherem-spinoza/) | [Review record](../pilots/cherem-spinoza-review.md) |
| Rembrandt and Spinoza | 1957 | [Read](http://127.0.0.1:4000/leonroth/works/rembrandt-spinoza-review/) | [Review record](../pilots/rembrandt-spinoza-review.md) |
| Message of the Bible | 1959 | [Read](http://127.0.0.1:4000/leonroth/works/message-bible-review/) | [Review record](../pilots/message-bible-review.md) |
| The Resurgence of Hebrew | 1959 | [Read](http://127.0.0.1:4000/leonroth/works/resurgence-hebrew/) | [Review record](../pilots/resurgence-hebrew-review.md) |
| Tradition and Change | 1959 | [Read](http://127.0.0.1:4000/leonroth/works/tradition-change-review/) | [Review record](../pilots/tradition-change-review.md) |
| Authority, Religion and Law | 1960 | [Read](http://127.0.0.1:4000/leonroth/works/authority-religion-law/) | [Review record](../pilots/authority-religion-law-review.md) |
| Bridging a Gap | 1960 | [Read](http://127.0.0.1:4000/leonroth/works/jewish-values-review/) | [Review record](../pilots/jewish-values-review.md) |
| The Jewish Faith | 1961 | [Read](http://127.0.0.1:4000/leonroth/works/religion-israel-review/) | [Review record](../pilots/religion-israel-review.md) |

## Source and editorial findings

- All 57 PDF page images in the twenty original/public pairs match pixel-for-pixel at 170 dpi. Every article page was read visually, with enlarged crops where needed. No PDF was changed. Text layers or local Apple Vision OCR supplied proposals, not authoritative transcriptions.
- Shared newspaper/journal pages include neighboring material. Each record specifies the article boundaries and exclusions; cover and contents pages are identified separately.
- Boloney’s Medusa passage has two unreadable words on PDF page 3. Explicit editorial markers preserve these gaps. Five other candidates were deferred for heavier fading, blots, or binding loss: In His Image, Sacred Books of the World, Aspects of Italian Jewry, Twenty Five Years, and Ambassador. These catalog entries create no reading pages.
- The scans correct filename dates for The Jewish Faith (June 2, 1961) and The ‘Cherem’ on Spinoza (July 27, 1956). St George for England is Desiderata 7, number 2, not number 12. I.A. and the Hebrew University concludes on page 22. Existing bibliography entries remain unchanged.
- The two Achad Ha’am letters have date qualifiers in their reading-page titles. Authority, Religion and Law retains the source’s section-number jump from 3 to 5. Title-asterisk note relocations are recorded for the Bergson, Authority, and Resurgence essays.
- Historical claims, spellings, and printer errors are retained. Book-level metadata for The General Humanities follows the Foundation bibliography and still needs comparison with the full volume. Attribution of the two A.B.F.-signed reviews follows that bibliography.

## Hebrew quotation correction

English curly quotation marks have fixed shapes: RTL does not mirror their glyphs. Kramdown was therefore producing inappropriate English-style pairs in Hebrew prose. The two affected existing transcriptions now encode symmetric double quotes as `&quot;`, which survive smart punctuation as ordinary straight quotes. Hebrew abbreviation marks remain ׳ and ״, strings stay in logical order, and no invisible direction overrides are added. The new Bergson essay follows the same convention. English text keeps its existing quotation conventions.

See [W3C Hebrew Layout Requirements, quotations](https://www.w3.org/International/hlreq/#quotations). The two affected source records have updated body hashes and document this presentation amendment. It does not confer editorial acceptance. A proficient Hebrew reader should review the new memorial essay, including the pointed title, names, and source note.

## Technical validation

- Metadata validation passes for all 36 works. Publication fixture tests pass normal omission, explicit draft preview, approved-only release, index/sitemap exclusion, and rejection of invalid release metadata.
- Both preview base paths (`/leonroth/` and the custom-domain root shape) pass: 55 HTML pages, all 17 original routes, 1,623 internal-link checks, and 209 preserved PDF URLs. The index lists 36 works.
- The normal build passes with 18 HTML pages and 601 internal-link checks. All 253 output files match the preceding batch’s normal build byte-for-byte except the generated feed timestamp. No works route, archive stylesheet, or archive sitemap entry leaks into normal output.
- All 36 pages pass browser overflow checks at 320px and 390px. Four Hebrew articles use RTL and 32 English articles use LTR. Visual checks cover Hebrew symmetric quotes in the existing review and new Bergson essay, its 15px footnote and working return link, desktop English dialogue/quotation layout at 19px, an English source note and return link, and Boloney’s two visible gap markers. Temporary viewport overrides were reset.
- All 36 current body hashes match their review records. The two earlier Hebrew body changes consist only of quote-glyph encoding; the other fourteen earlier editions are unchanged.
- Builds have no Jekyll errors; existing Minimal Mistakes Sass deprecation warnings remain. No layout, stylesheet, configuration, or workflow needed modification.

## Files in this batch

Twenty work files and twenty corresponding source records are added (one pair for each row above). The two existing Hebrew work files and their records are modified for quotation typography. README, the catalog, editorial plan, architecture notes, and this guide record the new batch. No layout, CSS, configuration, workflow, bibliography, or PDF changes are part of this batch. Unrelated concurrent migration/PDF edits are excluded from its commit.

Complete path list (41 added, 8 modified):

```text
README.md
_docs/batches/2026-09-09-twenty-works.md
_docs/digitization-catalog.yml
_docs/digitization-plan.md
_docs/digitized-works.md
_docs/pilots/abrahams-hebrew-university-review.md
_docs/pilots/ahad-haam-letter-april-16-review.md
_docs/pilots/ahad-haam-letter-april-30-review.md
_docs/pilots/ambassadors-english-review.md
_docs/pilots/authority-religion-law-review.md
_docs/pilots/boloney-review.md
_docs/pilots/cherem-spinoza-review.md
_docs/pilots/freedom-government-introduction-review.md
_docs/pilots/general-humanities-review.md
_docs/pilots/henri-bergson-memoriam-review.md
_docs/pilots/jerusalem-university-review.md
_docs/pilots/jewish-values-review.md
_docs/pilots/magnes-hebrew-university-review.md
_docs/pilots/magnes-letter-review.md
_docs/pilots/message-bible-review.md
_docs/pilots/qibya-letter-review.md
_docs/pilots/religion-israel-review.md
_docs/pilots/rembrandt-spinoza-review.md
_docs/pilots/resurgence-hebrew-review.md
_docs/pilots/righteousness-israel-review.md
_docs/pilots/st-george-england-review.md
_docs/pilots/tradition-change-review.md
_works/1930-jerusalem-university.md
_works/1941-henri-bergson-memoriam.md
_works/1942-ambassadors-english.md
_works/1944-righteousness-israel.md
_works/1945-freedom-government-introduction.md
_works/1949-abrahams-hebrew-university.md
_works/1949-magnes-hebrew-university.md
_works/1950-general-humanities.md
_works/1951-boloney.md
_works/1953-qibya-letter.md
_works/1954-ahad-haam-letter-april-16.md
_works/1954-ahad-haam-letter-april-30.md
_works/1954-st-george-england.md
_works/1955-magnes-letter.md
_works/1956-cherem-spinoza.md
_works/1957-rembrandt-spinoza-review.md
_works/1959-message-bible-review.md
_works/1959-resurgence-hebrew.md
_works/1959-tradition-change-review.md
_works/1960-authority-religion-law.md
_works/1960-jewish-values-review.md
_works/1961-religion-israel-review.md
```
