#!/usr/bin/env python3
"""Build /it/ pages from English HTML + Italian dictionary. Re-run after copy changes."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://relocateinstyle.swiss"
PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "lifestyle.html",
    "ticino.html",
    "membership.html",
    "contact.html",
    "travel-contact.html",
    "packages.html",
    "approach.html",
    "shop-swiss-villages.html",
]


def lookup(data: dict, key: str) -> str:
    cur = data
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return ""
        cur = cur[part]
    return cur if isinstance(cur, str) else ""


def page_key(name: str) -> str:
    stem = name.replace(".html", "")
    return "home" if stem == "index" else stem


def canonical(name: str, italian: bool) -> str:
    prefix = "/it" if italian else ""
    if name == "index.html":
        return f"{HOST}{prefix}/"
    return f"{HOST}{prefix}/{name}"


def seo_links(name: str, italian: bool) -> str:
    en = canonical(name, False)
    it = canonical(name, True)
    canon = it if italian else en
    return "\n".join([
        f'  <link rel="canonical" href="{canon}">',
        f'  <link rel="alternate" hreflang="en" href="{en}">',
        f'  <link rel="alternate" hreflang="it" href="{it}">',
        f'  <link rel="alternate" hreflang="x-default" href="{en}">',
    ])


def switcher(name: str, italian: bool) -> str:
    if name == "index.html":
        en_href, it_href = "index.html" if not italian else "../index.html", "it/" if not italian else "index.html"
        # keep consistent file links
        en_href = "../index.html" if italian else "index.html"
        it_href = "index.html" if italian else "it/index.html"
    else:
        en_href = f"../{name}" if italian else name
        it_href = name if italian else f"it/{name}"
    en_active = "" if italian else " is-active"
    it_active = " is-active" if italian else ""
    label = "Lingua" if italian else "Language"
    return (
        f'    <nav class="lang-switch" aria-label="{label}">\n'
        f'      <a class="lang-switch-opt{en_active}" href="{en_href}" hreflang="en" lang="en">EN</a>\n'
        f'      <a class="lang-switch-opt{it_active}" href="{it_href}" hreflang="it" lang="it">IT</a>\n'
        f'    </nav>'
    )


SEO_RE = re.compile(
    r'\n(?:  <link rel="(?:canonical|alternate)"[^>]*>\n)+',
)
SWITCH_RE = re.compile(
    r'\s*<nav class="lang-switch".*?</nav>',
    re.S,
)
TOGGLE = '<button class="nav-toggle" id="nav-toggle" aria-label="Menu" data-i18n-aria="nav.menu">'


def strip_injected(html: str) -> str:
    html = SEO_RE.sub("\n", html)
    html = SWITCH_RE.sub("", html)
    return html


def insert_chrome(html: str, name: str, italian: bool) -> str:
    html = strip_injected(html)
    icon = '  <link rel="icon" href="assets/images/logo.png" type="image/png">'
    icon_it = '  <link rel="icon" href="../assets/images/logo.png" type="image/png">'
    needle = icon_it if icon_it in html else icon
    html = html.replace(needle, needle + "\n" + seo_links(name, italian), 1)
    html = html.replace("    " + TOGGLE, switcher(name, italian) + "\n    " + TOGGLE, 1)
    html = html.replace('css/style.css?v=66', 'css/style.css?v=75')
    html = html.replace('js/i18n.js?v=2', 'js/i18n.js?v=3')
    return html


def apply_translations(html: str, data: dict, name: str) -> str:
    def text_sub(m):
        val = lookup(data, m.group(1))
        return m.group(0) if not val else m.group(2) + val + m.group(3)

    html = re.sub(
        r'data-i18n="([^"]+)"([^>]*>)([^<]*)(<)',
        lambda m: f'data-i18n="{m.group(1)}"{m.group(2)}{lookup(data, m.group(1)) or m.group(3)}{m.group(4)}',
        html,
    )
    html = re.sub(
        r'<(?P<tag>[\w:-]+)(?P<pre>[^>]*\sdata-i18n-html="(?P<key>[^"]+)"[^>]*)>(?P<body>.*?)</(?P=tag)>',
        lambda m: f'<{m.group("tag")}{m.group("pre")}>{lookup(data, m.group("key")) or m.group("body")}</{m.group("tag")}>',
        html,
        flags=re.S,
    )
    html = re.sub(
        r'(data-i18n-aria="([^"]+)")(\s[^>]*aria-label=")([^"]*)(")',
        lambda m: f'{m.group(1)}{m.group(3)}{lookup(data, m.group(2)) or m.group(4)}{m.group(5)}',
        html,
    )
    html = re.sub(
        r'(data-i18n-alt="([^"]+)")(\s[^>]*alt=")([^"]*)(")',
        lambda m: f'{m.group(1)}{m.group(3)}{lookup(data, m.group(2)) or m.group(4)}{m.group(5)}',
        html,
    )
    title = lookup(data, f"meta.{page_key(name)}.title")
    desc = lookup(data, f"meta.{page_key(name)}.description")
    if title:
        html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)
    if desc:
        html = re.sub(
            r'(<meta name="description" content=")[^"]*(")',
            lambda m: f"{m.group(1)}{desc}{m.group(2)}",
            html,
            count=1,
        )
    html = html.replace('<html lang="en">', '<html lang="it">', 1)
    html = re.sub(
        r'(name="_next" value="https://relocateinstyle\.swiss/)(?!it/)',
        r'\1it/',
        html,
    )
    html = html.replace("aria-label=\"Language\"", "aria-label=\"Lingua\"")
    return html


def prefix_assets(html: str) -> str:
    html = html.replace('href="css/', 'href="../css/')
    html = html.replace('src="js/', 'src="../js/')
    html = html.replace('src="assets/', 'src="../assets/')
    html = html.replace('href="assets/', 'href="../assets/')
    html = html.replace('poster="assets/', 'poster="../assets/')
    html = html.replace('"assets/images/', '"../assets/images/')
    html = html.replace("'assets/", "'../assets/")
    html = html.replace('href="css/', 'href="../css/')  # no-op safety
    return html


def main() -> None:
    data = json.loads((ROOT / "js/locales/it.json").read_text())
    out_dir = ROOT / "it"
    out_dir.mkdir(exist_ok=True)

    for name in PAGES:
        src = ROOT / name
        html = src.read_text()
        en = insert_chrome(html, name, False)
        src.write_text(en)

        it_html = insert_chrome(html, name, True)
        it_html = apply_translations(it_html, data, name)
        it_html = prefix_assets(it_html)
        (out_dir / name).write_text(it_html)
        print("built", name)

    urls = []
    for name in PAGES:
        urls.append(canonical(name, False))
        urls.append(canonical(name, True))
    body = "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}</urlset>\n"
    )
    robots = ROOT / "robots.txt"
    if not robots.exists():
        robots.write_text("User-agent: *\nAllow: /\nSitemap: https://relocateinstyle.swiss/sitemap.xml\n")
    print("sitemap.xml updated")


if __name__ == "__main__":
    main()
