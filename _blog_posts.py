# -*- coding: utf-8 -*-
from _blog_data_a import POSTS_A
from _blog_data_b import POSTS_B
from _blog_data_c import POSTS_C

POSTS = POSTS_A + POSTS_B + POSTS_C

# Three dedicated 600x400 images per blog post (1 featured + 2 inline article-images).
# All paths are blog-relative (../imgs/...).
# Each entry is {"src": path, "alt": descriptive alt text matching the surrounding paragraph}.
BLOG_IMAGES = {
    "soft-enamel-vs-hard-enamel": [
        {"src": "../imgs/blog/soft-enamel-vs-hard-enamel-1.jpg",
         "alt": "Soft enamel vs hard enamel challenge coins side by side showing the textured and smooth finishes"},
        {"src": "../imgs/blog/soft-enamel-vs-hard-enamel-2.jpg",
         "alt": "Close-up of recessed soft enamel wells with raised metal ridges on a challenge coin"},
        {"src": "../imgs/blog/soft-enamel-vs-hard-enamel-3.jpg",
         "alt": "Close-up of a smooth polished hard enamel challenge coin surface flush with the metal"},
    ],
    "how-to-design-a-challenge-coin": [
        {"src": "../imgs/blog/how-to-design-a-challenge-coin-1.jpg",
         "alt": "Hand-drawn challenge coin sketch with color palette and a finished coin sample"},
        {"src": "../imgs/blog/how-to-design-a-challenge-coin-2.jpg",
         "alt": "Rope edge and chain edge details on custom challenge coins"},
        {"src": "../imgs/blog/how-to-design-a-challenge-coin-3.jpg",
         "alt": "Digital challenge coin design proof displayed on a monitor"},
    ],
    "challenge-coin-etiquette": [
        {"src": "../imgs/blog/challenge-coin-etiquette-1.jpg",
         "alt": "A custom challenge coin held in an open palm"},
        {"src": "../imgs/blog/challenge-coin-etiquette-2.jpg",
         "alt": "Two hands exchanging a challenge coin in a handshake gesture"},
        {"src": "../imgs/blog/challenge-coin-etiquette-3.jpg",
         "alt": "Collection of challenge coins displayed in a presentation case"},
    ],
    "coin-size-guide": [
        {"src": "../imgs/blog/coin-size-guide-1.jpg",
         "alt": "Three challenge coins in different sizes showing a size comparison"},
        {"src": "../imgs/blog/coin-size-guide-2.jpg",
         "alt": "Custom die-cut shield shaped challenge coin"},
        {"src": "../imgs/blog/coin-size-guide-3.jpg",
         "alt": "Hand holding a challenge coin to show its two-inch diameter"},
    ],
    "challenge-coin-edge-types": [
        {"src": "../imgs/blog/challenge-coin-edge-types-1.jpg",
         "alt": "Challenge coins with rope, chain, reeded, and sunburst edge styles"},
        {"src": "../imgs/blog/challenge-coin-edge-types-2.jpg",
         "alt": "Macro close-up of a rope edge texture on a challenge coin"},
        {"src": "../imgs/blog/challenge-coin-edge-types-3.jpg",
         "alt": "Challenge coin with a decorative bezel edge and ornate rim"},
    ],
    "2d-vs-3d-challenge-coins": [
        {"src": "../imgs/blog/2d-vs-3d-challenge-coins-1.jpg",
         "alt": "Flat 2D challenge coin compared with a sculpted 3D challenge coin"},
        {"src": "../imgs/blog/2d-vs-3d-challenge-coins-2.jpg",
         "alt": "Close-up of deeply sculpted 3D relief on a challenge coin"},
        {"src": "../imgs/blog/2d-vs-3d-challenge-coins-3.jpg",
         "alt": "Challenge coin combining 2D enamel color with a 3D relief emblem"},
    ],
}

# Inject images into each post
for p in POSTS:
    p["images"] = BLOG_IMAGES.get(p["slug"], [])
    if p["images"]:
        # Canonical image URL + featured alt text
        p["image"] = p["images"][0]["src"]
        p["image_alt"] = p["images"][0]["alt"]
