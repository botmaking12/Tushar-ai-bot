# ============================================================
# 👑 BABADEV AI — ADMIN PANEL
# ============================================================
# 📊 Admin Dashboard
# 👥 User Statistics
# 💎 Premium Management
# 🔐 Admin-only access
# ============================================================

from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# ============================================================
# 👑 ADMIN CONFIG
# ============================================================

try:
    from config import ADMIN_IDS
except ImportError:
    ADMIN_IDS = []


# ============================================================
# 🔐 ADMIN CHECK
# ============================================================

def is_admin(user_id: int) -> bool:
    """Check whether the Telegram user is an admin."""
    try:
        return int(user_id) in [int(x) for x in ADMIN_IDS]
    except Exception:
        return False


# ============================================================
# 🎨 ADMIN HOME TEXT
# ============================================================

def admin_home_text() -> str:
    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "      👑 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "        𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "🛡️ 𝐒𝐲𝐬𝐭𝐞𝐦 𝐂𝐨𝐧𝐭𝐫𝐨𝐥 𝐂𝐞𝐧𝐭𝐞𝐫\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "📊 𝐔𝐬𝐞𝐫 𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐬\n"
        "💎 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭\n"
        "📈 𝐀𝐈 𝐔𝐬𝐚𝐠𝐞\n"
        "🔐 𝐋𝐢𝐦𝐢𝐭𝐬 & 𝐂𝐨𝐧𝐭𝐫𝐨𝐥\n"
        "⚙️ 𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐮𝐬\n\n"

        "✨ Select an option below 👇\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈\n"
        "💠 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐟𝐨𝐫 𝐒𝐭𝐮𝐝𝐲 & 𝐂𝐫𝐞𝐚𝐭𝐢𝐯𝐢𝐭𝐲"
    )


# ============================================================
# 🎛️ ADMIN KEYBOARD
# ============================================================

def admin_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "📊 𝐔𝐬𝐞𝐫 𝐒𝐭𝐚𝐭𝐬",
                callback_data="admin:users"
            ),
            InlineKeyboardButton(
                "💎 𝐏𝐫𝐞𝐦𝐢𝐮𝐦",
                callback_data="admin:premium"
            ),
        ],
        [
            InlineKeyboardButton(
                "📈 𝐀𝐈 𝐔𝐬𝐚𝐠𝐞",
                callback_data="admin:usage"
            ),
            InlineKeyboardButton(
                "🔐 𝐋𝐢𝐦𝐢𝐭𝐬",
                callback_data="admin:limits"
            ),
        ],
        [
            InlineKeyboardButton(
                "⚙️ 𝐒𝐲𝐬𝐭𝐞𝐦",
                callback_data="admin:system"
            ),
            InlineKeyboardButton(
                "📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭",
                callback_data="admin:broadcast"
            ),
        ],
        [
            InlineKeyboardButton(
                "🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡",
                callback_data="admin:home"
            ),
            InlineKeyboardButton(
                "⬅️ 𝐀𝐈 𝐇𝐨𝐦𝐞",
                callback_data="ai:home"
            ),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# ============================================================
# 📊 BASIC STATISTICS
# ============================================================

def admin_stats_text(
    total_users: int = 0,
    active_users: int = 0,
    premium_users: int = 0,
    total_requests: int = 0,
) -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "       📊 𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐒\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 : `{total_users}`\n"
        f"🟢 𝐀𝐜𝐭𝐢𝐯𝐞       : `{active_users}`\n"
        f"💎 𝐏𝐫𝐞𝐦𝐢𝐮𝐦      : `{premium_users}`\n"
        f"🤖 𝐀𝐈 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐬 : `{total_requests}`\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 𝐀𝐍𝐀𝐋𝐘𝐓𝐈𝐂𝐒"
    )


# ============================================================
# 💎 PREMIUM STATUS
# ============================================================

def premium_admin_text(
    premium_users: int = 0,
    revenue: float = 0,
) -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "        💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"👑 Premium Users : `{premium_users}`\n"
        f"💰 Revenue       : `₹{revenue:.2f}`\n\n"

        "🎁 Premium Features\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "⚡ Higher AI limits\n"
        "📄 Advanced PDF tools\n"
        "📝 Unlimited quizzes\n"
        "🌐 Web search\n"
        "🔊 AI Voice\n"
        "🚫 Fewer daily restrictions\n\n"

        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# 📈 AI USAGE
# ============================================================

def usage_admin_text(
    today_requests: int = 0,
    pdf_requests: int = 0,
    ocr_requests: int = 0,
    voice_requests: int = 0,
    quiz_requests: int = 0,
) -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "        📈 𝐀𝐈 𝐔𝐒𝐀𝐆𝐄\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"🤖 Total AI       : `{today_requests}`\n"
        f"📄 PDF           : `{pdf_requests}`\n"
        f"🖼️ OCR           : `{ocr_requests}`\n"
        f"🎤 Voice         : `{voice_requests}`\n"
        f"📝 Quiz          : `{quiz_requests}`\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📅 𝐓𝐨𝐝𝐚𝐲'𝐬 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐲"
    )


# ============================================================
# 🔐 LIMIT SETTINGS
# ============================================================

def limits_admin_text(
    free_limit: int = 10,
    premium_limit: int = 100,
) -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "       🔐 𝐔𝐒𝐀𝐆𝐄 𝐋𝐈𝐌𝐈𝐓𝐒\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"🆓 Free Users\n"
        f"   ➜ `{free_limit}` requests/day\n\n"

        f"💎 Premium Users\n"
        f"   ➜ `{premium_limit}` requests/day\n\n"

        "⚙️ Limits can be changed from the\n"
        "admin configuration later.\n\n"

        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# ⚙️ SYSTEM STATUS
# ============================================================

def system_status_text() -> str:

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "       ⚙️ 𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "🟢 Bot Engine     : ONLINE\n"
        "🟢 Database       : READY\n"
        "🟢 Gemini AI      : READY\n"
        "🟢 OCR Engine     : READY\n"
        "🟢 PDF Engine     : READY\n"
        "🟢 Voice Engine   : READY\n"
        "🟢 Quiz Engine    : READY\n"
        "🟢 Web Search     : READY\n\n"

        f"🕐 Server Time    : `{now}`\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# 🚫 ACCESS DENIED
# ============================================================

def access_denied_text() -> str:
    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "          🚫 𝐀𝐂𝐂𝐄𝐒𝐒\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "❌ You are not authorized to access\n"
        "the Admin Panel.\n\n"

        "🔐 Admin access required.\n\n"

        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# 📢 BROADCAST MENU
# ============================================================

def broadcast_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 Send Broadcast",
                callback_data="admin:broadcast:send"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅️ Admin Panel",
                callback_data="admin:home"
            )
        ]
    ])


# ============================================================
# 🔙 BACK BUTTON
# ============================================================

def admin_back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "⬅️ 𝐀𝐝𝐦𝐢𝐧 𝐏𝐚𝐧𝐞𝐥",
                callback_data="admin:home"
            )
        ]
    ])
