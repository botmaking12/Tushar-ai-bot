# ============================================================
# 🔱 BABADEV AI
# 📄 PDF ENGINE
# ============================================================

from pathlib import Path
from pypdf import PdfReader


# ============================================================
# 📄 PDF TEXT EXTRACTION
# ============================================================

def extract_pdf_text(file_path: str) -> str:
    """
    Extract readable text from a PDF.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {file_path}"
        )

    if path.suffix.lower() != ".pdf":
        raise ValueError(
            "Only PDF files are supported."
        )

    reader = PdfReader(str(path))

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):
        try:
            text = page.extract_text() or ""

            if text.strip():
                pages.append(
                    f"\n--- 📄 Page {page_number} ---\n"
                    f"{text.strip()}"
                )

        except Exception:
            continue

    return "\n".join(pages).strip()


# ============================================================
# 📊 PDF INFORMATION
# ============================================================

def get_pdf_info(file_path: str) -> dict:

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            "PDF file not found."
        )

    reader = PdfReader(str(path))

    return {
        "file_name": path.name,
        "file_size": path.stat().st_size,
        "pages": len(reader.pages),
    }


# ============================================================
# ✂️ TEXT CLEANER
# ============================================================

def clean_pdf_text(text: str) -> str:

    if not text:
        return ""

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        lines.append(line)

    return "\n".join(lines)


# ============================================================
# 🧠 PREPARE AI SUMMARY PROMPT
# ============================================================

def build_summary_prompt(
    text: str,
    language: str = "Hindi"
) -> str:

    text = clean_pdf_text(text)

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 📚

Analyze the following PDF content carefully.

🌍 Language:
{language}

Create a clear and student-friendly summary.

Requirements:

✨ Use headings
📌 Highlight important points
🧠 Explain difficult concepts simply
📖 Keep important terminology
📝 Add key points
🎯 Focus on exam-relevant information

PDF CONTENT:

{text}
"""


# ============================================================
# 📝 PREPARE MCQ PROMPT
# ============================================================

def build_mcq_prompt(
    text: str,
    language: str = "Hindi",
    number_of_questions: int = 10
) -> str:

    text = clean_pdf_text(text)

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 🎓

Create {number_of_questions} multiple-choice
questions from the PDF content below.

🌍 Language:
{language}

For every question provide:

1️⃣ Question
A) Option
B) Option
C) Option
D) Option

✅ Correct Answer
💡 Short Explanation

Rules:

• Questions must be based only on the supplied PDF.
• Do not invent information.
• Mix easy, medium and difficult questions.
• Keep terminology accurate.
• Make questions useful for competitive exams.

PDF CONTENT:

{text}
"""


# ============================================================
# 📚 STUDY NOTES PROMPT
# ============================================================

def build_notes_prompt(
    text: str,
    language: str = "Hindi"
) -> str:

    text = clean_pdf_text(text)

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 🎓📚

Convert the following PDF into
well-organized study notes.

Language:
{language}

Format:

╭━━━━━━━━━━━━━━━━━━━━╮
      📚 STUDY NOTES
╰━━━━━━━━━━━━━━━━━━━━╯

🔹 Main Topic
🔹 Important Definitions
🔹 Key Points
🔹 Important Facts
🔹 Clinical / Practical Points
🔹 Exam Points
🔹 Quick Revision

Use attractive emojis and clear headings.

IMPORTANT:
Use only information present in the PDF.

PDF CONTENT:

{text}
"""


# ============================================================
# 🔍 KEY POINTS PROMPT
# ============================================================

def build_keypoints_prompt(
    text: str,
    language: str = "Hindi"
) -> str:

    text = clean_pdf_text(text)

    return f"""
You are 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈 ⚡

Extract the most important points from
the following PDF.

Language:
{language}

Return:

🎯 Important Topics
📌 Important Facts
🧠 Important Concepts
📝 Exam Points
⭐ Must Remember

Keep the answer concise and useful
for quick revision.

PDF:

{text}
"""


# ============================================================
# 📊 TEXT STATISTICS
# ============================================================

def text_statistics(text: str) -> dict:

    if not text:
        return {
            "characters": 0,
            "words": 0,
            "lines": 0,
        }

    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
    }


# ============================================================
# 🛡️ TEXT LIMIT
# ============================================================

def limit_text(
    text: str,
    max_characters: int = 50000
) -> str:

    if not text:
        return ""

    return text[:max_characters]


# ============================================================
# 🧪 QUICK TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈")
    print("   📄 PDF ENGINE")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━╯")
    print()
    print("✅ PDF module loaded successfully")
    print("📚 Summary engine     : READY")
    print("📝 MCQ engine         : READY")
    print("🎓 Study notes        : READY")
    print("🔍 Key points         : READY")
    print()
    print("🔱 Created for Babadev AI")
