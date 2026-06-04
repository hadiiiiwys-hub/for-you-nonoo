# ============================================================
# LOVE GAME CONFIGURATION FILE
# Edit everything here — questions, answers, photos, messages
# ============================================================

# ── RELATIONSHIP INFO ──────────────────────────────────────
RELATIONSHIP_START_DATE = "2023-02-14"   # Format: YYYY-MM-DD
PARTNER_NAME = "My Love"                 # Name shown in messages
YOUR_NAME    = "Your Name"               # Your name

# ── WELCOME SCREEN ────────────────────────────────────────
WELCOME_TITLE   = "Welcome to Our Love Journey ❤️"
WELCOME_MESSAGE = "A little game just for you, to celebrate everything we are."

# ── LEVEL 1 — Romantic Question ──────────────────────────
LEVEL1 = {
    "question": "Do you remember when we first met?",
    "answer":   "coffee shop",          # Correct answer (case-insensitive, partial match OK)
    "hint":     "Think about where we had that first nervous coffee ☕",
    "reward_message": "You remembered! That day changed everything for me. 💕",
    "reward_image": "images/level1.jpg",  # Place your photo at static/images/level1.jpg
}

# ── LEVEL 2 — Memory Challenge ───────────────────────────
LEVEL2 = {
    "question": "Which city did we visit on our first trip together?",
    "choices":  ["Paris 🗼", "Rome 🍕", "Barcelona 🌊", "Vienna 🎭"],
    "answer":   "Paris 🗼",             # Must match one of the choices exactly
    "voice_file": "audio/memory.mp3",   # Place your recording at static/audio/memory.mp3
    "message": "That trip was pure magic. Every street felt like it was made for us. 🌹",
}

# ── LEVEL 3 — Memory Gallery ─────────────────────────────
LEVEL3_CARDS = [
    {
        "title": "Our First Date ✨",
        "image": "images/memory1.jpg",      # static/images/memory1.jpg
        "description": "That evening felt like a dream. The way you laughed...",
        "message": "I knew you were special the moment I saw you smile.",
    },
    {
        "title": "Adventure Together 🌄",
        "image": "images/memory2.jpg",      # static/images/memory2.jpg
        "description": "The world is better with you in it.",
        "message": "Every adventure is ten times better with you by my side.",
    },
    {
        "title": "Quiet Moments 🌙",
        "image": "images/memory3.jpg",      # static/images/memory3.jpg
        "description": "Sometimes the best moments are the silent ones.",
        "message": "I love the quiet moments most — just being with you is enough.",
    },
]

# ── LEVEL 4 — Find the Heart ─────────────────────────────
LEVEL4 = {
    "correct_index": 4,   # 0–8, which of the 9 hearts is the right one
    "celebration_message": "You found it! Just like you found your way into my heart. 💖",
}

# ── LEVEL 5 — Secret Message Puzzle ──────────────────────
LEVEL5 = {
    "phrase": "YOU ARE MY EVERYTHING",   # The phrase to unscramble
    "success_message": "Yes! That's exactly how I feel. Every single day. 🎉",
}

# ── FINAL LEVEL — Slideshow ──────────────────────────────
FINAL_LEVEL = {
    "slideshow_images": [
        "images/slide1.jpg",   # Place photos at static/images/slideN.jpg
        "images/slide2.jpg",
        "images/slide3.jpg",
        "images/slide4.jpg",
        "images/slide5.jpg",
    ],
    "background_music": "audio/music.mp3",   # static/audio/music.mp3
    "love_letter": """My dearest {partner},

From the very first moment I saw you, I knew my life would never be the same.
You are the missing piece I never knew I was searching for.

Every day with you is a gift — your laugh, your warmth, your endless kindness
make me fall in love with you all over again.

Thank you for every memory we've built together. Thank you for choosing me.

This little journey is just a tiny glimpse of how much you mean to me.

Forever yours,
{yours}""",
}

# ── FINAL SURPRISE ────────────────────────────────────────
FINAL_SURPRISE = {
    "custom_message": "You are the greatest adventure of my life, and I never want it to end. 💍",
    "button_label":   "Click for the Final Surprise ❤️",
}

# ── EASTER EGG ────────────────────────────────────────────
EASTER_EGG = {
    "title":   "You found the secret! 🥚✨",
    "message": "Not everyone finds this page. But then again, you've always been extraordinary.",
    "image":   "images/easter_egg.jpg",   # static/images/easter_egg.jpg
}
