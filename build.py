# Builds the site pages from one shared header and footer.
# Run: python3 build.py   (writes the .html files next to this script)
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "050-6274092"
TEL = "0506274092"
WA = "972506274092"
EMAIL = "gatnio@gmail.com"

NAV = [
    ("index.html", "בית"),
    ("partners.html", "השותפים"),
    ("criminal.html", "פלילי וחקירות"),
    ("administrative.html", "צווי סגירה ורישוי"),
    ("lpa-wills.html", "ייפוי כוח וצוואות"),
    ("contact.html", "צור קשר"),
]

LOGO_DEFS = open(os.path.join(ROOT, "partials", "logo-defs.html"), encoding="utf-8").read()

ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11Z"></path><circle cx="12" cy="10" r="2.6"></circle></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="m3 7 9 6 9-6"></path></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6.5 3.5c.5 1.4 1.1 2.6 2 3.7.4.5.3 1.1-.1 1.5l-1.4 1.3c1 2.4 2.8 4.2 5.2 5.2l1.3-1.4c.4-.4 1-.5 1.5-.1 1.1.9 2.3 1.5 3.7 2 .7.2 1.1 1 .9 1.7l-.6 2c-.2.6-.8 1-1.4.9-6.3-1-11.4-6.1-12.4-12.4-.1-.6.3-1.2.9-1.4l2-.6c.7-.2 1.5.2 1.7.9Z"></path></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>'


def header(current):
    links = "\n".join(
        f'      <a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    return f'''<a class="skip" href="#main">דלג לתוכן</a>
{LOGO_DEFS}
<header>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="משרד עורכי דין א.א.ג, עמוד הבית">
      <svg width="30" height="38" viewBox="0 0 100 128" aria-hidden="true"><use href="#aagLogo"></use></svg>
      <span class="brand-name">א.א.ג<small>משרד עורכי דין · אור יהודה</small></span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">תפריט</button>
    <nav class="links" id="site-nav" aria-label="ניווט ראשי">
{links}
    </nav>
    <a class="btn btn-gold btn-sm" href="tel:{TEL}">לתיאום פגישה</a>
  </div>
</header>'''


def footer():
    return f'''<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="שליחת הודעת וואטסאפ למשרד">{ICON_WA}<span>וואטסאפ</span></a>
<footer>
  <div class="wrap">
    <div class="footer-row">
      <span>משרד עורכי דין א.א.ג · רחוב החרושת 4, אור יהודה · <a href="tel:{TEL}">{PHONE}</a></span>
      <span class="footer-links"><a href="contact.html">צור קשר</a><a href="accessibility.html">הצהרת נגישות</a><span>© 2026 כל הזכויות שמורות</span></span>
    </div>
    <p class="disclaimer">המידע באתר הוא מידע כללי. הוא אינו ייעוץ משפטי ואינו תחליף לפגישה עם עורך דין שבוחן את הנסיבות של המקרה שלכם.</p>
  </div>
</footer>
<script>
  (function(){{
    var b=document.querySelector('.menu-toggle'), n=document.getElementById('site-nav');
    if(!b||!n) return;
    b.addEventListener('click',function(){{
      var o=n.classList.toggle('open'); b.setAttribute('aria-expanded', o?'true':'false');
    }});
  }})();
</script>'''


def page(filename, title, description, body):
    full_title = title if filename == "index.html" else f"{title} | משרד עורכי דין א.א.ג"
    html = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:locale" content="he_IL">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@500;700&family=Heebo:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
{header(filename)}
<main id="main">
{body.strip()}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)


def page_hero(crumb, h1, lede):
    return f'''<section class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">בית</a> / {crumb}</div>
    <h1>{h1}</h1>
    <p>{lede}</p>
  </div>
</section>'''


def aside(title, text, urgent=False):
    return f'''<aside class="aside-box{" urgent" if urgent else ""}">
  <h3>{title}</h3>
  <p>{text}</p>
  <a class="btn btn-gold" href="tel:{TEL}">חיוג למשרד, {PHONE}</a>
  <a class="btn btn-ghost-dark" href="https://wa.me/{WA}" target="_blank" rel="noopener">הודעה בוואטסאפ</a>
</aside>'''


if __name__ == "__main__":
    import pages
    pages.build(globals())
    print("built")
