# Domain cutover — September 9, 2026

## Current progress

- Namecheap is now both the registrar and the authoritative DNS provider (`dns1.registrar-servers.com` and `dns2.registrar-servers.com`). The user saved BasicDNS and the new records.
- The existing A, CNAME, MX, and NS records were captured from the user's Wix screenshots. Public lookups are saved in `dns-before-namecheap.json`.
- No apex TXT, AAAA, CAA, DS, or `_dmarc` TXT answer was returned by the public lookups. The user confirmed that Wix's TXT and SRV sections are empty.
- GitHub Pages custom domain is now `www.leonroth.org`.
- The custom-domain root rebuild passed all checks and deployed successfully: https://github.com/furchtgott/leonroth/actions/runs/34373034457
- Direct HTTP checks against GitHub's server with the `www.leonroth.org` Host header passed for `/`, `/books-by-leon-roth/`, and `/about-us/`. These checks bypassed public DNS without changing it and confirmed domain-root links and the removal of the obsolete conference sentence.
- Both Namecheap nameservers were checked directly over TCP: all four GitHub A records, the `www` CNAME, all five forwarding MX records, and the generated SPF TXT record are correct. The user corrected the initially mistyped fourth A record. The verified snapshot is saved in `dns-after-namecheap.json`.
- Google and Cloudflare's public resolvers now return the correct A and CNAME records. There are no conflicting apex AAAA or CAA records. Other caches and GitHub's domain-check display returned older records during the transition.
- GitHub approved a certificate for both `www.leonroth.org` and `leonroth.org`, expiring December 8, 2026. HTTPS enforcement was enabled and confirmed through the API on September 9, 2026.
- Live HTTPS requests passed certificate validation and returned HTTP 200 from GitHub for the homepage, `/books-by-leon-roth/`, and the original Oona Ajzenstat PDF. The HTTPS apex redirects to HTTPS `www`; HTTP requests also redirect to the HTTPS site.
- The user confirmed that they do not use email addresses at `@leonroth.org`; no forwarding-destination migration or email-delivery test is needed. The existing MX records remain preserved.
- Direct HTTP checks on GitHub also confirmed the apex redirects to `www`, and the original Oona Ajzenstat review PDF URL returns HTTP 200 with `application/pdf`.

## Namecheap website records

Use Namecheap BasicDNS and Advanced DNS → Host Records. TTL can be Automatic. Replace conflicting web records for `@` and `www`, including any default parking or URL redirect records for those hosts.

| Type | Host | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `furchtgott.github.io` |

`@` means `leonroth.org`. Do not include `https://` or `/leonroth` in the CNAME value. Do not recreate the Wix NS records in Host Records; selecting BasicDNS establishes the new nameservers.

The Wix screenshot also had a legacy mobile alias, `m.leonroth.org → www16.wixdns.net`. This alias was not re-created at Namecheap. The new responsive site uses `www.leonroth.org` on phones and desktops; the old `m` hostname is not provided by the new DNS. GitHub's automatic apex/www redirect does not cover `m`.

## Preserve email forwarding

These are the current mail-server records, all with original TTL 1 hour:

| Type | Host | Value | Priority |
|---|---|---|---|
| MX | `@` | `eforward1.registrar-servers.com` | 10 |
| MX | `@` | `eforward2.registrar-servers.com` | 10 |
| MX | `@` | `eforward3.registrar-servers.com` | 10 |
| MX | `@` | `eforward4.registrar-servers.com` | 15 |
| MX | `@` | `eforward5.registrar-servers.com` | 20 |

Namecheap's Advanced DNS → Mail Settings → Email Forwarding option creates its forwarding MX records automatically. Keep the generated SPF TXT record. Check Domain → Redirect Email for the existing aliases and destination addresses; DNS lookups cannot reveal them. Preserving MX alone does not verify that forwarding destinations exist or delivery works.

## Final deployment

After HTTPS enforcement is enabled, the deployment workflow reads GitHub's HTTPS origin for canonical and metadata URLs. Publishing these cutover records triggers that rebuild. Future pushes to `main` continue to use the current GitHub Pages domain settings automatically.

GitHub's domain-check UI may temporarily retain its earlier InvalidCNAMEError even after the certificate is approved. The authoritative and public DNS answers, valid TLS connection, GitHub response headers, and saved HTTPS-enforcement setting independently confirm the successful cutover.

Sources: [GitHub custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Namecheap nameservers](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/), [Namecheap host records](https://www.namecheap.com/support/knowledgebase/article.aspx/434/2237/how-do-i-set-up-host-records-for-a-domain/), [Namecheap email forwarding](https://www.namecheap.com/support/knowledgebase/article.aspx/308/2214/how-to-set-up-free-email-forwarding/).
