import os, html as H

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ovp-demo-v4')) + os.sep

# ---------------------------------------------------------------- helpers
def T(label):
    return f'<span class="tbd">[OVP: {label}]</span>'

ICONS = {
 'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 'chart': '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 'megaphone': '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
 'landmark': '<path d="M3 22h18"/><path d="M6 18v-7"/><path d="M10 18v-7"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M12 2 20 7H4z"/>',
 'briefcase': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 'heart': '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
 'clipboard': '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
 'map': '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15"/><path d="M15 6v15"/>',
 'cycle': '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
 'message': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'mic': '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
 'compass': '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-2.12 6.36-6.36 2.12 2.12-6.36 6.36-2.12z"/>',
 'file': '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 'chevron': '<path d="m6 9 6 6 6-6"/>',
 'menu': '<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/>',
 'presentation': '<path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/><path d="m7 21 5-5 5 5"/>',
 'share': '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.59 13.51 6.83 3.98"/><path d="m15.41 6.51-6.82 3.98"/>',
 'check': '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
 'video': '<path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
 'download': '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
 'shield': '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
}
def I(name, cls='icon'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'

def chip_icon(name, variant=''):
    return ''

def ext(href, text, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<a{c} href="{href}" target="_blank" rel="noopener noreferrer">{text}<span class="visually-hidden"> (opens in a new tab)</span></a>'

# ---------------------------------------------------------------- content
SERVICES = [
 dict(slug='strategy-execution', name='Strategy & Execution', icon='target',
      line='Turn strategy into plans your people actually adopt — and results you can measure.'),
 dict(slug='organizational-performance', name='Organizational Performance', icon='chart',
      line="Diagnose what's slowing you down and design processes built to last."),
 dict(slug='leadership-change', name='Leadership & Change', icon='users',
      line='Build leaders and teams that grow from their strengths through every change.'),
 dict(slug='strategic-communication', name='Strategic Communication', icon='megaphone',
      line='Set the right tone with every audience and turn messages into measurable engagement.'),
]

CLIENTS = ['Delaware Department of Labor', 'California Department of Public Health', 'Illinois Action for Children',
           'American Licorice Company', 'Riveredge Hospital', '7 Mindsets', '34 Strong', 'PASO',
           'National Coalition of 100 Black Women', 'Mas Que Salud']

Q = {
 'darren': dict(text='Alejandro and the team at OVP are seasoned veterans, and know how to create meaningful change, build trust, focus on strengths and help to improve employee engagement. They are true professionals and make real lasting impact on their clients.',
                name='Darren Virassammy', role='Co-founder & COO, 34 Strong Inc.'),
 'robert': dict(text='We are having an excellent experience with OVP Consulting group. They are mainly trying to help us to improve our strategic communications and we believe this is going to be really useful for our growth as small charity.',
                name='Robert Memba, MD, PhD', role='President, Mas Que Salud NGO'),
 'roy': dict(text='Alejandro’s ability to blend long-term strategic thinking with laser-sharp attention to daily detail on multiple issues is extremely impressive. He has deep insight regarding audiences and customers at the local, national and international level. Alejandro’s talent, clarity and experience add up to an invaluable resource for companies of all sizes in any industry.',
             name='Roy Heffley', role='Executive Consultant, Williamsburg, VA'),
 'hillary': dict(text='What drew me to OVP was their genuine interest in wanting my venture to succeed. I am in awe of the depth of knowledge they bring from a marketing perspective, and what is equally impressive is the time they have taken to get to know the ins and outs of my business. This is undoubtedly the best method for implementing a successful action plan. I am excited about the future of my business, and my continued partnership with OVP Consulting.',
                 name='Hillary Herring', role='Owner, CrossFit Inner Stallion, Southfield, MI'),
}
def quote(key, cls='quote'):
    q = Q[key]
    return f'''<figure class="{cls}">
          <blockquote><p>“{q['text']}”</p></blockquote>
          <figcaption><strong>{q['name']}</strong>{q['role']}</figcaption>
        </figure>'''

TEAM = [
 dict(name='Alejandro Bodipo-Memba', role='CEO & Founder', img='team-alejandro.webp',
      short='Has led projects in strategic communications, executive leadership training, team building and management consulting across the U.S., Europe and Latin America.',
      long='Alejandro has led projects in strategic communications, executive leadership training, team building and management consulting across the U.S., Europe and Latin America. He uses a systems-thinking approach to complex process problems, and makes performance-based leadership behavior and team building part of every client solution.'),
 dict(name='Ebony Tran', role='Chief of Staff & Operations', img='team-ebony.webp',
      short='25 years of global experience and a former senior U.S. Foreign Service Officer; ICF-accredited coach.',
      long='Ebony brings 25 years of global experience and served as a senior U.S. Foreign Service Officer. An International Coaching Federation–accredited (ACC) coach, she has empowered senior leaders and driven organizational effectiveness across the public and private sectors.'),
 dict(name='Al Pacha', role='Director of Information Technology', img='team-al.webp',
      short='25+ years developing IT solutions; architect of OVP’s proprietary assessment tools.',
      long='Al has more than 25 years of experience developing IT solutions, with depth in systems analysis, project management and risk management. He is the architect of OVP’s proprietary organizational assessment tools.'),
]

def team_card(m, p, full=False):
    body = m['long'] if full else m['short']
    return f'''<li class="team-row">
            <h3>{m['name']}</h3>
            <span class="team-role">{m['role']}</span>
            <p>{body}</p>
          </li>'''

def team_list(p, full=False):
    return '<ul class="team-list" role="list">' + ''.join(team_card(m, p, full) for m in TEAM) + '</ul>'

# ---------------------------------------------------------------- chrome
NAV = [('services.html', 'Services'), ('who-we-serve.html', 'Who We Serve'), ('our-work.html', 'Our Work'),
       ('insights.html', 'Insights'), ('about.html', 'About')]

def header(p, current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if current == href else ''
        if href == 'services.html':
            subs = ''.join(f'<li><a href="{p}services/{s["slug"]}.html">{s["name"]}<span>{s["line"]}</span></a></li>' for s in SERVICES)
            items.append(f'''<li class="has-sub">
            <a class="nav-link" href="{p}services.html"{cur}>Services</a>
            <button class="sub-toggle" type="button" aria-expanded="false" aria-controls="sub-services"><span class="visually-hidden">Show service pages</span>{I('chevron')}</button>
            <ul class="submenu" id="sub-services">{subs}</ul>
          </li>''')
        else:
            items.append(f'<li><a class="nav-link" href="{p}{href}"{cur}>{label}</a></li>')
    items.append(f'<li><a class="btn btn--primary header-cta" href="{p}contact.html">Book a consultation</a></li>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{p}index.html"><img src="{p}assets/img/ovp-logo.png" alt="OVP Management Consulting" width="150" height="36"></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{I('menu')}</button>
      <nav id="site-nav" class="nav" aria-label="Main">
        <ul class="nav-list">
          {''.join(items)}
        </ul>
      </nav>
      <a class="btn btn--primary header-cta header-cta--desktop" href="{p}contact.html">Book a consultation</a>
    </div>
  </header>'''

def footer(p):
    svc = ''.join(f'<li><a href="{p}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{p}index.html" class="brand-foot"><img src="{p}assets/img/ovp-logo-white.png" alt="OVP Management Consulting" width="185" height="44" loading="lazy"></a>
          <p>Next-level consulting for sustainable success.</p>
        </div>
        <div>
          <h2>Services</h2>
          <ul>{svc}</ul>
        </div>
        <div>
          <h2>Company</h2>
          <ul>
            <li><a href="{p}about.html">About</a></li>
            <li><a href="{p}our-work.html">Our Work</a></li>
            <li><a href="{p}insights.html">Insights</a></li>
            <li><a href="{p}government.html">Government Contracting</a></li>
          </ul>
        </div>
        <div>
          <h2>Contact</h2>
          <ul>
            <li><a href="{p}contact.html">Book a consultation</a></li>
            <li>{T('email')}</li>
            <li>{T('phone')}</li>
            <li>{T('address')}</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 OVP Management Consulting Group Inc.</p>
        <ul>
          <li><a href="{p}privacy.html">Privacy Policy</a></li>
          <li><a href="{p}privacy.html#accessibility">Accessibility</a></li>
        </ul>
      </div>
    </div>
  </footer>'''

def page(path, title, desc, current, body, alt=False):
    depth = path.count('/')
    p = '../' * depth
    bcls = ' class="page-alt"' if alt else ''
    doc = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>{title}</title>
  <meta name="description" content="{H.escape(desc)}">
  <link rel="icon" href="{p}assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&amp;family=Source+Serif+4:opsz,wght@8..60,400&amp;display=swap">
  <link rel="stylesheet" href="{p}assets/css/ovp.css">
  <script src="{p}assets/js/ovp.js" defer></script>
</head>
<body{bcls}>
  {header(p, current)}
  <main id="main" tabindex="-1">
{body(p)}
  </main>
  {footer(p)}
</body>
</html>
'''
    full = OUT + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(doc)

def cta(p, title, text, btn='Book a consultation', theme='theme-accent'):
    return f'''    <section class="section cta-band {theme}" aria-labelledby="cta-title">
      <div class="container">
        <div>
          <h2 id="cta-title">{title}</h2>
          <p>{text}</p>
        </div>
        <div class="btn-row"><a class="btn btn--primary" href="{p}contact.html">{btn}</a></div>
      </div>
    </section>'''

def service_cards(p, items, heading='h3'):
    rows = ''.join(f'''<li class="svc-row">
            <{heading}><a href="{p}services/{s['slug']}.html">{s['name']}</a></{heading}>
            <p>{s['line']}</p>
            <span class="arrow" aria-hidden="true">→</span>
          </li>''' for s in items)
    return f'<ol class="svc-list reveal">{rows}</ol>'

def breadcrumb(p, trail):
    lis = []
    for i, (href, label) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
        else:
            lis.append(f'<li><a href="{p}{href}">{label}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'

def client_list(names, cls='client-list'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{n}</li>' for n in names) + '</ul>'

# ---------------------------------------------------------------- HOME
def home(p):
    return f'''    <section class="hero" aria-labelledby="hero-title">
      <img class="hero-bg" src="{p}assets/img/hero-washington.webp" alt="" width="1800" height="1198" fetchpriority="high">
      <div class="container">
        <div class="hero-inner">
          <span class="eyebrow">Management consulting for public agencies, businesses &amp; nonprofits</span>
          <h1 id="hero-title">Building on strengths to deliver lasting results.</h1>
          <p class="lead">OVP helps organizations turn strategy into execution — by building on what their people already do best.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="{p}contact.html">Book a consultation</a>
            <a class="btn btn--tertiary" href="{p}our-work.html">See our work</a>
          </div>
        </div>
      </div>
    </section>

    <section class="theme-light" aria-label="Clients">
      <div class="container client-strip">
        <p class="eyebrow">Trusted by</p>
        {client_list(CLIENTS)}
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="help-title">
      <div class="container split">
        <div>
          <span class="eyebrow">Services</span>
          <h2 id="help-title">How we help</h2>
          <p class="lead mt-4">Four practice areas, one approach: start from what your people already do well, then build the plan, processes and messages around it.</p>
          <div class="mt-4"><a class="btn btn--tertiary" href="{p}services.html">All services</a></div>
        </div>
        {service_cards(p, SERVICES)}
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="numbers-title" style="padding-top:0">
      <div class="container">
        <h2 id="numbers-title" class="visually-hidden">OVP at a glance</h2>
        <div class="stats reveal">
          <div class="stat"><span class="stat-value">{T('years in business')}</span><span class="stat-label">Years in business</span></div>
          <div class="stat"><span class="stat-value">{T('organizations served')}</span><span class="stat-label">Organizations served</span></div>
          <div class="stat"><span class="stat-value">{T('leaders coached')}</span><span class="stat-label">Leaders coached</span></div>
          <div class="stat"><span class="stat-value">{T('sectors')}</span><span class="stat-label">Sectors</span></div>
        </div>
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="case-title">
      <div class="container split">
        <div>
          <span class="eyebrow">Case study · Government</span>
          <h2 id="case-title">Delaware Department of Labor</h2>
          <div class="mt-4"><a class="btn btn--tertiary" href="{p}our-work/case-study.html">Read the case study</a></div>
        </div>
        <div>
          <figure class="media-frame"><img src="{p}assets/img/arch-chamber.webp" alt="An empty legislative chamber with rows of desks facing the speaker’s chair" width="1600" height="820" loading="lazy"></figure>
          <dl class="case-steps">
            <div><dt>Challenge</dt><dd>New agency leadership needed to explain fast-moving pandemic changes to staff and the public — without a change plan or a unified communications strategy.</dd></div>
            <div><dt>What we did</dt><dd>Ran a needs assessment, centralized communications, set measurement criteria, led town halls and media, and built a communications charter.</dd></div>
            <div><dt>Result</dt><dd>Documented gains over four years in online engagement, media interviews and leadership visibility. The “Did You Know…?” campaign became one of the department’s best-recognized efforts.</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="serve-title">
      <div class="container">
        <div class="section-head section-head--row">
          <div>
            <span class="eyebrow">Sectors</span>
            <h2 id="serve-title">Who we serve</h2>
          </div>
          <a class="btn btn--tertiary" href="{p}who-we-serve.html">Who we serve</a>
        </div>
        <div class="grid grid--3 reveal">
          <article class="sector">
            <img src="{p}assets/img/arch-capitol.webp" alt="Pennsylvania Avenue leading to the U.S. Capitol in Washington, D.C." width="1600" height="1180" loading="lazy">
            <h3>Government &amp; public agencies</h3>
            <p>Communications, change management and leadership development for state agencies and public programs.</p>
          </article>
          <article class="sector">
            <img src="{p}assets/img/arch-glass-facade.webp" alt="The glass facade of an office building against a pale sky" width="1400" height="1336" loading="lazy">
            <h3>Businesses</h3>
            <p>Team engagement, process improvement and leadership training for small and midsize firms ready to grow.</p>
          </article>
          <article class="sector">
            <img src="{p}assets/img/arch-residential.webp" alt="A modern residential building with balconies seen from street level" width="1400" height="1867" loading="lazy">
            <h3>Nonprofits &amp; community organizations</h3>
            <p>Strategic communications, capacity building and mentoring programs that help mission-driven teams reach more people.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section theme-dark" aria-labelledby="gov-title">
      <div class="container split">
        <div>
          <span class="eyebrow">For public buyers</span>
          <h2 id="gov-title">Working with government?</h2>
          <p class="lead mt-4">Company identifiers, capabilities, past performance and the roles we can take on a contract — on one page.</p>
          <div class="btn-row mt-6">
            <a class="btn btn--primary" href="{p}government.html">Government contracting</a>
            <span class="btn btn--secondary" role="link" aria-disabled="true">{I('download')} Capability statement {T('PDF')}</span>
          </div>
        </div>
        <div>
          <h3 class="visually-hidden">Company credentials</h3>
          <dl class="data-rows">
            <div><dt>UEI</dt><dd>{T('UEI')}</dd></div>
            <div><dt>CAGE code</dt><dd>{T('CAGE code')}</dd></div>
            <div><dt>NAICS</dt><dd>{T('NAICS codes')}</dd></div>
            <div><dt>Certifications</dt><dd>{T('business certifications')}</dd></div>
            <div><dt>Contract vehicles</dt><dd>{T('GSA / state vehicles')}</dd></div>
            <div><dt>Coaching</dt><dd>ICF ACC-credentialed</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="method-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">How we work</span>
          <h2 id="method-title">A strengths-based method, from first conversation to measured result</h2>
          <p>We use CliftonStrengths and our own assessment tools to understand what your team does best — then design around it.</p>
        </div>
        <ol class="steps steps--3 reveal">
          <li class="step"><h3>Discover strengths</h3><p>Assess your people, processes and communications to see what already works and where the gaps are.</p></li>
          <li class="step"><h3>Design the plan</h3><p>Agree on success measures with leadership, then build a plan your teams can own.</p></li>
          <li class="step"><h3>Deliver &amp; measure</h3><p>Work alongside your staff to put the plan into practice and report progress against the measures we set together.</p></li>
        </ol>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="team-title">
      <div class="container split">
        <div>
          <span class="eyebrow">Leadership</span>
          <h2 id="team-title">Senior people on every engagement</h2>
          <p class="lead mt-4">The people you meet in the first conversation are the people who do the work.</p>
          <div class="mt-4"><a class="btn btn--tertiary" href="{p}about.html#team">Meet the team</a></div>
        </div>
        {team_list(p)}
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="quotes-title">
      <div class="container split">
        <div>
          <span class="eyebrow">Clients</span>
          <h2 id="quotes-title">What clients say</h2>
        </div>
        <div class="stack-lg reveal">
          {quote('darren', 'quote quote--feature')}
          {quote('robert')}
        </div>
      </div>
    </section>

{cta(p, 'Ready to build on your strengths?', 'Tell us what you’re working on. We’ll set up a short call to understand your goals and suggest where to start.')}'''

# ---------------------------------------------------------------- SERVICE PAGES
SVC_DETAIL = {
 'strategy-execution': dict(
   img='arch-boardroom.webp', w=1400, h=1120,
   alt='An empty boardroom with a long table and chairs beside floor-to-ceiling windows',
   intro='Plans fail in the gap between the leadership retreat and the work of every day. We help you close that gap — with clear priorities, owners and measures your people help shape.',
   challenge=('Your strategy exists. Getting it done is the hard part.',
     ['Priorities compete for the same people and budget. Ownership is unclear once the plan leaves the leadership team. Progress is reported late, if at all — so by the time a project drifts, it is expensive to fix.',
      'We help leadership teams agree on what success looks like before the work starts, then build the routines that keep a plan moving.']),
   deliver=[('compass', 'Strategic planning facilitation', 'Structured sessions that bring leaders to agreement on priorities and trade-offs.'),
            ('target', 'Success measures agreed up front', 'Clear, shared definitions of success set with senior leaders before work begins.'),
            ('map', 'Implementation roadmaps', 'Work plans that sequence tasks, owners and milestones for each initiative.'),
            ('chart', 'Executive scorecards', 'A short set of indicators leaders review regularly to track progress.'),
            ('file', 'Leadership progress reports', 'Periodic summaries that show what moved, what stalled and what is next.'),
            ('cycle', 'Operating rhythm', 'Recurring working meetings that keep teams aligned as plans change.')],
   steps=[('Discover', 'Interview leaders and staff and review current plans to understand goals, strengths and constraints.'),
          ('Align', 'Facilitate agreement on priorities and the measures that will define success.'),
          ('Plan', 'Build the roadmap, owners, milestones and reporting rhythm.'),
          ('Deliver & measure', 'Support execution and report progress against the agreed measures.')],
   results=[('plans delivered', 'Strategic plans delivered'), ('on-time milestone rate', 'Milestones met on schedule'), ('client satisfaction score', 'Client satisfaction')],
   case=('34 Strong · CalPERS', 'Leadership training for California’s largest public pension fund',
         'Working with 34 Strong, OVP agreed success metrics with senior executives at CalPERS, then built a two-month work plan to design and deliver a management course for two cohorts of new Section Leaders.',
         None),
   quote='roy',
   faq=[('How does an engagement start?', 'With a needs assessment. We talk with your leaders and staff, review what is already in place and propose a scope based on what we find.'),
        ('How long does a strategy engagement take?', f'It depends on scope. Typical engagements run {T("typical engagement length")}.'),
        ('Do you work with public agencies?', 'Yes. Our clients include the Delaware Department of Labor and the California Department of Public Health. See our <a href="../government.html">government contracting</a> page for company details.')]),
 'organizational-performance': dict(
   img='arch-corridor.webp', w=1400, h=935,
   alt='A long, empty office corridor lined with glass partitions',
   intro='When work slows down, the cause is rarely one person or one tool. We diagnose how work actually flows, then design processes your team can sustain long after we leave.',
   challenge=('Everyone is busy. Results still lag.',
     ['Handoffs break down, work gets duplicated and nobody can say exactly where time goes. Quick fixes add steps instead of removing them.',
      'We use Continuous Improvement Process Design methods and problem-solving techniques to evaluate your processes and make recommendations for a reliable long-term payoff.']),
   deliver=[('clipboard', 'Organizational assessment', 'OVP’s proprietary assessment tools show where performance is strong and where it stalls.'),
            ('map', 'Process maps', 'Clear maps of how work moves today — and how it should move.'),
            ('cycle', 'Continuous improvement design', 'Kaizen-style process design that builds in small, steady gains.'),
            ('check', 'Countermeasure tools', 'Simple tools that help teams find root causes and fix them for good.'),
            ('chart', 'Executive scorecards', 'A shared view of the indicators that matter most.'),
            ('file', 'Standard templates', 'Documented ways of working so good practice survives staff changes.')],
   steps=[('Assess', 'Use our assessment tools, interviews and data to see how work really happens.'),
          ('Map', 'Map current processes and pinpoint the delays, rework and gaps.'),
          ('Redesign', 'Design improved processes and countermeasures with the people who do the work.'),
          ('Sustain', 'Set up scorecards and routines so improvements hold over time.')],
   results=[('processes redesigned', 'Processes redesigned'), ('time saved', 'Time saved per cycle'), ('client satisfaction score', 'Client satisfaction')],
   case=('PASO West Suburban Action Project', 'Systems that help a growing nonprofit work as one team',
         'OVP ran a needs assessment, introduced an engagement model to guide performance improvement, and brought in executive scorecards, countermeasure tools and process maps to systematize how PASO measures and improves its work.',
         None),
   quote='hillary',
   faq=[('What are your assessment tools?', 'OVP has developed a proprietary set of organizational assessment tools. We choose the ones that fit your questions and share the results with your leadership team.'),
        ('Will this disrupt day-to-day work?', 'We design sessions around your schedule and involve the people who do the work, so changes are practical from day one.'),
        ('Do you use a specific methodology?', 'We draw on Continuous Improvement (Kaizen) process design and structured problem-solving, adapted to your organization’s size and sector.')]),
 'leadership-change': dict(
   img='arch-towers-fog.webp', w=1400, h=933,
   alt='Glass office towers seen from below, rising into fog',
   intro='Change asks more of leaders and teams than any plan admits. We help people understand their strengths, lead through uncertainty and build a culture that keeps improving.',
   challenge=('Change stalls when people are left behind.',
     ['New structures, new leaders and new ways of working can leave teams unsure of their role. Engagement drops just when you need it most.',
      'We establish workplace norms that uncover your teams’ talents, maximize the organization’s potential and promote performance improvement — and give members and leaders the tools to sustain growth.']),
   deliver=[('compass', 'CliftonStrengths assessments', 'Individual and team strengths profiles that give everyone a shared language.'),
            ('users', 'Team engagement workshops', 'Sessions that set shared principles for how your team works together.'),
            ('presentation', 'Leadership training programs', 'Custom modules, workbooks and coaching for new and experienced leaders.'),
            ('message', 'Executive & team coaching', 'One-on-one and group coaching, including ICF-credentialed coaching.'),
            ('file', 'Individual development plans', 'Practical plans that turn feedback into next steps for each participant.'),
            ('chart', 'Program evaluation', 'Kirkpatrick-model surveys that measure reaction and learning.')],
   steps=[('Discover strengths', 'Profile individual and team strengths and listen to how people experience the change.'),
          ('Design', 'Build the program — workshops, modules, coaching — around your goals and culture.'),
          ('Develop', 'Deliver training and coaching, pairing new leaders with experienced ones where it helps.'),
          ('Measure', 'Evaluate what people learned and how they apply it, and adjust.')],
   results=[('leaders trained', 'Leaders trained'), ('engagement change', 'Change in team engagement'), ('participant rating', 'Participant rating')],
   case=('Illinois Action for Children', 'A six-month mentorship program built on trust',
         'OVP designed six training modules with virtual workshops and a leadership assessment, paired newer community mentors with experienced practitioners, and gave every participant an individual development plan.',
         None),
   quote='darren',
   faq=[('What is a strengths-based approach?', 'Instead of starting from what is missing, we start from what each person does best — then build roles, teams and development plans around those strengths.'),
        ('Can programs be delivered virtually?', 'Yes. Programs can combine virtual workshops, in-person sessions and one-on-one coaching.'),
        ('Are your coaches credentialed?', 'Our Chief of Staff & Operations is an International Coaching Federation (ICF) ACC-credentialed coach.')]),
 'strategic-communication': dict(
   img='arch-towers-dark.webp', w=1400, h=933,
   alt='Dark glass skyscrapers seen from street level',
   intro='Set the right tone and increase positive engagement with customers and collaborators alike. Our strategic communications work generates measurable results, while broadening your team’s impact.',
   challenge=('The message is right. It is not reaching people.',
     ['Internal and external communications pull in different directions. Staff hear about changes late. The public, media and partners get a partial picture — and trust suffers.',
      'We bring communications under one plan, give leaders the tools to speak with confidence and measure what is working.']),
   deliver=[('file', 'Communications charter', 'The mission, vision and values that guide how your organization communicates.'),
            ('map', 'Communication plans', 'Project-level plans with audiences, messages, channels and timing.'),
            ('message', 'Media & reputation management', 'Media relations, interviews and reputation campaigns.'),
            ('users', 'Town halls & internal communications', 'Formats that keep staff informed and heard during change.'),
            ('chart', 'Measurement criteria', 'Clear indicators for digital, social and earned media.'),
            ('video', 'Video & documentary content', 'Series and stories that show your work to the communities you serve.')],
   steps=[('Assess', 'Survey staff and review current channels to understand what reaches people today.'),
          ('Align', 'Agree on a charter, audiences and the measures that will define success.'),
          ('Deliver', 'Plan and run campaigns, media opportunities and internal communications.'),
          ('Report', 'Track engagement and report results to leadership regularly.')],
   results=[('engagement growth', 'Growth in audience engagement'), ('media placements', 'Media placements'), ('campaigns delivered', 'Campaigns delivered')],
   case=('Delaware Department of Labor', 'Pandemic-era communications for a state agency',
         'OVP centralized communications, set up weekly strategy meetings, ran organization-wide surveys, led town halls and media opportunities, and documented improved results over four years.',
         'our-work/case-study.html'),
   quote='robert',
   faq=[('Can you act as our communications lead?', 'Yes. At the Delaware Department of Labor, OVP served as coordinating director for communications; at PASO we serve as chief engagement and communications counsel.'),
        ('Do you work in Spanish?', f'{T("confirm Spanish-language services")}'),
        ('How do you measure communications?', 'We agree on measurement criteria at the start — for example, online engagement, media coverage and requests for leadership appearances — and report against them.')]),
}

def service_page(s):
    d = SVC_DETAIL[s['slug']]
    def body(p):
        deliver = ''.join(f'''<li><h3>{t}</h3><p>{tx}</p></li>''' for ic, t, tx in d['deliver'])
        steps = ''.join(f'<li class="step"><h3>{t}</h3><p>{tx}</p></li>' for t, tx in d['steps'])
        stats = ''.join(f'<div class="stat"><span class="stat-value">{T(v)}</span><span class="stat-label">{l}</span></div>' for v, l in d['results'])
        faq = ''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in d['faq'])
        others = [o for o in SERVICES if o['slug'] != s['slug']]
        ctag, ctitle, ctext, clink = d['case']
        link = f'<a class="btn btn--tertiary" href="{p}{clink}">Read the case study</a>' if clink else f'<a class="btn btn--tertiary" href="{p}our-work.html">See more of our work</a>'
        ch_title, ch_paras = d['challenge']
        return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('services.html', 'Services'), ('', s['name'])])}
        <div class="split split--even split--center">
          <div>
            <h1 id="page-title">{s['name']}</h1>
            <p class="lead">{d['intro']}</p>
            <div class="btn-row">
              <a class="btn btn--primary" href="{p}contact.html">Book a consultation</a>
            </div>
          </div>
          <figure class="page-hero-media"><img src="{p}assets/img/{d['img']}" alt="{d['alt']}" width="{d['w']}" height="{d['h']}" fetchpriority="high"></figure>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="challenge-title">
      <div class="container split split--top">
        <div>
          <span class="eyebrow">The challenge</span>
          <h2 id="challenge-title">{ch_title}</h2>
        </div>
        <div class="prose">{''.join(f'<p>{x}</p>' for x in ch_paras)}</div>
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="do-title">
      <div class="container">
        <div class="section-head"><span class="eyebrow">What we do</span><h2 id="do-title">What you get</h2></div>
        <ul class="deliverables reveal" role="list">{deliver}</ul>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="how-title">
      <div class="container">
        <div class="section-head"><span class="eyebrow">How it works</span><h2 id="how-title">Four steps, built around your team</h2></div>
        <ol class="steps steps--4 reveal">{steps}</ol>
      </div>
    </section>

    <section class="section theme-dark" aria-labelledby="results-title">
      <div class="container">
        <div class="section-head"><span class="eyebrow">Results</span><h2 id="results-title">What clients can expect to measure</h2></div>
        <div class="stats">{stats}</div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="case-title">
      <div class="container split split--top">
        <div>
          <span class="eyebrow">Related work · {ctag}</span>
          <h2 id="case-title">{ctitle}</h2>
          <p class="lead mt-4">{ctext}</p>
          <div class="mt-4">{link}</div>
        </div>
        <div>{quote(d['quote'], 'quote quote--feature')}</div>
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="faq-title">
      <div class="container split split--top">
        <div><span class="eyebrow">FAQ</span><h2 id="faq-title">Common questions</h2></div>
        <div class="accordion">{faq}</div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="other-title">
      <div class="container">
        <div class="section-head"><h2 id="other-title">Other services</h2></div>
        {service_cards(p, others)}
      </div>
    </section>

{cta(p, f'Talk to us about {s["name"].lower().replace("&", "and")}', 'Book a consultation and we’ll discuss your goals, your team and a sensible first step.')}'''
    page(f'services/{s["slug"]}.html', f'{s["name"]} | OVP Management Consulting', s['line'], 'services.html', body, alt=True)

# ---------------------------------------------------------------- SERVICES OVERVIEW
def services_page(p):
    return f'''    <section class="page-hero theme-light" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Services')])}
        <div class="split">
          <h1 id="page-title">Services</h1>
          <p class="lead">Four practice areas that work on their own or together — each grounded in a strengths-based approach and measured against goals we agree with you up front.</p>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-label="Service areas">
      <div class="container split">
        <figure class="media-frame"><img src="{p}assets/img/arch-office-glass.webp" alt="An empty open-plan office with glass-walled meeting rooms" width="1600" height="1068" loading="lazy"></figure>
        {service_cards(p, SERVICES, 'h2')}
      </div>
    </section>

{cta(p, 'Not sure where to start?', 'Most engagements begin with a needs assessment. Book a consultation and we’ll help you find the right starting point.')}'''

# ---------------------------------------------------------------- WHO WE SERVE
def who_page(p):
    blocks = [
     ('government', 'Government &amp; public agencies', 'arch-capitol.webp', 1180, 'Pennsylvania Avenue leading to the U.S. Capitol in Washington, D.C.',
      'Public agencies face pressure to communicate clearly, adapt quickly and develop leaders — often with lean teams. We have supported state agencies with communications, change management and leadership programs.',
      ['strategic-communication', 'leadership-change', 'strategy-execution'],
      ['Delaware Department of Labor', 'California Department of Public Health', 'CalPERS (with 34 Strong)']),
     ('business', 'Businesses', 'arch-glass-facade.webp', 1336, 'The glass facade of an office building against a pale sky',
      'Small and midsize firms need teams that work well together, processes that scale and the readiness to pursue larger contracts. We help them build all three.',
      ['organizational-performance', 'leadership-change', 'strategy-execution'],
      ['American Licorice Company', 'Riveredge Hospital', '7 Mindsets', '34 Strong']),
     ('nonprofit', 'Nonprofits &amp; community organizations', 'arch-residential.webp', 1867, 'A modern residential building with balconies seen from street level',
      'Mission-driven organizations need to tell their story to communities, media and donors, and to build capacity without burning out their people.',
      ['strategic-communication', 'organizational-performance', 'leadership-change'],
      ['Illinois Action for Children', 'PASO West Suburban Action Project', 'National Coalition of 100 Black Women – Delaware Chapter', 'Mas Que Salud']),
    ]
    out = []
    for i, (anchor, title, img, h, alt, text, svcs, clients) in enumerate(blocks):
        theme = 'theme-light' if i % 2 == 0 else 'theme-alt'
        svc_links = ''.join(f'<li><a href="{p}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES if s['slug'] in svcs)
        out.append(f'''    <section class="section {theme}" id="{anchor}" aria-labelledby="{anchor}-title">
      <div class="container split split--top">
        <figure class="media-frame"><img src="{p}assets/img/{img}" alt="{alt}" width="1400" height="{h}" loading="lazy"></figure>
        <div class="stack-lg">
          <div><h2 id="{anchor}-title">{title}</h2><p class="lead mt-4">{text}</p></div>
          <div><h3>Relevant services</h3><ul class="link-list mt-4">{svc_links}</ul></div>
          <div><h3>Clients in this sector</h3><div class="mt-4">{client_list(clients, 'client-list client-list--stack')}</div></div>
        </div>
      </div>
    </section>''')
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Who We Serve')])}
        <h1 id="page-title">Who we serve</h1>
        <p class="lead">We work with public agencies, businesses and nonprofits — organizations that depend on people to carry their mission forward.</p>
        <nav class="filter mt-4" aria-label="Jump to sector" style="margin-bottom:0">
          <a href="#government">Government</a><a href="#business">Businesses</a><a href="#nonprofit">Nonprofits</a>
        </nav>
      </div>
    </section>

{chr(10).join(out)}

{cta(p, 'Working in one of these sectors?', 'Book a consultation to talk about your goals and where we can help first.', theme='theme-accent')}'''

# ---------------------------------------------------------------- GOVERNMENT
def gov_page(p):
    rows = [('Legal name', 'OVP Management Consulting Group Inc.'), ('UEI', T('UEI')), ('CAGE code', T('CAGE code')),
            ('NAICS codes', T('NAICS codes')), ('Business certifications', T('small / minority business certifications')),
            ('Contract vehicles', T('GSA schedule or state vehicles')), ('Contracting contact', T('name, email, phone'))]
    table = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rows)
    pillars = service_cards(p, SERVICES)
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container split split--even">
        <div>
          {breadcrumb(p, [('index.html', 'Home'), ('', 'Government Contracting')])}
          <h1 id="page-title">Government contracting</h1>
          <p class="lead">Everything a contracting officer or teaming partner needs to evaluate OVP, in the order you need it.</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="{p}contact.html">Contact our team</a>
            <span class="btn btn--secondary" role="link" aria-disabled="true">{I('download')} Capability statement {T('PDF')}</span>
          </div>
        </div>
        <nav aria-label="On this page">
          <ol class="q-index" role="list">
            <li><a href="#contract"><b>1</b>Can we contract with OVP?</a></li>
            <li><a href="#capabilities"><b>2</b>What does OVP do?</a></li>
            <li><a href="#performance"><b>3</b>Where has OVP done it?</a></li>
            <li><a href="#roles"><b>4</b>What role can OVP play?</a></li>
          </ol>
        </nav>
      </div>
    </section>

    <section class="section theme-light" id="contract" aria-labelledby="q1">
      <div class="container split split--top">
        <div>
          <span class="q-label"><b>1</b>Eligibility</span>
          <h2 id="q1">Can we contract with OVP?</h2>
          <p class="lead mt-4">Company identifiers and registrations for procurement and teaming.</p>
        </div>
        <div class="table-wrap"><table class="data-table"><caption class="visually-hidden">OVP company data</caption><tbody>{table}</tbody></table></div>
      </div>
    </section>

    <section class="section theme-alt" id="capabilities" aria-labelledby="q2">
      <div class="container">
        <div class="section-head"><span class="q-label"><b>2</b>Capabilities</span><h2 id="q2">What does OVP do?</h2></div>
        {pillars}
      </div>
    </section>

    <section class="section theme-light" id="performance" aria-labelledby="q3">
      <div class="container split split--top">
        <div>
          <span class="q-label"><b>3</b>Past performance</span>
          <h2 id="q3">Where has OVP done it?</h2>
          <p class="lead mt-4">Public-sector work, delivered directly and with partners.</p>
          <ul class="mt-6 stack" role="list">
            <li class="chip"><b>State agency</b> Delaware Department of Labor</li>
            <li class="chip"><b>State agency</b> California Department of Public Health</li>
            <li class="chip"><b>Public pension fund</b> CalPERS, with 34 Strong</li>
          </ul>
        </div>
        <article class="card">
          <img src="{p}assets/img/arch-chamber.webp" alt="" width="1600" height="820" loading="lazy" style="aspect-ratio:16/9;object-fit:cover">
          <span class="tag">Case study</span>
          <h3><a href="{p}our-work/case-study.html">Delaware Department of Labor: communications and change during the pandemic</a></h3>
          <p>Centralized communications, staff surveys, town halls and media relations, with documented improvement over four years.</p>
          <span class="btn btn--tertiary" aria-hidden="true">Read the case study</span>
        </article>
      </div>
    </section>

    <section class="section theme-alt" id="roles" aria-labelledby="q4">
      <div class="container">
        <div class="section-head"><span class="q-label"><b>4</b>Contracting roles</span><h2 id="q4">What role can OVP play?</h2></div>
        <div class="grid grid--3">
          <article class="role">{chip_icon('landmark')}<h3>Prime contractor</h3><p>OVP leads the engagement and contracts directly with your agency.</p><p class="small">{T('confirm prime contract experience')}</p></article>
          <article class="role">{chip_icon('share', ' icon-chip--cyan')}<h3>Subcontractor / teaming partner</h3><p>OVP brings communications, leadership and process expertise to a larger team — as we did with 34 Strong for CalPERS.</p></article>
          <article class="role">{chip_icon('file')}<h3>Direct purchase</h3><p>Defined-scope work bought directly, such as a workshop series or an assessment.</p><p class="small">{T('purchase thresholds / card acceptance')}</p></article>
        </div>
      </div>
    </section>

    <section class="section theme-dark" aria-labelledby="cap-title">
      <div class="container split">
        <div>
          <h2 id="cap-title">Capability statement</h2>
          <p class="lead mt-4">A two-page summary of identifiers, core competencies, past performance and differentiators.</p>
        </div>
        <div class="btn-row">
          <span class="btn btn--secondary" role="link" aria-disabled="true">{I('download')} Download capability statement {T('PDF')}</span>
        </div>
      </div>
    </section>

{cta(p, 'Planning a solicitation or teaming arrangement?', 'Talk to us early. We’ll share past performance details and discuss how OVP can support your team.', btn='Contact our team')}'''

# ---------------------------------------------------------------- OUR WORK
CASES = [
 ('government', 'Government', 'Delaware Department of Labor', 'Strategic Communication · Leadership & Change',
  'Emergency communications and change management for a state agency during the pandemic, with documented gains over four years.', 'our-work/case-study.html'),
 ('business', 'Business', '34 Strong · CalPERS', 'Leadership & Change',
  'A management course for new Section Leaders at California’s public pension fund, designed with Kaizen methods and evaluated with the Kirkpatrick model.', None),
 ('nonprofit', 'Nonprofit', 'Illinois Action for Children', 'Leadership & Change',
  'A six-month mentorship training program with virtual workshops, a leadership assessment and individual development plans.', None),
 ('nonprofit', 'Nonprofit', 'PASO West Suburban Action Project', 'Strategic Communication · Organizational Performance',
  'Reputation management, a professional communications function and performance tools for a social justice organization.', None),
 ('nonprofit', 'Nonprofit', 'National Coalition of 100 Black Women – Delaware Chapter', 'Strategic Communication',
  'A five-part documentary series on the opioid epidemic in Delaware’s African American community, written and co-produced by OVP.', None),
]
def work_page(p):
    def card(c):
        _, tag, title, svc, text, link = c
        if link:
            h = f'<h3><a href="{p}{link}">{title}</a></h3>'
            foot = '<span class="btn btn--tertiary" aria-hidden="true">Read the case study</span>'
            cls = 'card card--service'
        else:
            h = f'<h3>{title}</h3>'
            foot = f'<p class="small">Full case study: {T("approve write-up")}</p>'
            cls = 'card'
        return f'<article class="{cls}"><span class="tag">{tag} · {svc}</span>{h}<p>{text}</p>{foot}</article>'
    seen = set()
    cards = []
    for i, c in enumerate(CASES):
        key = c[0]
        anchor = f' id="{key}"' if key not in seen else ''
        seen.add(key)
        html_ = card(c).replace('<article class="', f'<article{anchor} class="case-card ', 1)
        if i == 0:
            html_ = html_.replace('<article id="government" class="case-card card card--service">', f'<article id="government" class="case-card card card--service card--feature"><img src="{p}assets/img/arch-chamber.webp" alt="" width="1600" height="820" loading="lazy"><div class="card-body">', 1).replace('</article>', '</div></article>')
            html_ = html_.replace('class="case-card card card--service card--feature"', 'class="case-card card card--service card--feature span-8"')
        elif i == 1:
            html_ = html_.replace('class="case-card card"', 'class="case-card card span-4"', 1)
        else:
            html_ = html_.replace('class="case-card card"', 'class="case-card card span-4"', 1)
        cards.append(html_)
    sects = [f'<h2 class="visually-hidden">Case studies</h2><div class="grid">{"".join(cards)}</div>']
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Our Work')])}
        <h1 id="page-title">Our work</h1>
        <p class="lead">Selected engagements with public agencies, businesses and nonprofits — each built around the client’s people and measured against goals we set together.</p>
      </div>
    </section>

    <section class="section theme-light" aria-label="Case studies">
      <div class="container">
        <nav class="filter" aria-label="Filter by sector">
          <a href="#government">Government</a><a href="#business">Businesses</a><a href="#nonprofit">Nonprofits</a>
        </nav>
        {''.join(sects)}
      </div>
    </section>

{cta(p, 'Have a challenge like these?', 'Book a consultation and tell us about your organization.')}'''

def case_page(p):
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('our-work.html', 'Our Work'), ('', 'Delaware Department of Labor')])}
        <div class="split split--even split--center">
          <div>
            <span class="eyebrow">Case study · Government</span>
            <h1 id="page-title">Delaware Department of Labor</h1>
            <p class="lead">Communications and change support for a state agency through the pandemic — and four years of measurable improvement.</p>
            <ul class="chips mt-4" role="list">
              <li class="chip"><b>Sector</b> State government</li>
              <li class="chip"><b>Services</b> Strategic Communication, Leadership &amp; Change</li>
              <li class="chip"><b>Start</b> 2020</li>
            </ul>
          </div>
          <figure class="page-hero-media"><img src="{p}assets/img/arch-chamber.webp" alt="An empty legislative chamber with rows of desks facing the speaker’s chair" width="1600" height="820" fetchpriority="high"></figure>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="c1">
      <div class="container split split--top">
        <div><span class="eyebrow">01 · Challenge</span><h2 id="c1">A new leadership team, a workforce sent home</h2></div>
        <div class="prose">
          <p>Starting in 2020, the COVID-19 pandemic forced Delaware state officials to reassess in-office and remote work. Newly appointed agency leadership needed to explain fast-moving changes to staff and to the public.</p>
          <p>An OVP needs assessment found key gaps: no strategic change management plan to help mid-level leaders supervise a distributed workforce, internal and external communications that weren’t working together, and no effective, secure technology solution for some communications gaps.</p>
        </div>
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="c2">
      <div class="container split split--top">
        <div><span class="eyebrow">02 · OVP’s role</span><h2 id="c2">Coordinating director for communications</h2></div>
        <div class="prose">
          <p>OVP centralized the department’s communications functions and served as coordinating director, managing external marketing, communications and advertising on the department’s behalf to keep every platform consistent.</p>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="c3">
      <div class="container">
        <div class="section-head"><span class="eyebrow">03 · Approach</span><h2 id="c3">New protocols for how the department communicates</h2></div>
        <ul class="deliverables" role="list">
          <li><h3>Weekly strategy meetings</h3><p>Established weekly strategic communications meetings.</p></li>
          <li><h3>Organization-wide surveys</h3><p>Surveyed staff to understand the current state of communications.</p></li>
          <li><h3>Measurement criteria</h3><p>Set criteria for digital and social media communications.</p></li>
          <li><h3>Charter and planning templates</h3><p>A communications charter with mission, vision and values, plus planning documents for specific projects.</p></li>
          <li><h3>Town halls and media</h3><p>Led internal town hall meetings and all external media opportunities.</p></li>
          <li><h3>Six-part TV series</h3><p>Developed a series for local cable access showcasing the department’s reach across Delaware.</p></li>
        </ul>
      </div>
    </section>

    <section class="section theme-dark" aria-labelledby="c4">
      <div class="container split split--top">
        <div><span class="eyebrow">04 · Result</span><h2 id="c4">Documented improvement across four years</h2></div>
        <div class="prose">
          <p>OVP documented improved results across multiple categories, including:</p>
          <ul>
            <li>Engagement with online and social media audiences</li>
            <li>The number of legacy media interviews</li>
            <li>Exposure of department leadership across state and regional media</li>
            <li>Requests for the Secretary of Labor to take part in public events</li>
          </ul>
          <p>The department’s “Did You Know…?” advertising campaign became one of its most widely recognized engagement efforts and helped improve its reputation.</p>
          <p>{T('headline metrics for this engagement')}</p>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="c5">
      <div class="container">
        <h2 id="c5" class="visually-hidden">Client testimonial</h2>
        <figure class="quote quote--feature" style="max-width:52rem">
          <blockquote><p>{T('client testimonial — Delaware Department of Labor')}</p></blockquote>
          <figcaption><strong>{T('name')}</strong>{T('title, Delaware Department of Labor')}</figcaption>
        </figure>
      </div>
    </section>

{cta(p, 'Facing a similar challenge?', 'We help public agencies communicate through change. Book a consultation to talk it through.')}'''

# ---------------------------------------------------------------- INSIGHTS
def insights_page(p):
    arts = [('Leadership', 'What Crisis Leadership Looks Like'),
            ('Leadership &amp; equity', 'Leadership, Race, and Equity: Understanding the Flint Water Crisis'),
            ('Leadership', 'Courage of Convictions: A Response to Terror')]
    cards = ''.join(f'''<article class="card article"><span class="meta">{tag} · {T("publish date")}</span><h3><a href="https://www.ovpconsulting.com/blog" target="_blank" rel="noopener noreferrer">{t}<span class="visually-hidden"> (opens in a new tab)</span></a></h3><p class="muted">{T("article summary")}</p><span class="btn btn--tertiary" aria-hidden="true">Read article</span></article>''' for tag, t in arts)
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Insights')])}
        <h1 id="page-title">Insights</h1>
        <p class="lead">Perspectives on leadership, strengths and communication from the OVP team.</p>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="articles-title">
      <div class="container">
        <div class="section-head"><h2 id="articles-title">Latest articles</h2></div>
        <div class="grid grid--3">{cards}</div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="podcast-title" style="padding-top:0">
      <div class="container">
        <div class="podcast">
          {chip_icon('mic')}
          <div>
            <span class="eyebrow">Podcast</span>
            <h2 id="podcast-title" style="font-size:var(--fs-xl)">Using Strengths as a GPS in Leadership</h2>
            <p>Alejandro Bodipo-Memba joins The Strengths Whisperer to explore how strengths change and evolve over time — and how they shape a leader’s approach.</p>
            {ext('https://www.ovpconsulting.com/podcast', 'Listen to the episode', 'btn btn--secondary')}
          </div>
        </div>
      </div>
    </section>

{cta(p, 'Want to bring these ideas to your team?', 'Book a consultation to talk about workshops, coaching or a strengths assessment.')}'''

# ---------------------------------------------------------------- ABOUT
def about_page(p):
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container split split--even split--center">
        <div>
          {breadcrumb(p, [('index.html', 'Home'), ('', 'About')])}
          <h1 id="page-title">Next-level consulting for sustainable success</h1>
          <p class="lead">OVP Management Consulting Group is a strengths-based consulting firm. We help organizations strengthen team dynamics, build sustainable operations and reach their goals.</p>
        </div>
        <figure class="page-hero-media"><img src="{p}assets/img/arch-office-glass.webp" alt="An empty open-plan office with glass-walled meeting rooms" width="1600" height="1068" fetchpriority="high"></figure>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="story-title">
      <div class="container split split--top">
        <div><span class="eyebrow">Our story</span><h2 id="story-title">Where OVP comes from</h2></div>
        <div class="prose">
          <p>{T('company history — founding year, founding story, milestones')}</p>
          <p>The name says what we do. We work with organizations to create the <strong>optimal value proposition</strong> — the relationship between customers, collaborators and the company that brings an organization’s vision within reach.</p>
        </div>
      </div>
    </section>

    <section class="section theme-alt" aria-labelledby="mission-title">
      <div class="container split split--top">
        <div><span class="eyebrow">Mission &amp; values</span><h2 id="mission-title">Success measured against your goals</h2></div>
        <div class="prose">
          <p>We measure success by our adherence to predetermined goals that support effective leadership development and are linked to our clients’ financial, employee engagement or strategic communications goals.</p>
          <p>{T('core values')}</p>
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="method-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">How we work</span>
          <h2 id="method-title">Strengths first</h2>
          <p>We use CliftonStrengths and OVP’s own assessment tools to understand what your people do best, then build plans, processes and messages around those strengths.</p>
        </div>
        <ol class="steps steps--3">
          <li class="step"><h3>Discover strengths</h3><p>Assess people, processes and communications to see what works and where the gaps are.</p></li>
          <li class="step"><h3>Design the plan</h3><p>Agree on success measures with leadership and build a plan teams can own.</p></li>
          <li class="step"><h3>Deliver &amp; measure</h3><p>Put the plan into practice alongside your staff and report progress against shared measures.</p></li>
        </ol>
      </div>
    </section>

    <section class="section theme-alt" id="team" aria-labelledby="team-title">
      <div class="container">
        <div class="split">
          <div><span class="eyebrow">Leadership team</span><h2 id="team-title">The people behind the work</h2></div>
          {team_list(p, True)}
        </div>
      </div>
    </section>

    <section class="section theme-light" aria-labelledby="cred-title">
      <div class="container split split--top">
        <div><span class="eyebrow">Credentials</span><h2 id="cred-title">Credentials &amp; registrations</h2></div>
        <ul class="chips" role="list">
          <li class="chip"><b>ICF</b> ACC-credentialed coaching</li>
          <li class="chip"><b>Assessments</b> CliftonStrengths</li>
          <li class="chip"><b>Certifications</b> {T('business certifications')}</li>
          <li class="chip"><b>NAICS</b> {T('NAICS codes')}</li>
          <li class="chip"><b>UEI / CAGE</b> {T('UEI / CAGE')}</li>
        </ul>
      </div>
    </section>

{cta(p, 'Let’s talk about your team', 'Book a consultation with our senior team to discuss your goals.')}'''

# ---------------------------------------------------------------- CONTACT
def contact_page(p):
    days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    cells = ''.join(f'<span class="dow" aria-hidden="true">{d}</span>' for d in days) + '<span></span>' * 4
    for n in range(1, 32):
        cls = 'sel' if n == 8 else ('open' if n in (6, 7, 9, 13, 14, 15, 20, 21, 22, 27, 28, 29) else '')
        cells += f'<span class="{cls}">{n}</span>' if cls else f'<span>{n}</span>'
    def field(id_, label, typ='text', ac=None, req=True, msg=''):
        a = f' autocomplete="{ac}"' if ac else ''
        r = ' required' if req else ''
        rl = ' <span class="req">(required)</span>' if req else ' <span class="req">(optional)</span>'
        d = f' aria-describedby="{id_}-err"' if req else ''
        err = f'<p class="error-msg" id="{id_}-err" data-msg="{msg}"></p>' if req else ''
        return f'<div class="field"><label for="{id_}">{label}{rl}</label><input id="{id_}" name="{id_}" type="{typ}"{a}{r}{d}>{err}</div>'
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Contact')])}
        <h1 id="page-title">Let’s talk</h1>
        <p class="lead">Tell us about your organization and what you’d like to achieve. We reply within {T('response time')}.</p>
      </div>
    </section>

    <section class="section theme-light" aria-label="Contact options">
      <div class="container split split--even">
        <div>
          <h2 style="font-size:var(--fs-xl);margin-bottom:var(--s-4)">Send us a message</h2>
          <form class="form" data-local novalidate>
            <div class="form-row">
              {field('name', 'Name', ac='name', msg='Enter your name.')}
              {field('email', 'Email', 'email', 'email', msg='Enter an email address, like name@agency.gov.')}
            </div>
            <div class="form-row">
              {field('organization', 'Organization', ac='organization', req=False)}
              <div class="field"><label for="sector">Sector <span class="req">(required)</span></label>
                <select id="sector" name="sector" required aria-describedby="sector-err">
                  <option value="">Choose a sector</option><option>Government</option><option>Business</option><option>Nonprofit</option><option>Other</option>
                </select><p class="error-msg" id="sector-err" data-msg="Choose the sector that best fits your organization."></p></div>
            </div>
            <div class="field"><label for="message">How can we help? <span class="req">(required)</span></label>
              <textarea id="message" name="message" required aria-describedby="message-err"></textarea>
              <p class="error-msg" id="message-err" data-msg="Tell us briefly what you’d like to discuss."></p></div>
            <div class="field">
              <div class="check"><input type="checkbox" id="consent" name="consent" required aria-describedby="consent-err">
                <label for="consent">I agree to the <a href="{p}privacy.html">Privacy Policy</a>. <span class="req">(required)</span></label></div>
              <p class="error-msg" id="consent-err" data-msg="Check this box to agree to the Privacy Policy."></p>
            </div>
            <div><button class="btn btn--primary" type="submit">Send message</button></div>
            <div class="form-status" role="status" tabindex="-1" hidden><strong>Message sent.</strong>Thanks for reaching out — we’ll reply soon.</div>
          </form>
        </div>
        <aside class="stack-lg" aria-label="Book a consultation">
          <div class="booking">
                        <h2>Book a 30-minute consultation</h2>
            <p class="muted">Pick a time that works for you. You’ll get a calendar invitation and a short questionnaire.</p>
            <div class="cal" role="img" aria-label="Scheduling calendar showing available days in October 2026">
              <div class="cal-head"><span class="cal-label">Scheduling calendar</span><span>October 2026</span></div>
              <div class="cal-grid">{cells}</div>
              <div class="cal-slots"><span>9:00 AM</span><span>11:30 AM</span><span>2:00 PM</span><span>4:30 PM</span></div>
            </div>
          </div>
          <ul class="contact-list" role="list">
            <li><b>Email</b><span>{T('email')}</span></li>
            <li><b>Phone</b><span>{T('phone')}</span></li>
            <li><b>Address</b><span>{T('address')}</span></li>
          </ul>
        </aside>
      </div>
    </section>'''

def privacy_page(p):
    return f'''    <section class="page-hero theme-alt" aria-labelledby="page-title">
      <div class="container">
        {breadcrumb(p, [('index.html', 'Home'), ('', 'Privacy Policy')])}
        <h1 id="page-title">Privacy Policy</h1>
      </div>
    </section>
    <section class="section theme-light" aria-label="Policy text">
      <div class="container prose">
        <p>{T('privacy policy text')}</p>
        <h2 id="accessibility">Accessibility</h2>
        <p>{T('accessibility statement')}</p>
      </div>
    </section>'''

# ---------------------------------------------------------------- STYLEGUIDE (temporary)
def styleguide(p):
    return f'''    <section class="section theme-light"><div class="container stack-lg">
      <span class="eyebrow">Eyebrow label</span><h1>Heading one</h1><h2>Heading two</h2><h3>Heading three</h3>
      <p class="lead">Lead paragraph text for introductions.</p><p>Body copy with a <a href="#">text link</a> and a {T('placeholder')}.</p>
      <div class="btn-row"><a class="btn btn--primary" href="#">Primary</a><a class="btn btn--secondary" href="#">Secondary</a><a class="btn btn--tertiary" href="#">Tertiary</a><span class="btn btn--secondary" aria-disabled="true">Disabled {T('PDF')}</span></div>
      <div class="grid grid--4">{service_cards(p, SERVICES)}</div>
      <div class="stats"><div class="stat"><span class="stat-value">{T('years')}</span><span class="stat-label">Label</span></div></div>
      <ul class="chips"><li class="chip"><b>UEI</b> {T('UEI')}</li><li class="chip"><b>ICF</b> ACC</li></ul>
      <div class="accordion"><details><summary>Question</summary><div><p>Answer.</p></div></details></div>
      <div class="grid grid--2">{quote('darren')}{quote('robert')}</div>
    </div></section>
    <section class="section theme-dark"><div class="container stack-lg"><span class="eyebrow">Dark</span><h2>Dark theme</h2><p class="lead">Lead on dark.</p><div class="btn-row"><a class="btn btn--primary" href="#">Primary</a><a class="btn btn--secondary" href="#">Secondary</a><a class="btn btn--tertiary" href="#">Tertiary</a></div><ul class="chips"><li class="chip"><b>CAGE</b> {T('CAGE')}</li></ul></div></section>
{cta(p, 'CTA band', 'Supporting text.')}'''

# ---------------------------------------------------------------- BUILD
page('index.html', 'OVP Management Consulting | Strategy, performance, leadership and communication', 'Management consulting for public agencies, businesses and nonprofits. OVP helps organizations turn strategy into execution by building on their people’s strengths.', 'index.html', home)
for s in SERVICES:
    service_page(s)
page('services.html', 'Services | OVP Management Consulting', 'Strategy & Execution, Organizational Performance, Leadership & Change and Strategic Communication.', 'services.html', services_page, alt=True)
page('who-we-serve.html', 'Who We Serve | OVP Management Consulting', 'Consulting for government agencies, businesses and nonprofits.', 'who-we-serve.html', who_page, alt=True)
page('government.html', 'Government Contracting | OVP Management Consulting', 'Company identifiers, capabilities, past performance and contracting roles for public buyers.', 'government.html', gov_page, alt=True)
page('our-work.html', 'Our Work | OVP Management Consulting', 'Case studies from public agencies, businesses and nonprofits.', 'our-work.html', work_page, alt=True)
page('our-work/case-study.html', 'Delaware Department of Labor | Case study | OVP Management Consulting', 'How OVP supported the Delaware Department of Labor with communications and change management.', 'our-work.html', case_page, alt=True)
page('insights.html', 'Insights | OVP Management Consulting', 'Articles and podcast episodes on leadership, strengths and communication.', 'insights.html', insights_page, alt=True)
page('about.html', 'About | OVP Management Consulting', 'A strengths-based consulting firm: our story, mission, method and team.', 'about.html', about_page, alt=True)
page('contact.html', 'Contact | OVP Management Consulting', 'Send a message or book a 30-minute consultation with OVP.', 'contact.html', contact_page, alt=True)
page('privacy.html', 'Privacy Policy | OVP Management Consulting', 'Privacy policy and accessibility statement.', '', privacy_page, alt=True)
if os.environ.get('STYLEGUIDE'):
    page('styleguide.html', 'Styleguide', 'Components', '', styleguide)
print('built')
