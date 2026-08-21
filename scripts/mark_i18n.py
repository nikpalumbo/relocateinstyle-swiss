#!/usr/bin/env python3
"""Add data-i18n attributes and i18n.js to HTML pages. Idempotent."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON = [
    (
        '      <a href="index.html" data-page="home">Home</a>\n      <a href="about.html" data-page="about">About</a>\n      <a href="services.html" data-page="services">Services</a>\n      <a href="lifestyle.html" data-page="lifestyle">Lifestyle</a>\n      <a href="ticino.html" data-page="partners">Partners</a>\n      <a href="membership.html" data-page="membership">Membership</a>\n      <a href="contact.html" data-page="contact" class="nav-cta">Contact</a>',
        '      <a href="index.html" data-page="home" data-i18n="nav.home">Home</a>\n      <a href="about.html" data-page="about" data-i18n="nav.about">About</a>\n      <a href="services.html" data-page="services" data-i18n="nav.services">Services</a>\n      <a href="lifestyle.html" data-page="lifestyle" data-i18n="nav.lifestyle">Lifestyle</a>\n      <a href="ticino.html" data-page="partners" data-i18n="nav.partners">Partners</a>\n      <a href="membership.html" data-page="membership" data-i18n="nav.membership">Membership</a>\n      <a href="contact.html" data-page="contact" class="nav-cta" data-i18n="nav.contact">Contact</a>',
    ),
    (
        '      <a href="about.html">About</a>\n      <a href="services.html">Services</a>\n      <a href="lifestyle.html">Lifestyle</a>\n      <a href="ticino.html">Partners</a>\n      <a href="membership.html">Membership</a>\n      <a href="contact.html">Contact</a>',
        '      <a href="about.html" data-i18n="nav.about">About</a>\n      <a href="services.html" data-i18n="nav.services">Services</a>\n      <a href="lifestyle.html" data-i18n="nav.lifestyle">Lifestyle</a>\n      <a href="ticino.html" data-i18n="nav.partners">Partners</a>\n      <a href="membership.html" data-i18n="nav.membership">Membership</a>\n      <a href="contact.html" data-i18n="nav.contact">Contact</a>',
    ),
    (
        '<p class="footer-address">Headquarters · Via Balestra 5, third floor<br>6900 Lugano, Switzerland</p>',
        '<p class="footer-address" data-i18n-html="footer.address">Headquarters · Via Balestra 5, third floor<br>6900 Lugano, Switzerland</p>',
    ),
    (
        '<p>© 2026 Relocateinstyle SA · Since 2012</p>',
        '<p data-i18n="footer.copy">© 2026 Relocateinstyle SA · Since 2012</p>',
    ),
    (
        '<button class="nav-toggle" id="nav-toggle" aria-label="Menu">',
        '<button class="nav-toggle" id="nav-toggle" aria-label="Menu" data-i18n-aria="nav.menu">',
    ),
]

SCRIPT_OLD = [
    '  <script src="js/main.js?v=8"></script>',
    '  <script src="js/main.js?v=6"></script>',
    '  <script src="js/main.js"></script>',
]
SCRIPT_NEW = '  <script src="js/i18n.js?v=1"></script>\n  <script src="js/main.js?v=8"></script>'

HEAD_CSS = [
    ('href="css/style.css?v=65"', 'href="css/style.css?v=66"'),
    ('href="css/style.css?v=64"', 'href="css/style.css?v=66"'),
    ('href="css/style.css?v=44"', 'href="css/style.css?v=66"'),
]

PAGE = {
    "index.html": [
        ('<p class="hero-desc reveal">We guide you through Switzerland with a global mindset and a local perspective. We go the extra mile!</p>',
         '<p class="hero-desc reveal" data-i18n="home.heroDesc">We guide you through Switzerland with a global mindset and a local perspective. We go the extra mile!</p>'),
        ('<a href="contact.html" class="btn btn-primary">Begin your journey</a>',
         '<a href="contact.html" class="btn btn-primary" data-i18n="common.beginJourney">Begin your journey</a>'),
        ('<a href="#teasers" class="btn btn-ghost" data-scroll="#teasers">Explore</a>',
         '<a href="#teasers" class="btn btn-ghost" data-scroll="#teasers" data-i18n="common.explore">Explore</a>'),
        ('        <span>Scroll</span>',
         '        <span data-i18n="common.scroll">Scroll</span>'),
        ('        <span class="marquee-highlight">Boutique Relocation to Ticino</span>',
         '        <span class="marquee-highlight" data-i18n="home.marquee1">Boutique Relocation to Ticino</span>'),
        ('        <span>Permits & Immigration</span>',
         '        <span data-i18n="home.marquee2">Permits & Immigration</span>'),
        ('        <span>Property Finding</span>',
         '        <span data-i18n="home.marquee3">Property Finding</span>'),
        ('        <span>School Integration</span>',
         '        <span data-i18n="home.marquee4">School Integration</span>'),
        ('        <span class="marquee-highlight">10 Languages Spoken</span>',
         '        <span class="marquee-highlight" data-i18n="home.marquee5">10 Languages Spoken</span>'),
        ('        <span>Family Relocation</span>',
         '        <span data-i18n="home.marquee6">Family Relocation</span>'),
        ('        <span>Concierge services</span>',
         '        <span data-i18n="home.marquee7">Concierge services</span>'),
        ('        <span>White-Glove Service</span>',
         '        <span data-i18n="home.marquee8">White-Glove Service</span>'),
        ('          <h2 class="section-title reveal">Not a service.<br><em>An experience.</em></h2>',
         '          <h2 class="section-title reveal" data-i18n-html="home.introTitle">Not a service.<br><em>An experience.</em></h2>'),
        ('          <p class="section-lead reveal">A long-standing boutique firm in Lugano guiding private individuals and families through every dimension of life in Ticino, bespoke care, no standardised solutions.</p>',
         '          <p class="section-lead reveal" data-i18n="home.introLead">A long-standing boutique firm in Lugano guiding private individuals and families through every dimension of life in Ticino, bespoke care, no standardised solutions.</p>'),
        ('            <a href="about.html" class="btn btn-ghost">Our story, vision & values →</a>',
         '            <a href="about.html" class="btn btn-ghost" data-i18n="home.introCta">Our story, vision & values →</a>'),
        ('            <span class="stat-label">Relocations</span>',
         '            <span class="stat-label" data-i18n="home.statRelocations">Relocations</span>'),
        ('            <span class="stat-label">Levels of service</span>',
         '            <span class="stat-label" data-i18n="home.statLevels">Levels of service</span>'),
        ('            <span class="stat-label">Relocation · Family Office · Real Estate</span>',
         '            <span class="stat-label" data-i18n="home.statPillars">Relocation · Family Office · Real Estate</span>'),
        ('            <span class="stat-label">Languages</span>',
         '            <span class="stat-label" data-i18n="home.statLangs">Languages</span>'),
        ('              <span class="teaser-label">Services</span>',
         '              <span class="teaser-label" data-i18n="home.teaserServicesLabel">Services</span>'),
        ('              <h3>What we do</h3>',
         '              <h3 data-i18n="home.teaserServicesTitle">What we do</h3>'),
        ('              <p>Relocation, Family Office & Real Estate, three pillars, one trusted advisor.</p>',
         '              <p data-i18n="home.teaserServicesText">Relocation, Family Office & Real Estate, three pillars, one trusted advisor.</p>'),
        ('              <span class="teaser-label">Lifestyle</span>',
         '              <span class="teaser-label" data-i18n="home.teaserLifestyleLabel">Lifestyle</span>'),
        ('              <h3>Travel &amp; accommodation</h3>',
         '              <h3 data-i18n="home.teaserLifestyleTitle">Travel &amp; accommodation</h3>'),
        ('              <p>Hotels &amp; hidden gems, holiday homes, commercial flights, private jet and yacht charter.</p>',
         '              <p data-i18n="home.teaserLifestyleText">Hotels &amp; hidden gems, holiday homes, commercial flights, private jet and yacht charter.</p>'),
        ('              <span class="teaser-label">Membership</span>',
         '              <span class="teaser-label" data-i18n="home.teaserMembershipLabel">Membership</span>'),
        ('              <h3>Ongoing support</h3>',
         '              <h3 data-i18n="home.teaserMembershipTitle">Ongoing support</h3>'),
        ('              <p>Helpdesk, resources and year-round access to your trusted advisor.</p>',
         '              <p data-i18n="home.teaserMembershipText">Helpdesk, resources and year-round access to your trusted advisor.</p>'),
        ('              <span class="teaser-link">Explore →</span>',
         '              <span class="teaser-link" data-i18n="home.teaserServicesCta">Explore →</span>'),
        ('              <span class="teaser-link">Learn more →</span>',
         '              <span class="teaser-link" data-i18n="home.teaserMembershipCta">Learn more →</span>'),
        ('        <h2 class="section-title">Ready to begin<br><em>your new chapter</em></h2>',
         '        <h2 class="section-title" data-i18n-html="home.ctaTitle">Ready to begin<br><em>your new chapter</em></h2>'),
        ('        <p class="section-lead">Request a confidential consultation. We respond discreetly and personally.</p>',
         '        <p class="section-lead" data-i18n="home.ctaLead">Request a confidential consultation. We respond discreetly and personally.</p>'),
        ('        <a href="contact.html" class="btn btn-primary">Connect with us</a>',
         '        <a href="contact.html" class="btn btn-primary" data-i18n="common.connect">Connect with us</a>'),
    ],
    "about.html": [
        ('        <h1 class="page-hero-title reveal">About us</h1>',
         '        <h1 class="page-hero-title reveal" data-i18n="about.hero">About us</h1>'),
        ('          <p class="body-text reveal">We are professional, caring solution finders. We listen to your needs and are your advocate to help create your home environment.</p>',
         '          <p class="body-text reveal" data-i18n="about.p1">We are professional, caring solution finders. We listen to your needs and are your advocate to help create your home environment.</p>'),
        ('          <p class="body-text reveal">We have travelled and lived internationally, and are respectful of different cultures, backgrounds and special needs.</p>',
         '          <p class="body-text reveal" data-i18n="about.p2">We have travelled and lived internationally, and are respectful of different cultures, backgrounds and special needs.</p>'),
        ('          <p class="body-text reveal">We act with utmost integrity both in our interaction with you and on your behalf. We are connected and on top of the job. We select and partner only with those service providers who share our demand for excellence, ethics and commitment to our clients.</p>',
         '          <p class="body-text reveal" data-i18n="about.p3">We act with utmost integrity both in our interaction with you and on your behalf. We are connected and on top of the job. We select and partner only with those service providers who share our demand for excellence, ethics and commitment to our clients.</p>'),
        ('          <p class="body-text reveal">Our team communicates in <strong>10 languages</strong>, ensuring smooth, barrier-free communication at every stage of the relocation.</p>',
         '          <p class="body-text reveal" data-i18n-html="about.p4Html">Our team communicates in <strong>10 languages</strong>, ensuring smooth, barrier-free communication at every stage of the relocation.</p>'),
        ('          <p class="body-text reveal">Based in Lugano since 2012, we accompany international and high-net-worth families through relocation to Switzerland, at the intersection of professional relocation, immigration consultancy, concierge services and Family Office support.</p>',
         '          <p class="body-text reveal" data-i18n="about.p5">Based in Lugano since 2012, we accompany international and high-net-worth families through relocation to Switzerland, at the intersection of professional relocation, immigration consultancy, concierge services and Family Office support.</p>'),
        ('            <div class="section-label reveal">Our mission</div>',
         '            <div class="section-label reveal" data-i18n="about.missionLabel">Our mission</div>'),
        ('            <p class="body-text reveal">To make every relocation to Switzerland a seamless, dignified and extraordinarily well-organised experience, allowing our clients to focus on what truly matters: their new life — with no unpleasant surprises along the way.</p>',
         '            <p class="body-text reveal" data-i18n="about.mission1">To make every relocation to Switzerland a seamless, dignified and extraordinarily well-organised experience, allowing our clients to focus on what truly matters: their new life — with no unpleasant surprises along the way.</p>'),
        ('            <p class="body-text reveal">To make relocating to Ticino feel not like administration, but like opening the door to a life you chose, with clarity, protection, and always in style. We anticipate every detail so nothing catches you off guard — ensuring you are fully protected and your interests are safeguarded at every step.</p>',
         '            <p class="body-text reveal" data-i18n="about.mission2">To make relocating to Ticino feel not like administration, but like opening the door to a life you chose, with clarity, protection, and always in style. We anticipate every detail so nothing catches you off guard — ensuring you are fully protected and your interests are safeguarded at every step.</p>'),
        ('          <div class="section-label">Our values</div>',
         '          <div class="section-label" data-i18n="about.valuesLabel">Our values</div>'),
        ('          <h2 class="section-title">Privileged point of entry</h2>',
         '          <h2 class="section-title" data-i18n="about.valuesTitle">Privileged point of entry</h2>'),
        ('            <h3>Trusted professionals</h3>',
         '            <h3 data-i18n="about.v1Title">Trusted professionals</h3>'),
        ('            <p>Personally vetted and selected for you.</p>',
         '            <p data-i18n="about.v1Text">Personally vetted and selected for you.</p>'),
        ('            <h3>Transparency</h3>',
         '            <h3 data-i18n="about.v2Title">Transparency</h3>'),
        ('            <p>Every step is clear and fully understood. No hidden procedures, no surprises, only honest guidance in your language.</p>',
         '            <p data-i18n="about.v2Text">Every step is clear and fully understood. No hidden procedures, no surprises, only honest guidance in your language.</p>'),
        ('            <h3>Bespoke care</h3>',
         '            <h3 data-i18n="about.v3Title">Bespoke care</h3>'),
        ('            <p>No templates, no one-size-fits-all packages. Every family receives a mandate shaped entirely around their situation.</p>',
         '            <p data-i18n="about.v3Text">No templates, no one-size-fits-all packages. Every family receives a mandate shaped entirely around their situation.</p>'),
        ('            <h3>Discretion</h3>',
         '            <h3 data-i18n="about.v4Title">Discretion</h3>'),
        ('            <p>All personal and financial information is handled with the utmost confidentiality, in full compliance with Swiss data protection law.</p>',
         '            <p data-i18n="about.v4Text">All personal and financial information is handled with the utmost confidentiality, in full compliance with Swiss data protection law.</p>'),
        ('        <div class="section-label reveal">Our team</div>',
         '        <div class="section-label reveal" data-i18n="about.teamLabel">Our team</div>'),
        ('        <h2 class="section-title reveal">The people behind your move</h2>',
         '        <h2 class="section-title reveal" data-i18n="about.teamTitle">The people behind your move</h2>'),
        ('              <p class="team-role">Founder Managing Partner</p>',
         '              <p class="team-role" data-i18n="about.roleFounder">Founder Managing Partner</p>'),
        ('              <p class="team-bio">A polyglot founder with Swiss and English heritage and a pragmatic, business-minded approach. Having lived internationally herself, Helen leads Relocateinstyle SA in Lugano, guiding every client from first consultation to settled life in Ticino with discretion, warmth and precision.</p>',
         '              <p class="team-bio" data-i18n="about.bioHelen">A polyglot founder with Swiss and English heritage and a pragmatic, business-minded approach. Having lived internationally herself, Helen leads Relocateinstyle SA in Lugano, guiding every client from first consultation to settled life in Ticino with discretion, warmth and precision.</p>'),
        ('              <p class="team-role">Relationship Manager</p>',
         '              <p class="team-role" data-i18n="about.roleRaffaella">Relationship Manager</p>'),
        ('              <p class="team-bio">For Raffaella, relationship management is about connecting people with new worlds and helping them feel at home. After living in Shanghai, Brazil and beyond, she knows firsthand how vital empathetic, expert support is when you relocate. Organised and fluent in five languages, she listens deeply, anticipates each client\'s needs, and builds lasting relationships founded on trust and understanding.</p>',
         '              <p class="team-bio" data-i18n="about.bioRaffaella">For Raffaella, relationship management is about connecting people with new worlds and helping them feel at home. After living in Shanghai, Brazil and beyond, she knows firsthand how vital empathetic, expert support is when you relocate. Organised and fluent in five languages, she listens deeply, anticipates each client\'s needs, and builds lasting relationships founded on trust and understanding.</p>'),
        ('              <p class="team-role">Back Office</p>',
         '              <p class="team-role" data-i18n="about.roleSimona">Back Office</p>'),
        ('              <p class="team-bio">Simona coordinates relocation operations with precision and care. With a trained architectural eye, she brings clarity and structure to every move — organising timelines, documents and local logistics so nothing is left to chance. As coordinator and back office lead, she is the steady point of contact that keeps your relocation running smoothly from first enquiry to settled life in Ticino.</p>',
         '              <p class="team-bio" data-i18n="about.bioSimona">Simona coordinates relocation operations with precision and care. With a trained architectural eye, she brings clarity and structure to every move — organising timelines, documents and local logistics so nothing is left to chance. As coordinator and back office lead, she is the steady point of contact that keeps your relocation running smoothly from first enquiry to settled life in Ticino.</p>'),
        ('              <a href="contact.html" class="btn btn-dark btn-sm">Get in touch</a>',
         '              <a href="contact.html" class="btn btn-dark btn-sm" data-i18n="about.getInTouch">Get in touch</a>'),
        ('          <div class="section-label">External team</div>',
         '          <div class="section-label" data-i18n="about.externalLabel">External team</div>'),
        ('          <h3 class="team-external-title">Authorised business developers</h3>',
         '          <h3 class="team-external-title" data-i18n="about.externalTitle">Authorised business developers</h3>'),
        ('              <p class="team-role">Business Developer</p>',
         '              <p class="team-role" data-i18n="about.roleBd">Business Developer</p>'),
        ('          <div class="section-label reveal">Why Lugano & Canton Ticino</div>',
         '          <div class="section-label reveal" data-i18n="about.whyLabel">Why Lugano & Canton Ticino</div>'),
        ('          <h2 class="section-title reveal">A destination chosen with intention</h2>',
         '          <h2 class="section-title reveal" data-i18n="about.whyTitle">A destination chosen with intention</h2>'),
        ('            <li>Swiss political, fiscal and legal stability</li>',
         '            <li data-i18n="about.why1">Swiss political, fiscal and legal stability</li>'),
        ('            <li>Quality of life among the highest in Europe</li>',
         '            <li data-i18n="about.why2">Quality of life among the highest in Europe</li>'),
        ('            <li>Mediterranean climate and the natural beauty of Ticino</li>',
         '            <li data-i18n="about.why3">Mediterranean climate and the natural beauty of Ticino</li>'),
        ('            <li>Proximity to Milan and major European hubs</li>',
         '            <li data-i18n="about.why4">Proximity to Milan and major European hubs</li>'),
        ('            <li>Tax opportunities: attractive fiscal rates and lump-sum taxation</li>',
         '            <li data-i18n="about.why5">Tax opportunities: attractive fiscal rates and lump-sum taxation</li>'),
        ('            <li>Discretion, security and privacy</li>',
         '            <li data-i18n="about.why6">Discretion, security and privacy</li>'),
        ('          <a href="ticino.html" class="btn btn-ghost reveal">Our partners →</a>',
         '          <a href="ticino.html" class="btn btn-ghost reveal" data-i18n="about.partnersCta">Our partners →</a>'),
        ('        <h2 class="section-title">Let\'s get in touch</h2>',
         '        <h2 class="section-title" data-i18n="about.ctaTitle">Let\'s get in touch</h2>'),
        ('        <p class="section-lead">Confidential, personal, and without obligation.</p>',
         '        <p class="section-lead" data-i18n="about.ctaLead">Confidential, personal, and without obligation.</p>'),
        ('        <a href="contact.html" class="btn btn-primary">Contact us</a>',
         '        <a href="contact.html" class="btn btn-primary" data-i18n="common.contactUs">Contact us</a>'),
    ],
}


def patch_file(path: Path, extra):
    text = path.read_text()
    orig = text
    if 'js/i18n.js' not in text:
        replaced = False
        for old in SCRIPT_OLD:
            if old in text:
                text = text.replace(old, SCRIPT_NEW, 1)
                replaced = True
                break
        if not replaced:
            print('NO SCRIPT', path.name)
    for a, b in HEAD_CSS:
        text = text.replace(a, b)
    for a, b in COMMON + extra:
        if a not in text:
            if b not in text:
                print('MISSING', path.name, a[:80].replace('\n', ' '))
        else:
            text = text.replace(a, b)
    if text != orig:
        path.write_text(text)
        print('updated', path.name)
    else:
        print('unchanged', path.name)


def main():
    for f in ROOT.glob('*.html'):
        extra = PAGE.get(f.name, [])
        patch_file(f, extra)


if __name__ == '__main__':
    main()
