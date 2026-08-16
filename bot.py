# ============================================================
# 🤖 TUSHAR AI BOT — MASTER TELEGRAM BOT
# ============================================================
# 👨‍💻 Created by: TUSHAR RATHVA
# 🔱 Brand: TUSHAR AI
#
# Features:
# 📄 PDF Summary
# 📑 PDF → MCQ
# 🖼️ OCR
# 🎤 Voice → Text
# 🔊 Text → Voice
# 🌐 Web Search
# 🧑‍🎓 Study Mode
# 📝 Quiz
# 👑 Premium
# 📊 Admin
# 📈 Statistics
# ⭐ Favorites
# 🗂️ AI Folders
# 🔐 Daily Limits
# 🌍 Hindi / Gujarati / English
# ============================================================

import logging
import os
import tempfile
from pathlib import Path

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# ============================================================
# 🔧 CONFIG
# ============================================================

try:
    from config import BOT_TOKEN, ADMIN_IDS
except Exception:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    ADMIN_IDS = []

try:
    from ai_config import (
        GEMINI_API_KEY,
        CREATOR_NAME,
        BOT_NAME,
    )
except Exception:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    CREATOR_NAME = os.getenv(
        "CREATOR_NAME",
        "TUSHAR RATHVA"
    )
    BOT_NAME = os.getenv(
        "BOT_NAME",
        "TUSHAR AI"
    )

# ============================================================
# 🧩 OPTIONAL MODULES
# ============================================================

try:
    import database
except Exception:
    database = None

try:
    import gemini_ai
except Exception:
    gemini_ai = None

try:
    import pdf_tools
except Exception:
    pdf_tools = None

try:
    import ocr_tools
except Exception:
    ocr_tools = None

try:
    import voice_tools
except Exception:
    voice_tools = None

try:
    import tts_tools
except Exception:
    tts_tools = None

try:
    import web_search
except Exception:
    web_search = None

try:
    import quiz_engine
except Exception:
    quiz_engine = None

try:
    import study_mode
except Exception:
    study_mode = None

try:
    import premium
except Exception:
    premium = None

try:
    import admin_panel
except Exception:
    admin_panel = None

try:
    import media_tools
except Exception:
    media_tools = None

# ============================================================
# 📝 LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

log = logging.getLogger("tushar-ai")

# ============================================================
# 🧠 USER MEMORY / SESSION
# ============================================================

users = {}

# ============================================================
# 🌍 LANGUAGES
# ============================================================

LANGUAGES = {
    "hi": "🇮🇳 Hindi",
    "gu": "🪔 Gujarati",
    "en": "🇬🇧 English",
}

DEFAULT_LANGUAGE = "hi"

# ============================================================
# 🔐 DAILY LIMIT
# ============================================================

FREE_DAILY_LIMIT = 20

# ============================================================
# 🏷️ BRAND
# ============================================================

WATERMARK = (
    f"\n\n━━━━━━━━━━━━━━━━━━━━\n"
    f"👨‍💻 Created by {CREATOR_NAME}\n"
    f"🤖 {BOT_NAME}\n"
    f"━━━━━━━━━━━━━━━━━━━━"
)

# ============================================================
# 🏠 HOME TEXT
# ============================================================

def home_text():
    return (
        "╔══════════════════════╗\n"
        "║   🤖 𝐓𝐔𝐒𝐇𝐀𝐑 𝐀𝐈   ║\n"
        "╚══════════════════════╝\n\n"

        "✨ 𝐘𝐨𝐮𝐫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐀𝐈 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭\n\n"

        "📚 Study • 🤖 AI • 🔎 Search • 🧠 Learn\n\n"

        "📄 PDF → Summary\n"
        "📑 PDF → MCQ\n"
        "🖼️ Image → Text\n"
        "🎤 Voice → Text\n"
        "🔊 Text → Voice\n"
        "🌐 Live Web Search\n"
        "🧑‍🎓 Personal Study Mode\n"
        "📝 Quiz Generator\n\n"

        "👇 नीचे से कोई feature चुनें:"
        + WATERMARK
    )


# ============================================================
# 🏠 HOME KEYBOARD
# ============================================================

def home_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🤖 AI Chat",
                callback_data="ai:chat"
            ),
            InlineKeyboardButton(
                "📚 Study",
                callback_data="study:home"
            ),
        ],

        [
            InlineKeyboardButton(
                "📄 PDF AI",
                callback_data="pdf:home"
            ),
            InlineKeyboardButton(
                "🖼️ OCR",
                callback_data="ocr:start"
            ),
        ],

        [
            InlineKeyboardButton(
                "🎤 Voice",
                callback_data="voice:start"
            ),
            InlineKeyboardButton(
                "🔊 Text → Voice",
                callback_data="tts:start"
            ),
        ],

        [
            InlineKeyboardButton(
                "🌐 Web Search",
                callback_data="web:start"
            ),
            InlineKeyboardButton(
                "📝 Quiz",
                callback_data="quiz:start"
            ),
        ],

        [
            InlineKeyboardButton(
                "⭐ Favorites",
                callback_data="favorites"
            ),
            InlineKeyboardButton(
                "🗂️ AI Folders",
                callback_data="folders"
            ),
        ],

        [
            InlineKeyboardButton(
                "👑 Premium",
                callback_data="premium"
            ),
            InlineKeyboardButton(
                "⚙️ Settings",
                callback_data="settings"
            ),
        ],

        [
            InlineKeyboardButton(
                "📊 My Statistics",
                callback_data="stats"
            ),
        ],

    ])


# ============================================================
# 🌍 LANGUAGE KEYBOARD
# ============================================================

def language_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🇮🇳 हिन्दी",
                callback_data="lang:hi"
            ),
            InlineKeyboardButton(
                "🪔 ગુજરાતી",
                callback_data="lang:gu"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇬🇧 English",
                callback_data="lang:en"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ Home",
                callback_data="home"
            ),
        ],
    ])


# ============================================================
# 📄 PDF KEYBOARD
# ============================================================

def pdf_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📄 AI Summary",
                callback_data="pdf:summary"
            ),
        ],

        [
            InlineKeyboardButton(
                "📑 Generate MCQ",
                callback_data="pdf:mcq"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ AI Home",
                callback_data="home"
            ),
        ],

    ])


# ============================================================
# 📚 STUDY KEYBOARD
# ============================================================

def study_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🧑‍🎓 Study Mode",
                callback_data="study:start"
            ),
        ],

        [
            InlineKeyboardButton(
                "📝 Quiz Practice",
                callback_data="quiz:start"
            ),
        ],

        [
            InlineKeyboardButton(
                "📊 My Progress",
                callback_data="stats"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ Home",
                callback_data="home"
            ),
        ],

    ])


# ============================================================
# ⚙️ SETTINGS KEYBOARD
# ============================================================

def settings_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🌍 Language",
                callback_data="settings:language"
            ),
        ],

        [
            InlineKeyboardButton(
                "📊 Statistics",
                callback_data="stats"
            ),
        ],

        [
            InlineKeyboardButton(
                "🔄 Reset Session",
                callback_data="settings:reset"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ Home",
                callback_data="home"
            ),
        ],

    ])


# ============================================================
# 👋 START
# ============================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user
    uid = user.id

    users.setdefault(
        uid,
        {
            "language": DEFAULT_LANGUAGE,
            "messages": 0,
            "favorites": [],
            "folder": "General",
        }
    )

    text = (
        "🌟 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐔𝐒𝐇𝐀𝐑 𝐀𝐈 🌟\n\n"
        f"👋 Hello {user.first_name}!\n\n"
        "🧠 Smart AI • 📚 Study • 🔎 Search\n"
        "📄 PDF • 🖼️ OCR • 🎤 Voice • 📝 Quiz\n\n"
        "👇 Tap the button below to enter AI Home."
        + WATERMARK
    )

    await update.message.reply_text(
        text,
        reply_markup=home_keyboard()
    )


# ============================================================
# ❓ HELP
# ============================================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "╭━━━「 🆘 HELP 」━━━╮\n\n"

        "🤖 AI Chat\n"
        "📄 PDF Summary / MCQ\n"
        "🖼️ OCR\n"
        "🎤 Voice → Text\n"
        "🔊 Text → Voice\n"
        "🌐 Web Search\n"
        "🧑‍🎓 Study Mode\n"
        "📝 Quiz Generator\n"
        "⭐ Favorites\n"
        "🗂️ AI Folders\n"
        "👑 Premium\n\n"

        "💡 बस message भेजो और AI से बात शुरू करो!"
        + WATERMARK
    )


# ============================================================
# 📊 STATUS
# ============================================================

async def status_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "🟢 𝐓𝐔𝐒𝐇𝐀𝐑 𝐀𝐈 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄\n\n"
        "⚡ AI Engine: READY\n"
        "📚 Study: READY\n"
        "📄 PDF: READY\n"
        "🖼️ OCR: READY\n"
        "🎤 Voice: READY\n"
        "🔊 TTS: READY\n"
        "🌐 Web: READY\n"
        "📝 Quiz: READY"
        + WATERMARK
    )


# ============================================================
# 🔧 SAFE FUNCTION CALL
# ============================================================

async def call_module(
    module,
    possible_names,
    *args,
    **kwargs
):

    if module is None:
        return None

    for name in possible_names:

        fn = getattr(module, name, None)

        if fn is None:
            continue

        try:

            result = fn(*args, **kwargs)

            if hasattr(result, "__await__"):
                result = await result

            return result

        except TypeError:
            continue

        except Exception as exc:
            log.exception(
                "Module function failed: %s",
                name
            )
            return f"ERROR:{exc}"

    return None


# ============================================================
# 🤖 AI CHAT
# ============================================================

async def ai_chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    uid = update.effective_user.id
    message = update.message.text.strip()

    users.setdefault(
        uid,
        {
            "language": DEFAULT_LANGUAGE,
            "messages": 0,
            "favorites": [],
            "folder": "General",
        }
    )

    users[uid]["messages"] += 1

    await update.message.chat.send_action(
        ChatAction.TYPING
    )

    result = await call_module(
        gemini_ai,
        [
            "generate_response",
            "generate_text",
            "ask_gemini",
            "chat",
            "ask",
            "generate",
        ],
        message
    )

    if result is None:

        result = (
            "⚠️ AI engine अभी properly connected नहीं है.\n\n"
            "Check करो:\n"
            "1️⃣ GEMINI_API_KEY\n"
            "2️⃣ gemini_ai.py\n"
            "3️⃣ requirements.txt\n"
            "4️⃣ Server logs"
        )

    elif isinstance(result, str) and result.startswith(
        "ERROR:"
    ):

        result = (
            "❌ AI Error\n\n"
            f"{result[6:]}"
        )

    await update.message.reply_text(
        f"🤖 𝐓𝐔𝐒𝐇𝐀𝐑 𝐀𝐈\n
