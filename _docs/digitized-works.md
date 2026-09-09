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

Each work is a Markdown document in `_works/`. The filename is for editorial organization; the explicit `permalink` is the stable reader-facing URL. One pilot exists: `1921-david-nieto.md`, using metadata and the PDF link already in `essays-english.md`. It now contains a complete scan-checked draft, explicitly unpublished and pending independent editorial review. See [the plan](digitization-plan.md) and [pilot record](pilots/david-nieto-review.md).

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

Status values are `forthcoming`, `in_progress`, `scan_checked`, and `verified`. They describe editorial state; publication additionally requires an explicit `published: true`. Use `scan_checked` after a complete scan comparison and `verified` only after independent editorial approval, recorded with `reviewed_by`, `reviewed_on`, `reviewed_revision`, and `review_record`. The David Nieto pilot remains `scan_checked` and `published: false`.

The layout reuses the existing site shell, navigation, footer, reading-page classes, serif typography, and color variables. The extra CSS only targets archive components, with a narrower reading measure, mobile sizing, logical list/quote spacing, and footnotes.

Start essay sections at `##` because the layout supplies the title's `h1`. Normal Markdown headings, emphasis, blockquotes, and lists work. Kramdown footnotes use:

```markdown
A sentence with a note.[^1]

[^1]: The note, checked against the original scan.
```

## Hebrew and mixed text

`language: Hebrew` (also `he` or `עברית`) automatically sets the work's main reading region to `lang="he" dir="rtl"` and selects the Hebrew Essays return link. English/default works use `lang="en" dir="ltr"` and English Essays. You do not need to set page-wide direction for Hebrew.

The Foundation's existing English site navigation and metadata labels remain LTR. The title and transcription inherit the reading region's language and direction. Metadata values use `<bdi>` to isolate mixed Hebrew, English, and numbers. CSS logical properties place list indentation and blockquote borders on the correct side, including in footnotes. For an English phrase embedded in Hebrew prose, use `<span lang="en" dir="ltr">English phrase</span>` when needed. For works in other languages, review language tags and the return destination before adding them.

## Index and future bibliography integration

The index automatically lists `site.works`, filtered by publication eligibility outside an explicit preview; no duplicate public catalog data is needed. The separate `_docs/digitization-catalog.yml` tracks editorial candidates without creating pages. The index sorts by numeric year (undated items last), with title sorting as a tie-breaker. Change `sort_by` in `_preview/works/index.html` to `title` or `language` for those orders. Later, simple Liquid `group_by: 'language'` or `group_by: 'year'` can provide section headings. No JavaScript filtering is necessary.

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

Check that the collection is output-enabled when implementing this. A missing, unpublished, or unverified edition must leave the PDF as the title link. The pilot's `scan_checked` status must not redirect bibliography readers to an unapproved edition. Start with one reviewed entry; preserve existing citations, order, unlinked works, and multipart PDF references. Do not derive slugs from titles at render time.

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

Visit `/leonroth/`, `/leonroth/essays-english/`, `/leonroth/essays-hebrew/`, `/leonroth/works/`, and `/leonroth/works/david-nieto/` on `http://127.0.0.1:4000`. Follow the sample's PDF link. Check desktop and mobile widths, keyboard focus, and a temporary Hebrew fixture with headings, lists, and a footnote. Do not commit QA fixtures as archive content.

For a custom-domain-shaped build, create an override **outside the repository** containing `url: "https://www.leonroth.org"` and `baseurl: ""`. Append it to the comma-separated config list, build to a temporary destination, then run `tools/check_site.py --site /your/temp/output --baseurl ''`. This only builds files locally; it changes no hosting settings.

Normal builds must have no `works/` output, no `assets/css/works.css`, and no work routes in the sitemap. Compare pre-feature and post-feature normal builds: HTML, navigation, bibliography links, PDFs, and CSS should match; the feed's build timestamp can vary. Existing Minimal Mistakes Sass deprecation warnings predate this feature.

The existing Pages pull-request workflow validates the normal production build without deployment. A separate `works-check.yml` PR workflow now checks editorial metadata, publication boundaries, and both normal and opt-in preview builds. It has only `contents: read` permission and no deployment steps. No hosted preview or production deployment setting was added or changed.

### Validation performed on September 9, 2026

- Normal builds: 18 HTML pages, all 17 original routes, 601 internal links, and 209 PDF URLs passed the existing checker.
- Preview builds under both `/leonroth/` and a custom-domain-shaped empty base path: 20 HTML pages and 650 internal links passed, with all original routes and PDFs preserved. No Jekyll errors; only existing theme/dependency warnings.
- Built an isolated snapshot of the initial production commit, then applied only this feature's ten files and rebuilt with the custom-domain configuration. All 253 output paths were preserved, with no additions. Every file was byte-identical except `feed.xml`'s generated `<updated>` timestamp; normalizing only that timestamp made it identical too. No works pages, stylesheet, or sitemap entries leaked into the normal build.
- Browser checks covered the homepage, both essay bibliographies, index, and sample. The 390px mobile checks showed no horizontal overflow; the sample also passed at 320px, and its desktop layout was visually inspected.
- Temporary Hebrew and minimal-metadata fixtures exercised missing publication/PDF fields, optional metadata, headings, emphasis, quotes, lists, and footnotes. Hebrew rendered with `lang="he"`, RTL text, 27px right-side list indentation, and a 3px right-side quote border. Footnote and return links worked. An inherited theme rule that compounded font shrinking was overridden only for archive footnotes; note text renders at 15px. These fixtures were never added to `_works/` and are removed by the final preview build.

During this task, a separate change advanced remote `main` to `962dace83e44af07ce90095b520c1a1e191609f2` ("Repair embedded bibliography PDF links"), with its own successful production workflow run. That commit changes `MIGRATION.md`, the printable bibliography PDF, and `migration/bibliography-links.json`. Those concurrently edited working-tree files are deliberately excluded from this feature's commit. This task did not modify or push `main`, dispatch a workflow, or deploy. Its local `main` reference remains at the inspected starting commit. Reconcile with the current remote branch and rerun validation before a future merge.

## Before merging or publishing

- Review the pilot's citation, original PDF association, full transcription, and documented editorial choices; independent editorial verification is pending.
- Review the English/mobile presentation and Hebrew reading direction on representative real text.
- Keep unrelated concurrent PDF/migration edits out of this feature's commit.
- Confirm the default build continues to omit the archive. Do not dispatch the Pages workflow for preview.
- Publishing, adding navigation, and migrating bibliography links are separate future changes requiring review.
