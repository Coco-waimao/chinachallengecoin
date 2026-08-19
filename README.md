# ChinaChallengeCoin — Static Website

Factory-direct custom challenge coin manufacturer website. Pure static HTML/CSS/JS, no build step.

## Structure

```
├── index.html          Homepage (hero, guarantee, products, by-purpose, process, knowledge, why-us, testimonials, faq, quote, contact)
├── product.html        Product overview (large cards, no filter)
├── aboutus.html        About page
├── blog.html           Blog listing
├── privacy.html        Privacy policy
├── thank-you.html      Form thank-you page
├── product/<slug>/     11 product landing pages
├── blog/               6 SEO articles
├── css/style.css       Single stylesheet
├── js/main.js          Single script
├── imgs/               Compressed images (hero + 12 products)
├── sitemap.xml
├── robots.txt
└── CNAME               Domain for GitHub Pages
```

## Deploy

Any static host works (GitHub Pages, Cloudflare Pages, Vercel, Netlify). The `CNAME` file is ready for GitHub Pages with `www.chinachallengecoin.com`.

## Before going live

1. Contact email is `cocohan520@gmail.com` (already wired into every `mailto:` across the site). Still replace the placeholder phone/WhatsApp and address in `index.html`, `aboutus.html`, `product.html`.
2. Set your real Web3Forms access key in `index.html` (search for `YOUR_WEB3FORMS_ACCESS_KEY`).
3. Confirm the trust metrics (`9.7/10`, `98%`, `50K+`) match your real numbers.
4. Swap placeholder product images if you have real coin photography.
