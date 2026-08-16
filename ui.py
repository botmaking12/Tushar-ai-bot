# ============================================================
# 🔱 BABADEV AI — PROFESSIONAL TELEGRAM UI
# ============================================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    BOT_NAME,
    CREATOR_NAME,
    CREATOR_USERNAME,
    SUPPORTED_LANGUAGES,
    brand_footer,
)


# ============================================================
# 🔱 BRAND HEADER
# ============================================================

def brand_header():
    return (
        "╭━━━━━━━━━━━━━━━━━━━━╮\n"
        "     🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )


def brand_credit():
    return (
        "\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"👨‍💻 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐛𝐲: {CREATOR_NAME}\n"
        f"📸 {CREATOR_USERNAME}\n"
        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )


# ============================================================
# 🏠 HOME TEXT
# ============================================================

def home_text():
    return (
        f"{brand_header()}\n\n"

        "🤖 **Your Personal AI Assistant**\n"
        "✨ Learn • Create • Search • Study\n\n"

        "╭─────── 🚀 𝐀𝐈 𝐓𝐎𝐎𝐋𝐒 ───────╮\n"
        "│ 🤖 AI Chat\n"
        "│ 📄 PDF Summary\n"
        "│ 📑 PDF → MCQ\n"
        "│ 🖼️ Image → Text\n"
        "│ 🎤 Voice → Text\n"
        "│ 🔊 Text → Voice\n"
        "│ 🌐 Live Web Search\n"
        "╰────────────────────────────╯\n\n"

        "╭─────── 🎓 𝐒𝐓𝐔𝐃𝐘 ───────╮\n"
        "│ 🧑‍🎓 Personal Study Mode\n"
        "│ 📝 Quiz Generator\n"
        "│ 📚 Smart Notes\n"
        "│ 🩺 Nursing Study Mode\n"
        "╰────────────────────────╯"

        + brand_credit()
    )


# ============================================================
# 🏠 MAIN KEYBOARD
# ============================================================

def home_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🤖 𝐀𝐈 𝐂𝐡𝐚𝐭",
                callback_data="ai:chat"
            ),
            InlineKeyboardButton(
                "🧑‍🎓 𝐒𝐭𝐮𝐝𝐲",
                callback_data="ai:study"
            ),
        ],

        [
            InlineKeyboardButton(
                "📄 𝐏𝐃𝐅 𝐀𝐈",
                callback_data="ai:pdf"
            ),
            InlineKeyboardButton(
                "📑 𝐏𝐃𝐅 → 𝐌𝐂𝐐",
                callback_data="ai:pdfmcq"
            ),
        ],

        [
            InlineKeyboardButton(
                "🖼️ 𝐎𝐂𝐑",
                callback_data="ai:ocr"
            ),
            InlineKeyboardButton(
                "🎤 𝐕𝐨𝐢𝐜𝐞",
                callback_data="ai:voice"
            ),
        ],

        [
            InlineKeyboardButton(
                "🔊 𝐓𝐞𝐱𝐭 → 𝐕𝐨𝐢𝐜𝐞",
                callback_data="ai:tts"
            ),
            InlineKeyboardButton(
                "🌐 𝐖𝐞𝐛 𝐒𝐞𝐚𝐫𝐜𝐡",
                callback_data="ai:web"
            ),
        ],

        [
            InlineKeyboardButton(
                "📝 𝐐𝐮𝐢𝐳",
                callback_data="ai:quiz"
            ),
            InlineKeyboardButton(
                "📚 𝐍𝐨𝐭𝐞𝐬",
                callback_data="ai:notes"
            ),
        ],

        [
            InlineKeyboardButton(
                "⭐ 𝐅𝐚𝐯𝐨𝐫𝐢𝐭𝐞𝐬",
                callback_data="user:favorites"
            ),
            InlineKeyboardButton(
                "🗂️ 𝐅𝐨𝐥𝐝𝐞𝐫𝐬",
                callback_data="user:folders"
            ),
        ],

        [
            InlineKeyboardButton(
                "📈 𝐒𝐭𝐚𝐭𝐬",
                callback_data="user:stats"
            ),
            InlineKeyboardButton(
                "👑 𝐏𝐫𝐞𝐦𝐢𝐮𝐦",
                callback_data="premium:home"
            ),
        ],

        [
            InlineKeyboardButton(
                "🌍 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞",
                callback_data="settings:language"
            ),
            InlineKeyboardButton(
                "⚙️ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬",
                callback_data="settings:home"
            ),
        ],

        [
            InlineKeyboardButton(
                "❌ 𝐂𝐥𝐨𝐬𝐞",
                callback_data="ai:close"
            )
        ],
    ])


# ============================================================
# 🤖 AI CHAT MENU
# ============================================================

def chat_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "💬 𝐍𝐞𝐰 𝐂𝐡𝐚𝐭",
                callback_data="chat:new"
            ),
            InlineKeyboardButton(
                "🗑️ 𝐂𝐥𝐞𝐚𝐫",
                callback_data="chat:clear"
            ),
        ],

        [
            InlineKeyboardButton(
                "⭐ 𝐒𝐚𝐯𝐞",
                callback_data="chat:save"
            ),
            InlineKeyboardButton(
                "🗂️ 𝐅𝐨𝐥𝐝𝐞𝐫",
                callback_data="chat:folder"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ 𝐀𝐈 𝐇𝐨𝐦𝐞",
                callback_data="ai:home"
            )
        ],
    ])


# ============================================================
# 🌍 LANGUAGE MENU
# ============================================================

def language_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🇮🇳 हिन्दी",
                callback_data="lang:hi"
            ),
        ],

        [
            InlineKeyboardButton(
                "🪷 ગુજરાતી",
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
                "⬅️ 𝐁𝐚𝐜𝐤",
                callback_data="ai:home"
            ),
        ],
    ])


# ============================================================
# 🧑‍🎓 STUDY MENU
# ============================================================

def study_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📚 𝐒𝐭𝐮𝐝𝐲 𝐓𝐨𝐩𝐢𝐜",
                callback_data="study:topic"
            ),
        ],

        [
            InlineKeyboardButton(
                "📝 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐌𝐂𝐐",
                callback_data="study:mcq"
            ),
            InlineKeyboardButton(
                "📖 𝐒𝐦𝐚𝐫𝐭 𝐍𝐨𝐭𝐞𝐬",
                callback_data="ai:notes"
            ),
        ],

        [
            InlineKeyboardButton(
                "🩺 𝐍𝐮𝐫𝐬𝐢𝐧𝐠 𝐌𝐨𝐝𝐞",
                callback_data="study:nursing"
            ),
        ],

        [
            InlineKeyboardButton(
                "📝 𝐐𝐮𝐢𝐳",
                callback_data="ai:quiz"
            ),
            InlineKeyboardButton(
                "📊 𝐌𝐲 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬",
                callback_data="user:stats"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ 𝐀𝐈 𝐇𝐨𝐦𝐞",
                callback_data="ai:home"
            )
        ],
    ])


# ============================================================
# 📄 PDF MENU
# ============================================================

def pdf_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📄 𝐒𝐮𝐦𝐦𝐚𝐫𝐢𝐳𝐞 𝐏𝐃𝐅",
                callback_data="pdf:summary"
            ),
        ],

        [
            InlineKeyboardButton(
                "📑 𝐏𝐃𝐅 → 𝐌𝐂𝐐",
                callback_data="pdf:mcq"
            ),
        ],

        [
            InlineKeyboardButton(
                "🔑 𝐊𝐞𝐲𝐰𝐨𝐫𝐝𝐬",
                callback_data="pdf:keywords"
            ),
            InlineKeyboardButton(
                "📝 𝐍𝐨𝐭𝐞𝐬",
                callback_data="pdf:notes"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ 𝐀𝐈 𝐇𝐨𝐦𝐞",
                callback_data="ai:home"
            )
        ],
    ])


# ============================================================
# 🖼️ OCR MENU
# ============================================================

def ocr_keyboard():

    return InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "🖼️ 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐓𝐞𝐱𝐭",
                callback_data="ocr:text"
            ),
        ],

        [
            InlineKeyboardButton(
                "🧠 𝐄𝐱𝐩𝐥𝐚𝐢𝐧 𝐈𝐦𝐚𝐠𝐞",
                callback_data="ocr:explain"
            ),
        ],

        [
            InlineKeyboardButton(
                "🌍 𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐞",
                callback_data="ocr:translate"
            ),
        ],

        [
            InlineKeyboardButton(
                "⬅️ 𝐀𝐈 𝐇𝐨𝐦𝐞",
                callback_data="ai:home"
            )
        ],
    ])


#
