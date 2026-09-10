# Digitized works: development architecture

## Production boundary

Inspected on September 9, 2026 before editing:

- Repository: `furchtgott/leonroth`; production branch: `main`, initially at `3ee31456eb674e731a8990a8a9b052af48808877`.
- GitHub Pages reports `build_type: workflow`, source `main` at `/`, and `https://www.leonroth.org/` as the live URL. This is an Actions deployment, not GitHub's branch-based Jekyll builder.
- `.github/workflows/pages.yml` builds pushes to `main`, pull requests, and manual dispatches. Pull requests only build and check. **Manual dispatch can deploy**, including when selecting another branch, so do not use it for staging.
- The workflow uses Ruby 4.0, Jekyll 4.4.1, Minimal Mistakes 4.28.1, and a temporary URL/base-path config from `actions/configure-pages`. Local layouts (`default`, `reading`, `foundation-home`), includes, and `assets/css/main.scss` provide the Foundation's design.
- This work is isolated on `feature/digitized-works`. The production workflow, navigation, bibliography, hosting settings, DNS, and original scans remain unchanged. Following approval of the roadmap, the branch was pushed and draft PR #1 opened; no merge or deployment is authorized. `_config.yml` now adds only a works-scoped `published: false` default, which does not register or publish the collection.

The collection is registered **only in `_config.works-preview.yml`**. Without that explicit config, Jekyll ignores `_works/` and `_preview/`. `_preview/` holds the index and its stylesheet, with explicit public permalinks for local inspection. `_docs/` also stays out of site output.

The preview explicitly sets `works_preview: true` and `unpublished: true`. These settings must stay out of production. Works default to unpublished even after a future production collection registration; the public index requires both `published: true` and `digitization_status: verified`. The metadata checker also requires a named editorial reviewer, review date, reviewed content commit, and review record for verified editions.

The shared head includes the extra stylesheet only for `work` and `works-index` layouts, preserving the rendered head of existing pages. New preview pages have `noindex, nofollow` and `sitemap: false`; those are discovery controls, not access controls. The normal build's omission of these pages is the publication boundary.

Merging this feature alone should not create or change a public URL or existing content. Publishing the archive later requires a separate, deliberate change to register the collection in production and promote the index and stylesheet out of `_preview/`. Review the preview labels, robots metadata, and sitemap flags at that time. Keep stable work permalinks and existing PDF paths.

## Content model

Each work is a Markdown document in `_works/`. The filename is for editorial organization; the explicit `permalink` is the stable reader-facing URL. The first six unpublished works are: David Nieto (1921), accepted by the project owner; Spinoza in Recent English Thought (1927); Note on the Relationship between Locke and Descartes (1935); the Hebrew review Justice and Charity in Israel (1944); the Hebrew introduction to Freedom and Government (1945); and Philosophical Classics in Hebrew: Building a Language (1946). Ten more were added in the previous batch, and [the latest twenty-work batch](batches/2026-09-09-twenty-works.md) brings the archive to thirty-six. The thirty-five works other than David Nieto remain scan-checked drafts awaiting their own editorial review. Each has a source/review record under `_docs/pilots/`. See [the plan](digitization-plan.md) for selection and next steps.

To add a work, copy the sample, choose a unique filename and permalink, and edit its front matter and Markdown body:

```yaml
---
layout: work
title: "Title of the work"
author: "Leon Roth"
year: 1932
publication: "Publication name"
volume: "4"
issue: "26"
pages: "3–7"
language: "Hebrew"
pdf: "/_files/ugd/existing-file.pdf"
permalink: "/works/unique-title/"
source_type: "Journal article"
digitization_status: "forthcoming"
published: false
sitemap: false
---
```

Replace the example PDF path with an existing file. Use `layout: work`, `title`, and a unique `permalink` for every work. Author falls back to Leon Roth. Other metadata may be omitted; absent or empty values do not produce labels or citation separators. The PDF button appears only when a PDF path exists. Internal links use `relative_url` for both the custom-domain root and `/leonroth/` previews.

`year` is an integer when known; omit unknown years. Keep volume, issue, and page ranges as quoted strings. Optional `editors`, `publisher`, `place`, `original_title`, `translated_title`, `translator`, `notes`, and `source_type` are plain text. Use a YAML list for `topics`. Notes appear in a separate editorial section; the layout escapes metadata. Rich prose belongs in the Markdown body.

Status values are `forthcoming`, `in_progress`, `scan_checked`, and `verified`. They describe editorial state; publication additionally requires an explicit `published: true`. Use `scan_checked` after a complete scan comparison and `verified` only after editorial acceptance, recorded with `reviewed_by`, `reviewed_on`, `reviewed_revision`, and `review_record`. State the actual review scope without inventing a comparison method or reviewer qualifications. David Nieto is `verified`; the other thirty-five are `scan_checked`; all thirty-six keep `published: false`.

The layout reuses the existing site shell, navigation, footer, reading-page classes, serif typography, and color variables. The extra CSS only targets archive components, with a narrower reading measure, mobile sizing, logical list/quote spacing, and footnotes.

Start essay sections at `##` because the layout supplies the title's `h1`. Normal Markdown headings, emphasis, blockquotes, and lists work. Kramdown footnotes use:

```markdown
A sentence with a note.[^1]

[^1]: The note, checked against the original scan.
```

Do not add editorial page numbers or page-break markers to the Markdown body. The owner requested continuous reading text. Keep the publication page range in `pages`, retain Roth’s own citations and numbered sections, and keep any scan-page mapping in the internal review record. The original scan remains linked at the top and bottom. The old page-marker include and CSS rule have been removed. Use decimal-only `pages: "5–6"` in the English citation; explain Hebrew source folios in review notes if useful.

## Hebrew and mixed text

`language: Hebrew` (also `he` or `עברית`) automatically sets the work's main reading region to `lang="he" dir="rtl"` and selects the Hebrew Essays return link. English/default works use `lang="en" dir="ltr"` and English Essays. You do not need to set page-wide direction for Hebrew.

The Foundation's existing English site navigation and metadata labels remain LTR. The title and transcription inherit the reading region's language and direction. Metadata values use `<bdi>` to isolate mixed Hebrew, English, and numbers. CSS logical properties place list indentation and blockquote borders on the correct side, including in footnotes. For an English phrase embedded in Hebrew prose, use `<span lang="en" dir="ltr">English phrase</span>` when needed. For works in other languages, review language tags and the return destination before adding them.

Use `&quot;` for symmetric double quotation marks in Hebrew Markdown. This preserves ordinary quotation marks through Kramdown’s English smart punctuation; keep geresh/gershayim for abbreviations. See the [quotation convention](digitization-plan.md#hebrew-quotation-typography-september-9-2026).

## Index and future bibliography integration

The index automatically lists `site.works`, filtered by publication eligibility outside an explicit preview; no duplicate public catalog data is needed. The separate `_docs/digitization-catalog.yml` tracks editorial candidates without creating pages. The index also displays an optional translated title, making a Hebrew heading such as `הקדמה` identifiable to English readers. It sorts by numeric year (undated items last), with title sorting as a tie-breaker. Change `sort_by` in `_preview/works/index.html` to `title` or `language` for those orders. Later, simple Liquid `group_by: 'language'` or `group_by: 'year'` can provide section headings. No JavaScript filtering is necessary.

The existing English and Hebrew bibliographies are Markdown lists, not structured data. Leave those lists and all PDF URLs as-is for now.

A later, incremental migration can introduce a bibliography entry include, with `title`, `pdf`, and optional `readable` (a work permalink). Resolve `readable` against `site.works` and require a verified transcription before changing the title's destination. For example, future entry data could be:

```yaml
title: "David Nieto and the Orthodoxy of Spinozism"
pdf: "/_files/ugd/01b672_c3b427c331294b0194fdc13ddab509d8.pdf"
readable: "/works/david-nieto/"
```

Proposed rendering logic, **not connected to the current bibliography**:

```liquid
{% assign edition = site.works | where: 'url', entry.readable | first %}
{% if edition and edition.published == true and edition.digitization_status == 'verified' %}
  <a href="{{ edition.url | relative_url }}">{{ entry.title | escape }}</a>
  <a href="{{ entry.pdf | relative_url }}">PDF</a>
{% elsif entry.pdf %}
  <a href="{{ entry.pdf | relative_url }}">{{ entry.title | escape }}</a>
{% else %}
  {{ entry.title | escape }}
{% endif %}
```

Check that the collection is output-enabled when implementing this. A missing, unpublished, or unverified edition must leave the PDF as the title link. A pilot's `published: false` flag must prevent bibliography redirection even after editorial acceptance. Start with one reviewed entry; preserve existing citations, order, unlinked works, and multipart PDF references. Do not derive slugs from titles at render time.

## Local validation

Use the installed Ruby 4.0 and the existing locked gems; no new dependency is required. Commands below use the local `vendor/bundle` cache. Omit `BUNDLE_PATH=vendor/bundle` if your bundle is installed elsewhere.

```sh
# Current site, with the archive excluded
BUNDLE_PATH=vendor/bundle bundle exec jekyll build
python3 tools/check_site.py

# Opt-in archive preview
BUNDLE_PATH=vendor/bundle bundle exec jekyll build --config _config.yml,_config.works-preview.yml --destination _site_test
python3 tools/check_site.py --site _site_test
BUNDLE_PATH=vendor/bundle bundle exec jekyll serve --config _config.yml,_config.works-preview.yml --destination _site_test --host 127.0.0.1
```

Visit `/leonroth/`, `/leonroth/essays-english/`, `/leonroth/essays-hebrew/`, and `/leonroth/works/` on `http://127.0.0.1:4000`, then open the thirty-six reading pages from the index. Follow each scan link. Check desktop and mobile widths, keyboard focus, the seven English notes/backlinks, the Hebrew review's note/backlink, the Brandon review's source-editor note/backlink, and Hebrew reading direction. Use temporary fixtures for structural elements absent from these works, such as Hebrew lists and block quotes. Do not commit QA fixtures as archive content.

For a custom-domain-shaped build, create an override **outside the repository** containing `url: "https://www.leonroth.org"` and `baseurl: ""`. Append it to the comma-separated config list, build to a temporary destination, then run `tools/check_site.py --site /your/temp/output --baseurl ''`. This only builds files locally; it changes no hosting settings.

Normal builds must have no `works/` output, no `assets/css/works.css`, and no work routes in the sitemap. Compare pre-feature and post-feature normal builds: HTML, navigation, bibliography links, PDFs, and CSS should match; the feed's build timestamp can vary. Existing Minimal Mistakes Sass deprecation warnings predate this feature.

The existing Pages pull-request workflow validates the normal production build without deployment. A separate `works-check.yml` PR workflow now checks editorial metadata, publication boundaries, and both normal and opt-in preview builds. It has only `contents: read` permission and no deployment steps. No hosted preview or production deployment setting was added or changed.

### Initial architecture validation performed on September 9, 2026 (historical)

- Normal builds: 18 HTML pages, all 17 original routes, 601 internal links, and 209 PDF URLs passed the existing checker.
- Preview builds under both `/leonroth/` and a custom-domain-shaped empty base path: 20 HTML pages and 650 internal links passed, with all original routes and PDFs preserved. No Jekyll errors; only existing theme/dependency warnings.
- Built an isolated snapshot of the initial production commit, then applied only this feature's ten files and rebuilt with the custom-domain configuration. All 253 output paths were preserved, with no additions. Every file was byte-identical except `feed.xml`'s generated `<updated>` timestamp; normalizing only that timestamp made it identical too. No works pages, stylesheet, or sitemap entries leaked into the normal build.
- Browser checks covered the homepage, both essay bibliographies, index, and sample. The 390px mobile checks showed no horizontal overflow; the sample also passed at 320px, and its desktop layout was visually inspected.
- Temporary Hebrew and minimal-metadata fixtures exercised missing publication/PDF fields, optional metadata, headings, emphasis, quotes, lists, and footnotes. Hebrew rendered with `lang="he"`, RTL text, 27px right-side list indentation, and a 3px right-side quote border. Footnote and return links worked. An inherited theme rule that compounded font shrinking was overridden only for archive footnotes; note text renders at 15px. These fixtures were never added to `_works/` and are removed by the final preview build.

During this task, a separate change advanced remote `main` to `962dace83e44af07ce90095b520c1a1e191609f2` ("Repair embedded bibliography PDF links"), with its own successful production workflow run. That commit changes `MIGRATION.md`, the printable bibliography PDF, and `migration/bibliography-links.json`. Those concurrently edited working-tree files are deliberately excluded from this feature's commit. This task did not modify or push `main`, dispatch a workflow, or deploy. Its local `main` reference remains at the inspected starting commit. Reconcile with the current remote branch and rerun validation before a future merge.

### Second pilot batch validation, September 9, 2026 (before marker removal)

- Normal output still contains 18 HTML pages, 601 checked local links, and all 209 PDF URLs. Compared with the previous pilot build, no output paths were added or removed and every byte matched except the generated feed timestamp.
- Both base-path preview builds contain 22 HTML pages and pass 731 local-link checks, with all 17 original routes and 209 PDF URLs retained. The index contains three unpublished works in year order.
- Metadata checks pass for all three works. The temporary-fixture publication tests pass normal omission, explicit draft preview, approved-only release, index/sitemap exclusion, and rejection of invalid approval/publication metadata.
- The English pilot has seven working notes/backlinks, with 15px note text. The Hebrew introduction uses real RTL text, preserved Hebrew source labels, and the correct two PDF page destinations. Both passed 390px and 320px overflow checks and desktop inspection. The range shown in the English citation stays LTR; the index displays the optional translated title.
- Original/public PDF page images match at 180 dpi for both new pilots. Their hashes and page checks are recorded in the corresponding review records. The David Nieto Markdown body hash still matches the revision accepted by the user.

### Third batch and continuous reading validation, September 9, 2026

- Added three complete unpublished works: Locke and Descartes (1935), Justice and Charity in Israel (1944, Hebrew), and Philosophical Classics in Hebrew (1946, English). Their eight source pages were visually checked, and original/public render pairs were pixel-identical at 200 dpi. Each review record identifies article boundaries, source hashes, and editorial choices.
- Removed inline editorial page markers from the three earlier works, the include, and its CSS rule. Comparing each earlier Markdown body after removing only marker syntax and its surrounding whitespace gives identical text. No source wording, footnotes, numbered paragraphs, or citation page ranges changed.
- Normal output remains 18 HTML pages, all 17 original routes, 601 checked internal links, and 209 PDF URLs. All 253 output paths match the previous batch's normal build byte-for-byte except the generated feed timestamp.
- Both `/leonroth/` and custom-domain-root previews pass with 25 HTML pages, 801 checked internal links, and all 209 PDF URLs. All six work pages are free of editorial page markers. Metadata validation and the publication-boundary fixture tests pass.
- All three additions passed desktop inspection and 390px/320px overflow checks. The Hebrew review uses RTL text and has a working note and return link; its note text remains 15px. Locke's ten source paragraph numbers and partial-word emphasis render correctly. The index lists six unpublished works in year order.

### Ten-work batch validation, September 9, 2026

The archive now contains sixteen unpublished works. Both preview base paths pass with 35 HTML pages, 1,073 local-link checks, and all 209 retained PDF URLs. Metadata and publication-boundary tests pass. Normal output remains 253 files, byte-identical to the previous normal build except the generated feed timestamp. See the [batch review guide](batches/2026-09-09-ten-works.md#technical-validation) for source comparisons and browser checks. No layout, stylesheet, configuration, workflow, PDF, or bibliography page was changed in this batch.

### Twenty-work batch validation, September 9, 2026

The archive contains thirty-six unpublished works, including four Hebrew texts. Both preview shapes pass with 55 HTML pages, 1,623 internal-link checks, and all 209 PDF URLs. Normal output preserves all 253 files byte-for-byte except the feed timestamp. Metadata, publication-boundary tests, all body hashes, and 320px/390px overflow checks pass. Hebrew quote typography is corrected in the two affected earlier works. See the [twenty-work review guide](batches/2026-09-09-twenty-works.md) for the complete queue, source gaps, exclusions, and browser checks.

## Before merging or publishing

- David Nieto and editorial standard version 1 have been accepted by the project owner, with the later instruction to remove editorial page numbers. The other thirty-five works need their own editorial acceptance, including all four Hebrew texts and all source notes.
- Review the English/mobile presentation and Hebrew reading direction on representative real text.
- Keep unrelated concurrent PDF/migration edits out of this feature's commit.
- Confirm the default build continues to omit the archive. Do not dispatch the Pages workflow for preview.
- Publishing, adding navigation, and migrating bibliography links are separate future changes requiring review.
