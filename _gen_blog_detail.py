# -*- coding: utf-8 -*-
import os, json, re

BASE = r"C:\code\chinachallengecoin\blog"

PRODUCTS = {
    "soft-enamel-coins": ("Soft Enamel Coins", "Recessed enamel with a tactile, layered finish."),
    "hard-enamel-coins": ("Hard Enamel Coins", "Polished, glass-smooth surface with a premium feel."),
    "3d-coins": ("3D Coins", "Deeply sculpted relief for striking depth and shadow."),
    "uv-printed-coins": ("UV Printed Coins", "Full-color, photo-realistic printing on metal."),
    "no-color-coins": ("No Color Coins", "Pure metal engraving with timeless elegance."),
    "minted-coins": ("Minted Coins", "Mirror proof finish for a collectible struck look."),
    "single-sided-coins": ("Single-Sided Coins", "One detailed face with a flat, customizable back."),
    "bottle-opener-coins": ("Bottle Opener Coins", "A working opener built into an elegant coin."),
    "magnetic-golf-coins": ("Magnetic Golf Coins", "A detachable ball marker — collectible and practical."),
    "fidget-edc-coins": ("Fidget EDC Coins", "A precision spinning mechanism for everyday carry."),
    "spinner-coins": ("Spinner Coins", "A rotating center for a satisfying desk companion."),
}

from _blog_posts import POSTS
POST_LOOKUP = {p["slug"]: p for p in POSTS}

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def render_body(body, inline_images=None):
    """Return (html, toc_items, faq_pairs). inline_images: list of image paths
    to scatter across the article body (after selected H2 sections)."""
    html = []
    toc = []
    faqs = []
    h2_count = 0
    total_h2 = sum(1 for b in body if b[0] == "h2")
    # Decide which H2 indices (1-based) to insert images after. We aim for
    # roughly 1/3 and 2/3 of the article so images are well-distributed.
    insert_after = set()
    if inline_images and total_h2 >= 4:
        insert_after.add(max(1, total_h2 // 3))
        insert_after.add(max(2, (2 * total_h2) // 3))
    image_idx = 0

    for block in body:
        kind = block[0]
        if kind == "h2":
            h2_count += 1
            html.append('<h2 id="%s">%s</h2>' % (slugify(block[1]), block[1]))
            toc.append(block[1])
            if h2_count in insert_after and image_idx < len(inline_images):
                item = inline_images[image_idx]
                html.append(
                    '<div class="article-image"><img src="%s" alt="%s" loading="lazy"></div>'
                    % (item["src"], item["alt"])
                )
                image_idx += 1
        elif kind == "h3":
            html.append("<h3>%s</h3>" % block[1])
        elif kind == "p":
            html.append("<p>%s</p>" % block[1])
        elif kind == "ul":
            html.append("<ul>" + "".join("<li>%s</li>" % x for x in block[1]) + "</ul>")
        elif kind == "ol":
            html.append("<ol>" + "".join("<li>%s</li>" % x for x in block[1]) + "</ol>")
        elif kind == "table":
            t = block[1]
            head = "".join("<th>%s</th>" % c for c in t["head"])
            rows = "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in t["rows"])
            html.append('<table class="article-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (head, rows))
        elif kind == "cta":
            html.append('<div class="cta-box"><h3>Ready to Design Your Custom Coins?</h3><p>Get a free quote and digital proof in 12 hours. Our team will help you refine your design for the best possible result.</p><a href="../index.html#quote" class="btn btn-white">Get Free Quote</a></div>')
        elif kind == "faq":
            html.append('<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>')
            for q, a in block[1]:
                html.append('<h3>%s</h3><p>%s</p>' % (q, a))
                faqs.append((q, a))
    return "\n".join(html), toc, faqs

def render_toc(toc):
    return "\n".join('<li><a href="#%s">%s</a></li>' % (slugify(t), t) for t in toc)

def related_product_card(slug):
    name, desc = PRODUCTS[slug]
    return ('<a href="../product/%s/index.html" class="related-article"><img src="../imgs/products/%s.jpg" alt="%s">'
            '<div class="related-article-info"><h4>%s</h4><span>%s</span></div></a>' % (slug, slug, name, name, desc))

def more_article_card(slug):
    p = POST_LOOKUP[slug]
    return ('<article class="blog-card"><div class="blog-image"><img src="%s" alt="%s" loading="lazy">'
            '<span class="blog-category">%s</span></div><div class="blog-content"><div class="blog-meta">'
            '<span><i class="far fa-calendar"></i> %s</span><span><i class="far fa-clock"></i> %s</span></div>'
            '<h3><a href="%s.html">%s</a></h3><p>%s</p><a href="%s.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a></div></article>'
            % (p["image"], p["title"], p["category"], p["date"], p["read"], slug, p["title"], p["intro"][:120] + "...", slug))

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}} | ChinaChallengeCoin</title>
    <meta name="description" content="{{META}}">
    <meta name="keywords" content="{{KEYWORDS}}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://www.chinachallengecoin.com/blog/{{SLUG}}.html">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='48' fill='%23d97706'/><circle cx='50' cy='50' r='34' fill='none' stroke='%23fff' stroke-width='5'/></svg>">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script type="application/ld+json">{{ARTICLE_JSON}}</script>
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
                <a href="../index.html" class="logo"><span class="logo-icon">🪙</span><span class="logo-text">China<span>Challenge</span>Coin</span></a>
                <nav class="main-nav" id="mainNav">
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../product.html">Products</a></li>
                        <li><a href="../blog.html">Blog</a></li>
                        <li><a href="../index.html#why-us">Why Us</a></li>
                        <li><a href="../aboutus.html">About</a></li>
                        <li><a href="../index.html#contact">Contact</a></li>
                    </ul>
                </nav>
                <div class="header-actions">
                    <a href="../index.html#quote" class="btn btn-gold">Get Free Quote</a>
                    <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
                </div>
            </div>
        </div>
    </header>

    <div class="breadcrumb">
        <div class="container">
            <nav aria-label="breadcrumb">
            <ol class="breadcrumb-list">
                <li><a href="../index.html">Home</a></li>
                <li class="separator"><i class="fas fa-chevron-right"></i></li>
                <li><a href="../blog.html">Blog</a></li>
                <li class="separator"><i class="fas fa-chevron-right"></i></li>
                <li aria-current="page">{{TITLE}}</li>
            </ol>
            </nav>
        </div>
    </div>

    <div class="container">
        <div class="article-layout">
            <article class="article-main">
                <div class="article-meta">
                    <span class="article-category">{{CATEGORY}}</span>
                    <span><i class="far fa-calendar"></i> {{DATE}}</span>
                    <span><i class="far fa-clock"></i> {{READ}}</span>
                </div>
                <h1>{{TITLE}}</h1>
                <div class="article-byline">ChinaChallengeCoin Team</div>
                <div class="article-intro">{{INTRO}}</div>
                <div class="article-featured-image"><img src="{{IMAGE}}" alt="{{IMAGE_ALT}}" loading="lazy"></div>
                <div class="article-body">{{BODY}}</div>
                <div class="article-tags">
                    <span class="tag-label">Tags:</span>{{TAGS}}
                </div>
                <div class="article-share">
                    <span class="share-label">Share:</span>
                    <div class="share-buttons">
                        <a href="https://www.facebook.com/coco.han.39566" target="_blank" class="share-btn" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="share-btn" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                        <a href="https://www.instagram.com/greentree09/" target="_blank" class="share-btn" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="https://wa.me/8615711047494" target="_blank" class="share-btn" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
            </article>

            <aside class="article-sidebar">
                <div class="sidebar-widget toc-widget">
                    <h3>Table of Contents</h3>
                    <ul class="toc-list">{{TOC}}</ul>
                </div>
                <div class="sidebar-widget">
                    <h3>Related Coin Styles</h3>
                    <div class="related-articles">{{RELATED_PRODUCTS}}</div>
                </div>
                <div class="sidebar-widget cta-widget">
                    <h3>Need Custom Coins?</h3>
                    <p>Get a free quote with a digital proof in 12 hours.</p>
                    <a href="../index.html#quote" class="btn btn-white btn-full">Get Free Quote</a>
                </div>
            </aside>
        </div>
    </div>

    <section class="related" style="padding:0 0 4rem;">
        <div class="container">
            <div class="section-header">
                <span class="section-eyebrow">Keep Reading</span>
                <h2>More Articles You Might Like</h2>
            </div>
            <div class="blog-grid">{{MORE_ARTICLES}}</div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../index.html" class="footer-logo"><span class="logo-icon">🪙</span><span class="logo-text">China<span style="color:var(--gold-light)">Challenge</span>Coin</span></a>
                    <p>Factory-direct custom challenge coins with no minimum order. Free design and 12-hour proofs.</p>
                    <div class="footer-certificates"><span><i class="fas fa-shield-alt"></i> Quality Guarantee</span><span><i class="fas fa-leaf"></i> Eco-Friendly Finish</span></div>
                </div>
                <div class="footer-links"><h4>Coin Styles</h4><ul><li><a href="../product/soft-enamel-coins/index.html">Soft Enamel</a></li><li><a href="../product/hard-enamel-coins/index.html">Hard Enamel</a></li><li><a href="../product/3d-coins/index.html">3D Coins</a></li><li><a href="../product/uv-printed-coins/index.html">UV Printed</a></li><li><a href="../product/no-color-coins/index.html">No Color</a></li><li><a href="../product/minted-coins/index.html">Minted</a></li><li><a href="../product/bottle-opener-coins/index.html">Bottle Opener</a></li><li><a href="../product/single-sided-coins/index.html">Single-Sided</a></li><li><a href="../product/magnetic-golf-coins/index.html">Magnetic Golf</a></li></ul></div>
                <div class="footer-links"><h4>Company</h4><ul><li><a href="../aboutus.html">About Us</a></li><li><a href="../blog.html">Blog</a></li><li><a href="../index.html#faq">FAQ</a></li><li><a href="../index.html#contact">Contact</a></li></ul></div>
                <div class="footer-links"><h4>Support</h4><ul><li><a href="../index.html#knowledge">Edge Types</a></li><li><a href="../index.html#process">How It Works</a></li><li><a href="../privacy.html">Privacy Policy</a></li><li><a href="../index.html#quote">Get a Quote</a></li></ul></div>
            </div>
            <div class="footer-bottom"><p>&copy; 2026 ChinaChallengeCoin. All rights reserved.</p><p>Custom Challenge Coins | Made with care in China</p></div>
        </div>
    </footer>

    <button class="back-to-top" id="backToTop" aria-label="Back to top"><i class="fas fa-arrow-up"></i></button>
    <script src="../js/main.js"></script>
</body>
</html>
"""

count = 0
for p in POSTS:
    body_html, toc, faqs = render_body(p["body"], inline_images=p.get("images", [])[1:])
    toc_html = render_toc(toc)
    tags = "\n".join('<a href="#" class="tag">%s</a>' % t for t in p["tags"])
    related_products = "\n".join(related_product_card(s) for s in p["products"])
    more = [s for s in POST_LOOKUP if s != p["slug"]][:3]
    more_html = "\n".join(more_article_card(s) for s in more)

    article_json = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["title"], "description": p["meta"],
        "image": "https://www.chinachallengecoin.com/" + p["image"].replace("../", ""),
        "author": {"@type": "Organization", "name": "ChinaChallengeCoin"},
        "publisher": {"@type": "Organization", "name": "ChinaChallengeCoin"},
        "datePublished": "2026-08-01", "dateModified": "2026-08-16",
        "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.chinachallengecoin.com/blog/" + p["slug"] + ".html"},
    }, ensure_ascii=False)

    faq_json = ""
    if faqs:
        faq_json = json.dumps({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
        }, ensure_ascii=False)

    breadcrumb_json = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.chinachallengecoin.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.chinachallengecoin.com/blog.html"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": "https://www.chinachallengecoin.com/blog/" + p["slug"] + ".html"},
        ],
    }, ensure_ascii=False)

    html = (TEMPLATE
            .replace("{{TITLE}}", p["title"])
            .replace("{{SLUG}}", p["slug"])
            .replace("{{META}}", p["meta"])
            .replace("{{KEYWORDS}}", p["keywords"])
            .replace("{{CATEGORY}}", p["category"])
            .replace("{{DATE}}", p["date"])
            .replace("{{READ}}", p["read"])
            .replace("{{IMAGE}}", p["image"])
            .replace("{{IMAGE_ALT}}", p.get("image_alt", p["title"]))
            .replace("{{INTRO}}", p["intro"])
            .replace("{{BODY}}", body_html)
            .replace("{{TOC}}", toc_html)
            .replace("{{TAGS}}", tags)
            .replace("{{RELATED_PRODUCTS}}", related_products)
            .replace("{{MORE_ARTICLES}}", more_html)
            .replace("{{ARTICLE_JSON}}", article_json)
            .replace("{{FAQ_JSON}}", faq_json)
            .replace("{{BREADCRUMB_JSON}}", breadcrumb_json))

    with open(os.path.join(BASE, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    count += 1

print(f"Generated {count} blog detail pages.")
