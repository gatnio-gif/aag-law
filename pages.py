# Page content for the A.A.G site. Edit text here, then run: python3 build.py

ICON_CRIM = '''<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="10" y="8" width="20" height="9" rx="1" transform="rotate(-35 20 12.5)"></rect><line x1="22" y1="20" x2="10" y2="32"></line><line x1="6" y1="40" x2="22" y2="40"></line><line x1="14" y1="40" x2="14" y2="33"></line></svg>'''
ICON_ADMIN = '''<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 5 h16 l6 6 v32 h-22 z"></path><path d="M29 5 v6 h6"></path><line x1="18" y1="22" x2="30" y2="22"></line><line x1="18" y1="29" x2="30" y2="29"></line><line x1="18" y1="36" x2="26" y2="36"></line></svg>'''
ICON_SEAL = '''<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="24" cy="19" r="12"></circle><path d="M24 10 l2.6 5.4 5.9.6 -4.4 4 1.2 5.8 -5.3 -3 -5.3 3 1.2-5.8 -4.4-4 5.9-.6 Z"></path><line x1="18" y1="29" x2="13" y2="43"></line><line x1="30" y1="29" x2="35" y2="43"></line></svg>'''
ICON_PEN = '''<svg class="icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 38 l4-12 18-18 8 8 -18 18 z"></path><line x1="28" y1="12" x2="36" y2="20"></line><line x1="8" y1="43" x2="40" y2="43"></line></svg>'''


GALLERY = '''<div class="office-gallery">
  <img src="images/office-room.jpg" alt="חדר פגישות במשרד א.א.ג באור יהודה" width="1200" height="900" loading="lazy">
  <img src="images/office-door-aksul.jpg" alt="דלת החדר של עו&quot;ד אהרון אקסול במשרד" width="1140" height="855" loading="lazy">
  <img src="images/office-door-gatenyo.jpg" alt="דלת החדר של עו&quot;ד יצחק גטניו במשרד" width="800" height="600" loading="lazy">
  <img src="images/office-door-ifergan.jpg" alt="שלט המשרד על דלת החדר של עו&quot;ד חיים איפרגן" width="990" height="660" loading="lazy">
</div>'''

PARTNERS = [
    ("aksul", 'עו"ד אהרון אקסול', "ניצב (בגמלאות)"),
    ("ifergan", 'עו"ד חיים איפרגן', "תת ניצב (בגמלאות)"),
    ("gatenyo", 'עו"ד יצחק גטניו', "ניצב משנה (בגמלאות)"),
]


def home(g):
    TEL, PHONE = g["TEL"], g["PHONE"]
    rank_items = "\n".join(
        f'      <div class="rank-item"><span class="r-label">שותף</span><span class="r-name">{n}</span><span class="r-value">{r}</span></div>'
        for _, n, r in PARTNERS)
    cards = "\n".join(
        f'''      <div class="partner-card">
        <div class="partner-photo"><img src="images/partner-{k}.jpg" alt="{n.replace('"','&quot;')}" width="480" height="600" loading="lazy"></div>
        <h3>{n}</h3>
        <div class="rank-badge"><svg width="26" height="33" viewBox="0 0 100 128" aria-hidden="true"><use href="#aagLogo"></use></svg><span>{r}</span></div>
      </div>''' for k, n, r in PARTNERS)
    body = f'''
<section class="hero">
  <svg class="hero-emblem" viewBox="0 0 100 128" aria-hidden="true"><use href="#aagLogoOutline"></use></svg>
  <div class="wrap hero-inner">
    <span class="eyebrow">משרד עורכי דין א.א.ג · אור יהודה</span>
    <h1>לצדכם עומד מי שהכיר את המערכת מבפנים</h1>
    <p class="lede">אנחנו שלושה שותפים, שלושה קצינים בכירים בדימוס של משטרת ישראל, וכיום עורכי דין העוסקים בדין הפלילי, בדין המנהלי, ברישוי עסקים ובייפויי כוח מתמשכים וצוואות. שנים של ניסיון בחקירות, באכיפה ובעבודה מול הרשויות עומדות היום לרשות הלקוחות שלנו.</p>
    <div class="hero-ctas">
      <a class="btn btn-gold" href="tel:{TEL}">לתיאום פגישה</a>
      <a class="btn btn-ghost-dark" href="#practice">תחומי העיסוק שלנו</a>
    </div>
    <div class="rank-strip">
{rank_items}
    </div>
  </div>
</section>

<section class="about" id="about">
  <div class="wrap about-grid">
    <div>
      <div class="section-head">
        <span class="eyebrow">היתרון שלנו</span>
        <h2>ניסיון שאי אפשר ללמוד מספר</h2>
      </div>
      <p>שלושתנו שירתנו שנים ארוכות במשטרת ישראל, בדרגות בכירות. ישבנו בצד השני של השולחן. ניהלנו חקירות, קיבלנו החלטות אכיפה וליווינו הליכי רישוי מתוך הרשות עצמה.</p>
      <p>כשעברנו לצד של הלקוח, הבאנו איתנו את הידע המשפטי ואת ההבנה איך הגורמים שמולכם חושבים ופועלים בפועל. זה ההבדל שאנחנו מביאים לכל תיק.</p>
    </div>
    <div class="then-now">
      <div class="tn-item"><span class="tn-k">מאיפה הגענו</span><span class="tn-v">חקירות, אכיפה ורישוי בתוך משטרת ישראל</span></div>
      <div class="tn-item"><span class="tn-k">מה למדנו</span><span class="tn-v">איך מתקבלות ההחלטות שמולן אתם ניצבים</span></div>
      <div class="tn-item"><span class="tn-k">מה זה נותן לכם היום</span><span class="tn-v">עורך דין שמכיר את הדרך, מהפגישה הראשונה</span></div>
    </div>
  </div>
</section>

<section class="practice" id="practice">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">תחומי עיסוק</span>
      <h2>איפה אנחנו נכנסים לתמונה</h2>
    </div>
    <div class="card-grid">
      <a class="p-card" href="criminal.html">{ICON_CRIM}
        <h3>דין פלילי וחקירות</h3>
        <p>ייצוג בחקירות משטרה, בהליכי מעצר ושחרור, מול הפרקליטות, בכתבי אישום ובבקשות להשבת תפוסים.</p>
        <span class="more">לפרטים</span>
      </a>
      <a class="p-card" href="administrative.html">{ICON_ADMIN}
        <h3>צווי סגירה ורישוי עסקים</h3>
        <p>צו סגירה מנהלי בגלל העסקת שוהים שלא כדין, צווי הגבלת שימוש, רישיון עסק ועבודה מול הרשות המקומית והמשטרה.</p>
        <span class="more">לפרטים</span>
      </a>
      <a class="p-card" href="lpa-wills.html">{ICON_PEN}
        <h3>ייפוי כוח מתמשך וצוואות</h3>
        <p>ייפוי כוח מתמשך שנכתב לפי המצב שלכם, צוואות, צוואות הדדיות, צו קיום צוואה והתנגדויות.</p>
        <span class="more">לפרטים</span>
      </a>
    </div>
  </div>
</section>

<section class="partners" id="partners">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">מי אנחנו</span>
      <h2>השותפים במשרד</h2>
    </div>
    <div class="partner-grid">
{cards}
    </div>
    <p class="partner-note">שלושה עורכי דין, שלושה קצינים בכירים בגמלאות. <a href="partners.html" style="color:var(--gold-2)">להכיר את השותפים</a></p>
  </div>
</section>

<section class="practice">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">המשרד</span>
      <h2>רחוב החרושת 4, אור יהודה</h2>
    </div>
    {GALLERY}
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">איך אנחנו עובדים</span>
      <h2>מה מקבלים כשפונים אלינו</h2>
    </div>
    <div class="trust-grid">
      <div class="trust-item"><span class="t-num">01</span><h3>זמינות אישית</h3><p>הפנייה מגיעה ישירות לעורך הדין שמטפל בתיק. לא לתא קולי.</p></div>
      <div class="trust-item"><span class="t-num">02</span><h3>היכרות מהשטח</h3><p>ידע מעשי בדרך שבה פועלות רשויות האכיפה, מעבר להיכרות עם לשון החוק.</p></div>
      <div class="trust-item"><span class="t-num">03</span><h3>דיסקרטיות מלאה</h3><p>ניהול התיק בשקט ובמקצועיות, בלי רעש מיותר סביב הלקוח.</p></div>
      <div class="trust-item"><span class="t-num">04</span><h3>ליווי מלא</h3><p>מהפגישה הראשונה ועד סוף ההליך, כולל כל שלב מול הרשויות.</p></div>
    </div>
  </div>
</section>

{contact_block(g)}
'''
    g["page"]("index.html", "משרד עורכי דין א.א.ג | אור יהודה",
              "משרד עורכי דין א.א.ג באור יהודה. שלושה שותפים, קצינים בכירים בדימוס של משטרת ישראל: דין פלילי, צווי סגירה ורישוי עסקים, ייפוי כוח מתמשך וצוואות.",
              body)


def contact_block(g):
    return f'''<section class="contact" id="contact">
  <div class="wrap contact-grid">
    <div class="contact-list">
      <div class="c-row">{g["ICON_PIN"]}<div><div class="c-k">כתובת המשרד</div><div class="c-v">רחוב החרושת 4, אור יהודה</div></div></div>
      <div class="c-row">{g["ICON_PHONE"]}<div><div class="c-k">נייד, עו"ד יצחק גטניו</div><div class="c-v"><a href="tel:{g["TEL"]}">{g["PHONE"]}</a></div></div></div>
      <div class="c-row">{g["ICON_PHONE"]}<div><div class="c-k">טל' ופקס</div><div class="c-v"><a href="tel:035594333">03-5594333</a></div></div></div>
      <div class="c-row">{g["ICON_MAIL"]}<div><div class="c-k">דוא"ל</div><div class="c-v"><a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a></div></div></div>
    </div>
    <div class="contact-cta">
      <h3>נשמח לשמוע מכם</h3>
      <p>ספרו לנו בקצרה במה מדובר, ונחזור אליכם לתיאום פגישה במשרד באור יהודה. בעניין דחוף, כמו צו סגירה או זימון לחקירה, עדיף להתקשר.</p>
      <a class="btn btn-gold" href="tel:{g["TEL"]}">חיוג למשרד</a>
      <a class="btn btn-ghost-dark" href="https://wa.me/{g["WA"]}" target="_blank" rel="noopener">הודעה בוואטסאפ</a>
    </div>
  </div>
</section>'''


def partners(g):
    bios = {
        "aksul": '<p>שירת שנים ארוכות במשטרת ישראל ופרש בדרגת ניצב, הדרגה הבכירה ביותר במשטרה אחרי דרגת המפכ"ל. היום הוא עורך דין ושותף במשרד.</p>',
        "ifergan": '<p>שירת שנים ארוכות במשטרת ישראל ופרש בדרגת תת ניצב. במהלך שירותו עסק בין היתר בחקירות נגד ארגוני פשיעה. היום הוא עורך דין ושותף במשרד.</p>',
        "gatenyo": '<p>שירת שנים ארוכות במשטרת ישראל ופרש בדרגת ניצב משנה. ניהל צוותי חקירה בתיקים מורכבים, בהם חקירות הונאה במחוז תל אביב. היום הוא עורך דין ושותף במשרד, ובעל תואר מוסמך במשפטים (LL.M.) מאוניברסיטת בר אילן.</p><p>עו"ד גטניו הוסמך על ידי האפוטרופוס הכללי לערוך ייפויי כוח מתמשכים, וערך עשרות כאלה.</p>',
    }
    blocks = "\n".join(
        f'''    <article class="profile" id="{k}">
      <div class="partner-photo"><img src="images/partner-{k}.jpg" alt="{n.replace('"','&quot;')}" width="480" height="600" loading="lazy"></div>
      <div>
        <h2>{n}</h2>
        <span class="rank">{r}</span>
        {bios[k]}
      </div>
    </article>''' for k, n, r in PARTNERS)
    body = f'''
{g["page_hero"]("השותפים", "שלושה עורכי דין, שלושה קצינים בכירים בגמלאות", "כל אחד מאיתנו הגיע לעריכת הדין אחרי שנים ארוכות של שירות במשטרת ישראל. את הניסיון הזה אנחנו מביאים לכל תיק.")}
<section>
  <div class="wrap">
{blocks}
  </div>
</section>
{contact_block(g)}
'''
    g["page"]("partners.html", "השותפים", "השותפים במשרד עורכי דין א.א.ג: עו\"ד אהרון אקסול, ניצב בגמלאות, עו\"ד חיים איפרגן, תת ניצב בגמלאות, ועו\"ד יצחק גטניו, ניצב משנה בגמלאות.", body)


def criminal(g):
    body = f'''
{g["page_hero"]("פלילי וחקירות", "קיבלתם זימון לחקירה? השעות הראשונות חשובות", "רוב הטעויות בתיק פלילי נעשות לפני שמישהו פונה לעורך דין. שיחה אחת לפני החקירה יכולה לשנות את כל ההמשך.")}
<section>
  <div class="wrap layout-aside">
    <div class="prose">
      <h2>לפני חקירה במשטרה</h2>
      <p>לחשוד יש זכות להיוועץ בעורך דין. כדאי לממש אותה לפני שמגיעים לתחנה, ולא אחרי. אנחנו עוברים איתכם על מה שידוע, מסבירים מה צפוי בחדר החקירות ומה הזכויות שלכם שם.</p>
      <p>ניהלנו חקירות כאלה בעצמנו, מהצד של החוקרים. אנחנו יודעים מה מחפשים בחקירה ומה עלול להזיק לכם.</p>
      <h2>מעצר ושחרור</h2>
      <p>ייצוג בדיוני מעצר, בבקשות לשחרור בתנאים ובבקשות לשינוי תנאים. בשלב הזה כל שעה חשובה, ולכן אנחנו זמינים גם מחוץ לשעות העבודה.</p>
      <h2>השבת תפוסים</h2>
      <p>המשטרה תפסה כסף, רכב, טלפון או מסמכים? אפשר לבקש מבית המשפט להורות על החזרתם. אנחנו מגישים את הבקשה, מנהלים את הדיון ופועלים מול היחידה החוקרת.</p>
      <h2>מכתב יידוע לפני כתב אישום</h2>
      <p>כשמגיע מכתב שמודיע שהתיק הועבר לשקילת הגשת כתב אישום, יש הזדמנות לפנות לתביעה או לפרקליטות לפני ההחלטה. פנייה מנומקת יכולה להביא לסגירת התיק או להקלה משמעותית. חשוב לא לפספס את המועד שנקבע במכתב.</p>
      <h2>כתב אישום, משפט וערעור</h2>
      <p>אם הוגש כתב אישום, אנחנו מלווים את התיק לאורך כל ההליך בבית המשפט, כולל משא ומתן עם התביעה, ניהול ההוכחות, טיעונים לעונש וערעור.</p>
    </div>
    {g["aside"]("זימון לחקירה או מעצר", "התקשרו לפני שאתם מגיעים לתחנה. השיחה הראשונה נועדה להבין את המצב ולהגיד לכם מה עושים עכשיו.", True)}
  </div>
</section>
'''
    g["page"]("criminal.html", "דין פלילי וחקירות", "ייצוג בחקירות משטרה, מעצרים, השבת תפוסים, מכתבי יידוע וכתבי אישום, על ידי עורכי דין שהיו קצינים בכירים במשטרת ישראל.", body)


def administrative(g):
    body = f'''
{g["page_hero"]("צווי סגירה ורישוי עסקים", "קיבלתם צו סגירה לעסק? הזמן קצר", "צו סגירה מנהלי עוצר את העסק מיד. ככל שפונים מוקדם יותר, כך יש יותר דרכים לפעול.")}
<section>
  <div class="wrap layout-aside">
    <div class="prose">
      <h2>צו סגירה בגלל העסקת שוהים שלא כדין</h2>
      <p>מפקד מחוז במשטרה רשאי להוציא צו סגירה מנהלי לעסק או לאתר בנייה שבו נמצאו עובדים שוהים בלתי חוקיים. הצו נכנס לתוקף מהר, והנזק לעסק מצטבר מכל יום שהוא סגור.</p>
      <p>רוב התיקים המנהליים במשרד הם בדיוק צווים כאלה. אנחנו מכירים את ההליך מבפנים, כולל את השיקולים של מי שחותם על הצו.</p>
      <h2>איך אנחנו פועלים</h2>
      <div class="steps">
        <div class="step"><div><h3>פגישה מיידית</h3><p>עוברים על הצו, על נסיבות הביקורת ועל מסמכי העובדים, ובודקים איפה הצו חלש.</p></div></div>
        <div class="step"><div><h3>בקשה לשימוע</h3><p>פנייה דחופה לגורם שהוציא את הצו, עם הטענות והמסמכים שתומכים בביטולו או בקיצורו.</p></div></div>
        <div class="step"><div><h3>בקשה לבית משפט השלום</h3><p>אם השימוע לא הספיק, מגישים בקשה דחופה לבית משפט השלום לביטול הצו.</p></div></div>
        <div class="step"><div><h3>חזרה לעבודה</h3><p>ליווי עד פתיחת העסק מחדש, והמלצות מעשיות שיעזרו למנוע צו נוסף.</p></div></div>
      </div>
      <h2>צווי הגבלת שימוש</h2>
      <p>ייצוג בערר ובבקשות לבית המשפט נגד צווים מנהליים שמגבילים שימוש במקום, כולל אתרי בנייה.</p>
      <h2>רישוי עסקים</h2>
      <p>ליווי בבקשה לרישיון עסק, התמודדות עם תנאים ודרישות של הגורמים המאשרים, ערר על סירוב או על התליית רישיון, וייצוג מול הרשות המקומית ומשטרת ישראל.</p>
    </div>
    {g["aside"]("העסק נסגר היום?", "התקשרו עכשיו. ההחלטה מה עושים קודם, שימוע או בית משפט, תלויה בפרטי הצו, ואת זה בודקים בשיחה הראשונה.", True)}
  </div>
</section>
'''
    g["page"]("administrative.html", "צווי סגירה ורישוי עסקים", "צו סגירה מנהלי בגלל העסקת שוהים שלא כדין, צווי הגבלת שימוש ורישוי עסקים. בקשות שימוע ובקשות דחופות לבית משפט השלום.", body)


def lpa_wills(g):
    body = f'''
{g["page_hero"]("ייפוי כוח מתמשך וצוואות", "להחליט עכשיו מי ידאג לכם ולרכוש שלכם", "ייפוי כוח מתמשך וצוואה הם שני מסמכים שכדאי לערוך כשהכול בסדר. כך ההחלטות נשארות שלכם.")}
<section>
  <div class="wrap layout-aside">
    <div class="prose">
      <h2>ייפוי כוח מתמשך</h2>
      <p>ייפוי כוח מתמשך מאפשר לכם לבחור היום מי יקבל החלטות בשמכם, אם יום אחד לא תוכלו לעשות זאת בעצמכם. ההחלטות יכולות לכלול עניינים אישיים, רפואיים ורכושיים, וגם הנחיות מקדימות שמבטאות את הרצונות שלכם.</p>
      <p>עו"ד יצחק גטניו הוסמך על ידי האפוטרופוס הכללי לערוך ייפויי כוח מתמשכים, וערך עשרות כאלה. אין אצלנו נוסח אחד לכולם. כל ייפוי כוח נכתב לפי המצב המשפחתי, הרכוש והרצונות של הלקוח שיושב מולנו.</p>
      <h2>איך זה עובד</h2>
      <div class="steps">
        <div class="step"><div><h3>פגישת היכרות</h3><p>מדברים על המשפחה, על הרכוש ועל מה חשוב לכם, ומחליטים את מי למנות ובאילו תחומים.</p></div></div>
        <div class="step"><div><h3>ניסוח</h3><p>כותבים את המסמך ואת ההנחיות המקדימות לפי מה שסוכם, ועוברים עליו איתכם.</p></div></div>
        <div class="step"><div><h3>חתימה והפקדה</h3><p>חתימה בפני עורך הדין והפקדת המסמך אצל האפוטרופוס הכללי.</p></div></div>
      </div>
      <h2>צוואות</h2>
      <p>עריכת צוואה שמתאימה לכם, כולל צוואות הדדיות לבני זוג. אנחנו מקפידים על נוסח ברור וחתימה כדין, כדי לצמצם את הסיכוי למחלוקת בין היורשים בעתיד.</p>
      <h2>צו קיום צוואה והתנגדויות</h2>
      <p>הגשת בקשה לצו קיום צוואה, הגשת התנגדות לצוואה וייצוג מי שהצוואה שלו מותקפת.</p>
    </div>
    {g["aside"]("לקבוע פגישה", "הפגישה הראשונה מתקיימת במשרד באור יהודה. אם יש קושי להגיע, נמצא פתרון.")}
  </div>
</section>
'''
    g["page"]("lpa-wills.html", "ייפוי כוח מתמשך וצוואות", "ייפוי כוח מתמשך שנכתב לפי המצב שלכם, על ידי עורך דין שהוסמך על ידי האפוטרופוס הכללי. צוואות, צוואות הדדיות, צו קיום צוואה והתנגדויות.", body)


def contact(g):
    gallery = '<div class="section-head" style="margin-top:56px"><span class="eyebrow">המשרד</span><h2>כך נראה המשרד</h2></div>' + GALLERY
    body = f'''
{g["page_hero"]("צור קשר", "צור קשר עם המשרד", "המשרד נמצא ברחוב החרושת 4 באור יהודה. אפשר להתקשר, לשלוח הודעה בוואטסאפ או מייל.")}
{contact_block(g)}
<section>
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">איך מגיעים</span><h2>רחוב החרושת 4, אור יהודה</h2></div>
    <iframe class="map" title="מפה: רחוב החרושת 4, אור יהודה" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=%D7%94%D7%97%D7%A8%D7%95%D7%A9%D7%AA%204%20%D7%90%D7%95%D7%A8%20%D7%99%D7%94%D7%95%D7%93%D7%94&hl=iw&output=embed"></iframe>
{gallery}
  </div>
</section>
'''
    g["page"]("contact.html", "צור קשר", "משרד עורכי דין א.א.ג, רחוב החרושת 4, אור יהודה. טלפון 050-6274092.", body)


def accessibility(g):
    body = f'''
{g["page_hero"]("הצהרת נגישות", "הצהרת נגישות", "אנחנו רוצים שכל אחד יוכל להשתמש באתר ולפנות אלינו.")}
<section>
  <div class="wrap prose">
    <h2>מה עשינו באתר</h2>
    <p>האתר נבנה במטרה לעמוד בתקנות שוויון זכויות לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע"ג 2013, ובתקן הישראלי ת"י 5568, המבוסס על הנחיות WCAG 2.0 ברמה AA.</p>
    <ul>
      <li>האתר כתוב בעברית, מימין לשמאל, ומוגדר כך לקוראי מסך.</li>
      <li>אפשר לנווט בכל האתר באמצעות המקלדת, וקישור "דלג לתוכן" מופיע בתחילת כל עמוד.</li>
      <li>לתמונות יש תיאור טקסטואלי.</li>
      <li>הניגודיות בין הטקסט לרקע נבחרה כך שיהיה קל לקרוא.</li>
      <li>האתר מותאם לטלפונים ומאפשר הגדלה של הטקסט בדפדפן.</li>
    </ul>
    <h2>נתקלתם בבעיה?</h2>
    <p>אם משהו באתר לא נגיש לכם, נשמח לשמוע ולתקן. אפשר לפנות לעו"ד יצחק גטניו בטלפון <a href="tel:{g["TEL"]}">{g["PHONE"]}</a> או במייל <a href="mailto:{g["EMAIL"]}">{g["EMAIL"]}</a>.</p>
    <h2>נגישות המשרד</h2>
    <p>לפרטים על הסדרי הנגישות במשרד ברחוב החרושת 4 באור יהודה, אפשר להתקשר אלינו לפני ההגעה.</p>
    <p>ההצהרה עודכנה באוקטובר 2026.</p>
  </div>
</section>
'''
    g["page"]("accessibility.html", "הצהרת נגישות", "הצהרת הנגישות של אתר משרד עורכי דין א.א.ג.", body)


def build(g):
    home(g); partners(g); criminal(g); administrative(g); lpa_wills(g); contact(g); accessibility(g)
