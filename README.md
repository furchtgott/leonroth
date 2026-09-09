# Leon Roth Foundation

A Jekyll website using [Minimal Mistakes 4.28.1](https://mmistakes.github.io/minimal-mistakes/), prepared for GitHub Pages at `furchtgott/leonroth`. Content and linked documents were migrated from the Foundation’s Wix site. The original downloads in `Site Files/` remain untouched and are excluded from Git and publishing.

The live site is **https://www.leonroth.org/**. Namecheap manages the domain registration and DNS; GitHub Pages hosts the website and provides its HTTPS certificate. The bare domain redirects to `www`, and HTTPS is enforced.

## Preview locally

Use Ruby 4.0, then run:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

On this Mac, the newly installed Ruby is available at `/opt/homebrew/opt/ruby/bin/`; use that `bundle` executable instead of the older macOS system Ruby. Open [the local preview](http://127.0.0.1:4000/leonroth/).

### Digitized works development preview

The digital archive is opt-in and is **not included in normal or production builds**:

```sh
BUNDLE_PATH=vendor/bundle bundle exec jekyll serve --config _config.yml,_config.works-preview.yml --destination _site_test
```

Open [the works index](http://127.0.0.1:4000/leonroth/works/) or one of the unpublished pilots:

- [David Nieto](http://127.0.0.1:4000/leonroth/works/david-nieto/) — accepted by the project owner.
- [Spinoza in Recent English Thought](http://127.0.0.1:4000/leonroth/works/spinoza-recent-english-thought/) — seven footnotes; editorial review pending.
- [Introduction to Freedom and Government](http://127.0.0.1:4000/leonroth/works/freedom-government-introduction/) — Hebrew; review by a proficient reader pending.

See [the content model and safety notes](_docs/digitized-works.md), [the digitization plan](_docs/digitization-plan.md), and [the pilot review record](_docs/pilots/david-nieto-review.md).

Works default to `published: false`; this preview config explicitly includes them. Scan checking, editorial acceptance, and permission to publish are separate decisions. Before committing an edition, run:

```sh
BUNDLE_PATH=vendor/bundle bundle exec ruby tools/check_works.rb
BUNDLE_PATH=vendor/bundle bundle exec ruby tools/test_works_publication.rb
```

The archive PR workflow runs these checks plus normal and preview builds, with no deployment permissions.

Do not manually dispatch `pages.yml` for a preview: its deployment job also runs on `workflow_dispatch`. Keep the production workflow and its configuration unchanged.

## Edit the site

- Each interior page is an ordinary Markdown file in the project root. Edit its text and links beneath the opening `---` configuration block.
- `index.html` contains the homepage; `_data/navigation.yml` contains the menu.
- `assets/css/main.scss` contains the Foundation’s visual overrides. The underlying theme is installed as a versioned gem, without modifying the theme itself.
- `assets/images/` contains the three images used on the site.
- `_files/ugd/` retains the PDFs’ original public URL paths. Look up a document by its original filename or page label in `migration/assets.json`.
- `assets/documents/` contains the corrected Chapter III of *Seven Chapters on England*.
- Use `{{ '/page-or-file-path' | relative_url }}` in links, so the site works both under `/leonroth/` and at the root of the custom domain.

The `tools/import_content.py` script was a one-time importer. Do not rerun it over edited pages: doing so would replace subsequent corrections. The remaining migration tools are retained for provenance and maintenance, and do not run during normal website builds.

## Validate

```sh
bundle exec jekyll build
python3 tools/check_site.py
```

The check verifies every local link, fragment, image description, original page route, original PDF address, and the published size. It also ensures the original downloads and migration/build tools are excluded from the published site.

## Publish the GitHub preview

The repository is intended to be public for free GitHub Pages hosting. After signing into the GitHub CLI as `furchtgott`:

```sh
gh auth login --hostname github.com --git-protocol https --web --scopes workflow
gh repo create furchtgott/leonroth --public --source=. --remote=origin --push
gh api --method POST repos/furchtgott/leonroth/pages -f build_type=workflow
gh workflow run pages.yml
```

Run the repository-creation command only if the repository has not already been created. If it exists, use its existing remote and `git push` instead. In GitHub, Settings → Pages must have **GitHub Actions** selected as its source.

The included workflow builds and checks the site on every push to `main`, then deploys it. Pull requests build and check without deploying. It reads the URL and base path from GitHub Pages, so a later custom-domain change does not require editing every link.

The custom-domain cutover was completed on September 9, 2026. See [MIGRATION.md](MIGRATION.md) for the archive inventory and content corrections, and [the DNS cutover record](migration/dns-cutover.md) for the saved DNS settings and verification.
