# ============================================================
# 🔱 BABADEV AI
# 🌐 LIVE WEB SEARCH ENGINE
# ============================================================

import html
from urllib.parse import quote_plus

import aiohttp
from bs4 import BeautifulSoup


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# ⚙️ SETTINGS
# ============================================================

SEARCH_URL = (
    "https://www.google.com/search?q={}"
)

MAX_RESULTS = 5

TIMEOUT_SECONDS = 15


# ============================================================
# 🌐 SEARCH WEB
# ============================================================

async def search_web(
    query: str,
    max_results: int = MAX_RESULTS
) -> list:

    query = query.strip()

    if not query:
        return []

    encoded_query = quote_plus(
        query
    )

    url = SEARCH_URL.format(
        encoded_query
    )

    headers = {
        "User-Agent":
            (
                "Mozilla/5.0 "
                "(Linux; Android 10) "
                "AppleWebKit/537.36 "
                "Chrome/120.0 Mobile Safari/537.36"
            )
    }

    timeout = aiohttp.ClientTimeout(
        total=TIMEOUT_SECONDS
    )

    async with aiohttp.ClientSession(
        timeout=timeout,
        headers=headers
    ) as session:

        async with session.get(
            url
        ) as response:

            if response.status != 200:
                raise RuntimeError(
                    f"Web search failed: "
                    f"HTTP {response.status}"
                )

            page = await response.text()

    return parse_search_results(
        page,
        max_results
    )


# ============================================================
# 🔍 PARSE SEARCH RESULTS
# ============================================================

def parse_search_results(
    page: str,
    max_results: int = MAX_RESULTS
) -> list:

    soup = BeautifulSoup(
        page,
        "html.parser"
    )

    results = []

    for item in soup.select(
        "div.MjjYud"
    ):

        title_tag = item.select_one(
            "h3"
        )

        link_tag = item.select_one(
            "a"
        )

        if not title_tag or not link_tag:
            continue

        title = (
            title_tag.get_text(
                " ",
                strip=True
            )
        )

        link = link_tag.get(
            "href",
            ""
        )

        if not link.startswith(
            "http"
        ):
            continue

        description_tag = item.select_one(
            ".VwiC3b"
        )

        description = ""

        if description_tag:
            description = (
                description_tag.get_text(
                    " ",
                    strip=True
                )
            )

        results.append(
            {
                "title": html.unescape(
                    title
                ),
                "url": link,
                "description":
                    html.unescape(
                        description
                    ),
            }
        )

        if len(results) >= max_results:
            break

    return results


# ============================================================
# 🧾 FORMAT RESULTS
# ============================================================

def format_search_results(
    query: str,
    results: list
) -> str:

    if not results:

        return (
            "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
            f"   {BRAND}\n"
            "   🌐 𝐖𝐄𝐁 𝐒𝐄𝐀𝐑𝐂𝐇\n"
            "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

            f"🔎 Query:\n{query}\n\n"

            "❌ No useful results found."
        )

    lines = [
        "╭━━━━━━━━━━━━━━━━━━━━━━╮",
        f"   {BRAND}",
        "   🌐 𝐋𝐈𝐕𝐄 𝐖𝐄𝐁 𝐒𝐄𝐀𝐑𝐂𝐇",
        "╰━━━━━━━━━━━━━━━━━━━━━━╯",
        "",
        f"🔎 𝐐𝐮𝐞𝐫𝐲: {query}",
        "",
    ]

    for index, result in enumerate(
        results,
        start=1
    ):

        title = result.get(
            "title",
            "Untitled"
        )

        description = result.get(
            "description",
            ""
        )

        url = result.get(
            "url",
            ""
        )

        lines.extend(
            [
                f"🌐 {index}. {title}",
                "",
                (
                    f"📝 {description}"
                    if description
                    else "📝 No description available."
                ),
                "",
                f"🔗 {url}",
                "",
                "━━━━━━━━━━━━━━━━━━━━━━",
                "",
            ]
        )

    lines.append(
        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )

    return "\n".join(
        lines
    )


# ============================================================
# 🧠 BUILD AI RESEARCH PROMPT
# ============================================================

def build_research_prompt(
    query: str,
    results: list,
    language: str = "Hindi"
) -> str:

    sources = []

    for index, result in enumerate(
        results,
        start=1
    ):

        sources.append(
            f"""
SOURCE {index}

Title:
{result.get("title", "")}

URL:
{result.get("url", "")}

Description:
{result.get("description", "")}
"""
        )

    source_text = "\n".join(
        sources
    )

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 🌐🧠

Answer the user's query using the
web-search results supplied below.

🌍 Response language:
{language}

User query:
{query}

IMPORTANT:

• Clearly distinguish facts from uncertainty.
• Do not invent information.
• Use the supplied sources as evidence.
• Mention important sources when appropriate.
• If the search results are insufficient,
  clearly say that more verification is needed.

SEARCH RESULTS:

{source_text}
"""


# ============================================================
# 🔗 SOURCE LIST
# ============================================================

def get_sources(
    results: list
) -> list:

    sources = []

    for result in results:

        url = result.get(
            "url",
            ""
        )

        if url:
            sources.append(
                {
                    "title":
                        result.get(
                            "title",
                            "Source"
                        ),
                    "url":
                        url,
                }
            )

    return sources


# ============================================================
# 🧪 ENGINE STATUS
# ============================================================

def engine_status() -> dict:

    return {
        "engine":
            "Web Search",
        "enabled":
            True,
        "max_results":
            MAX_RESULTS,
        "timeout":
            TIMEOUT_SECONDS,
    }


# ============================================================
# 🚀 TEST
# ============================================================

if __name__ == "__main__":

    status = engine_status()

    print()
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈")
    print("   🌐 𝐖𝐄𝐁 𝐒𝐄𝐀𝐑𝐂𝐇")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    print()

    print("🌐 Search Engine : READY")
    print(
        f"🔎 Max Results   : "
        f"{status['max_results']}"
    )
    print(
        f"⏱️ Timeout       : "
        f"{status['timeout']} sec"
    )
    print()
    print(
        "✅ Web search module loaded."
    )
    print(
        "🔱 Created for Babadev AI"
      )
