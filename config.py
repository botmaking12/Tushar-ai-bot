# ============================================================
# 🔱 BABADEV AI — CONFIGURATION
# ============================================================

import os
from pathlib import Path


# ============================================================
# 📂 BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# 🤖 TELEGRAM BOT
# ============================================================

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    ""
)


# ============================================================
# 🧠 GOOGLE GEMINI AI
# ============================================================

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY",
    ""
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


# ============================================================
# 👑 ADMIN
# ============================================================

def get_admin_ids():
    raw = os.getenv(
        "ADMIN_IDS",
        ""
    )

    if not raw.strip():
        return set()

    result = set()

    for value in raw.split(","):

        value = value.strip()

        if value.isdigit():
            result.add(int(value))

    return result


ADMIN_IDS = get_admin_ids()


# ============================================================
# 🔱 BRANDING
# ============================================================

BOT_NAME = os.getenv(
    "BOT_NAME",
    "𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
)

BOT_USERNAME = os.getenv(
    "BOT_USERNAME",
    ""
)

CREATOR_NAME = os.getenv(
    "CREATOR_NAME",
    "TUSHAR RATHVA"
)

CREATOR_USERNAME = os.getenv(
    "CREATOR_USERNAME",
    "@tushueditz"
)

BRAND_STYLE = (
    "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
    "✨ Powered by Gemini AI\n"
    f"👨‍💻 Created by {CREATOR_NAME}\n"
    f"📸 {CREATOR_USERNAME}"
)


# ============================================================
# 🖼️ BOT IMAGES
# ============================================================

START_IMAGE = os.getenv(
    "START_IMAGE",
    ""
)

AI_HOME_IMAGE = os.getenv(
    "AI_HOME_IMAGE",
    ""
)

PDF_IMAGE = os.getenv(
    "PDF_IMAGE",
    ""
)

OCR_IMAGE = os.getenv(
    "OCR_IMAGE",
    ""
)

VOICE_IMAGE = os.getenv(
    "VOICE_IMAGE",
    ""
)

QUIZ_IMAGE = os.getenv(
    "QUIZ_IMAGE",
    ""
)


# ============================================================
# 🌍 LANGUAGES
# ============================================================

SUPPORTED_LANGUAGES = {
    "hi": "🇮🇳 हिन्दी",
    "gu": "🪷 ગુજરાતી",
    "en": "🇬🇧 English",
}


DEFAULT_LANGUAGE = os.getenv(
    "DEFAULT_LANGUAGE",
    "hi"
)


# ============================================================
# 🔐 DAILY LIMITS
# ============================================================

FREE_DAILY_LIMIT = int(
    os.getenv(
        "FREE_DAILY_LIMIT",
        "20"
    )
)

PREMIUM_DAILY_LIMIT = int(
    os.getenv(
        "PREMIUM_DAILY_LIMIT",
        "200"
    )
)


# ============================================================
# 👑 PREMIUM
# ============================================================

PREMIUM_ENABLED = (
    os.getenv(
        "PREMIUM_ENABLED",
        "true"
    ).lower()
    == "true"
)


PREMIUM_PRICE = int(
    os.getenv(
        "PREMIUM_PRICE",
        "99"
    )
)


PREMIUM_DAYS = int(
    os.getenv(
        "PREMIUM_DAYS",
        "30"
    )
)


# ============================================================
# 💳 UPI
# ============================================================

UPI_ID = os.getenv(
    "UPI_ID",
    ""
)

UPI_NAME = os.getenv(
    "UPI_NAME",
    CREATOR_NAME
)


# ============================================================
# 📊 USER FEATURES
# ============================================================

ENABLE_STATISTICS = True

ENABLE_FAVORITES = True

ENABLE_CHAT_FOLDERS = True

ENABLE_STUDY_MODE = True

ENABLE_QUIZ = True

ENABLE_PDF = True

ENABLE_OCR = True

ENABLE_VOICE = True

ENABLE_TTS = True

ENABLE_WEB_SEARCH = True


# ============================================================
# 📁 STORAGE
# ============================================================

DATA_DIR = BASE_DIR / "data"

UPLOAD_DIR = DATA_DIR / "uploads"

TEMP_DIR = DATA_DIR / "temp"

PDF_DIR = DATA_DIR / "pdf"

AUDIO_DIR = DATA_DIR / "audio"

IMAGE_DIR = DATA_DIR / "images"


for directory in (
    DATA_DIR,
    UPLOAD_DIR,
    TEMP_DIR,
    PDF_DIR,
    AUDIO_DIR,
    IMAGE_DIR,
):
    directory.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# 📄 FILE LIMITS
# ============================================================

MAX_FILE_SIZE_MB = int(
    os.getenv(
        "MAX_FILE_SIZE_MB",
        "50"
    )
)

MAX_TEXT_LENGTH = int(
    os.getenv(
        "MAX_TEXT_LENGTH",
        "50000"
    )
)


# ============================================================
# 🛡️ SECURITY
# ============================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    ""
)


# ============================================================
# 🎨 UI BRAND COLORS / STYLE NAMES
# ============================================================

EMOJIS = {
    "home": "🏠",
    "ai": "🤖",
    "pdf": "📄",
    "mcq": "📑",
    "ocr": "🖼️",
    "voice": "🎤",
    "tts": "🔊",
    "web": "🌐",
    "study": "🧑‍🎓",
    "quiz": "📝",
    "admin": "📊",
    "premium": "👑",
    "stats": "📈",
    "favorite": "⭐",
    "folder": "🗂️",
    "limit": "🔐",
    "language": "🌍",
    "settings": "⚙️",
    "back": "⬅️",
    "close": "❌",
    "success": "✅",
    "error": "❌",
    "loading": "⏳",
}


# ============================================================
# 📝 FOOTER / WATERMARK
# ============================================================

def brand_footer():
    return (
        "\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        f"👨‍💻 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 {CREATOR_NAME}\n"
        f"📸 {CREATOR_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━"
    )


# ============================================================
# 🏠 HOME TEXT
# ============================================================

def home_text():
    return (
        "╭━━━━━━━━━━━━━━━━━━╮\n"
        "     🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "╰━━━━━━━━━━━━━━━━━━╯\n\n"

        "🤖 Your Smart AI Assistant\n"
        "✨ Study • Create • Search • Learn\n\n"

        "📄 PDF → Summary\n"
        "📑 PDF → MCQ\n"
        "🖼️ Image → Text\n"
        "🎤 Voice → Text\n"
        "🔊 Text → Voice\n"
        "🌐 Live Web Search\n"
        "🧑‍🎓 Personal Study Mode\n"
        "📝 Quiz Generator\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        f"👨‍💻 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲 {CREATOR_NAME}\n"
        f"📸 {CREATOR_USERNAME}\n"
        "━━━━━━━━━━━━━━━━━━"
    )


# ============================================================
# 🔧 CONFIG CHECK
# ============================================================

def config_status():

    missing = []

    if not BOT_TOKEN:
        missing.append(
            "BOT_TOKEN"
        )

    if not GOOGLE_API_KEY:
        missing.append(
            "GOOGLE_API_KEY"
        )

    return {
        "ready": len(missing) == 0,
        "missing": missing,
    }


# ============================================================
# 🚀 STARTUP INFORMATION
# ============================================================

def startup_info():

    status = config_status()

    if status["ready"]:

        return (
            "╭━━━━━━━━━━━━━━━━━━╮\n"
            "   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
            "╰━━━━━━━━━━━━━━━━━━╯\n\n"
            "🟢 AI Engine: READY\n"
            "🧠 Gemini: CONNECTED\n"
            "🌍 Languages: HI / GU / EN\n"
            "📄 PDF: ENABLED\n"
            "🖼️ OCR: ENABLED\n"
            "🎤 Voice: ENABLED\n"
            "📝 Quiz: ENABLED\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"👨‍💻 {CREATOR_NAME}"
        )

    return (
        "⚠️ 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n\n"
        "🔴 Configuration incomplete.\n\n"
        "Missing:\n"
        + "\n".join(
            f"❌ {item}"
            for item in status["missing"]
        )
)
