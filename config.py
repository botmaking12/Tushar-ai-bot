# ============================================================
# 🔱 BABADEV AI — CONFIGURATION
# ============================================================
# Central configuration for the complete AI Telegram Bot.
# ============================================================

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# ============================================================
# 🤖 TELEGRAM BOT
# ============================================================

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

# Example:
# ADMIN_IDS=123456789,987654321

ADMIN_IDS = {
    int(user_id.strip())
    for user_id in os.getenv("ADMIN_IDS", "").split(",")
    if user_id.strip().isdigit()
}


# ============================================================
# 🧠 GOOGLE GEMINI AI
# ============================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
).strip()

GEMINI_VISION_MODEL = os.getenv(
    "GEMINI_VISION_MODEL",
    "gemini-2.5-flash"
).strip()

GEMINI_TTS_MODEL = os.getenv(
    "GEMINI_TTS_MODEL",
    "gemini-2.5-flash-preview-tts"
).strip()


# ============================================================
# 🌐 LIVE WEB SEARCH
# ============================================================

WEB_SEARCH_ENABLED = (
    os.getenv(
        "WEB_SEARCH_ENABLED",
        "true"
    ).lower()
    in ("1", "true", "yes", "on")
)


# ============================================================
# 🔱 BABADEV AI BRANDING
# ============================================================

BOT_NAME = os.getenv(
    "BOT_NAME",
    "BABADEV AI"
).strip()

BOT_SHORT_NAME = os.getenv(
    "BOT_SHORT_NAME",
    "BABADEV"
).strip()

CREATOR_NAME = os.getenv(
    "CREATOR_NAME",
    "Tushar"
).strip()


# Premium footer
BRAND_FOOTER = (
    "╭━━━ 🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 ━━━╮\n"
    f"┃ ✨ Powered by {BOT_NAME}\n"
    f"┃ 👑 Created by {CREATOR_NAME}\n"
    "╰━━━━━━━━━━━━━━━━━━━━━━╯"
)


# Short watermark
BRAND_WATERMARK = (
    f"🔱 {BOT_NAME} • 👑 {CREATOR_NAME}"
)


# ============================================================
# 🌍 SUPPORTED LANGUAGES
# ============================================================

SUPPORTED_LANGUAGES = {
    "hi": "🇮🇳 हिन्दी",
    "gu": "🪔 ગુજરાતી",
    "en": "🇬🇧 English",
}

DEFAULT_LANGUAGE = os.getenv(
    "DEFAULT_LANGUAGE",
    "hi"
).strip().lower()

if DEFAULT_LANGUAGE not in SUPPORTED_LANGUAGES:
    DEFAULT_LANGUAGE = "hi"


# ============================================================
# 🔐 FREE USER LIMITS
# ============================================================

FREE_DAILY_LIMIT = int(
    os.getenv(
        "FREE_DAILY_LIMIT",
        "20"
    )
)

FREE_PDF_LIMIT = int(
    os.getenv(
        "FREE_PDF_LIMIT",
        "3"
    )
)

FREE_OCR_LIMIT = int(
    os.getenv(
        "FREE_OCR_LIMIT",
        "10"
    )
)

FREE_VOICE_LIMIT = int(
    os.getenv(
        "FREE_VOICE_LIMIT",
        "10"
    )
)

FREE_WEB_SEARCH_LIMIT = int(
    os.getenv(
        "FREE_WEB_SEARCH_LIMIT",
        "10"
    )
)

FREE_QUIZ_LIMIT = int(
    os.getenv(
        "FREE_QUIZ_LIMIT",
        "5"
    )
)


# ============================================================
# 👑 PREMIUM USER LIMITS
# ============================================================

PREMIUM_DAILY_LIMIT = int(
    os.getenv(
        "PREMIUM_DAILY_LIMIT",
        "200"
    )
)

PREMIUM_PDF_LIMIT = int(
    os.getenv(
        "PREMIUM_PDF_LIMIT",
        "50"
    )
)

PREMIUM_OCR_LIMIT = int(
    os.getenv(
        "PREMIUM_OCR_LIMIT",
        "100"
    )
)

PREMIUM_VOICE_LIMIT = int(
    os.getenv(
        "PREMIUM_VOICE_LIMIT",
        "100"
    )
)

PREMIUM_WEB_SEARCH_LIMIT = int(
    os.getenv(
        "PREMIUM_WEB_SEARCH_LIMIT",
        "100"
    )
)

PREMIUM_QUIZ_LIMIT = int(
    os.getenv(
        "PREMIUM_QUIZ_LIMIT",
        "50"
    )
)


# ============================================================
# 👑 PREMIUM SYSTEM
# ============================================================

PREMIUM_ENABLED = (
    os.getenv(
        "PREMIUM_ENABLED",
        "true"
    ).lower()
    in ("1", "true", "yes", "on")
)


# ============================================================
# 💳 UPI / PAYMENT
# ============================================================

UPI_ID = os.getenv(
    "UPI_ID",
    ""
).strip()

PREMIUM_MONTHLY_PRICE = int(
    os.getenv(
        "PREMIUM_MONTHLY_PRICE",
        "99"
    )
)

PREMIUM_YEARLY_PRICE = int(
    os.getenv(
        "PREMIUM_YEARLY_PRICE",
        "799"
    )
)


# ============================================================
# 🗄️ DATABASE
# ============================================================

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "babadev_ai.db"
).strip()


# ============================================================
# 📁 STORAGE DIRECTORIES
# ============================================================

DATA_DIR = Path(
    os.getenv(
        "DATA_DIR",
        "data"
    )
)

UPLOAD_DIR = DATA_DIR / "uploads"
PDF_DIR = DATA_DIR / "pdf"
VOICE_DIR = DATA_DIR / "voice"
TTS_DIR = DATA_DIR / "tts"
TEMP_DIR = DATA_DIR / "temp"


# ============================================================
# 📄 FILE SETTINGS
# ============================================================

MAX_FILE_SIZE_MB = int(
    os.getenv(
        "MAX_FILE_SIZE_MB",
        "50"
    )
)

MAX_PDF_PAGES = int(
    os.getenv(
        "MAX_PDF_PAGES",
        "100"
    )
)


# ============================================================
# 🧠 AI CHAT SETTINGS
# ============================================================

MAX_HISTORY_MESSAGES = int(
    os.getenv(
        "MAX_HISTORY_MESSAGES",
        "30"
    )
)


# ============================================================
# ⏱️ NETWORK SETTINGS
# ============================================================

REQUEST_TIMEOUT = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        "120"
    )
)


# ============================================================
# 🛡️ BOT SECURITY
# ============================================================

ALLOW_GROUPS = (
    os.getenv(
        "ALLOW_GROUPS",
        "false"
    ).lower()
    in ("1", "true", "yes", "on")
)

DELETE_TEMP_FILES = (
    os.getenv(
        "DELETE_TEMP_FILES",
        "true"
    ).lower()
    in ("1", "true", "yes", "on")
)


# ============================================================
# 🧪 DEBUG MODE
# ============================================================

DEBUG = (
    os.getenv(
        "DEBUG",
        "false"
    ).lower()
    in ("1", "true", "yes", "on")
)


# ============================================================
# 🔐 ADMIN CHECK
# ============================================================

def is_admin(user_id: int) -> bool:
    """Return True when the Telegram user is an admin."""

    return user_id in ADMIN_IDS


# ============================================================
# ⚙️ CONFIG VALIDATION
# ============================================================

def validate_config():
    """
    Validate required configuration.

    Returns:
        list[str]: Configuration errors.
    """

    errors = []

    if not BOT_TOKEN:
        errors.append(
            "❌ BOT_TOKEN is missing"
        )

    if not GEMINI_API_KEY:
        errors.append(
            "❌ GEMINI_API_KEY is missing"
        )

    if not ADMIN_IDS:
        errors.append(
            "❌ ADMIN_IDS is missing"
        )

    return errors


# ============================================================
# 📊 SAFE CONFIG SUMMARY
# ============================================================

def config_summary() -> str:
    """
    Return a safe configuration summary.

    Secrets such as BOT_TOKEN and GEMINI_API_KEY
    are never displayed.
    """

    premium_status = (
        "🟢 ENABLED"
        if PREMIUM_ENABLED
        else "🔴 DISABLED"
    )

    search_status = (
        "🟢 ENABLED"
        if WEB_SEARCH_ENABLED
        else "🔴 DISABLED"
    )

    return (
        "╭━━━ ✨ 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 ✨ ━━━╮\n"
        f"┃ 🤖 Bot       : {BOT_NAME}\n"
        f"┃ 🧠 AI Model  : {GEMINI_MODEL}\n"
        f"┃ 🌍 Languages : "
        f"{len(SUPPORTED_LANGUAGES)}\n"
        f"┃ 👑 Premium   : {premium_status}\n"
        f"┃ 🌐 Web Search: {search_status}\n"
        f"┃ 🔐 Free Limit: "
        f"{FREE_DAILY_LIMIT}/day\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"
        f"🔱 {BOT_NAME}\n"
        f"👑 Created by {CREATOR_NAME}"
)
