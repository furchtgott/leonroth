# Wix → GitHub Pages migration

Captured September 8–9, 2026 from [leonroth.org](https://www.leonroth.org/), using the downloaded `Site Files/` originals.

## Scope and archive

- All **17 published pages** from Wix’s sitemap are migrated, including the seven book chapter indexes.
- All **209 distinct public PDF URLs** matched a local downloaded file by SHA-256. Their `/_files/ugd/...pdf` paths are retained.
- The correct Chapter III of *Seven Chapters on England* adds one previously unlinked document, for **210 published PDFs**.
- The portrait, 1956 Philosophy Congress photograph, and ex libris use the downloaded originals. Other images and unlinked PDFs remain in `Site Files/` and are excluded from Git and the published site.
- There are no runtime Wix dependencies. Normal builds require Jekyll and the pinned theme, not the migration Python libraries or a Wix account.

The full original download contained 232 files, totaling 1,088,075,977 bytes. The completed published site is approximately **906 MB**, below the conservative 1,000,000,000-byte GitHub Pages limit. Lossless PDF optimization reduces the linked PDFs to approximately **896 MB**; no originals in `Site Files/` are overwritten. The reports in `migration/pdf-optimization.json`, `migration/pdf-palettes.json`, and `migration/pdf-jpegs.json` record the transformations, size changes, checksums, and verification results. JPEG optimization changes entropy coding only; it does not resize images or lower image quality.

## Validation

- Production Jekyll builds and local-link checks pass for both `/leonroth/` and the future custom-domain root.
- All 601 local links and fragments resolve, all 17 original routes exist, and all 209 original PDF addresses are present.
- All 16 interior pages were checked at phone width without horizontal overflow or missing images. Desktop and mobile dropdown navigation were exercised.
- All modified JPEGs and palette images were checked for identical decoded pixels. Sample English and Hebrew PDFs also rendered pixel-identically to their originals.
- Automated validation runs again in GitHub Actions before deployment.

## Content corrections

1. On the old *Seven Chapters on England* page, Chapter III pointed to Chapter II’s PDF. The link now uses the supplied Hebrew Chapter III, whose heading is “Local Authorities and Public Education.” The old Chapter II URL still works.
2. Removed an invisible, empty link on *The Guide for the Perplexed*. It led to Chapter IV of *Judaism: A Portrait*, which remains properly linked from that book.
3. Removed the mission page’s obsolete announcement of a planned 2019 conference at the owner's request. The digitized library is now described as available in Resources.
4. Replaced the defunct Littman publisher URL with the verified [Oxford Academic book page](https://academic.oup.com/liverpool-scholarship-online/book/40108).
5. Promoted book part headings and conference session headings to semantic headings, repositioned photo captions beside their images, and used the English title plus a transliterated subtitle for *Seven Chapters on England*. Bibliography text, ordering, and references are otherwise retained.
6. Nested Oona Ajzenstat's October 1999 review beneath its book entry, *Is There a Jewish Philosophy? Rethinking Fundamentals.*

The legacy external link to Neve Gordon’s “A Jewish Voice for Coexistence” (`worlddialogue.org/print.php?id=173`) returns HTTP 410 Gone. Its bibliographic citation is preserved; the original article was not among the linked local downloads. This is an inherited external-source issue, independent of the migrated site’s local links. The advisory board names and affiliations are copied from the original site and have not been independently updated.

## URLs

The live site is `https://www.leonroth.org/`; the original project preview was `https://furchtgott.github.io/leonroth/`. Original page paths use directory indexes (for example `/leon-roth/`), with the usual web-server redirect from the slashless `/leon-roth`. PDF paths are unchanged. Old `static.wixstatic.com` URLs remain controlled by Wix; our domain cannot redirect addresses on Wix’s domain.

The GitHub Actions workflow uses `actions/configure-pages` to select the correct hostname and base path at build time. A custom-domain deployment therefore builds for the domain root automatically. With an Actions publishing workflow, a `CNAME` file is not needed; the custom domain is set in GitHub’s Pages settings.

## Domain cutover

Completed September 9, 2026: Namecheap BasicDNS is authoritative, GitHub's certificate covers both domain names, HTTPS enforcement is enabled, and live HTTPS checks passed for the homepage, an interior page, a migrated PDF, and the apex redirect. See [the cutover record](migration/dns-cutover.md) for the original and final DNS snapshots.

Before the cutover, the domain used **`ns0.wixdns.net` and `ns1.wixdns.net`**, making Wix the authoritative DNS provider even though Namecheap was the registrar. The transition procedure is retained below for reference.

1. Confirm the GitHub preview, all pages, PDFs, and HTTPS work.
2. Save the current complete Wix DNS zone, including MX, TXT, CAA, verification records, and any unrelated subdomains. Prepare those records at Namecheap before switching nameservers. The public website crawl does not reveal every DNS record.
3. Verify ownership of `leonroth.org` in GitHub’s account Pages settings. Use the exact TXT record GitHub supplies; do not invent its value.
4. Set the repository’s Pages custom domain to **`www.leonroth.org`** and rebuild. Do this before pointing DNS at GitHub.
5. If migrating DNS to Namecheap, switch to Namecheap BasicDNS and recreate the preserved records plus the web records below. Alternatively, the same web records can be changed at the current DNS provider while its service remains active. Do not assume Wix will continue DNS service after cancellation.

| Type | Host | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `furchtgott.github.io` |

Replace only conflicting Wix web-hosting records. Preserve email and other service records; if there are existing apex AAAA records, replace the Wix values with GitHub’s documented IPv6 values or remove those web-only AAAA records so IPv6 visitors do not continue reaching Wix.

6. Verify the DNS results, GitHub’s domain check, the homepage, an interior page, and a PDF through `www.leonroth.org`. Enable **Enforce HTTPS** once the certificate is ready. Confirm `leonroth.org` redirects to `www.leonroth.org`.
7. Cancel Wix only after the site and any DNS/email dependencies are confirmed working independently.

Keep the Wix plan active during the transition so the saved original DNS configuration provides a practical rollback path.

Sources checked for the deployment instructions: [GitHub Pages custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [custom publishing workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), and [Pages size limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).
