# ============================================================
# 🔱 BABADEV AI — CONFIGURATION
# ============================================================

import os


# ============================================================
# 🤖 BOT CONFIG
# ============================================================

BOT_NAME = "𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"

BOT_BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"

BOT_FOOTER = (
    "\n\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
    "✨ Created with AI Technology\n"
    "━━━━━━━━━━━━━━━━━━━━━━"
)


# ============================================================
# 🖼️ START PHOTO
# ============================================================
# GitHub me apna Telegram photo/file_id baad me yahan set karna.

START_PHOTO = os.getenv(
    "START_PHOTO",
    ""
)


# ============================================================
# 👤 CREATOR / WATERMARK
# ============================================================

CREATOR_NAME = os.getenv(
    "CREATOR_NAME",
    "TUSHAR RATHVA"
)

CREATOR_USERNAME = os.getenv(
    "CREATOR_USERNAME",
    "@tushueditz"
)

WATERMARK = (
    f"© 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 • "
    f"𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 "
    f"{CREATOR_NAME}"
)


# ============================================================
# 🌍 LANGUAGES
# ============================================================

LANGUAGES = {
    "hi": {
        "name": "🇮🇳 हिन्दी",
        "code": "hi",
    },

    "gu": {
        "name": "🪷 ગુજરાતી",
        "code": "gu",
    },

    "en": {
        "name": "🇬🇧 English",
        "code": "en",
    },
}


DEFAULT_LANGUAGE = "hi"


# ============================================================
# 🤖 AI MODEL
# ============================================================

AI_MODEL = os.getenv(
    "AI_MODEL",
    "gemini-2.5-flash"
)


# ============================================================
# 🔑 GEMINI API KEY
# ============================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
)


# ============================================================
# 🌐 WEB SEARCH
# ============================================================

WEB_SEARCH_ENABLED = True


# ============================================================
# 📄 PDF SETTINGS
# ============================================================

PDF_MAX_SIZE_MB = 20

PDF_MAX_PAGES = 100


# ============================================================
# 🖼️ OCR SETTINGS
# ============================================================

OCR_MAX_SIZE_MB = 10


# ============================================================
# 🎤 VOICE SETTINGS
# ============================================================

VOICE_MAX_SIZE_MB = 20


# ============================================================
# 🔊 TEXT TO SPEECH
# ============================================================

TTS_MAX_TEXT_LENGTH = 5000


# ============================================================
# 📝 QUIZ SETTINGS
# ============================================================

DEFAULT_QUIZ_COUNT = 10

MAX_QUIZ_COUNT = 50


# ============================================================
# 📑 MCQ SETTINGS
# ============================================================

DEFAULT_MCQ_COUNT = 10

MAX_MCQ_COUNT = 50


# ============================================================
# 🔐 SECURITY
# ============================================================

MAX_MESSAGE_LENGTH = 12000


# ============================================================
# 💬 AI CHAT
# ============================================================

MAX_CHAT_HISTORY = 20


# ============================================================
# ⭐ FAVORITES
# ============================================================

MAX_FAVORITES_PER_USER = 100


# ============================================================
# 🗂️ CHAT FOLDERS
# ============================================================

MAX_FOLDERS_PER_USER = 50


# ============================================================
# 🧑‍🎓 STUDY MODE
# ============================================================

STUDY_MODE_ENABLED = True


STUDY_SUBJECTS = [
    "Medical-Surgical Nursing",
    "Gynaecology & Obstetrics",
    "Community Health Nursing",
    "Child Health Nursing",
    "Fundamentals of Nursing",
    "Mental Health Nursing",
    "General Knowledge",
    "History",
    "Gujarati",
    "English",
    "Maths",
]


# ============================================================
# 💎 PREMIUM
# ============================================================

FREE_DAILY_LIMIT = 10

PREMIUM_DAILY_LIMIT = 100


# ============================================================
# 🧾 PREMIUM PLANS
# ============================================================

PREMIUM_PLANS = {
    "7": {
        "days": 7,
        "price": 29,
        "title": "🟢 7 Days",
    },

    "30": {
        "days": 30,
        "price": 99,
        "title": "🔵 30 Days",
    },

    "90": {
        "days": 90,
        "price": 249,
        "title": "🟣 90 Days",
    },
}


# ============================================================
# 💳 UPI
# ============================================================
# Apna real UPI ID baad me environment variable me set karna.

UPI_ID = os.getenv(
    "UPI_ID",
    ""
)


# ============================================================
# 📊 ADMIN
# ============================================================

ADMIN_IDS = []

admin_env = os.getenv(
    "ADMIN_IDS",
    ""
)

if admin_env:

    for value in admin_env.split(","):

        value = value.strip()

        if value.isdigit():

            ADMIN_IDS.append(
                int(value)
            )


# ============================================================
# 🧹 HELPER
# ============================================================

def get_language_name(
    language_code: str
) -> str:

    language = LANGUAGES.get(
        language_code
    )

    if not language:

        language = LANGUAGES[
            DEFAULT_LANGUAGE
        ]

    return language["name"]


# ============================================================
# 🏷️ FOOTER
# ============================================================

def branded_footer() -> str:

    return (
        "\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        f"👤 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 "
        f"{CREATOR_NAME}\n"
        f"📌 {CREATOR_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )


# ============================================================
# 🏠 HOME TEXT
# ============================================================

def home_text() -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "      🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "✨ आपका Personal AI Assistant\n\n"

        "🤖 Ask anything\n"
        "📄 Summarize PDFs\n"
        "📑 Generate MCQs\n"
        "🖼️ OCR Images\n"
        "🎤 Voice → Text\n"
        "🔊 Text → Voice\n"
        "🌐 Live Web Search\n"
        "🧑‍🎓 Personal Study Mode\n"
        "📝 Quiz Generator\n\n"

        "🌍 Hindi • Gujarati • English\n\n"

        branded_footer()
    )


# ============================================================
# 🩺 CONFIG STATUS
# ============================================================

def config_status() -> dict:

    return {
        "bot_name": BOT_NAME,
        "ai_model": AI_MODEL,
        "gemini_configured": bool(
            GEMINI_API_KEY
        ),
        "web_search": WEB_SEARCH_ENABLED,
        "study_mode": STUDY_MODE_ENABLED,
        "premium": True,
        "languages": list(
            LANGUAGES.keys()
        ),
        "creator": CREATOR_NAME,
}
