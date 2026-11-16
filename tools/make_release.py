"""Build the copy of the website that goes on prwgas.com.

The GitHub preview stays hidden from Google; the prwgas.com copy must not be.
Run from the repo root:  python3 tools/make_release.py
Writes download/prwgas-website.zip (index.html and img/ at the top level).
"""
import zipfile, pathlib, re, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://prwgas.com/"
html = (ROOT / "index.html").read_text()
html, n = re.subn(r'<meta name="robots" content="noindex, nofollow">(<!--.*?-->)?\n', "", html)
assert n == 1, "draft tag not found"
html = html.replace("https://tduyywss.github.io/prw-gas-site/", DOMAIN)
html = html.replace('<meta property="og:image" content="https://prwgas.com/img/share.jpg">',
                    '<link rel="canonical" href="https://prwgas.com/">\n<meta property="og:image" content="https://prwgas.com/img/share.jpg">')
assert "tduyywss" not in html and "noindex" not in html

out = ROOT / "download" / "prwgas-website.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("index.html", html)
    z.writestr("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://prwgas.com/sitemap.xml\n")
    today = datetime.date.today().isoformat()
    z.writestr("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               f'  <url><loc>https://prwgas.com/</loc><lastmod>{today}</lastmod></url>\n'
               '</urlset>\n')
    z.write(ROOT / "404.html", "404.html")
    for f in sorted((ROOT / "img").iterdir()):
        if f.is_file() and f.name != "logo.png":
            z.write(f, f"img/{f.name}")
print(out, round(out.stat().st_size / 1024), "KB")
for i in zipfile.ZipFile(out).infolist(): print("  ", i.filename)
