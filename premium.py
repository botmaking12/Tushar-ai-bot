# ============================================================
# 💎 BABADEV AI — PREMIUM SYSTEM
# ============================================================
# 👑 Premium Users
# 💰 UPI Payment
# 🔐 Daily Limits
# ⭐ Premium Status
# ============================================================

from datetime import datetime, timedelta


# ============================================================
# ⚙️ PREMIUM CONFIG
# ============================================================

FREE_DAILY_LIMIT = 10
PREMIUM_DAILY_LIMIT = 100

PREMIUM_PLANS = {
    "7": {
        "days": 7,
        "price": 29,
        "name": "7 Days",
    },
    "30": {
        "days": 30,
        "price": 99,
        "name": "30 Days",
    },
    "90": {
        "days": 90,
        "price": 249,
        "name": "90 Days",
    },
}


# ============================================================
# 🧠 TEMPORARY PREMIUM STORE
# ============================================================
# Later database.py ke saath connect kiya jayega.

_premium_users = {}
_usage = {}


# ============================================================
# 💎 PREMIUM CHECK
# ============================================================

def is_premium(user_id: int) -> bool:
    """Return True if user's premium subscription is active."""

    user_id = int(user_id)
    data = _premium_users.get(user_id)

    if not data:
        return False

    expires_at = data.get("expires_at")

    if not expires_at:
        return False

    if datetime.now() >= expires_at:
        _premium_users.pop(user_id, None)
        return False

    return True


# ============================================================
# 📅 PREMIUM EXPIRY
# ============================================================

def premium_expiry(user_id: int):
    data = _premium_users.get(int(user_id))

    if not data:
        return None

    return data.get("expires_at")


# ============================================================
# 👑 ACTIVATE PREMIUM
# ============================================================

def activate_premium(
    user_id: int,
    days: int,
    payment_id: str = "",
):
    """
    Activate premium subscription.

    Payment verification should be performed before
    calling this function.
    """

    user_id = int(user_id)

    now = datetime.now()

    existing = _premium_users.get(user_id)

    if existing and existing.get("expires_at"):
        start_from = max(
            now,
            existing["expires_at"]
        )
    else:
        start_from = now

    expires_at = start_from + timedelta(days=days)

    _premium_users[user_id] = {
        "user_id": user_id,
        "started_at": now,
        "expires_at": expires_at,
        "payment_id": payment_id,
    }

    return _premium_users[user_id]


# ============================================================
# ❌ REMOVE PREMIUM
# ============================================================

def remove_premium(user_id: int) -> bool:
    return _premium_users.pop(int(user_id), None) is not None


# ============================================================
# 📊 DAILY USAGE
# ============================================================

def _today_key():
    return datetime.now().strftime("%Y-%m-%d")


def get_usage(user_id: int) -> int:

    user_id = int(user_id)

    user_data = _usage.setdefault(
        user_id,
        {}
    )

    return int(
        user_data.get(
            _today_key(),
            0
        )
    )


# ============================================================
# ➕ INCREASE USAGE
# ============================================================

def increase_usage(
    user_id: int,
    amount: int = 1,
):
    user_id = int(user_id)

    today = _today_key()

    user_data = _usage.setdefault(
        user_id,
        {}
    )

    user_data[today] = (
        int(user_data.get(today, 0))
        + int(amount)
    )

    return user_data[today]


# ============================================================
# 🔐 DAILY LIMIT
# ============================================================

def daily_limit(user_id: int) -> int:

    if is_premium(user_id):
        return PREMIUM_DAILY_LIMIT

    return FREE_DAILY_LIMIT


# ============================================================
# ✅ CAN USE AI?
# ============================================================

def can_use_ai(user_id: int) -> bool:

    return get_usage(user_id) < daily_limit(user_id)


# ============================================================
# 📈 REMAINING REQUESTS
# ============================================================

def remaining_requests(user_id: int) -> int:

    remaining = (
        daily_limit(user_id)
        - get_usage(user_id)
    )

    return max(0, remaining)


# ============================================================
# 🧾 USE ONE REQUEST
# ============================================================

def use_request(user_id: int) -> bool:

    if not can_use_ai(user_id):
        return False

    increase_usage(user_id)

    return True


# ============================================================
# 💎 PREMIUM PLANS TEXT
# ============================================================

def premium_plans_text() -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "        💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "🚀 Unlock the full power of\n"
        "𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 ✨\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐁𝐄𝐍𝐄𝐅𝐈𝐓𝐒\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "⚡ Higher daily AI limit\n"
        "📄 Advanced PDF processing\n"
        "📑 More MCQ generation\n"
        "🖼️ OCR processing\n"
        "🎤 Voice tools\n"
        "🔊 AI Text-to-Voice\n"
        "🌐 Web Search\n"
        "🧑‍🎓 Study Mode\n"
        "📝 Quiz Generator\n"
        "⭐ Favorites\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💰 𝐏𝐋𝐀𝐍𝐒\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "🟢 7 Days  → ₹29\n"
        "🔵 30 Days → ₹99\n"
        "🟣 90 Days → ₹249\n\n"

        "👇 Choose your plan below"
    )


# ============================================================
# 🎛️ PREMIUM KEYBOARD
# ============================================================

def premium_keyboard():
    from telegram import (
        InlineKeyboardButton,
        InlineKeyboardMarkup,
    )

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🟢 7 Days • ₹29",
                callback_data="premium:7"
            ),
        ],
        [
            InlineKeyboardButton(
                "🔵 30 Days • ₹99",
                callback_data="premium:30"
            ),
        ],
        [
            InlineKeyboardButton(
                "🟣 90 Days • ₹249",
                callback_data="premium:90"
            ),
        ],
        [
            InlineKeyboardButton(
                "⭐ My Premium Status",
                callback_data="premium:status"
            ),
        ],
        [
            InlineKeyboardButton(
                "⬅️ AI Home",
                callback_data="ai:home"
            ),
        ],
    ])


# ============================================================
# 💳 PAYMENT INFORMATION
# ============================================================

def payment_text(plan_key: str) -> str:

    plan = PREMIUM_PLANS.get(
        str(plan_key)
    )

    if not plan:
        return "❌ Invalid premium plan."

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "        💳 𝐏𝐀𝐘𝐌𝐄𝐍𝐓\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"💎 Plan: {plan['name']}\n"
        f"💰 Amount: ₹{plan['price']}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📲 𝐔𝐏𝐈 𝐏𝐀𝐘𝐌𝐄𝐍𝐓\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        "UPI payment integration will be\n"
        "connected with the final payment\n"
        "gateway configuration.\n\n"

        "⚠️ Premium should only be activated\n"
        "after payment is successfully verified.\n\n"

        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# ⭐ PREMIUM STATUS
# ============================================================

def premium_status_text(user_id: int) -> str:

    if not is_premium(user_id):

        return (
            "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
            "        ⭐ 𝐒𝐓𝐀𝐓𝐔𝐒\n"
            "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

            "🆓 Current Plan: FREE\n\n"

            f"📊 Used Today: `{get_usage(user_id)}`\n"
            f"🔐 Daily Limit: `{daily_limit(user_id)}`\n"
            f"⚡ Remaining: `{remaining_requests(user_id)}`\n\n"

            "💎 Upgrade to Premium for higher\n"
            "limits and additional AI features."
        )

    expiry = premium_expiry(user_id)

    expiry_text = (
        expiry.strftime("%d %b %Y, %I:%M %p")
        if expiry
        else "Unknown"
    )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "        💎 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "👑 Status: ACTIVE\n"
        f"📅 Expires: `{expiry_text}`\n\n"

        f"📊 Used Today: `{get_usage(user_id)}`\n"
        f"⚡ Remaining: `{remaining_requests(user_id)}`\n"
        f"🔐 Daily Limit: `{daily_limit(user_id)}`\n\n"

        "✨ Thank you for supporting\n"
        "𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 🔱"
    )


# ============================================================
# 🚫 LIMIT REACHED
# ============================================================

def limit_reached_text(user_id: int) -> str:

    if is_premium(user_id):
        return (
            "⚠️ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐋𝐈𝐌𝐈𝐓 𝐑𝐄𝐀𝐂𝐇𝐄𝐃\n\n"
            "Aaj ka AI usage limit complete ho gaya hai.\n"
            "⏰ Kal phir se available hoga.\n\n"
            "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
        )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        "       🔐 𝐃𝐀𝐈𝐋𝐘 𝐋𝐈𝐌𝐈𝐓\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "🆓 Aaj ka free AI limit complete ho gaya.\n\n"

        "💎 Premium me upgrade karke\n"
        "higher daily limit unlock karo.\n\n"

        "🚀 More AI • More PDF • More Quiz\n"
        "🔊 Voice • 🌐 Search • 🧑‍🎓 Study Mode\n\n"

        "👇 Upgrade to continue"
    )


# ============================================================
# 🔧 PAYMENT PLACEHOLDER
# ============================================================

def verify_payment(
    payment_id: str,
    expected_amount: int,
) -> bool:
    """
    IMPORTANT:
    This is only a safe placeholder.

    Real UPI/payment gateway verification must happen
    before activating Premium.

    Never trust a user-supplied payment screenshot,
    transaction ID, or callback by itself.
    """

    if not payment_id:
        return False

    return False


# ============================================================
# 🧹 CLEAN OLD DATA
# ============================================================

def cleanup_expired_premium():

    now = datetime.now()

    expired = [
        user_id
        for user_id, data in _premium_users.items()
        if data.get("expires_at")
        and data["expires_at"] <= now
    ]

    for user_id in expired:
        _premium_users.pop(
            user_id,
            None
        )

    return len(expired)
