#!/usr/bin/env python3
"""Genererer v2-sider fra kilde-HTML med nyt layout."""

import re
from pathlib import Path

SRC = Path(r"C:\Users\Ano\Documents\Hjemmeside")
OUT = Path(r"C:\Users\Ano\Documents\AI\Projekter\helstedrengoering-v2")

SIDEBAR_LINKS = [
    ("rengoering.html", "Rengøring"),
    ("specialrengoering.html", "Specialrengøring"),
    ("social-rengoering.html", "Socialrengøring"),
    ("sandblaesning.html", "Sandblæsning"),
    ("toeris-rensning.html", "Tørisrensning"),
    ("facaderensning.html", "Facaderensning"),
    ("graffiti-rensning.html", "Graffitirensning"),
    ("pcb-sanering.html", "PCB sanering"),
    ("skimmelsanering.html", "Skimmelsvampsanering"),
    ("fugt-og-vandskader.html", "Fugt- og vandskader"),
    ("mijloesanering.html", "Miljøsanering"),
]

SERVICE_OPTIONS = """<option value="">Vælg ydelse (valgfrit)</option>
              <option>Rengøring</option><option>Specialrengøring</option><option>Socialrengøring</option>
              <option>Sandblæsning</option><option>Tørisrensning</option><option>Facaderensning</option>
              <option>Graffitirensning</option><option>PCB sanering</option>
              <option>Skimmelsvampsanering</option><option>Fugt- og vandskader</option><option>Miljøsanering</option>
              <option>Andet</option>"""

THEME_FLASH = """<script>(function(){var t=localStorage.getItem('helsted-theme');if(t==='dark')document.documentElement.setAttribute('data-theme','dark');})()</script>"""


def nav(active: str = "") -> str:
    def cls(page: str) -> str:
        return ' class="active"' if page == active else ""

    return f"""<header class="site-header">
  <div class="container header-inner">
    <a href="index.html" class="logo">
      <img src="assets/img/helsted_logo.png" alt="Helsted Specialrengøring logo" width="52" height="52" />
      <div class="logo-text">
        <span class="logo-name">Helsted Specialrengøring</span>
        <span class="logo-sub">og Skadeservice ApS</span>
      </div>
    </a>
    <nav class="main-nav" id="mainNav" aria-label="Hovedmenu">
      <ul>
        <li><a href="profil.html"{cls("profil")}>Profil</a></li>
        <li class="has-dropdown">
          <a href="vi-tilbyder.html"{cls("vi-tilbyder")}>Vi tilbyder</a>
          <ul class="dropdown">
            <li><a href="rengoering.html"{cls("rengoering")}>Rengøring</a></li>
            <li><a href="specialrengoering.html"{cls("specialrengoering")}>Specialrengøring</a></li>
            <li><a href="social-rengoering.html"{cls("social-rengoering")}>Socialrengøring</a></li>
            <li class="has-sub"><a href="ekspert-opgaver.html"{cls("ekspert-opgaver")}>Ekspertopgaver</a>
              <ul class="sub-dropdown">
                <li><a href="sandblaesning.html"{cls("sandblaesning")}>Sandblæsning</a></li>
                <li><a href="toeris-rensning.html"{cls("toeris-rensning")}>Tørisrensning</a></li>
                <li><a href="facaderensning.html"{cls("facaderensning")}>Facaderensning</a></li>
                <li><a href="graffiti-rensning.html"{cls("graffiti-rensning")}>Graffitirensning</a></li>
                <li><a href="pcb-sanering.html"{cls("pcb-sanering")}>PCB sanering</a></li>
                <li><a href="skimmelsanering.html"{cls("skimmelsanering")}>Skimmelsvampsanering</a></li>
                <li><a href="fugt-og-vandskader.html"{cls("fugt-og-vandskader")}>Fugt- og vandskader</a></li>
                <li><a href="mijloesanering.html"{cls("mijloesanering")}>Miljøsanering</a></li>
              </ul>
            </li>
          </ul>
        </li>
        <li><a href="referencer.html"{cls("referencer")}>Referencer</a></li>
        <li><a href="kontakt.html" class="nav-cta{' active' if active == 'kontakt' else ''}">Kontakt</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <button type="button" class="theme-toggle" id="themeToggle" aria-label="Skift til mørkt tema">🌙</button>
      <button class="nav-toggle" id="navToggle" aria-label="Åbn menu" aria-expanded="false" aria-controls="mainNav">☰</button>
    </div>
  </div>
</header>
<div class="nav-overlay" id="navOverlay"></div>"""


def footer() -> str:
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/Helsted-logo-hvid.png" alt="Helsted logo" loading="lazy" onerror="this.src='assets/img/helsted_logo.png'" />
        <p>43 års erfaring med specialopgaver indenfor rengøring i Randers Kronjylland.</p>
      </div>
      <div class="footer-col">
        <h4>Vi tilbyder</h4>
        <ul>
          <li><a href="rengoering.html">Rengøring</a></li>
          <li><a href="specialrengoering.html">Specialrengøring</a></li>
          <li><a href="sandblaesning.html">Sandblæsning</a></li>
          <li><a href="skimmelsanering.html">Skimmelsvampsanering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Kontakt</h4>
        <ul>
          <li><a href="tel:+4520801850">20 80 18 50</a></li>
          <li><a href="mailto:info@helstedrengoering.dk">info@helstedrengoering.dk</a></li>
          <li>Vestergade 21, Asferg, 8990 Fårup</li>
          <li>CVR: 45972968</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>©2026 Helsted Specialrengøring og Skadeservice ApS</span>
      <span>Asferg</span>
    </div>
  </div>
</footer>
<button class="scroll-top" id="scrollTop" aria-label="Tilbage til top">↑</button>
<script src="assets/js/main.js"></script>"""


def topbar() -> str:
    return """<div class="topbar">Har du brug for hjælp? Ring os: <a href="tel:+4520801850">20 80 18 50</a></div>"""


def sidebar(current: str = "") -> str:
    links = []
    for href, label in SIDEBAR_LINKS:
        c = ' class="current"' if href.replace(".html", "") == current or href == current + ".html" else ""
        links.append(f'<li><a href="{href}"{c}>{label}</a></li>')
    link_html = "\n            ".join(links)
    return f"""<aside class="aside">
        <div class="aside-box">
          <div class="aside-title">Vi tilbyder:</div>
          <ul class="aside-links">
            {link_html}
          </ul>
        </div>
        <div class="aside-contact">
          <h4>Har du brug for hjælp?</h4>
          <p>Kontakt os på tlf. 20 80 18 50 eller udfyld formularen herunder – så kontakter vi dig hurtigst muligt.</p>
          <a href="tel:+4520801850">20 80 18 50</a>
          <a href="kontakt.html" class="btn">Kontaktformular</a>
        </div>
      </aside>"""


def contact_form_block() -> str:
    return f"""<div class="contact-form fade-in">
        <h3>Skriv til os</h3>
        <form name="kontakt" method="POST" data-netlify="true" netlify-honeypot="bot-field" id="contactForm">
          <input type="hidden" name="form-name" value="kontakt" />
          <p hidden><label>Bot: <input name="bot-field" /></label></p>
          <div class="form-row">
            <div class="form-group"><label for="name">Navn *</label><input type="text" id="name" name="name" placeholder="Dit fulde navn" required /></div>
            <div class="form-group"><label for="phone">Telefon</label><input type="tel" id="phone" name="phone" placeholder="Dit telefonnummer" /></div>
          </div>
          <div class="form-group"><label for="email">E-mail *</label><input type="email" id="email" name="email" placeholder="din@email.dk" required /></div>
          <div class="form-group">
            <label for="service">Ydelse</label>
            <select id="service" name="service">
              {SERVICE_OPTIONS}
            </select>
          </div>
          <div class="form-group"><label for="message">Besked *</label><textarea id="message" name="message" placeholder="Beskriv din opgave..." required></textarea></div>
          <button type="submit" class="btn btn-primary">Send besked</button>
          <p class="form-note">Vi svarer hurtigst muligt.</p>
          <div class="form-success" id="formSuccess">Tak for din besked! Vi vender tilbage hurtigst muligt.</div>
        </form>
      </div>"""


def contact_info_block() -> str:
    return """<div class="contact-info fade-in">
        <div class="contact-block">
          <div class="contact-icon" aria-hidden="true">📞</div>
          <div><h4>Telefon</h4><a href="tel:+4520801850">20 80 18 50</a></div>
        </div>
        <div class="contact-block">
          <div class="contact-icon" aria-hidden="true">✉️</div>
          <div><h4>E-mail</h4><a href="mailto:info@helstedrengoering.dk">info@helstedrengoering.dk</a></div>
        </div>
        <div class="contact-block">
          <div class="contact-icon" aria-hidden="true">📍</div>
          <div><h4>Adresse</h4><p>Vestergade 21<br />Asferg, 8990 Fårup</p></div>
        </div>
        <div class="contact-block">
          <div class="contact-icon" aria-hidden="true">🏢</div>
          <div><h4>CVR</h4><p>45972968</p></div>
        </div>
      </div>"""


def wrap_page(title: str, active: str, breadcrumb: str, h1: str, content: str, with_sidebar: bool = True, extra_head: str = "") -> str:
    sidebar_html = sidebar(active) if with_sidebar else ""
    layout = "page-layout" if with_sidebar else ""
    article_class = "page-content fade-in"
    main_inner = f"""<article class="{article_class}">
          {content}
        </article>
        {sidebar_html}"""

    if not with_sidebar:
        main_inner = f"""<div class="container" style="padding:2.5rem 0 4rem">
        <article class="{article_class}">
          {content}
        </article>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="stylesheet" href="assets/css/main.css" />
  {THEME_FLASH}
  {extra_head}
</head>
<body>
  <a class="skip-link" href="#main">Spring til indhold</a>
  {topbar()}
  {nav(active)}
  <main id="main">
    <div class="page-hero">
      <div class="container">
        <div class="breadcrumb">{breadcrumb}</div>
        <h1>{h1}</h1>
      </div>
    </div>
    <div class="container {layout}">
      {main_inner}
    </div>
  </main>
  {footer()}
</body>
</html>"""


def extract_between(html: str, start: str, end: str) -> str:
    i = html.find(start)
    if i < 0:
        return ""
    i += len(start)
    j = html.find(end, i)
    return html[i:j].strip() if j >= 0 else html[i:].strip()


def clean_content(html: str) -> str:
    html = re.sub(r'\s*class="btn btn-primary"[^>]*', ' class="btn btn-primary"', html)
    html = re.sub(r'\s*style="[^"]*"', "", html)
    html = html.replace('class="page-img"', 'class="page-img"')
    html = html.replace('class="page-img contain"', 'class="page-img contain"')
    html = html.replace('class="current"', 'class="current"')
    return html


def page_key(filename: str) -> str:
    return Path(filename).stem


def build_inner(filename: str):
    src = (SRC / filename).read_text(encoding="utf-8")
    title_m = re.search(r"<title>([^<]+)</title>", src)
    title = title_m.group(1) if title_m else filename

    breadcrumb_raw = extract_between(src, '<div class="breadcrumb">', '</div>')
    if not breadcrumb_raw:
        breadcrumb_raw = extract_between(src, '<div class="page-header"><div class="container"><div class="breadcrumb">', '</div>')
    breadcrumb = breadcrumb_raw.replace('›', ' / ')

    h1_m = re.search(r'<div class="page-header"[^>]*>.*?<h1>([^<]+)</h1>', src, re.DOTALL)
    if not h1_m:
        h1_m = re.search(r'page-header.*?<h1>([^<]+)</h1>', src, re.DOTALL)
    h1 = h1_m.group(1) if h1_m else ""

    content = extract_between(src, '<main class="page-content">', '</main>')
    if not content:
        content = extract_between(src, '<main class="page-content"', '</main>')
        if content.startswith(">"):
            content = content[1:].strip()
    content = clean_content(content)

    key = page_key(filename)
    no_sidebar = filename == "referencer.html"
    out = wrap_page(title, key, breadcrumb, h1, content, with_sidebar=not no_sidebar)
    (OUT / filename).write_text(out, encoding="utf-8")
    print(f"  {filename}")


def build_index():
    sand_img = "sandblæsning.jpg"
    for f in (OUT / "assets" / "img").iterdir():
        if "sandbl" in f.name.lower() and f.suffix == ".jpg":
            sand_img = f.name
            break

    html = f"""<!DOCTYPE html>
<html lang="da">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Helsted Specialrengøring og Skadeservice ApS</title>
  <meta name="description" content="43 års erfaring med specialopgaver indenfor rengøring. Rengøring, specialrengøring og erhvervsrengøring i Randers Kronjylland." />
  <link rel="canonical" href="https://helstedrengoering.dk/" />
  <link rel="stylesheet" href="assets/css/main.css" />
  {THEME_FLASH}
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Helsted Specialrengøring og Skadeservice ApS","telephone":"+4520801850","email":"info@helstedrengoering.dk","address":{{"@type":"PostalAddress","streetAddress":"Vestergade 21, Asferg","addressLocality":"Fårup","postalCode":"8990","addressCountry":"DK"}},"vatID":"45972968"}}</script>
</head>
<body>
  <a class="skip-link" href="#main">Spring til indhold</a>
  {topbar()}
  {nav("index")}
  <main id="main">
    <section class="hero">
      <div class="container hero-grid">
        <div class="fade-in">
          <span class="hero-badge">43 års erfaring</span>
          <h1>43 års erfaring med specialopgaver indenfor rengøring<span>Vi udfører intelligent skadeservice</span></h1>
          <p class="hero-lead">Rengøring, specialrengøring og erhvervsrengøring i Randers Kronjylland</p>
          <p>Helsted Specialrengøring og Skadeservice ApS er kendetegnet i lokalmiljøet for tillid, pålidelighed og ikke mindst høj kvalitet i vores arbejde.</p>
          <div class="hero-actions">
            <a href="kontakt.html" class="btn btn-primary">Kontakt os</a>
            <a href="vi-tilbyder.html" class="btn btn-outline">Vi tilbyder</a>
          </div>
        </div>
        <div class="hero-image fade-in">
          <img src="assets/img/hero-gade.jpg" alt="Helsted Specialrengøring i Randers" width="600" height="400" />
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container about-grid">
        <div class="about-photo fade-in">
          <img src="assets/img/about-rens.jpg" alt="Specialrengøring" loading="lazy" />
          <div class="experience-badge"><strong>43</strong><span>Års erfaring</span></div>
        </div>
        <div class="fade-in">
          <h2 class="section-title" style="text-align:left">Helsted Specialrengøring og Skadeservice ApS</h2>
          <div class="divider" style="margin:0 0 1.5rem"></div>
          <p>Helsted Specialrengøring og Skadeservice ApS er kendetegnet i lokalmiljøet for tillid, pålidelighed og ikke mindst høj kvalitet i vores arbejde.</p>
          <p>Vores engagerede medarbejdere er specialuddannet indenfor vores ekspertopgaver, hvilket gør at vi har opretholdt et tillidsfuldt forhold til vores kunder gennem mange år.</p>
          <p>Vi sætter pris på punktlighed og ærlighed og sætter en ære i at overholde vores aftaler.</p>
          <p><a href="profil.html"><strong>Se mere om os her →</strong></a></p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="section-title fade-in">Vi tilbyder</h2>
        <div class="divider"></div>
        <p class="section-intro fade-in">Helsted Specialrengøring og Skadeservice ApS udfører et stort omfang af specialrengøring, herunder kan nævnes sandblæsning, tøris-, facade– og graffitirensning i Randers.</p>
        <p class="section-intro fade-in">Vi udfører også den daglige rengøring, herunder kan nævnes, gulvpolering, håndværkerrengøring, industriservice, kontorrengøring samt trappevask.</p>
        <p class="section-intro fade-in">Derudover hjælper vi med skimmelsanering og fugtskader. <a href="vi-tilbyder.html"><strong>Se mere her!</strong></a></p>

        <h3 class="section-title fade-in" style="font-size:1.35rem;margin-top:2.5rem">Ekspertopgaver</h3>

        <div class="cards" style="margin-top:1.5rem">
          <article class="card fade-in"><a class="card-link" href="sandblaesning.html"><div class="card-img"><img src="assets/img/{sand_img}" alt="Sandblæsning" loading="lazy" /></div><div class="card-body"><h3>Sandblæsning</h3><p>Våd- og tør-sandblæsning samt lavtrykssandblæsning</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="toeris-rensning.html"><div class="card-img"><img src="assets/img/dryice.jpg" alt="Tørisrensning" loading="lazy" /></div><div class="card-body"><h3>Tørisrensning</h3><p>Skånsomt for emnet og miljøet – ingen kemikalier</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="facaderensning.html"><div class="card-img"><img src="assets/img/facaderens.jpg" alt="Facaderensning" loading="lazy" /></div><div class="card-body"><h3>Facaderensning</h3><p>Skånsom facaderensning giver resultater</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="graffiti-rensning.html"><div class="card-img"><img src="assets/img/graffiti.jpg" alt="Graffitirensning" loading="lazy" /></div><div class="card-body"><h3>Graffitirensning</h3><p>Kemi- og tørismetode til effektiv fjernelse</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="pcb-sanering.html"><div class="card-placeholder" aria-hidden="true">🔬</div><div class="card-body"><h3>PCB sanering</h3><p>Efter gældende retningslinjer for miljø og arbejdsmiljø</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="skimmelsanering.html"><div class="card-img"><img src="assets/img/skimmelsvamp_vaeg.jpg" alt="Skimmelsvampsanering" loading="lazy" /></div><div class="card-body"><h3>Skimmelsvampsanering</h3><p>Skimmelsanering af dit hjem i Randers</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="fugt-og-vandskader.html"><div class="card-img"><img src="assets/img/hero-badekar.jpg" alt="Fugt- og vandskader" loading="lazy" /></div><div class="card-body"><h3>Fugt- og vandskader</h3><p>Vores absolutte spidskompetence – 43 års erfaring</p></div></a></article>
          <article class="card fade-in"><a class="card-link" href="mijloesanering.html"><div class="card-img"><img src="assets/img/special-rengoering.jpg" alt="Miljøsanering" loading="lazy" /></div><div class="card-body"><h3>Miljøsanering</h3><p>Screening og miljøsanering for PCB, bly og kviksølv</p></div></a></article>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <h2 class="section-title fade-in">Referencer</h2>
        <div class="divider"></div>
        <p class="section-intro fade-in">Nedenstående er et udpluk af vores tilfredse kunder</p>
        <div class="ref-grid fade-in">
          <div class="ref-item"><span class="ref-dot"></span><span>Fuks Ejendomme I/S</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Gjensidige Forsikring A/S</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Hestia Ejendomme</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Alm. Brand A/S</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Hobro Malerfirma</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>ISS Facility Service A/S</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Jorton A/S</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>Jensen Byg Service ApS</span></div>
          <div class="ref-item"><span class="ref-dot"></span><span>RM Thor A/S</span></div>
        </div>
        <p style="text-align:center;margin-top:1.5rem"><a href="referencer.html"><strong>Se flere her →</strong></a></p>
      </div>
    </section>

    <section class="section" id="kontakt">
      <div class="container">
        <h2 class="section-title fade-in">Kontakt</h2>
        <div class="divider"></div>
        <p class="section-intro fade-in">Har du brug for hjælp? Kontakt os på tlf. 20 80 18 50 eller udfyld formularen herunder – så kontakter vi dig hurtigst muligt.</p>
        <div class="contact-grid">
          {contact_info_block()}
          {contact_form_block()}
        </div>
      </div>
    </section>
  </main>
  {footer()}
</body>
</html>"""
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print("  index.html")


def build_kontakt():
    content = f"""<p style="font-size:1.05rem;color:var(--muted);margin-bottom:2rem">Har du brug for hjælp? Kontakt os på tlf. 20 80 18 50 eller udfyld formularen herunder – så kontakter vi dig hurtigst muligt.</p>
        <div class="contact-grid">
          {contact_info_block()}
          {contact_form_block()}
        </div>"""
    out = wrap_page(
        "Kontakt – Helsted Specialrengøring og Skadeservice ApS",
        "kontakt",
        '<a href="index.html">Forside</a> / Kontakt',
        "Kontakt",
        content,
        with_sidebar=False,
    )
    (OUT / "kontakt.html").write_text(out, encoding="utf-8")
    print("  kontakt.html")


def build_referencer():
    src = (SRC / "referencer.html").read_text(encoding="utf-8")
    items = re.findall(r'<div class="client-item"><div class="client-dot"></div><span>([^<]+)</span></div>', src)
    grid = "\n          ".join(
        f'<div class="ref-item fade-in"><span class="ref-dot"></span><span>{name}</span></div>' for name in items
    )
    content = f"""<p style="margin-bottom:2rem;font-size:1.05rem;color:var(--muted)">Nedenstående er et udpluk af vores tilfredse kunder</p>
        <div class="ref-grid">
          {grid}
        </div>"""
    out = wrap_page(
        "Referencer – Helsted Specialrengøring og Skadeservice ApS",
        "referencer",
        '<a href="index.html">Forside</a> / Referencer',
        "Referencer",
        content,
        with_sidebar=False,
    )
    (OUT / "referencer.html").write_text(out, encoding="utf-8")
    print("  referencer.html")


def main():
    pages = [
        "profil.html", "vi-tilbyder.html", "rengoering.html", "specialrengoering.html",
        "social-rengoering.html", "ekspert-opgaver.html", "sandblaesning.html",
        "toeris-rensning.html", "facaderensning.html", "graffiti-rensning.html",
        "pcb-sanering.html", "skimmelsanering.html", "fugt-og-vandskader.html",
        "mijloesanering.html", "job.html",
    ]
    print("Bygger sider...")
    build_index()
    build_kontakt()
    build_referencer()
    for p in pages:
        build_inner(p)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print("Færdig!")


if __name__ == "__main__":
    main()
