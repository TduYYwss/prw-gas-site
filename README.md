# PRW Gas Services Ltd: website

Draft website for PRW Gas Services Ltd, a Gas Safe registered engineer in Bishopton, Renfrewshire.

Live at: https://tduyywss.github.io/prw-gas-site/

## Still needed from Paul
(Gas Safe number, company number and Facebook link are now in.)
All of these go in the `CONFIG` block at the bottom of `index.html`, apart from the bio.

1. **Gas Safe number** (`gasSafe`).
2. **Facebook page link** (`facebook`). The review buttons point to it.
3. **Company number and registered office** (`companyNumber`, `registeredOffice`). A limited company's website must show these by law. They appear in the footer once filled in.
4. **Areas covered** (`areas`). The current list is a guess at towns near Bishopton.
5. **Bio**: the bracketed text in the "Meet Paul" section.
6. **A daytime photo** of him in work gear, to replace `img/headshot.jpg`.

## Notes
- The quote and booking forms open WhatsApp with the message already written. Nothing is stored on the site.
- `img/share.jpg` is the picture that shows when the link is shared on WhatsApp or Facebook.
- If the site moves to its own domain, update the two `og:` web addresses near the top of `index.html`.
- **Draft:** a `noindex` tag keeps the site out of Google. Remove that line from `index.html` when the details above are in.

## Going live on prwgas.com
- `python3 tools/make_release.py` builds `download/prwgas-website.zip`: the site with the draft "hide from Google" tag removed and the link previews pointed at prwgas.com. **Re-run it after every change** and send Paul the new zip.
- Paul uploads that zip to Cloudflare Pages, following the guide at `go-live/` (https://tduyywss.github.io/prw-gas-site/go-live/).
- This GitHub copy stays hidden from Google, so search engines only list prwgas.com.
