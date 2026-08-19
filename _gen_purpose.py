# -*- coding: utf-8 -*-
"""Generate purpose-based challenge coin detail pages (6 purposes).
Each page: gallery (3 dedicated images) + info + tabs + related + CTA + JSON-LD.
"""
import os
import json

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "purpose")

RATING_BREAKDOWN = [("5 star", 92), ("4 star", 5), ("3 star", 2), ("2 star", 1), ("1 star", 0)]

REVIEWS = [
    ("James R.", "Exactly the look we wanted for our department. The proof came back fast and the final coins exceeded expectations.", "2 weeks ago"),
    ("Melissa T.", "Ordered for our annual sales awards — the team loved them. Great communication from start to finish.", "1 month ago"),
    ("Robert K.", "Quality is superb and the turnaround was quicker than promised. Will order again.", "1 month ago"),
]

PURPOSES = [
    {
        "slug": "business-coins", "name": "Business Coins", "category": "Business",
        "title": "Custom Business Challenge Coins for Teams & Recognition",
        "meta": "Custom business challenge coins that reward performance, rally your team, and put your brand in their pocket. No minimum order, free design and 12-hour proof.",
        "keywords": "business challenge coins, corporate challenge coins, employee recognition coins, company award coins, branded coins",
        "short": "Branded coins that reward performance, rally teams, and turn clients into loyal partners.",
        "images": ["business-coins-1.jpg", "business-coins-2.jpg", "business-coins-3.jpg"],
        "overview": [
            "Business challenge coins started as a military tradition, but companies have made them their own. A well-made coin turns a sales milestone, a years-of-service anniversary, or a client thank-you into something people keep on their desk instead of in a drawer.",
            "Because the design is fully custom, the coin carries your logo, your colors, and your message in a way that a plaque or certificate cannot. Enamel color matching means your brand blue is your brand blue, right down to the Pantone number.",
            "Companies order them in every size, from small runs of executive gifts to thousands of pieces for global teams. Whichever route you take, the result is the same: a physical token of appreciation that says more than an email ever will.",
        ],
        "features": [
            ["Brand color matching", "Enamel matched to Pantone so your logo colors stay exact."],
            ["Custom shapes", "Round, die-cut, or shaped like your logo — any outline works."],
            ["Fast proofs", "Free digital proof within 12 hours, revisions included."],
            ["No minimum order", "Order one executive coin or thousands for a global team."],
            ["Premium finishes", "Gold, silver, antique, or black nickel plating to fit your brand."],
            ["Worldwide shipping", "Reliable delivery to offices and warehouses anywhere."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Soft or hard, matched to Pantone"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, copper, antique, black nickel"], ["Texture", "Recessed, flat, or 3D relief"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm (3D to 6 mm)"], ["Shapes", "Round, die-cut, custom"]]),
            ("Options", [["Edge styles", "12 options"], ["Back side", "Logo, engraving, or blank"], ["Extras", "Bottle opener, magnets, spinners"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "Factory-direct pricing", "Worldwide shipping"],
        "applications": ["Sales awards", "Annual meetings", "Client gifts", "Onboarding kits", "Brand promotion", "Distributor incentives"],
        "faq": [
            ["Can you match my exact brand colors?", "Yes. We match enamel to Pantone colors, so your logo and brand colors stay consistent from proof to finished coin."],
            ["What is the smallest order I can place?", "There is no minimum. Many companies start with a small run for executive gifts, then scale up."],
            ["How long does a business coin order take?", "After proof approval, production is typically 7\u201310 business days, plus shipping."],
            ["Can I use my company logo as the coin shape?", "Absolutely. Die-cut coins can follow the outline of your logo or any custom shape."],
        ],
        "related": ["soft-enamel-coins", "hard-enamel-coins", "uv-printed-coins"],
    },
    {
        "slug": "military-coins", "name": "Military Coins", "category": "Military",
        "title": "Custom Military Challenge Coins & Unit Coins",
        "meta": "Custom military challenge coins honoring service and unit pride. Eagle, wings, and insignia designs with no minimum order and free 12-hour proof.",
        "keywords": "military challenge coins, army coins, unit coins, custom military coins, service coins",
        "short": "Unit coins that honor service, celebrate camaraderie, and carry tradition in every pocket.",
        "images": ["military-coins-1.jpg", "military-coins-2.jpg", "military-coins-3.jpg"],
        "overview": [
            "The challenge coin tradition was born in the military, and unit coins are still its most powerful expression. A coin stamped with your unit's insignia becomes part of the identity — carried, traded, and checked on demand.",
            "Military coins often combine sculpted 3D relief for the emblem with enamel color for the details, which gives them the weight and presence the tradition demands. Black nickel and antique finishes are popular for a rugged, service-ready look.",
            "From recruit graduation coins to retirement keepsakes, each order is built around the unit's story. We help you refine the artwork so every detail — wings, motto, border — reads clearly at coin scale.",
        ],
        "features": [
            ["Sculpted relief", "3D emblem detail that catches light and reads from across a room."],
            ["Tactical finishes", "Black nickel, antique bronze, and gunmetal plating options."],
            ["Unit mottos", "Engraved or enameled text around the border or on the back."],
            ["Die-struck detail", "Crisp lines on small insignia, wings, and stars."],
            ["No minimum order", "A single coin for a retirement or thousands for a brigade."],
            ["Rugged durability", "Built for daily carry in the field, not just display."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Soft, hard, or no color"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, antique, black nickel"], ["Relief", "Flat 2D or sculpted 3D"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 3\u2033 (38\u201376 mm)"], ["Thickness", "3\u20136 mm for 3D relief"], ["Shapes", "Round, shield, die-cut"]]),
            ("Options", [["Edge styles", "Rope, chain, reeded and more"], ["Back side", "Unit motto, rosters, or seal"], ["Extras", "Bottle opener, lanyard hole"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "3D relief available", "Worldwide shipping"],
        "applications": ["Unit insignia", "Deployment coins", "Recruit graduation", "Retirement honors", "Reunions", "Memorials"],
        "faq": [
            ["Can you recreate my unit's insignia?", "Yes. Send us your artwork, patch, or photo and we will redraw it to coin-ready vector quality, then show you a free proof."],
            ["What finish is most popular for military coins?", "Antique bronze and black nickel are the most requested for a rugged, service look, with gold and silver for formal pieces."],
            ["Can 3D relief and enamel be combined?", "Absolutely. Most military coins use 3D relief for the emblem and enamel color for selected details."],
            ["Is there a minimum order?", "No minimum. We make everything from single retirement keepsakes to large unit runs."],
        ],
        "related": ["3d-coins", "no-color-coins", "minted-coins"],
    },
    {
        "slug": "police-coins", "name": "Police Coins", "category": "Police",
        "title": "Custom Police & Law Enforcement Challenge Coins",
        "meta": "Custom police challenge coins honoring officers and department pride. Shield badges, stars, and unit seals with no minimum order and free proof.",
        "keywords": "police challenge coins, law enforcement coins, custom police coins, department coins, officer coins",
        "short": "Department coins that honor duty, build brotherhood, and recognize officers who serve.",
        "images": ["police-coins-1.jpg", "police-coins-2.jpg", "police-coins-3.jpg"],
        "overview": [
            "Law enforcement units have adopted the challenge coin as a way to honor officers and build morale. A department coin stamped with the shield or badge becomes a point of pride that officers carry through every shift.",
            "The most popular police coin designs center on the shield, the star, or the department seal, usually in gold plating with deep blue and gold enamel. Hard enamel gives a polished, formal look that suits the gravity of the badge.",
            "Coins are used for promotions, retirements, SWAT and K-9 teams, memorials, and community outreach. Each one is custom-made, so the department's identity — motto, unit number, founding year — is worked into the design.",
        ],
        "features": [
            ["Badge-style relief", "Shield and star emblems struck with crisp detail."],
            ["Formal finishes", "Gold and silver plating for a polished, official look."],
            ["Unit-specific text", "Unit number, motto, and dates engraved or enameled."],
            ["Hard enamel option", "Smooth, glass-like surface that resists daily wear."],
            ["No minimum order", "Single commemorative coins to full department runs."],
            ["Commemorative quality", "Built to be kept, displayed, and handed down."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Soft or hard, Pantone matched"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, antique, black nickel"], ["Relief", "Flat or sculpted emblem"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 2.5\u2033 (38\u201364 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, shield, die-cut"]]),
            ("Options", [["Edge styles", "Standard, rope, reeded"], ["Back side", "Badge, motto, or memorial text"], ["Extras", "Lanyard hole, velvet pouch"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "Hard or soft enamel", "Worldwide shipping"],
        "applications": ["Department insignia", "Promotion coins", "Retirement honors", "Memorial coins", "Team and unit coins", "Community outreach"],
        "faq": [
            ["Can the coin feature our department seal?", "Yes. Send us the seal or badge artwork and we will prepare it for coin production, with a free proof for approval."],
            ["What plating looks most official?", "Gold and silver are the most popular for police coins, giving a formal finish that matches the badge."],
            ["Can you add a specific officer's name?", "Yes. Names, dates, and badge numbers can be engraved or enameled on the back of the coin."],
            ["Do you make memorial coins?", "We do. Memorial coins can include a photo-style portrait, dates, and a message of remembrance."],
        ],
        "related": ["hard-enamel-coins", "3d-coins", "no-color-coins"],
    },
    {
        "slug": "firefighter-coins", "name": "Firefighter Coins", "category": "Firefighter",
        "title": "Custom Firefighter Challenge Coins & Department Coins",
        "meta": "Custom firefighter challenge coins honoring courage and brotherhood. Maltese cross, axe, and ladder designs with no minimum order and free proof.",
        "keywords": "firefighter challenge coins, fire department coins, custom firefighter coins, fire service coins, maltese cross coins",
        "short": "Brave-service coins that honor firefighters, mark department milestones, and build brotherhood.",
        "images": ["firefighter-coins-1.jpg", "firefighter-coins-2.jpg", "firefighter-coins-3.jpg"],
        "overview": [
            "Fire departments have embraced challenge coins as tokens of brotherhood. The Maltese cross, the axe, and the ladder are the classic symbols, and a well-made coin gives them the weight they deserve.",
            "Red and gold dominate firefighter coin designs — red for courage, gold for the honor of the service. Soft enamel with a raised metal border is the classic choice, giving the coin a texture that matches its meaning.",
            "Departments use coins for academy graduations, promotions, retirements, and memorials. Each design can carry the department name, motto, station number, or a fallen brother's tribute.",
        ],
        "features": [
            ["Maltese cross detail", "The classic fire service emblem, struck with precision."],
            ["Vivid enamel", "Deep reds and golds that hold their color for years."],
            ["Department identity", "Station numbers, mottos, and names worked into the design."],
            ["Tactile finish", "Raised metal ridges give the coin a substantial feel."],
            ["No minimum order", "One honor coin or a full department order."],
            ["Keepsake quality", "Built to be carried, displayed, and remembered."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Soft or hard, Pantone matched"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, antique, black nickel"], ["Relief", "Flat or sculpted emblem"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 2.5\u2033 (38\u201364 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, shield, die-cut"]]),
            ("Options", [["Edge styles", "Standard, rope, reeded"], ["Back side", "Station motto or memorial text"], ["Extras", "Lanyard hole, velvet pouch"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "Classic fire service symbols", "Worldwide shipping"],
        "applications": ["Academy graduation", "Promotion coins", "Retirement honors", "Memorial coins", "Station milestones", "Charity fundraisers"],
        "faq": [
            ["Can you design a coin around our department's badge?", "Yes. Share your badge, patch, or artwork and we will adapt it into a coin-ready design with a free proof."],
            ["What are the most common firefighter coin colors?", "Red and gold are the most traditional, with black accents for a bold, modern look."],
            ["Can you engrave a name on the back?", "Yes. Names, dates, station numbers, and memorial tributes can be engraved or enameled on the reverse."],
            ["Do you offer memorial coins?", "We do. We can include a portrait, dates, and a personal message with care and respect."],
        ],
        "related": ["soft-enamel-coins", "hard-enamel-coins", "3d-coins"],
    },
    {
        "slug": "honor-awards-coins", "name": "Honor &amp; Awards Coins", "category": "Honor & Awards",
        "title": "Custom Honor & Award Challenge Coins",
        "meta": "Custom honor and award challenge coins that recognize achievement with style. Star medals, laurels, and premium finishes with no minimum order.",
        "keywords": "award challenge coins, honor coins, achievement coins, recognition coins, custom award coins",
        "short": "Recognition coins that turn achievements into keepsakes worth displaying.",
        "images": ["honor-awards-coins-1.jpg", "honor-awards-coins-2.jpg", "honor-awards-coins-3.jpg"],
        "overview": [
            "Some achievements deserve more than a certificate. An award coin is a physical mark of recognition — something the recipient can hold, display, and keep for decades.",
            "The most striking award coins use gold or silver plating with hard enamel for a jewelry-like finish. Stars, laurel wreaths, and engraved names give each piece a formal, celebratory feel.",
            "Organizations use them for annual awards, leadership recognition, volunteer honors, and milestone achievements. Because every coin is custom, the design can be as unique as the accomplishment it marks.",
        ],
        "features": [
            ["Premium plating", "Gold and silver finishes with a jewelry-grade look."],
            ["Hard enamel option", "Smooth, polished surface ideal for formal awards."],
            ["Engraved names", "Recipient names and dates engraved on the reverse."],
            ["Star and laurel motifs", "Classic symbols of achievement, struck in relief."],
            ["Presentation ready", "Pairs beautifully with velvet boxes or acrylic stands."],
            ["No minimum order", "Single awards or full recognition programs."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Hard or soft, Pantone matched"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, rose gold, antique"], ["Relief", "Flat, sculpted, or debossed"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 3\u2033 (38\u201376 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, star, shield, die-cut"]]),
            ("Options", [["Edge styles", "Standard, rope, reeded"], ["Back side", "Engraved name and date"], ["Extras", "Velvet box, acrylic stand"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "Premium plating options", "Presentation packaging"],
        "applications": ["Annual awards", "Leadership recognition", "Volunteer honors", "Retirement tributes", "Program milestones", "Executive gifts"],
        "faq": [
            ["Can you engrave the recipient's name?", "Yes. Names, titles, and dates are commonly engraved on the back for a personal, lasting touch."],
            ["What finish looks most premium?", "Gold and silver hard-enamel coins have a jewelry-like finish that photographs and displays beautifully."],
            ["Do you offer display packaging?", "Yes. Velvet boxes, coin capsules, and acrylic stands are available to complete the presentation."],
            ["Is there a minimum order for awards?", "No. You can order a single award coin or a full recognition program."],
        ],
        "related": ["hard-enamel-coins", "minted-coins", "3d-coins"],
    },
    {
        "slug": "anniversary-coins", "name": "Anniversary Coins", "category": "Anniversary",
        "title": "Custom Anniversary & Commemorative Challenge Coins",
        "meta": "Custom anniversary challenge coins for company milestones, reunions, and commemorative events. Year emblems and keepsake designs with no minimum order.",
        "keywords": "anniversary coins, commemorative coins, milestone coins, custom anniversary challenge coins, keepsake coins",
        "short": "Milestone coins that mark anniversaries, reunions, and moments worth remembering.",
        "images": ["anniversary-coins-1.jpg", "anniversary-coins-2.jpg", "anniversary-coins-3.jpg"],
        "overview": [
            "An anniversary is a story worth telling, and a commemorative coin is a way to make it tangible. Whether it is a company's 25th year or a reunion's 40th, a coin carries the milestone forward.",
            "Anniversary coins usually feature the year or years of the celebration, framed by stars, laurels, or the organization's emblem. Gold and deep red are classic choices, giving the coin a warm, celebratory feel.",
            "These coins double as invitations, souvenirs, and keepsakes — handed out at the event, then kept on desks and shelves as a reminder of the milestone. Custom dies mean the design is yours alone.",
        ],
        "features": [
            ["Year emblems", "Dates and milestone years struck in bold relief."],
            ["Celebratory design", "Stars, laurels, and emblem accents that feel festive."],
            ["Keepsake quality", "Premium plating and enamel that last for decades."],
            ["Custom dies", "Your exact design, no templates, no compromises."],
            ["Event-ready", "Pairs with velvet pouches for handouts and gifts."],
            ["No minimum order", "One keepsake or thousands for a big celebration."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "Soft or hard, Pantone matched"], ["Base metal", "Zinc alloy or brass"], ["Plating", "Gold, silver, antique, rose gold"], ["Relief", "Flat or sculpted emblem"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 3\u2033 (38\u201376 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, die-cut, custom"]]),
            ("Options", [["Edge styles", "Standard, rope, reeded"], ["Back side", "Event details and dates"], ["Extras", "Velvet pouch, presentation box"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": ["No minimum order quantity", "Free digital proof in 12 hours", "Custom dies for unique designs", "Worldwide shipping"],
        "applications": ["Company milestones", "Class reunions", "Wedding keepsakes", "Organization anniversaries", "Event souvenirs", "Family commemorations"],
        "faq": [
            ["Can the coin include specific dates?", "Yes. Years, dates, and event details are commonly featured on the front or engraved on the back."],
            ["How early should I order for an event?", "Allow 7\u201310 business days for production after proof approval, plus shipping time. Rush options may be available."],
            ["Can you match an existing logo or emblem?", "Yes. Send us the artwork and we will adapt it into a coin-ready design with a free proof."],
            ["Do you offer event packaging?", "Yes. Velvet pouches and presentation boxes are available for handing out coins at your event."],
        ],
        "related": ["minted-coins", "hard-enamel-coins", "soft-enamel-coins"],
    },
]

LOOKUP = {p["slug"]: p for p in PURPOSES}


def feature_li(title, desc):
    return "<li><i class=\"fas fa-check\"></i> <strong>%s:</strong> %s</li>" % (title, desc)


def spec_card(title, rows):
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (k, v) for k, v in rows)
    return '<div class="spec-card"><h3>%s</h3><table class="spec-table">%s</table></div>' % (title, body)


def faq_item(q, a):
    return ('<div class="faq-item"><button class="faq-question"><span>%s</span><i class="fas fa-chevron-down"></i></button>'
            '<div class="faq-answer"><p>%s</p></div></div>' % (q, a))


def related_card(slug):
    p = LOOKUP[slug] if slug in LOOKUP else None
    if p:
        # purpose -> purpose related card
        short = p.get("short", "")
        if len(short) > 64:
            cut = short.rfind(" ", 0, 64)
            short = short[:cut if cut > 30 else 64] + "..."
        img = "../../imgs/purpose/" + p["images"][0]
        return ('<article class="product-card"><div class="product-image"><img src="%s" alt="%s" loading="lazy"></div>'
                '<div class="product-info"><h3>%s</h3><p>%s</p><a href="../../purpose/%s/index.html" class="btn btn-outline">View Details</a></div></article>'
                % (img, p["name"], p["name"], short, p["slug"]))
    # fallback to product cards
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    return None


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | ChinaChallengeCoin</title>
    <meta name="description" content="{{META}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.chinachallengecoin.com/purpose/{{SLUG}}/index.html">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='48' fill='%23d97706'/><circle cx='50' cy='50' r='34' fill='none' stroke='%23fff' stroke-width='5'/></svg>">
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script type="application/ld+json">{{PRODUCT_JSON}}</script>
    <script type="application/ld+json">{{FAQ_JSON}}</script>
    <script type="application/ld+json">{{BREADCRUMB_JSON}}</script>
</head>
<body>
    <div class="top-bar">
        <div class="container">
            <div class="top-bar-content">
                <div class="top-features">
                    <span><i class="fas fa-clock"></i> 12-Hour Free Proof</span>
                    <span><i class="fas fa-check-circle"></i> No Minimum Order</span>
                    <span><i class="fas fa-headset"></i> 24/7 Support</span>
                    <span><i class="fas fa-shipping-fast"></i> Worldwide Shipping</span>
                </div>
                <div class="top-contact"><a href="mailto:cocohan520@gmail.com"><i class="fas fa-envelope"></i> cocohan520@gmail.com</a></div>
            </div>
        </div>
    </div>

    <header class="header" id="header">
        <div class="container">
            <div class="header-content">
                <a href="../../index.html" class="logo"><span class="logo-icon">🪙</span><span class="logo-text">China<span>Challenge</span>Coin</span></a>
                <nav class="main-nav" id="mainNav">
                    <ul>
                        <li><a href="../../index.html">Home</a></li>
                        <li><a href="../../product.html">Products</a></li>
                        <li><a href="../../blog.html">Blog</a></li>
                        <li><a href="../../index.html#why-us">Why Us</a></li>
                        <li><a href="../../aboutus.html">About</a></li>
                        <li><a href="../../index.html#contact">Contact</a></li>
                    </ul>
                </nav>
                <div class="header-actions">
                    <a href="../../index.html#quote" class="btn btn-gold">Get Free Quote</a>
                    <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
                </div>
            </div>
        </div>
    </header>

    <div class="breadcrumb">
        <div class="container">
            <nav aria-label="breadcrumb">
            <ol class="breadcrumb-list">
                <li><a href="../../index.html">Home</a></li>
                <li class="separator"><i class="fas fa-chevron-right"></i></li>
                <li><a href="../../product.html">Products</a></li>
                <li class="separator"><i class="fas fa-chevron-right"></i></li>
                <li aria-current="page">{{NAME}}</li>
            </ol>
            </nav>
        </div>
    </div>

    <section class="product-detail">
        <div class="container">
            <div class="product-detail-grid">
                <div class="product-images">
                    <div class="main-image"><img src="../../imgs/purpose/{{IMG1}}" alt="{{NAME}}" id="mainImage"></div>
                    <div class="thumbnail-gallery">{{THUMBS}}</div>
                </div>
                <div class="product-info-detail">
                    <div class="product-header">
                        <span class="product-category-tag">{{CATEGORY}}</span>
                        <div class="product-rating-large">
                            <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                            <span class="rating-text">4.9 (1,286 reviews)</span>
                        </div>
                    </div>
                    <h1>{{TITLE}}</h1>
                    <p class="product-short-desc">{{SHORT}}</p>
                    <div class="product-actions">
                        <a href="../../index.html#quote" class="btn btn-gold btn-large"><i class="fas fa-calculator"></i> Get Custom Quote</a>
                        <a href="../../index.html#quote" class="btn btn-outline btn-large"><i class="fas fa-paper-plane"></i> Request Free Sample</a>
                    </div>
                    <div class="product-benefits">{{BENEFITS}}</div>
                </div>
            </div>
        </div>
    </section>

    <section class="product-tabs-section">
        <div class="container">
            <div class="product-tabs">
                <div class="tab-nav">
                    <button class="tab-nav-btn active" data-tab="overview">Overview</button>
                    <button class="tab-nav-btn" data-tab="specifications">Specifications</button>
                    <button class="tab-nav-btn" data-tab="reviews">Reviews</button>
                    <button class="tab-nav-btn" data-tab="faq">FAQ</button>
                </div>
                <div class="tab-content">
                    <div class="tab-panel active" id="overview">
                        <div class="overview-grid">
                            <div class="overview-content">
                                <h2>About {{NAME}}</h2>
                                <p>{{OVERVIEW_P1}}</p>
                                <p>{{OVERVIEW_P2}}</p>
                                <p>{{OVERVIEW_P3}}</p>
                                <h3>Key Features</h3>
                                <ul class="feature-list">{{FEATURES}}</ul>
                                <h3>Best Uses</h3>
                                <div class="use-cases">{{USECASES}}</div>
                            </div>
                            <div class="overview-image"><img src="../../imgs/purpose/{{IMG2}}" alt="{{NAME}} design detail"></div>
                        </div>
                    </div>

                    <div class="tab-panel" id="specifications">
                        <h2>Technical Specifications</h2>
                        <div class="spec-cards-grid">{{SPECS}}</div>
                    </div>

                    <div class="tab-panel" id="reviews">
                        <h2>Customer Reviews</h2>
                        <div class="reviews-summary">
                            <div class="rating-big">
                                <span class="rating-number">4.9</span>
                                <div class="stars-large"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i></div>
                                <span class="rating-count">Based on 1,286 reviews</span>
                            </div>
                            <div class="rating-breakdown">{{RATING_BARS}}</div>
                        </div>
                        <div class="reviews-list">{{REVIEWS}}</div>
                    </div>

                    <div class="tab-panel" id="faq">
                        <h2>Frequently Asked Questions</h2>
                        <div class="faq-list">{{FAQ_HTML}}</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="related-products">
        <div class="container">
            <h2>Related Coin Styles</h2>
            <div class="products-grid">{{RELATED}}</div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to Order {{NAME}}?</h2>
                <p>Get a free digital proof within 12 hours and a factory-direct quote — no minimum order.</p>
                <a href="../../index.html#quote" class="btn btn-gold btn-large">Start Your Order <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../../index.html" class="footer-logo"><span class="logo-icon">🪙</span><span class="logo-text">China<span style="color:var(--gold-light)">Challenge</span>Coin</span></a>
                    <p>Factory-direct custom challenge coins with no minimum order. Free design and 12-hour proofs.</p>
                    <div class="footer-certificates"><span><i class="fas fa-shield-alt"></i> Quality Guarantee</span><span><i class="fas fa-leaf"></i> Eco-Friendly Finish</span></div>
                </div>
                <div class="footer-links"><h4>Coin Styles</h4><ul><li><a href="../../product/soft-enamel-coins/index.html">Soft Enamel</a></li><li><a href="../../product/hard-enamel-coins/index.html">Hard Enamel</a></li><li><a href="../../product/3d-coins/index.html">3D Coins</a></li><li><a href="../../product/uv-printed-coins/index.html">UV Printed</a></li><li><a href="../../product/no-color-coins/index.html">No Color</a></li><li><a href="../../product/minted-coins/index.html">Minted</a></li><li><a href="../../product/bottle-opener-coins/index.html">Bottle Opener</a></li><li><a href="../../product/single-sided-coins/index.html">Single-Sided</a></li><li><a href="../../product/magnetic-golf-coins/index.html">Magnetic Golf</a></li></ul></div>
                <div class="footer-links"><h4>Company</h4><ul><li><a href="../../aboutus.html">About Us</a></li><li><a href="../../blog.html">Blog</a></li><li><a href="../../index.html#faq">FAQ</a></li><li><a href="../../index.html#contact">Contact</a></li></ul></div>
                <div class="footer-links"><h4>Support</h4><ul><li><a href="../../index.html#knowledge">Edge Types</a></li><li><a href="../../index.html#process">How It Works</a></li><li><a href="../../privacy.html">Privacy Policy</a></li><li><a href="../../index.html#quote">Get a Quote</a></li></ul></div>
            </div>
            <div class="footer-bottom"><p>&copy; 2026 ChinaChallengeCoin. All rights reserved.</p><p>Custom Challenge Coins | Made with care in China</p></div>
        </div>
    </footer>

    <button class="back-to-top" id="backToTop" aria-label="Back to top"><i class="fas fa-arrow-up"></i></button>
    <script src="../../js/main.js"></script>
    <script>
        document.querySelectorAll('.thumbnail').forEach(function(t){t.addEventListener('click',function(){var img=this.getAttribute('data-image');document.getElementById('mainImage').src=img;document.querySelectorAll('.thumbnail').forEach(function(x){x.classList.remove('active');});this.classList.add('active');});});
        document.querySelectorAll('.tab-nav-btn').forEach(function(b){b.addEventListener('click',function(){var id=this.getAttribute('data-tab');document.querySelectorAll('.tab-nav-btn').forEach(function(x){x.classList.remove('active');});document.querySelectorAll('.tab-panel').forEach(function(p){p.classList.remove('active');});this.classList.add('active');document.getElementById(id).classList.add('active');});});
    </script>
</body>
</html>
"""


def app_icon(app):
    mapping = [
        ("award", "fa-trophy"), ("annual", "fa-calendar-check"), ("client", "fa-handshake"),
        ("onboarding", "fa-user-plus"), ("brand", "fa-bullhorn"), ("incent", "fa-chart-line"),
        ("sales", "fa-chart-line"), ("unit", "fa-shield-halved"), ("deployment", "fa-globe"),
        ("graduation", "fa-graduation-cap"), ("retire", "fa-umbrella-beach"), ("reunion", "fa-users"),
        ("memorial", "fa-dove"), ("promotion", "fa-arrow-up"), ("team", "fa-users"),
        ("communit", "fa-building-columns"), ("department", "fa-building-shield"), ("badge", "fa-star"),
        ("academy", "fa-graduation-cap"), ("station", "fa-truck-monster"), ("charity", "fa-heart"),
        ("volunteer", "fa-hand-holding-heart"), ("leadership", "fa-user-tie"), ("executive", "fa-briefcase"),
        ("milestone", "fa-flag-checkered"), ("class", "fa-graduation-cap"), ("wedding", "fa-ring"),
        ("organization", "fa-sitemap"), ("event", "fa-calendar"), ("family", "fa-house-chimney"),
        ("company", "fa-building"), ("program", "fa-clipboard-check"), ("retirement", "fa-umbrella-beach"),
        ("corporate", "fa-building"), ("employee", "fa-user-check"), ("recognition", "fa-medal"),
        ("achievement", "fa-medal"), ("client", "fa-handshake"),
    ]
    for key, icon in mapping:
        if key in app.lower():
            return icon
    return "fa-circle"


count = 0
for p in PURPOSES:
    features = "\n".join(feature_li(t, d) for t, d in p["features"])
    specs = "\n".join(spec_card(t, rows) for t, rows in p["spec_groups"])
    benefits = "\n".join('<div class="benefit-item"><i class="fas fa-check-circle"></i><span>%s</span></div>' % b for b in p["benefits"])
    usecases = "\n".join('<div class="use-case"><i class="fas %s"></i><span>%s</span></div>' % (app_icon(a), a) for a in p["applications"])
    faq_html = "\n".join(faq_item(q, a) for q, a in p["faq"])

    # Related: link to the 3 concrete product pages
    import sys as _sys
    _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from _gen_detail import PRODUCTS as PRODUCT_LIST
    _plookup = {x["slug"]: x for x in PRODUCT_LIST}
    related_cards = []
    for s in p["related"]:
        prod = _plookup.get(s)
        if prod:
            short = prod.get("short", "")
            if len(short) > 64:
                cut = short.rfind(" ", 0, 64)
                short = short[:cut if cut > 30 else 64] + "..."
            related_cards.append(
                '<article class="product-card"><div class="product-image"><img src="../../imgs/products/%s.jpg" alt="%s" loading="lazy"></div>'
                '<div class="product-info"><h3>%s</h3><p>%s</p><a href="../../product/%s/index.html" class="btn btn-outline">View Details</a></div></article>'
                % (s, prod["name"], prod["name"], short, s))
    related = "\n".join(related_cards)

    thumbs = "".join(
        '<div class="thumbnail%s" data-image="../../imgs/purpose/%s"><img src="../../imgs/purpose/%s" alt="%s view %d"></div>'
        % (" active" if i == 0 else "", img, img, p["name"], i + 1)
        for i, img in enumerate(p["images"])
    )

    rating_bars = "\n".join(
        '<div class="rating-bar"><span>%s</span><div class="bar"><div class="fill" style="width:%s%%"></div></div><span>%s%%</span></div>' % (label, w, w)
        for label, w in RATING_BREAKDOWN
    )
    reviews = "\n".join(
        '<div class="review-item"><div class="review-header"><div class="reviewer-info"><span class="reviewer-name">%s</span><span class="verified-badge"><i class="fas fa-check-circle"></i> Verified Purchase</span></div><div class="review-rating"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div><p class="review-text">%s</p><span class="review-date">%s</span></div>'
        % (name, text, date) for name, text, date in REVIEWS
    )

    image_urls = "[" + ", ".join('"https://www.chinachallengecoin.com/imgs/purpose/%s"' % i for i in p["images"]) + "]"

    product_json = json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": p["title"], "description": p["meta"],
        "image": image_urls,
        "brand": {"@type": "Brand", "name": "ChinaChallengeCoin"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "1286"},
    }, ensure_ascii=False)

    faq_json = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]],
    }, ensure_ascii=False)

    breadcrumb_json = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.chinachallengecoin.com/"},
            {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://www.chinachallengecoin.com/product.html"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": "https://www.chinachallengecoin.com/purpose/" + p["slug"] + "/index.html"},
        ],
    }, ensure_ascii=False)

    html = (TEMPLATE
            .replace("{{TITLE}}", p["title"])
            .replace("{{META}}", p["meta"])
            .replace("{{KEYWORDS}}", p["keywords"])
            .replace("{{SLUG}}", p["slug"])
            .replace("{{NAME}}", p["name"])
            .replace("{{CATEGORY}}", p["category"])
            .replace("{{SHORT}}", p["short"])
            .replace("{{IMG1}}", p["images"][0])
            .replace("{{IMG2}}", p["images"][1])
            .replace("{{THUMBS}}", thumbs)
            .replace("{{OVERVIEW_P1}}", p["overview"][0])
            .replace("{{OVERVIEW_P2}}", p["overview"][1])
            .replace("{{OVERVIEW_P3}}", p["overview"][2])
            .replace("{{FEATURES}}", features)
            .replace("{{USECASES}}", usecases)
            .replace("{{SPECS}}", specs)
            .replace("{{FAQ_HTML}}", faq_html)
            .replace("{{BENEFITS}}", benefits)
            .replace("{{RELATED}}", related)
            .replace("{{RATING_BARS}}", rating_bars)
            .replace("{{REVIEWS}}", reviews)
            .replace("{{PRODUCT_JSON}}", product_json)
            .replace("{{FAQ_JSON}}", faq_json)
            .replace("{{BREADCRUMB_JSON}}", breadcrumb_json))

    d = os.path.join(BASE, p["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    count += 1
    print("Generated purpose page:", p["slug"])

print("Done:", count, "purpose pages")
