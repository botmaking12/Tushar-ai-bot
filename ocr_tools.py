# ============================================================
# 🔱 BABADEV AI
# 🖼️ IMAGE → TEXT OCR ENGINE
# ============================================================

from pathlib import Path
from PIL import Image
import pytesseract


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# 🖼️ OPEN IMAGE
# ============================================================

def open_image(file_path: str):
    """
    Open and validate an image file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"❌ Image not found: {file_path}"
        )

    allowed = {
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".bmp",
        ".tiff",
        ".tif"
    }

    if path.suffix.lower() not in allowed:
        raise ValueError(
            "❌ Unsupported image format."
        )

    return Image.open(path)


# ============================================================
# 🔍 BASIC OCR
# ============================================================

def extract_text(
    file_path: str,
    language: str = "eng"
) -> str:
    """
    Extract text from image using Tesseract OCR.
    """

    image = open_image(file_path)

    try:
        text = pytesseract.image_to_string(
            image,
            lang=language
        )
    except Exception as error:
        raise RuntimeError(
            f"OCR failed: {error}"
        )

    return clean_text(text)


# ============================================================
# 🧹 CLEAN OCR TEXT
# ============================================================

def clean_text(text: str) -> str:

    if not text:
        return ""

    cleaned_lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


# ============================================================
# 📊 OCR STATISTICS
# ============================================================

def text_statistics(text: str) -> dict:

    text = text or ""

    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
    }


# ============================================================
# 🌍 LANGUAGE MAPPING
# ============================================================

OCR_LANGUAGES = {
    "english": "eng",
    "hindi": "hin",
    "gujarati": "guj",
    "marathi": "mar",
    "bengali": "ben",
    "english+hindi": "eng+hin",
    "english+gujarati": "eng+guj",
    "hindi+english": "hin+eng",
    "gujarati+english": "guj+eng",
}


def get_ocr_language(language: str) -> str:

    language = (
        language
        .strip()
        .lower()
    )

    return OCR_LANGUAGES.get(
        language,
        "eng"
    )


# ============================================================
# 🧠 OCR RESULT FORMATTER
# ============================================================

def format_ocr_result(
    text: str,
    language: str = "English"
) -> str:

    stats = text_statistics(text)

    if not text:
        return (
            f"{BRAND}\n\n"
            "❌ 𝐍𝐨 𝐭𝐞𝐱𝐭 𝐝𝐞𝐭𝐞𝐜𝐭𝐞𝐝.\n\n"
            "🖼️ Please send a clearer image."
        )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   🖼️ 𝐎𝐂𝐑 𝐑𝐄𝐒𝐔𝐋𝐓\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"🌍 Language: {language}\n"
        f"🔤 Characters: {stats['characters']}\n"
        f"📝 Words: {stats['words']}\n"
        f"📄 Lines: {stats['lines']}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📖 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐄𝐃 𝐓𝐄𝐗𝐓\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        f"{text}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )


# ============================================================
# 📚 STUDY OCR PROMPT
# ============================================================

def build_ocr_ai_prompt(
    text: str,
    language: str = "Hindi"
) -> str:

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 🎓

An image was converted into text using OCR.

🌍 Response language:
{language}

Convert the extracted text into
clear and useful study material.

Use:

📌 Important Points
🧠 Simple Explanation
📝 Key Definitions
⭐ Exam Points
❓ Possible MCQs

IMPORTANT:
Do not invent information that is not present
in the extracted text.

━━━━━━━━━━━━━━━━━━━━━━

OCR TEXT:

{text}

━━━━━━━━━━━━━━━━━━━━━━
"""


# ============================================================
# 🧪 QUICK TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈")
    print("   🖼️ 𝐎𝐂𝐑 𝐄𝐍𝐆𝐈𝐍𝐄")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    print()
    print("🖼️ Image Reader     : READY")
    print("🔍 OCR Engine       : READY")
    print("🌍 Multi-Language   : READY")
    print("📊 Text Statistics  : READY")
    print("🎓 Study Converter  : READY")
    print()
    print("✅ OCR module loaded successfully.")
    print()
    print("🔱 Created for Babadev AI")
