#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def apply(name, pairs):
    path = ROOT / name
    text = path.read_text()
    for a, b in pairs:
        if a not in text:
            print('MISSING', name, a[:110].replace('\n',' '))
        else:
            text = text.replace(a, b)
    path.write_text(text)
    print('ok', name)

apply('packages.html', [
('<span class="mf-pill">Relocation Packages 2026</span>', '<span class="mf-pill" data-i18n="packages.pill">Relocation Packages 2026</span>'),
('<p class="mf-validity">Inbound · Annex A</p>', '<p class="mf-validity" data-i18n="packages.inbound">Inbound · Annex A</p>'),
('<p class="mf-tagline">Boutique Relocation &amp; Concierge · Since 2012</p>', '<p class="mf-tagline" data-i18n="packages.tagline">Boutique Relocation &amp; Concierge · Since 2012</p>'),
('<p class="mf-eyebrow">Inbound relocation to Switzerland</p>', '<p class="mf-eyebrow" data-i18n="packages.eyebrow">Inbound relocation to Switzerland</p>'),
('''              <p class="mf-hero-body">
                Three structured packages for your move to Ticino — from feasibility and settling-in
                essentials to full lifestyle, schooling and property support.
                Choose the level that matches your family and timeline; we tailor every step.
              </p>''',
 '              <p class="mf-hero-body" data-i18n="packages.hero">Three structured packages for your move to Ticino — from feasibility and settling-in essentials to full lifestyle, schooling and property support. Choose the level that matches your family and timeline; we tailor every step.</p>'),
('<p class="mf-answer-text">One partner for the whole journey —<br><em>clear scope, no surprises.</em></p>',
 '<p class="mf-answer-text" data-i18n-html="packages.answerHtml">One partner for the whole journey —<br><em>clear scope, no surprises.</em></p>'),
('<p class="pkg-tier-sub">Essentials to arrive &amp; settle</p>', '<p class="pkg-tier-sub" data-i18n="packages.bronzeSub">Essentials to arrive &amp; settle</p>'),
('<li>Feasibility study &amp; establishing relocation timeline</li>', '<li data-i18n="packages.b1">Feasibility study &amp; establishing relocation timeline</li>'),
('<li>Temporary housing (short-term rental)</li>', '<li data-i18n="packages.b2">Temporary housing (short-term rental)</li>'),
('<li>In-house VISA immigration support (ordinary or lump-sum taxation)***</li>', '<li data-i18n="packages.b3">In-house VISA immigration support (ordinary or lump-sum taxation)***</li>'),
('<li>Home finding assistance</li>', '<li data-i18n="packages.b4">Home finding assistance</li>'),
('<li>Settling in: local registrations</li>', '<li data-i18n="packages.b5">Settling in: local registrations</li>'),
('<li>Settling in: utilities registrations</li>', '<li data-i18n="packages.b6">Settling in: utilities registrations</li>'),
('<li>Healthcare registration (compulsory)</li>', '<li data-i18n="packages.b7">Healthcare registration (compulsory)</li>'),
('<li>Insurances registration (civil liability compulsory)</li>', '<li data-i18n="packages.b8">Insurances registration (civil liability compulsory)</li>'),
('<li>Support in driving licence conversion (Swiss and/or international)*</li>', '<li data-i18n="packages.b9">Support in driving licence conversion (Swiss and/or international)*</li>'),
('<li>Special rates with selected companies in Lugano through our introductions</li>', '<li data-i18n="packages.b10">Special rates with selected companies in Lugano through our introductions</li>'),
('<li>Corporate rates with starred hotels in the Lugano area for you, family &amp; friends</li>', '<li data-i18n="packages.b11">Corporate rates with starred hotels in the Lugano area for you, family &amp; friends</li>'),
('<p class="pkg-tier-sub">Bronze package +</p>', '<p class="pkg-tier-sub" data-i18n="packages.silverSub">Bronze package +</p>'),
('<li>School search, meet &amp; greet with school management</li>', '<li data-i18n="packages.s1">School search, meet &amp; greet with school management</li>'),
('<li>Local orientation &amp; integration</li>', '<li data-i18n="packages.s2">Local orientation &amp; integration</li>'),
('<li>Support in car registration, number plate conversion and homologation*</li>', '<li data-i18n="packages.s3">Support in car registration, number plate conversion and homologation*</li>'),
('<li>Support in car lease “all in”*</li>', '<li data-i18n="packages.s4">Support in car lease “all in”*</li>'),
('<li>Support with obtaining a Swiss phone number, prior to B permit*</li>', '<li data-i18n="packages.s5">Support with obtaining a Swiss phone number, prior to B permit*</li>'),
('<li>Support in travel planning (in-house IATA agency)*</li>', '<li data-i18n="packages.s6">Support in travel planning (in-house IATA agency)*</li>'),
('<p class="pkg-tier-sub">Silver package +</p>', '<p class="pkg-tier-sub" data-i18n="packages.goldSub">Silver package +</p>'),
('<li>Support in finding housestaff (in-house / external)*</li>', '<li data-i18n="packages.g1">Support in finding housestaff (in-house / external)*</li>'),
('<li>Guidance with financial services</li>', '<li data-i18n="packages.g2">Guidance with financial services</li>'),
('<li>Guidance with corporate services</li>', '<li data-i18n="packages.g3">Guidance with corporate services</li>'),
('<li>Support with family doctors, specialists and clinics</li>', '<li data-i18n="packages.g4">Support with family doctors, specialists and clinics</li>'),
('<li>Exclusive property finder support (buying)</li>', '<li data-i18n="packages.g5">Exclusive property finder support (buying)</li>'),
('<li>Support with after-school activities</li>', '<li data-i18n="packages.g6">Support with after-school activities</li>'),
('<li>Events and lifestyle planning</li>', '<li data-i18n="packages.g7">Events and lifestyle planning</li>'),
('<li>Help desk up to 8 months after arrival</li>', '<li data-i18n="packages.g8">Help desk up to 8 months after arrival</li>'),
('<p>*** Residency permits and lump-sum taxation invoiced separately.</p>', '<p data-i18n="packages.n1">*** Residency permits and lump-sum taxation invoiced separately.</p>'),
('<p>* Live costs will be invoiced separately.</p>', '<p data-i18n="packages.n2">* Live costs will be invoiced separately.</p>'),
('<p>VAT (8.1%) excluded.</p>', '<p data-i18n="packages.n3">VAT (8.1%) excluded.</p>'),
('<p class="mf-label">How we work</p>', '<p class="mf-label" data-i18n="packages.how">How we work</p>'),
('<h3>Discovery</h3>', '<h3 data-i18n="packages.h1Title">Discovery</h3>'),
('<p>We map your family, timeline and priorities — then recommend Bronze, Silver or Gold.</p>', '<p data-i18n="packages.h1Text">We map your family, timeline and priorities — then recommend Bronze, Silver or Gold.</p>'),
('<h3>Execute</h3>', '<h3 data-i18n="packages.h2Title">Execute</h3>'),
('<p>Immigration, housing, schooling and settling-in handled end to end by our Lugano team.</p>', '<p data-i18n="packages.h2Text">Immigration, housing, schooling and settling-in handled end to end by our Lugano team.</p>'),
('<h3>Settle</h3>', '<h3 data-i18n="packages.h3Title">Settle</h3>'),
('<p>Orientation, trusted introductions and ongoing help desk so you feel at home in Ticino.</p>', '<p data-i18n="packages.h3Text">Orientation, trusted introductions and ongoing help desk so you feel at home in Ticino.</p>'),
('<p class="mf-quote">“Inbound relocation, structured packages — clarity from day one.”</p>', '<p class="mf-quote" data-i18n="packages.quote">“Inbound relocation, structured packages — clarity from day one.”</p>'),
('<p>Headquarters · Via Balestra 5, third floor<br>6900 Lugano, Switzerland</p>', '<p data-i18n-html="membership.hqHtml">Headquarters · Via Balestra 5, third floor<br>6900 Lugano, Switzerland</p>'),
('<a href="contact.html" class="btn btn-primary">Enquire about a package</a>', '<a href="contact.html" class="btn btn-primary" data-i18n="packages.enquire">Enquire about a package</a>'),
])

apply('ticino.html', [
('<div class="section-label">With whom we work</div>', '<div class="section-label" data-i18n="partners.label">With whom we work</div>'),
('<h2 class="section-title">Trusted partners<br><em>across Ticino</em></h2>', '<h2 class="section-title" data-i18n-html="partners.title">Trusted partners<br><em>across Ticino</em></h2>'),
('<p class="body-text">We collaborate with a carefully selected network of schools and specialists, personally vetted by Helen and our team to support every stage of your relocation and life in Switzerland.</p>',
 '<p class="body-text" data-i18n="partners.p1">We collaborate with a carefully selected network of schools and specialists, personally vetted by Helen and our team to support every stage of your relocation and life in Switzerland.</p>'),
('<p class="body-text">Helen works with additional partners beyond those listed here. This is where we begin, opening the right doors for you and your family.</p>',
 '<p class="body-text" data-i18n="partners.p2">Helen works with additional partners beyond those listed here. This is where we begin, opening the right doors for you and your family.</p>'),
('<figcaption>Opening the door to your new life</figcaption>', '<figcaption data-i18n="partners.caption">Opening the door to your new life</figcaption>'),
('<div class="section-label">Education</div>', '<div class="section-label" data-i18n="partners.eduLabel">Education</div>'),
('<h2 class="section-title">International schools</h2>', '<h2 class="section-title" data-i18n="partners.eduTitle">International schools</h2>'),
('<p class="section-lead reveal" style="max-width:640px;margin-bottom:48px;">Schools we partner with across the canton, each with a direct link to learn more and get in touch.</p>',
 '<p class="section-lead reveal" style="max-width:640px;margin-bottom:48px;" data-i18n="partners.eduLead">Schools we partner with across the canton, each with a direct link to learn more and get in touch.</p>'),
('<span class="partner-link">Visit school →</span>', '<span class="partner-link" data-i18n="partners.visitSchool">Visit school →</span>'),
('<h2 class="section-title">Trusted partners</h2>', '<h2 class="section-title" data-i18n="partners.trustedTitle">Trusted partners</h2>'),
('<p class="section-lead reveal" style="max-width:640px;margin-bottom:48px;">Specialists we work with across Ticino and beyond.</p>',
 '<p class="section-lead reveal" style="max-width:640px;margin-bottom:48px;" data-i18n="partners.trustedLead">Specialists we work with across Ticino and beyond.</p>'),
('<p>Movers</p>', '<p data-i18n="partners.movers">Movers</p>'),
('<p>Hypothek partner</p>', '<p data-i18n="partners.hypo">Hypothek partner</p>'),
('<p>Real estate</p>', '<p data-i18n="partners.realEstate">Real estate</p>'),
('<p>The most beautiful villages in Switzerland</p>', '<p data-i18n="partners.svDesc">The most beautiful villages in Switzerland</p>'),
('<span class="partner-link">Visit website →</span>', '<span class="partner-link" data-i18n="partners.visitSite">Visit website →</span>'),
('<h2 class="section-title">Need guidance on<br><em>schools or partners?</em></h2>',
 '<h2 class="section-title" data-i18n-html="partners.ctaTitle">Need guidance on<br><em>schools or partners?</em></h2>'),
('<p class="section-lead">We help you find the right fit, confidentially and personally.</p>',
 '<p class="section-lead" data-i18n="partners.ctaLead">We help you find the right fit, confidentially and personally.</p>'),
('<a href="contact.html" class="btn btn-primary">Let\'s get in touch</a>',
 '<a href="contact.html" class="btn btn-primary" data-i18n="common.getInTouch">Let\'s get in touch</a>'),
])

apply('approach.html', [
('<p class="hero-eyebrow reveal">Our approach</p>', '<p class="hero-eyebrow reveal" data-i18n="approach.eyebrow">Our approach</p>'),
('<h1 class="page-hero-title reveal">Three paths.<br>One standard: <em>yours</em>.</h1>',
 '<h1 class="page-hero-title reveal" data-i18n-html="approach.heroHtml">Three paths.<br>One standard: <em>yours</em>.</h1>'),
('<p class="section-lead reveal" style="max-width:640px;margin:0 auto 48px;text-align:center;">Graduated levels of support, outlined privately during your confidential consultation, and tailored to your family\'s needs.</p>',
 '<p class="section-lead reveal" style="max-width:640px;margin:0 auto 48px;text-align:center;" data-i18n="approach.lead">Graduated levels of support, outlined privately during your confidential consultation, and tailored to your family\'s needs.</p>'),
('<h3>Foundations</h3>', '<h3 data-i18n="approach.foundations">Foundations</h3>'),
('<p>Core relocation guidance for a confident start in Ticino.</p>', '<p data-i18n="approach.essentialText">Core relocation guidance for a confident start in Ticino.</p>'),
('<button class="approach-more" aria-label="Learn more">+</button>', '<button class="approach-more" aria-label="Learn more" data-i18n-aria="approach.more">+</button>'),
('<p>Structured support covering permits, temporary housing, property finding, local and utility registrations, healthcare and insurance, with one trusted advisor throughout.</p>',
 '<p data-i18n="approach.essentialBack">Structured support covering permits, temporary housing, property finding, local and utility registrations, healthcare and insurance, with one trusted advisor throughout.</p>'),
('<a href="contact.html" class="btn btn-dark btn-sm">Enquire</a>', '<a href="contact.html" class="btn btn-dark btn-sm" data-i18n="approach.enquire">Enquire</a>'),
('<h3>Full accompaniment</h3>', '<h3 data-i18n="approach.full">Full accompaniment</h3>'),
('<p>Deep support for families making Ticino their home.</p>', '<p data-i18n="approach.completeText">Deep support for families making Ticino their home.</p>'),
('<p>Everything in Essential, plus school search, local orientation, car registration, travel planning and the integration support that transforms a new country into everyday life.</p>',
 '<p data-i18n="approach.completeBack">Everything in Essential, plus school search, local orientation, car registration, travel planning and the integration support that transforms a new country into everyday life.</p>'),
('<h3>White-glove</h3>', '<h3 data-i18n="approach.white">White-glove</h3>'),
('<p>End-to-end management for those who expect seamless.</p>', '<p data-i18n="approach.prestigeText">End-to-end management for those who expect seamless.</p>'),
('<p>Our most comprehensive level, homestaff, financial guidance, exclusive property search, lifestyle planning and an extended help desk long after arrival.</p>',
 '<p data-i18n="approach.prestigeBack">Our most comprehensive level, homestaff, financial guidance, exclusive property search, lifestyle planning and an extended help desk long after arrival.</p>'),
('<p class="approach-note reveal">Packages and fees are outlined privately during your confidential consultation.</p>',
 '<p class="approach-note reveal" data-i18n="approach.note">Packages and fees are outlined privately during your confidential consultation.</p>'),
('<div class="section-label">Beyond relocation</div>', '<div class="section-label" data-i18n="approach.beyond">Beyond relocation</div>'),
('<p class="body-text">Once your settlement in Ticino is established, we offer structured ongoing support for those who wish to delegate the management of daily, financial and relational needs to a single trusted point of contact.</p>',
 '<p class="body-text" data-i18n="approach.foLead">Once your settlement in Ticino is established, we offer structured ongoing support for those who wish to delegate the management of daily, financial and relational needs to a single trusted point of contact.</p>'),
('<li>Coordination with trustees, lawyers and tax advisors</li>', '<li data-i18n="approach.fo1">Coordination with trustees, lawyers and tax advisors</li>'),
('<li>Supervision of domestic service providers</li>', '<li data-i18n="approach.fo2">Supervision of domestic service providers</li>'),
('<li>Insurance, permit renewals and recurring obligations</li>', '<li data-i18n="approach.fo3">Insurance, permit renewals and recurring obligations</li>'),
('<li>Event planning, travel and family logistics</li>', '<li data-i18n="approach.fo4">Event planning, travel and family logistics</li>'),
('<li>Property management and local liaison</li>', '<li data-i18n="approach.fo5">Property management and local liaison</li>'),
('<li>Periodic reporting and a dedicated contact</li>', '<li data-i18n="approach.fo6">Periodic reporting and a dedicated contact</li>'),
('<a href="contact.html" class="btn btn-primary">Explore Family Office</a>', '<a href="contact.html" class="btn btn-primary" data-i18n="services.foCta">Explore Family Office</a>'),
('<h2 class="section-title">Not sure which level<br><em>is right for you?</em></h2>',
 '<h2 class="section-title" data-i18n-html="approach.ctaTitle">Not sure which level<br><em>is right for you?</em></h2>'),
('<p class="section-lead">We\'ll help you find the right path, confidentially and without obligation.</p>',
 '<p class="section-lead" data-i18n="approach.ctaLead">We\'ll help you find the right path, confidentially and without obligation.</p>'),
('<a href="contact.html" class="btn btn-primary">Let\'s get in touch</a>',
 '<a href="contact.html" class="btn btn-primary" data-i18n="common.getInTouch">Let\'s get in touch</a>'),
])
