/**
 * ChinaChallengeCoin - Custom Challenge Coins
 * Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function () {
    initMobileMenu();
    initStickyHeader();
    initBackToTop();
    initSmoothScroll();
    initFAQ();
    initKnowledgeTabs();
    initQuoteForm();
    initAnimations();
});

/* Mobile menu */
function initMobileMenu() {
    const toggle = document.getElementById('mobileMenuToggle');
    const nav = document.getElementById('mainNav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
        this.classList.toggle('active');
        nav.classList.toggle('active');
        document.body.classList.toggle('menu-open');
    });

    nav.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
            toggle.classList.remove('active');
            nav.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    });

    document.addEventListener('click', function (e) {
        if (!nav.contains(e.target) && !toggle.contains(e.target)) {
            toggle.classList.remove('active');
            nav.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    });
}

/* Sticky header shadow */
function initStickyHeader() {
    const header = document.getElementById('header');
    if (!header) return;
    window.addEventListener('scroll', function () {
        header.style.boxShadow = window.pageYOffset > 50
            ? '0 4px 6px -1px rgba(0,0,0,0.1)'
            : '0 1px 2px 0 rgba(0,0,0,0.05)';
    });
}

/* Back to top */
function initBackToTop() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;
    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    });
    btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

/* Smooth scroll for anchors */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const offset = target.getBoundingClientRect().top + window.pageYOffset - 80;
                window.scrollTo({ top: offset, behavior: 'smooth' });
            }
        });
    });
}

/* FAQ accordion */
function initFAQ() {
    document.querySelectorAll('.faq-item').forEach(function (item) {
        const q = item.querySelector('.faq-question');
        if (!q) return;
        q.addEventListener('click', function () {
            document.querySelectorAll('.faq-item').forEach(function (other) {
                if (other !== item) other.classList.remove('active');
            });
            item.classList.toggle('active');
        });
    });
}

/* Knowledge tabs (edge / color / size / packaging) */
function initKnowledgeTabs() {
    document.querySelectorAll('.tab-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const tabId = this.getAttribute('data-tab');
            const scope = this.closest('.knowledge-tabs');
            if (!scope) return;

            scope.querySelectorAll('.tab-btn').forEach(function (b) { b.classList.remove('active'); });
            this.classList.add('active');

            const panelsContainer = scope.parentElement;
            panelsContainer.querySelectorAll('.tab-panel').forEach(function (p) { p.classList.remove('active'); });
            const panel = panelsContainer.querySelector('#' + tabId);
            if (panel) panel.classList.add('active');
        });
    });
}

/* Quote form */
function initQuoteForm() {
    const form = document.getElementById('quoteForm');
    if (!form) return;

    form.addEventListener('submit', function (e) {
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        submitBtn.disabled = true;

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        if (!data.name || !data.email) {
            e.preventDefault();
            showNotification('Please fill in all required fields', 'error');
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(data.email)) {
            e.preventDefault();
            showNotification('Please enter a valid email address', 'error');
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            return;
        }

        showNotification('Thank you! Your quote request has been sent. We will contact you within 12 hours.', 'success');

        // Form will submit normally to Web3Forms
        setTimeout(function () {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        }, 2000);
    });
}

/* Toast notification */
function showNotification(message, type) {
    document.querySelectorAll('.notification').forEach(function (n) { n.remove(); });
    const el = document.createElement('div');
    el.className = 'notification notification-' + (type || 'success');
    el.innerHTML = '<i class="fas ' + (type === 'error' ? 'fa-exclamation-circle' : 'fa-check-circle') + '"></i> ' + message;
    document.body.appendChild(el);
    setTimeout(function () {
        el.style.transition = 'opacity 0.3s ease';
        el.style.opacity = '0';
        setTimeout(function () { el.remove(); }, 300);
    }, 5000);
}

/* Scroll-in animations */
function initAnimations() {
    const els = document.querySelectorAll('.product-card, .purpose-card, .why-us-card, .testimonial-card, .edge-item, .size-card, .metric-card');
    if (!('IntersectionObserver' in window)) return;
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    els.forEach(function (el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}
