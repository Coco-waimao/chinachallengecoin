# -*- coding: utf-8 -*-
import os, json

BASE = r"C:\code\chinachallengecoin\product"

def app_icon(text):
    t = text.lower()
    mapping = [
        ("military", "fa-shield-halved"), ("unit", "fa-shield-halved"),
        ("corporate", "fa-briefcase"), ("business", "fa-briefcase"),
        ("team", "fa-users"), ("club", "fa-users"), ("fraternity", "fa-users"),
        ("commemorative", "fa-calendar-check"), ("anniversary", "fa-calendar-check"), ("memorial", "fa-calendar-check"),
        ("promotional", "fa-gift"), ("giveaway", "fa-gift"), ("gift", "fa-gift"), ("groomsmen", "fa-gift"),
        ("trade", "fa-gift"), ("event", "fa-gift"), ("outing", "fa-flag"),
        ("fundraiser", "fa-heart"), ("charity", "fa-heart"),
        ("award", "fa-medal"), ("trophy", "fa-medal"), ("retirement", "fa-medal"), ("minimalist", "fa-medal"), ("ceremonial", "fa-medal"),
        ("executive", "fa-crown"), ("vip", "fa-crown"),
        ("logo", "fa-trademark"), ("brand", "fa-trademark"),
        ("police", "fa-shield-alt"), ("firefighter", "fa-fire-extinguisher"),
        ("golf", "fa-flag"), ("brewery", "fa-beer"), ("bar", "fa-beer"),
        ("magnet", "fa-magnet"), ("fridge", "fa-magnet"),
        ("badge", "fa-id-badge"), ("nameplate", "fa-tag"), ("membership", "fa-id-card"),
        ("desk", "fa-spinner"), ("fidget", "fa-spinner"), ("stress", "fa-spinner"),
        ("tech", "fa-microchip"), ("startup", "fa-rocket"), ("maker", "fa-microchip"),
        ("collector", "fa-box-open"), ("collectible", "fa-box-open"), ("limited", "fa-box-open"), ("edition", "fa-box-open"),
        ("sponsor", "fa-handshake"), ("creative", "fa-palette"),
        ("everyday", "fa-hand-spock"), ("carry", "fa-hand-spock"),
        ("stick-on", "fa-thumbtack"), ("country", "fa-flag"),
    ]
    for key, icon in mapping:
        if key in t:
            return icon
    return "fa-circle"

PRODUCTS = [
    {
        "slug": "soft-enamel-coins", "name": "Soft Enamel Coins", "category": "Soft Enamel",
        "title": "Custom Soft Enamel Coins",
        "meta": "Custom soft enamel challenge coins with recessed color and raised metal ridges. No minimum order, free design and 12-hour proof.",
        "keywords": "soft enamel coins, custom soft enamel challenge coins, recessed enamel coins, textured challenge coins",
        "short": "The classic challenge coin — recessed enamel and raised metal ridges for a textured, dimensional finish that reads clearly at coin scale.",
        "overview": [
            "Soft enamel is the most widely ordered challenge coin style, and for good reason. Each recessed area of the design is filled with colored enamel that sits just below the raised metal ridges, giving the coin a texture you can feel with your thumb and a depth that catches the light.",
            "Because the color sits slightly lower than the metal, soft enamel coins have a classic, layered look that works beautifully with multi-color designs — logos, unit insignias, and commemorative artwork all read clearly at coin scale.",
            "Soft enamel is also the most cost-effective way to get a detailed, full-color coin, which is why it remains the go-to choice for large team orders, military units, and promotional runs.",
        ],
        "features": [
            ["Tactile raised texture", "Recessed enamel below raised metal ridges gives a dimensional feel you can touch."],
            ["Full Pantone color range", "Match brand or unit colors precisely across a wide enamel palette."],
            ["Cost-effective", "The most affordable full-color coin style, ideal for bulk orders."],
            ["Detailed and durable", "Multi-color artwork stays crisp and holds up to daily carry."],
            ["Classic look", "The traditional challenge coin finish collectors and units expect."],
            ["Any shape or size", "Round, custom die-cut, and everything in between."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel fill", "Recessed below metal ridges"], ["Base metal", "Zinc alloy or brass"], ["Texture", "Raised, tactile ridges"], ["Durability", "Everyday-carry grade"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Plating", "Gold, silver, copper, antique, black nickel"], ["Colors", "Full Pantone range"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Military units", "Corporate logos", "Team and club insignia", "Commemorative events", "Promotional giveaways", "Fundraisers"],
        "faq": [
            ["What is the difference between soft and hard enamel?", "Soft enamel leaves the color slightly recessed below the raised metal ridges, giving a textured feel. Hard enamel is filled flush and polished flat for a smooth, glass-like surface."],
            ["Can you match my exact brand color?", "Yes. We match enamel to the Pantone color system, so your brand or unit colors stay consistent from proof to finished coin."],
            ["What sizes are available?", "Soft enamel coins typically run from 1.25 inches up to 3 inches, with custom die-cut shapes available at any size."],
            ["Is there a minimum order?", "No. We accept orders of any quantity, from a single keepsake to thousands of pieces."],
        ],
        "related": ["hard-enamel-coins", "3d-coins", "uv-printed-coins", "no-color-coins"],
    },
    {
        "slug": "hard-enamel-coins", "name": "Hard Enamel Coins", "category": "Hard Enamel",
        "title": "Custom Hard Enamel Coins",
        "meta": "Custom hard enamel challenge coins with a smooth, glass-like polished finish. Premium, durable, and scratch-resistant. No minimum order, free proof.",
        "keywords": "hard enamel coins, custom hard enamel challenge coins, polished enamel coins, premium challenge coins",
        "short": "Enamel filled flush and polished flat — a smooth, glass-like finish with a premium, jewelry-grade feel that lasts for years.",
        "overview": [
            "Hard enamel coins take the same colored enamel as soft enamel but fill it completely flush with the metal, then polish the surface flat through multiple passes until it is smooth as glass.",
            "The result is a premium, jewelry-like finish with no raised ridges — just a clean, glossy surface that looks and feels high-end and resists scratches and wear through years of handling.",
            "Hard enamel is the style of choice for executive gifts, awards, and recognition pieces that get displayed on a desk or in a case rather than carried in a pocket.",
        ],
        "features": [
            ["Glass-smooth surface", "Filled flush and polished flat for a seamless, glossy finish."],
            ["Scratch-resistant", "The flat, sealed surface stands up to years of handling."],
            ["Premium feel", "A jewelry-grade finish for high-end and executive pieces."],
            ["Vivid, flat color", "Deep, even enamel that looks rich and consistent."],
            ["Award-worthy", "The preferred finish for awards and recognition coins."],
            ["Custom shapes", "Any shape, size, and edge combination."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel fill", "Flush, polished flat"], ["Base metal", "Zinc alloy or brass"], ["Surface", "Smooth, glass-like"], ["Durability", "Scratch-resistant"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Plating", "Gold, silver, copper, antique"], ["Colors", "Full Pantone range"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Executive gifts", "Corporate awards", "Recognition coins", "VIP and client gifts", "Anniversary pieces", "Limited editions"],
        "faq": [
            ["How is hard enamel different from soft enamel?", "Hard enamel is filled flush to the metal and polished completely flat, so there are no raised ridges — the surface is smooth like glass. Soft enamel leaves the color recessed and textured."],
            ["Is hard enamel more durable?", "Yes. The flat, sealed surface is more resistant to scratches and wear, which is why it is favored for premium and long-displayed pieces."],
            ["Does hard enamel cost more?", "It typically costs more than soft enamel because of the extra filling and polishing steps, but the premium finish is worth it for high-end pieces."],
            ["Can I use multiple colors?", "Absolutely. Hard enamel supports full-color designs, and we match to the Pantone system."],
        ],
        "related": ["soft-enamel-coins", "3d-coins", "minted-coins", "no-color-coins"],
    },
    {
        "slug": "3d-coins", "name": "3D Coins", "category": "3D Relief",
        "title": "Custom 3D Coins",
        "meta": "Custom 3D challenge coins with deeply sculpted, multi-level relief for striking depth and detail. No minimum order, free design and proof.",
        "keywords": "3D challenge coins, custom 3D coins, sculpted relief coins, raised challenge coins",
        "short": "Deeply sculpted, multi-level relief that lifts your emblem off the metal for real depth, shadow, and drama.",
        "overview": [
            "3D coins are sculpted with raised, multi-level relief, so your emblem, mascot, or logo physically rises off the surface of the coin. The depth creates natural highlights and shadows that make the design pop from every angle.",
            "This style is ideal for bold subjects — eagles, shields, mascots, faces, and crests — where dimension and realism matter more than flat color. 3D relief can be combined with enamel accents for extra impact.",
            "3D coins can be sculpted on one side or both, and pair beautifully with antique finishes that emphasize the raised detail.",
        ],
        "features": [
            ["Multi-level relief", "Sculpted depth that lifts your design off the surface."],
            ["Highlights and shadow", "Relief catches light for a dramatic, dimensional look."],
            ["Bold subjects", "Perfect for emblems, mascots, and crests."],
            ["Single or double-sided", "Sculpted relief on one face or both."],
            ["Enamel accents", "Combine 3D relief with color for extra impact."],
            ["Realistic modeling", "High-detail sculpting for lifelike results."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Relief", "Multi-level sculpted"], ["Base metal", "Zinc alloy"], ["Sides", "Single or double-sided"], ["Detail", "High-detail sculpting"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 3\u2033 (38\u201376 mm)"], ["Thickness", "3\u20136 mm (deeper relief)"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Plating", "Antique gold, silver, copper, black nickel"], ["Finish", "Polished or antique"], ["Color accents", "Enamel fills"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201312 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Unit and military insignia", "Mascots and logos", "Commemorative pieces", "Challenge sets", "Corporate emblems", "Awards and trophies"],
        "faq": [
            ["What makes a coin 3D?", "3D refers to sculpted, raised relief that gives the design real depth — multiple levels of metal that rise off the surface, rather than a flat design."],
            ["Can 3D coins have color?", "Yes. 3D relief is often combined with enamel fill or antique plating to add color and emphasize the raised detail."],
            ["Is 3D more expensive?", "3D coins involve more sculpting and tooling, so they typically cost more than flat enamel coins, but the dramatic result is worth it for bold designs."],
            ["Can both sides be 3D?", "Absolutely. We can sculpt the relief on one side or both, depending on your design."],
        ],
        "related": ["soft-enamel-coins", "hard-enamel-coins", "minted-coins", "uv-printed-coins"],
    },
    {
        "slug": "uv-printed-coins", "name": "UV Printed Coins", "category": "UV Print",
        "title": "Custom UV Printed Coins",
        "meta": "Full-color UV printed challenge coins with photo-realistic detail, gradients, and no mold fee. No minimum order, free proof.",
        "keywords": "UV printed coins, custom UV printed challenge coins, full color printed coins, photo printed coins",
        "short": "Full-color, photo-realistic artwork printed flat onto metal — gradients and fine detail enamel cannot match.",
        "overview": [
            "UV printing lays full-color artwork directly onto the metal surface, capturing photographic detail, fine lines, and smooth gradients that enamel simply cannot reproduce. It is the fastest way to put a complex logo or image on a coin.",
            "Because no mold is required, UV printed coins skip the die-cutting step entirely — which means faster turnaround and no mold fee, making them ideal for rush orders and one-off designs.",
            "A clear protective coating is applied over the print to guard against scratches and keep the colors vivid through daily handling.",
        ],
        "features": [
            ["Photo-realistic detail", "Reproduces photographs and fine artwork faithfully."],
            ["Smooth gradients", "Handles color blends and gradients enamel cannot."],
            ["No mold fee", "Print directly to metal — skip the die-cutting step."],
            ["Fast turnaround", "A faster production path for time-sensitive orders."],
            ["Protective coating", "A clear gloss layer guards the print against wear."],
            ["Any artwork", "Logos, photos, illustrations — print whatever you design."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Print", "Full-color digital UV"], ["Base metal", "Zinc alloy or steel"], ["Coating", "Gloss clear coat"], ["Mold", "None required"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm (flat surface)"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Colors", "Unlimited full spectrum"], ["Detail", "Photos, gradients, fine lines"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "5\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Photographic logos", "Complex brand artwork", "Rush orders", "Event giveaways", "Detailed illustrations", "One-off designs"],
        "faq": [
            ["What is UV printing on a coin?", "UV printing uses digital full-color printing to lay artwork directly onto the metal surface, then cures it with UV light and seals it with a clear coat."],
            ["Does UV printing require a mold?", "No. Because the artwork is printed rather than die-struck, there is no mold fee and production is faster."],
            ["How durable is the print?", "A clear protective coating guards the artwork against scratches and fading through normal handling."],
            ["Can I print a photo?", "Yes — UV printing reproduces photographs and detailed illustrations that other coin styles cannot."],
        ],
        "related": ["soft-enamel-coins", "3d-coins", "single-sided-coins", "no-color-coins"],
    },
    {
        "slug": "no-color-coins", "name": "No Color Coins", "category": "No Color",
        "title": "Custom No Color Coins",
        "meta": "Custom no-color challenge coins with pure metal engraving and embossed relief. Elegant, timeless, no enamel. No minimum order.",
        "keywords": "no color coins, metal challenge coins, engraved challenge coins, antique finish coins",
        "short": "Pure metal, no enamel — crisp engraving and embossed relief that lets the metal do the talking.",
        "overview": [
            "Sometimes less is more. No-color coins skip the enamel entirely and rely on crisp engraving and embossed relief to carry the design, letting the natural texture and luster of the metal speak for itself.",
            "The look is elegant and timeless — think classic medallions and ceremonial pieces — and it is especially striking in antique gold, silver, and copper finishes that emphasize every raised line and recessed shadow.",
            "No-color coins are also a cost-effective option, since fewer color steps mean simpler, faster production.",
        ],
        "features": [
            ["Pure metal", "No enamel — just engraving and embossed relief."],
            ["Crisp engraving", "Fine lines and text read clearly in the metal."],
            ["Timeless look", "Classic, medallion-style elegance."],
            ["Rich finishes", "Antique gold, silver, copper, and more."],
            ["Cost-effective", "Fewer color steps mean simpler production."],
            ["Custom shapes", "Any shape or size you need."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Enamel", "None"], ["Base metal", "Zinc alloy or brass"], ["Detail", "Engraved &amp; embossed"], ["Style", "Timeless medallion"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Finish", "Antique or shiny gold, silver, copper, black nickel"], ["Edge options", "12 styles"], ["Accents", "Selective enamel available"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Ceremonial pieces", "Minimalist branding", "Memorial coins", "Antique-style collectibles", "Corporate keepsakes", "Challenge sets"],
        "faq": [
            ["What is a no-color coin?", "A no-color coin uses no enamel fill — the design is carried entirely by engraved lines and embossed relief in the metal itself."],
            ["Which finishes look best?", "Antique gold, silver, and copper are the most popular, as the darker recesses emphasize the raised detail."],
            ["Is it cheaper than enamel coins?", "Generally yes, because there are no color-fill steps in production."],
            ["Can I combine engraving with color?", "If you would like a little color, we can add selective enamel accents — just ask your designer."],
        ],
        "related": ["single-sided-coins", "minted-coins", "soft-enamel-coins", "hard-enamel-coins"],
    },
    {
        "slug": "minted-coins", "name": "Minted Coins", "category": "Proof Finish",
        "title": "Custom Minted Coins",
        "meta": "Custom minted challenge coins with a mirror-like proof finish and frosted relief — a collectible struck-coin look. No minimum order.",
        "keywords": "minted coins, custom minted challenge coins, proof finish coins, collectible coins",
        "short": "Struck like currency — a mirror-like proof finish against frosted relief for a collectible look.",
        "overview": [
            "Minted coins are struck with a proof finish, the same process used for collectible currency: a mirror-like polished field paired with frosted, raised relief. The contrast between the two surfaces is what gives proof coins their unmistakable depth and shine.",
            "The result is a coin that feels genuinely minted rather than machined — ideal for commemorative sets, limited editions, and any piece meant to be collected, displayed, and passed along.",
            "Minted coins can be produced in 2D or 3D relief and finished in a range of metals, from brilliant silver to deep antique bronze.",
        ],
        "features": [
            ["Mirror proof finish", "A polished, reflective field with sharp detail."],
            ["Frosted relief", "Raised detail in frosted contrast to the mirror field."],
            ["Struck-coin look", "Feels minted, like collectible currency."],
            ["Collectible", "Perfect for commemorative and limited sets."],
            ["2D or 3D relief", "Choose flat struck detail or sculpted depth."],
            ["Premium metal", "Brilliant silver, gold, and antique bronze."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Finish", "Proof (mirror + frosted)"], ["Base metal", "Brass or bronze"], ["Relief", "2D or 3D struck"], ["Style", "Collectible struck-coin"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 2.75\u2033 (38\u201370 mm)"], ["Thickness", "3\u20134 mm"], ["Shapes", "Round primarily"]]),
            ("Finishes &amp; Options", [["Metals", "Silver, gold, bronze, antique"], ["Edge options", "Reeded, plain, custom"], ["Packaging", "Capsule, box, pouch"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201312 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Commemorative sets", "Limited editions", "Anniversary coins", "Collector pieces", "Retirement gifts", "Special events"],
        "faq": [
            ["What is a proof finish?", "A proof finish pairs a mirror-polished field with frosted raised relief — the same technique used for collectible coins, giving striking depth and shine."],
            ["Can minted coins be 3D?", "Yes. Minted coins can be struck in 2D or sculpted 3D relief."],
            ["What metals are available?", "Brilliant silver, gold, and bronze are common, along with antique finishes for a more traditional look."],
            ["Is there a minimum order?", "No minimum — order a single collectible or a full commemorative run."],
        ],
        "related": ["hard-enamel-coins", "3d-coins", "no-color-coins", "soft-enamel-coins"],
    },
    {
        "slug": "bottle-opener-coins", "name": "Bottle Opener Coins", "category": "Functional",
        "title": "Custom Bottle Opener Coins",
        "meta": "Custom bottle opener challenge coins that combine a working opener with elegant metal design. No minimum order, free proof.",
        "keywords": "bottle opener coins, custom bottle opener challenge coins, functional challenge coins",
        "short": "A working bottle opener built right into the coin — the most useful challenge coin at the party.",
        "overview": [
            "Why carry a coin and a bottle opener when one will do? Bottle opener coins build a precise, working opener right into the edge of the coin, turning your brand or unit insignia into the most useful item at any gathering.",
            "The opener is precision-cut into the metal, so it opens bottles smoothly while the coin itself stays a display-worthy keepsake. Edges are finished cleanly to avoid sharp spots.",
            "Bottle opener coins are a favorite for breweries, events, groomsmen gifts, and any brand that wants to stay in someone's hand — literally.",
        ],
        "features": [
            ["Working opener", "A precision-cut opener that actually works."],
            ["Clean edges", "Finished smooth for safe, comfortable use."],
            ["Display-worthy", "Looks great on a shelf or in a pocket."],
            ["Multi-finish options", "Gunmetal, antique, shiny, and more."],
            ["Gift-ready", "The perfect groomsmen or event gift."],
            ["Custom shapes", "Coin-shaped or custom-cut silhouettes."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Function", "Bottle opener cutout"], ["Base metal", "Zinc alloy or steel"], ["Strength", "Reinforced 3\u20134 mm"], ["Edges", "Smooth, deburred"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "2\u2033 \u2013 2.5\u2033 (50\u201364 mm)"], ["Thickness", "3\u20134 mm (reinforced)"], ["Shapes", "Round or custom silhouette"]]),
            ("Finishes &amp; Options", [["Finish", "Gunmetal, antique, shiny"], ["Color", "Enamel or UV print"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Breweries and bars", "Groomsmen gifts", "Corporate events", "Fraternity and club gifts", "Trade shows", "Anniversary giveaways"],
        "faq": [
            ["Does the bottle opener actually work?", "Yes. The opener is precision-cut into the metal and finished smooth, so it opens bottles reliably without sharp edges."],
            ["What material is used?", "We typically use zinc alloy or steel, which gives the opener the strength it needs while keeping detail crisp."],
            ["Can the opener be a custom shape?", "Absolutely. The opener cutout can be built into a round coin or a fully custom silhouette."],
            ["Is it safe to carry?", "Yes — all edges are smoothed and deburred during finishing."],
        ],
        "related": ["magnetic-golf-coins", "single-sided-coins", "soft-enamel-coins", "3d-coins"],
    },
    {
        "slug": "single-sided-coins", "name": "Single-Sided Coins", "category": "Single-Sided",
        "title": "Custom Single-Sided Coins",
        "meta": "Custom single-sided challenge coins with one detailed face and a flat back — add engraving, magnet, or adhesive. No minimum order.",
        "keywords": "single-sided coins, custom single-sided challenge coins, one-sided coins, flat back coins",
        "short": "One detailed face, flat back — a clean, cost-effective coin you can engrave or turn into a magnet.",
        "overview": [
            "Single-sided coins put all the detail on one face and leave the back flat. It is a smart, cost-effective choice for clear, simple designs that do not need a second decorated side.",
            "The flat back is a blank canvas — engrave a message or date, add a 3M adhesive to turn the coin into a badge or plaque, or embed a magnet for fridge or locker use.",
            "Because only one side is tooled, single-sided coins are typically faster and more affordable to produce, making them ideal for awards, badges, and functional pieces.",
        ],
        "features": [
            ["One detailed face", "Full detail on the front, clean flat back."],
            ["Engrave the back", "Add a name, date, or message to the flat reverse."],
            ["Magnet or adhesive", "Turn it into a fridge magnet or stick-on badge."],
            ["Cost-effective", "Single-sided tooling saves time and cost."],
            ["Any shape", "Round, die-cut, or custom silhouettes."],
            ["Fast production", "A simpler build for quicker turnaround."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Sides", "Single decorated face"], ["Back", "Flat (engraving, magnet, or adhesive)"], ["Base metal", "Zinc alloy"], ["Profile", "Thin 2.5\u20133 mm"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.25\u2033 \u2013 3\u2033 (32\u201376 mm)"], ["Thickness", "2.5\u20133 mm (thin)"], ["Shapes", "Round, die-cut, custom"]]),
            ("Finishes &amp; Options", [["Plating", "Gold, silver, copper, black nickel"], ["Back options", "Engraving, magnet, 3M adhesive"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Awards and badges", "Fridge magnets", "Nameplates", "Simple logos", "Membership coins", "Stick-on emblems"],
        "faq": [
            ["What can I do with the flat back?", "The flat reverse can be left blank, engraved with a message or date, or fitted with a magnet or 3M adhesive."],
            ["Is single-sided cheaper?", "Generally yes — tooling only one side reduces production time and cost."],
            ["Can I add a magnet?", "Yes, we can embed a magnet in the flat back for fridge or locker use."],
            ["What sizes are available?", "From 1.25 inches up to 3 inches, with custom shapes available."],
        ],
        "related": ["no-color-coins", "soft-enamel-coins", "magnetic-golf-coins", "uv-printed-coins"],
    },
    {
        "slug": "magnetic-golf-coins", "name": "Magnetic Golf Coins", "category": "Golf",
        "title": "Custom Magnetic Golf Coins",
        "meta": "Custom magnetic golf challenge coins with a detachable ball marker. Collectible and practical on the green. No minimum order.",
        "keywords": "magnetic golf coins, custom golf ball marker coins, golf challenge coins, magnetic ball markers",
        "short": "A two-piece coin that splits into a base and a ball marker — collectible, and it earns its keep on the green.",
        "overview": [
            "Magnetic golf coins are a two-piece design: a coin base and a detachable ball marker held together with a strong embedded magnet. It is a collectible that is also genuinely useful every round.",
            "The base carries your full design — club crest, tournament logo, or brand — while the marker pops off for use on the green, then snaps back into place when you are done.",
            "They are a natural fit for tournaments, country clubs, and corporate golf events, where a practical keepsake beats a purely decorative one every time.",
        ],
        "features": [
            ["Detachable marker", "A ball marker that pops off the base and snaps back."],
            ["Golf-themed design", "Crests, logos, and course motifs."],
            ["Strong magnet", "Secure hold that will not come loose in the bag."],
            ["Event-ready", "The perfect tournament or outing keepsake."],
            ["Two-piece build", "A collectible base plus a working marker."],
            ["Full color", "Enamel or UV print with rich detail."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Build", "Two-piece magnetic"], ["Magnet", "Strong embedded"], ["Base metal", "Zinc alloy"], ["Detail", "Enamel or UV print"]]),
            ("Sizes &amp; Dimensions", [["Base", "1.5\u2033 \u2013 2\u2033 (38\u201350 mm)"], ["Marker", "~1\u2033 (25 mm)"], ["Thickness", "3 mm (with magnet)"]]),
            ("Finishes &amp; Options", [["Finish", "Silver, gold, black nickel"], ["Color", "Enamel or UV print"], ["Edge options", "12 styles"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201310 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Golf tournaments", "Country clubs", "Corporate golf events", "Charity outings", "Club crests", "Sponsor gifts"],
        "faq": [
            ["How does the magnetic coin work?", "The coin is two pieces — a base and a ball marker — held together by an embedded magnet. The marker pops off for use and snaps back when finished."],
            ["Is the magnet strong enough?", "Yes. We use a strong embedded magnet so the marker stays secure in a pocket or bag."],
            ["Can I put my club crest on it?", "Absolutely — enamel and UV printing both reproduce crests and logos in rich detail."],
            ["What sizes are available?", "Bases typically run 1.5 to 2 inches with a roughly 1-inch marker, and custom sizes are available."],
        ],
        "related": ["bottle-opener-coins", "single-sided-coins", "soft-enamel-coins", "3d-coins"],
    },
    {
        "slug": "fidget-edc-coins", "name": "Fidget EDC Coins", "category": "EDC",
        "title": "Custom Fidget EDC Coins",
        "meta": "Custom fidget EDC challenge coins with a precision spinning mechanism. Smooth, satisfying everyday carry. No minimum order.",
        "keywords": "fidget EDC coins, custom fidget coins, spinning challenge coins, EDC challenge coins",
        "short": "A precision spinning mechanism turns an ordinary coin into a smooth, satisfying everyday carry.",
        "overview": [
            "Fidget EDC coins add a precision spinning mechanism to the classic challenge coin, so you can give it a spin whenever the mood strikes. The machined bearing delivers a smooth, satisfying rotation that is genuinely calming.",
            "Built from machined metal — titanium, stainless steel, or bronze — these coins are designed for everyday carry and stand up to constant handling.",
            "For teams and brands that value craft and tactile design, a fidget coin is the kind of giveaway people keep on their desk and reach for all day.",
        ],
        "features": [
            ["Precision spin", "A smooth, satisfying rotation from a machined bearing."],
            ["Everyday carry", "Built to be carried and handled daily."],
            ["Machined metal", "Titanium, stainless, or bronze construction."],
            ["Calming fidget", "A subtle, satisfying way to channel focus."],
            ["Memorable giveaway", "A gift people actually keep and use."],
            ["Custom finishes", "Anodized colors and custom detailing."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Mechanism", "Precision bearing"], ["Material", "Titanium, stainless, bronze"], ["Build", "Machined metal"], ["Carry", "Everyday-carry grade"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 2\u2033 (38\u201350 mm)"], ["Thickness", "4\u20136 mm (mechanism depth)"], ["Shapes", "Round primarily"]]),
            ("Finishes &amp; Options", [["Finish", "Anodized, bead-blasted, polished"], ["Color", "Enamel or laser engraving"], ["Detail", "Custom engraving"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201312 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Everyday carry fans", "Team giveaways", "Tech and maker brands", "Trade show swag", "Stress-relief gifts", "Collector pieces"],
        "faq": [
            ["How does the spin mechanism work?", "The coin is built around a precision bearing, so the outer body spins smoothly around the center."],
            ["What materials are available?", "Titanium, stainless steel, and bronze, with anodized or bead-blasted finishes."],
            ["Is it durable?", "Yes — these coins are machined for everyday carry and constant handling."],
            ["Can I customize the design?", "Absolutely. We engrave or print your logo onto the spinning body."],
        ],
        "related": ["spinner-coins", "bottle-opener-coins", "single-sided-coins", "3d-coins"],
    },
    {
        "slug": "spinner-coins", "name": "Spinner Coins", "category": "Spinner",
        "title": "Custom Spinner Coins",
        "meta": "Custom spinner challenge coins with a rotating center. A satisfying desk companion and conversation piece. No minimum order.",
        "keywords": "spinner coins, custom spinner challenge coins, rotating coins, spinning desk coins",
        "short": "A rotating center turns the classic challenge coin into a satisfying desk companion.",
        "overview": [
            "Spinner coins add a rotating center to the traditional challenge coin, so you can flick it and watch the layered discs spin. It is the same collectible feel, with an interactive twist.",
            "The layered, anodized construction gives the coin a modern, high-tactile look, and the spinning action makes it a natural conversation piece on a desk or at a meetup.",
            "Spinner coins are great for stress relief, creative and tech brands, and any audience that appreciates a playful, hands-on design.",
        ],
        "features": [
            ["Rotating center", "A center disc that spins with a satisfying flick."],
            ["Layered build", "Stacked discs in anodized colors."],
            ["Stress relief", "A playful way to channel restless energy."],
            ["Conversation piece", "A coin people pick up and talk about."],
            ["Gift-ready", "A memorable giveaway for events and teams."],
            ["Custom finishes", "Anodized colors and custom detailing."],
        ],
        "spec_groups": [
            ("Materials &amp; Build", [["Mechanism", "Rotating center"], ["Material", "Aluminum, stainless, titanium"], ["Build", "Layered discs"], ["Style", "Interactive desk piece"]]),
            ("Sizes &amp; Dimensions", [["Sizes", "1.5\u2033 \u2013 2\u2033 (38\u201350 mm)"], ["Thickness", "4\u20136 mm (mechanism depth)"], ["Shapes", "Round primarily"]]),
            ("Finishes &amp; Options", [["Finish", "Anodized, bead-blasted"], ["Center", "Laser or UV printed"], ["Detail", "Custom engraving"]]),
            ("Production &amp; Ordering", [["Minimum order", "No minimum"], ["Proof", "Free within 12 hours"], ["Production", "7\u201312 business days"]]),
        ],
        "benefits": [
            "No minimum order quantity",
            "Free digital proof in 12 hours",
            "Factory-direct pricing",
            "Worldwide shipping",
        ],
        "applications": ["Desk companions", "Stress-relief gifts", "Tech and startup brands", "Trade show swag", "Creative teams", "Collector pieces"],
        "faq": [
            ["How does a spinner coin work?", "The coin has a rotating center disc mounted on a bearing, so you can flick it and watch it spin."],
            ["What materials are used?", "Aluminum, stainless steel, or titanium, with anodized or bead-blasted finishes."],
            ["Is it durable enough to spin daily?", "Yes — the bearing and layered build are designed for repeated use."],
            ["Can I customize the spinning disc?", "Yes, the center disc can carry your logo via laser engraving or UV print."],
        ],
        "related": ["fidget-edc-coins", "bottle-opener-coins", "single-sided-coins", "3d-coins"],
    },
]

LOOKUP = {p["slug"]: p for p in PRODUCTS}

REVIEWS = [
    ("Michael R.", "Excellent quality coins! The detail and finish came out even better than the proof showed. We ordered 500 pieces for our team and everyone was impressed. Fast turnaround too — got our proof within 8 hours!", "March 5, 2026"),
    ("Sarah K.", "I've ordered from several coin companies before, but this is by far the best. The quality is outstanding, communication was quick, and the coins arrived ahead of schedule. Highly recommend.", "February 28, 2026"),
    ("David L.", "Ordered custom coins for our club. The detail is incredible — even our complex logo came out perfectly. The proof process made it easy to get exactly what we wanted.", "February 20, 2026"),
]

RATING_BREAKDOWN = [("5 stars", 92), ("4 stars", 6), ("3 stars", 1.5), ("2 stars", 0.3), ("1 star", 0.2)]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | ChinaChallengeCoin</title>
    <meta name="description" content="{{META}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.chinachallengecoin.com/product/{{SLUG}}/index.html">
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
                    <div class="main-image"><img src="../../imgs/products/{{SLUG}}.jpg" alt="{{NAME}}"></div>
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
                            <div class="overview-image"><img src="../../imgs/products/{{SLUG}}.jpg" alt="{{NAME}} detail"></div>
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
        document.querySelectorAll('.tab-nav-btn').forEach(function(b){b.addEventListener('click',function(){var id=this.getAttribute('data-tab');document.querySelectorAll('.tab-nav-btn').forEach(function(x){x.classList.remove('active');});document.querySelectorAll('.tab-panel').forEach(function(p){p.classList.remove('active');});this.classList.add('active');document.getElementById(id).classList.add('active');});});
    </script>
</body>
</html>
"""

def feature_li(title, desc):
    return "<li><i class=\"fas fa-check\"></i> <strong>%s:</strong> %s</li>" % (title, desc)

def spec_card(title, rows):
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (k, v) for k, v in rows)
    return ('<div class="spec-card"><h3>%s</h3><table class="spec-table">%s</table></div>' % (title, body))

def faq_item(q, a):
    return ('<div class="faq-item"><button class="faq-question"><span>%s</span><i class="fas fa-chevron-down"></i></button>'
            '<div class="faq-answer"><p>%s</p></div></div>' % (q, a))

def related_card(slug):
    p = LOOKUP[slug]
    short = p.get("short", "")
    if len(short) > 64:
        cut = short.rfind(" ", 0, 64)
        short = short[:cut if cut > 30 else 64] + "..."
    return ('<article class="product-card"><div class="product-image"><img src="../../imgs/products/%s.jpg" alt="%s" loading="lazy"></div>'
            '<div class="product-info"><h3>%s</h3><p>%s</p><a href="../../product/%s/index.html" class="btn btn-outline">View Details</a></div></article>'
            % (slug, p["name"], p["name"], short, slug))

count = 0
for p in PRODUCTS:
    features = "\n".join(feature_li(t, d) for t, d in p["features"])
    specs = "\n".join(spec_card(t, rows) for t, rows in p["spec_groups"])
    benefits = "\n".join('<div class="benefit-item"><i class="fas fa-check-circle"></i><span>%s</span></div>' % b for b in p["benefits"])
    usecases = "\n".join('<div class="use-case"><i class="fas %s"></i><span>%s</span></div>' % (app_icon(a), a) for a in p["applications"])
    faq_html = "\n".join(faq_item(q, a) for q, a in p["faq"])
    related = "\n".join(related_card(s) for s in p["related"])

    rating_bars = "\n".join(
        '<div class="rating-bar"><span>%s</span><div class="bar"><div class="fill" style="width:%s%%"></div></div><span>%s%%</span></div>' % (label, w, w)
        for label, w in RATING_BREAKDOWN
    )
    reviews = "\n".join(
        '<div class="review-item"><div class="review-header"><div class="reviewer-info"><span class="reviewer-name">%s</span><span class="verified-badge"><i class="fas fa-check-circle"></i> Verified Purchase</span></div><div class="review-rating"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div><p class="review-text">%s</p><span class="review-date">%s</span></div>'
        % (name, text, date) for name, text, date in REVIEWS
    )

    product_json = json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": p["title"], "description": p["meta"],
        "image": "https://www.chinachallengecoin.com/imgs/products/" + p["slug"] + ".jpg",
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
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": "https://www.chinachallengecoin.com/product/" + p["slug"] + "/index.html"},
        ],
    }, ensure_ascii=False)

    html = (TEMPLATE
            .replace("{{TITLE}}", p["title"])
            .replace("{{NAME}}", p["name"])
            .replace("{{CATEGORY}}", p["category"])
            .replace("{{META}}", p["meta"])
            .replace("{{KEYWORDS}}", p["keywords"])
            .replace("{{SLUG}}", p["slug"])
            .replace("{{SHORT}}", p["short"])
            .replace("{{OVERVIEW_P1}}", p["overview"][0])
            .replace("{{OVERVIEW_P2}}", p["overview"][1])
            .replace("{{OVERVIEW_P3}}", p["overview"][2])
            .replace("{{FEATURES}}", features)
            .replace("{{SPECS}}", specs)
            .replace("{{BENEFITS}}", benefits)
            .replace("{{USECASES}}", usecases)
            .replace("{{FAQ_HTML}}", faq_html)
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

print(f"Generated {count} rich product pages.")
