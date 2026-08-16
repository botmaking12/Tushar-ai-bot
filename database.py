# ============================================================
# 🔱 BABADEV AI — DATABASE
# ============================================================
# SQLite database layer for:
# 👤 Users
# 💬 Chat history
# 👑 Premium
# 📊 Statistics
# ⭐ Favorites
# 🗂️ Chat folders
# 🔐 Daily usage limits
# 📝 Quiz history
# 📄 PDF history
# ============================================================

import aiosqlite
from datetime import datetime, timezone
from typing import Optional, Any

from config import DATABASE_PATH


# ============================================================
# 🕐 TIME HELPER
# ============================================================

def now_utc() -> str:
    """Return current UTC time in ISO format."""
    return datetime.now(timezone.utc).isoformat()


# ============================================================
# 🗄️ DATABASE INITIALIZATION
# ============================================================

async def init_db():
    """Create all required database tables."""

    async with aiosqlite.connect(DATABASE_PATH) as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                language TEXT DEFAULT 'hi',

                is_premium INTEGER DEFAULT 0,
                premium_until TEXT,

                daily_usage INTEGER DEFAULT 0,
                usage_date TEXT,

                total_messages INTEGER DEFAULT 0,
                total_files INTEGER DEFAULT 0,
                total_searches INTEGER DEFAULT 0,
                total_quizzes INTEGER DEFAULT 0,

                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,

                role TEXT NOT NULL,
                content TEXT NOT NULL,

                mode TEXT DEFAULT 'chat',

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                title TEXT NOT NULL,
                content TEXT NOT NULL,
                category TEXT DEFAULT 'general',

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS folders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                name TEXT NOT NULL,

                created_at TEXT NOT NULL,

                UNIQUE(user_id, name),

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS folder_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                folder_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,

                title TEXT,
                content TEXT NOT NULL,

                created_at TEXT NOT NULL,

                FOREIGN KEY(folder_id)
                    REFERENCES folders(id)
                    ON DELETE CASCADE,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS usage_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                feature TEXT NOT NULL,
                amount INTEGER DEFAULT 1,

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS quiz_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                topic TEXT,
                language TEXT,

                total_questions INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS pdf_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                filename TEXT,
                action TEXT,

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                user_id INTEGER NOT NULL,

                plan TEXT NOT NULL,
                amount INTEGER NOT NULL,

                payment_method TEXT,
                transaction_id TEXT,

                status TEXT DEFAULT 'pending',

                created_at TEXT NOT NULL,
                verified_at TEXT,

                FOREIGN KEY(user_id)
                    REFERENCES users(user_id)
                    ON DELETE CASCADE
            )
        """)

        await db.commit()


# ============================================================
# 👤 USER MANAGEMENT
# ============================================================

async def create_or_update_user(
    user_id: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    language: Optional[str] = None,
):
    """Create a user or update existing user information."""

    timestamp = now_utc()

    async with aiosqlite.connect(DATABASE_PATH) as db:

        cursor = await db.execute(
            """
            SELECT user_id
            FROM users
            WHERE user_id = ?
            """,
            (user_id,)
        )

        existing = await cursor.fetchone()

        if existing:

            await db.execute(
                """
                UPDATE users
                SET
                    username = COALESCE(?, username),
                    first_name = COALESCE(?, first_name),
                    language = COALESCE(?, language),
                    updated_at = ?
                WHERE user_id = ?
                """,
                (
                    username,
                    first_name,
                    language,
                    timestamp,
                    user_id,
                )
            )

        else:

            await db.execute(
                """
                INSERT INTO users (
                    user_id,
                    username,
                    first_name,
                    language,
                    usage_date,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    username,
                    first_name,
                    language or "hi",
                    timestamp[:10],
                    timestamp,
                    timestamp,
                )
            )

        await db.commit()


# ============================================================
# 👤 GET USER
# ============================================================

async def get_user(user_id: int):
    """Return user information as a dictionary."""

    async with aiosqlite.connect(DATABASE_PATH) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *
            FROM users
            WHERE user_id = ?
            """,
            (user_id,)
        )

        row = await cursor.fetchone()

        if not row:
            return None

        return dict(row)


# ============================================================
# 🌍 LANGUAGE
# ============================================================

async def set_language(
    user_id: int,
    language: str
):
    """Update user's preferred language."""

    async with aiosqlite.connect(DATABASE_PATH) as db:

        await db.execute(
            """
            UPDATE users
            SET language = ?, updated_at = ?
            WHERE user_id = ?
            """,
            (
                language,
                now_utc(),
                user_id,
            )
        )

        await db.commit()


# ============================================================
# 👑 PREMIUM
# ============================================================

async def set_premium(
    user_id: int,
    premium_until: Optional[str]
):
    """Enable premium for a user."""

    async with aiosqlite.connect(DATABASE_PATH) as db:

        await db.execute(
            """
            UPDATE users
            SET
                is_premium = 1,
                premium_until = ?,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                premium_until,
                now_utc(),
                user_id,
            )
        )

        await db.commit()


async def remove_premium(user_id: int):
    """Remove premium status."""

    async with aiosqlite.connect(DATABASE_PATH) as db:

        await db.execute(
            """
            UPDATE users
            SET
                is_premium = 0,
                premium_until = NULL,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                now_utc(),
                user_id,
            )
        )

        await db.commit()


# ============================================================
# 🔐 DAILY USAGE
# ============================================================

async def get_daily_usage(
    user_id: int
) -> int:

    user = await get_user(user_id)

    if not user:
        return 0

    today = datetime.now(
        timezone.utc
    ).date().isoformat()

    if user["usage_date"] != today:

        async with aiosqlite.connect(
            DATABASE_PATH
        ) as db:

            await db.execute(
                """
                UPDATE users
                SET
                    daily_usage = 0,
                    usage_date = ?,
                    updated_at = ?
                WHERE user_id = ?
                """,
                (
                    today,
                    now_utc(),
                    user_id,
                )
            )

            await db.commit()

        return 0

    return int(
        user["daily_usage"] or 0
    )


async def increment_daily_usage(
    user_id: int,
    amount: int = 1
):

    today = datetime.now(
        timezone.utc
    ).date().isoformat()

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            UPDATE users
            SET
                daily_usage =
                    CASE
                        WHEN usage_date != ?
                        THEN ?
                        ELSE daily_usage + ?
                    END,
                usage_date = ?,
                updated_at = ?
            WHERE user_id = ?
            """,
            (
                today,
                amount,
                amount,
                today,
                now_utc(),
                user_id,
            )
        )

        await db.commit()


# ============================================================
# 📊 FEATURE USAGE LOG
# ============================================================

async def log_usage(
    user_id: int,
    feature: str,
    amount: int = 1
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            INSERT INTO usage_logs (
                user_id,
                feature,
                amount,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                feature,
                amount,
                now_utc(),
            )
        )

        await db.execute(
            """
            UPDATE users
            SET
                total_messages =
                    total_messages +
                    CASE
                        WHEN ? IN ('chat', 'study')
                        THEN ?
                        ELSE 0
                    END,

                total_files =
                    total_files +
                    CASE
                        WHEN ? IN ('pdf', 'ocr', 'voice')
                        THEN ?
                        ELSE 0
                    END,

                total_searches =
                    total_searches +
                    CASE
                        WHEN ? = 'web_search'
                        THEN ?
                        ELSE 0
                    END,

                total_quizzes =
                    total_quizzes +
                    CASE
                        WHEN ? = 'quiz'
                        THEN ?
                        ELSE 0
                    END,

                updated_at = ?

            WHERE user_id = ?
            """,
            (
                feature,
                amount,
                feature,
                amount,
                feature,
                amount,
                feature,
                amount,
                now_utc(),
                user_id,
            )
        )

        await db.commit()


# ============================================================
# 💬 CHAT HISTORY
# ============================================================

async def add_chat_message(
    user_id: int,
    role: str,
    content: str,
    mode: str = "chat"
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            INSERT INTO chat_history (
                user_id,
                role,
                content,
                mode,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                role,
                content,
                mode,
                now_utc(),
            )
        )

        await db.commit()


async def get_chat_history(
    user_id: int,
    limit: int = 30
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT role, content, mode, created_at
            FROM chat_history
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (
                user_id,
                limit,
            )
        )

        rows = await cursor.fetchall()

        return [
            dict(row)
            for row in reversed(rows)
        ]


async def clear_chat_history(
    user_id: int
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            DELETE FROM chat_history
            WHERE user_id = ?
            """,
            (user_id,)
        )

        await db.commit()


# ============================================================
# ⭐ FAVORITES
# ============================================================

async def add_favorite(
    user_id: int,
    title: str,
    content: str,
    category: str = "general"
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        cursor = await db.execute(
            """
            INSERT INTO favorites (
                user_id,
                title,
                content,
                category,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                user_id,
                title,
                content,
                category,
                now_utc(),
            )
        )

        await db.commit()

        return cursor.lastrowid


async def get_favorites(
    user_id: int,
    category: Optional[str] = None
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        db.row_factory = aiosqlite.Row

        if category:

            cursor = await db.execute(
                """
                SELECT *
                FROM favorites
                WHERE user_id = ?
                AND category = ?
                ORDER BY id DESC
                """,
                (
                    user_id,
                    category,
                )
            )

        else:

            cursor = await db.execute(
                """
                SELECT *
                FROM favorites
                WHERE user_id = ?
                ORDER BY id DESC
                """,
                (user_id,)
            )

        rows = await cursor.fetchall()

        return [
            dict(row)
            for row in rows
        ]


async def delete_favorite(
    user_id: int,
    favorite_id: int
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            DELETE FROM favorites
            WHERE id = ?
            AND user_id = ?
            """,
            (
                favorite_id,
                user_id,
            )
        )

        await db.commit()


# ============================================================
# 🗂️ FOLDERS
# ============================================================

async def create_folder(
    user_id: int,
    name: str
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        try:

            cursor = await db.execute(
                """
                INSERT INTO folders (
                    user_id,
                    name,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    user_id,
                    name,
                    now_utc(),
                )
            )

            await db.commit()

            return cursor.lastrowid

        except aiosqlite.IntegrityError:

            return None


async def get_folders(
    user_id: int
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *
            FROM folders
            WHERE user_id = ?
            ORDER BY id DESC
            """,
            (user_id,)
        )

        rows = await cursor.fetchall()

        return [
            dict(row)
            for row in rows
        ]


async def delete_folder(
    user_id: int,
    folder_id: int
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            DELETE FROM folders
            WHERE id = ?
            AND user_id = ?
            """,
            (
                folder_id,
                user_id,
            )
        )

        await db.commit()


async def add_folder_message(
    user_id: int,
    folder_id: int,
    content: str,
    title: Optional[str] = None
):

    async with aiosqlite.connect(
        DATABASE_PATH
    ) as db:

        await db.execute(
            """
            INSERT INTO folder_messages (
                folder_id,
                user_
