# ============================================================
# 🔱 BABADEV AI
# 🧑‍🎓 PERSONAL STUDY MODE
# ============================================================

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# 📚 STUDY SESSION
# ============================================================

@dataclass
class StudySession:

    user_id: int

    subject: str = ""

    topic: str = ""

    language: str = "Hindi"

    level: str = "Medium"

    questions: int = 10

    score: int = 0

    answered: int = 0

    history: List[dict] = field(
        default_factory=list
    )


# ============================================================
# 🧠 SESSION STORAGE
# ============================================================

study_sessions: Dict[
    int,
    StudySession
] = {}


# ============================================================
# 🚀 CREATE SESSION
# ============================================================

def create_session(
    user_id: int,
    subject: str = "",
    topic: str = "",
    language: str = "Hindi",
    level: str = "Medium",
    questions: int = 10,
) -> StudySession:

    session = StudySession(
        user_id=user_id,
        subject=subject,
        topic=topic,
        language=language,
        level=level,
        questions=questions,
    )

    study_sessions[user_id] = session

    return session


# ============================================================
# 🔎 GET SESSION
# ============================================================

def get_session(
    user_id: int
) -> Optional[StudySession]:

    return study_sessions.get(
        user_id
    )


# ============================================================
# 🗑️ CLEAR SESSION
# ============================================================

def clear_session(
    user_id: int
):

    study_sessions.pop(
        user_id,
        None
    )


# ============================================================
# 📖 STUDY MENU
# ============================================================

def study_menu_text() -> str:

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   🧑‍🎓 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋 𝐒𝐓𝐔𝐃𝐘\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        "📚 𝐋𝐞𝐚𝐫𝐧 • 🧠 𝐏𝐫𝐚𝐜𝐭𝐢𝐜𝐞 • 📝 𝐓𝐞𝐬𝐭\n\n"

        "✨ Choose your study mode:\n\n"

        "📖 𝐄𝐱𝐩𝐥𝐚𝐢𝐧 𝐓𝐨𝐩𝐢𝐜\n"
        "📝 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐌𝐂𝐐\n"
        "🎯 𝐏𝐫𝐚𝐜𝐭𝐢𝐜𝐞 𝐐𝐮𝐢𝐳\n"
        "🧠 𝐐𝐮𝐢𝐜𝐤 𝐑𝐞𝐯𝐢𝐬𝐢𝐨𝐧\n"
        "📊 𝐌𝐲 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬\n"
        "⭐ 𝐅𝐚𝐯𝐨𝐫𝐢𝐭𝐞 𝐓𝐨𝐩𝐢𝐜𝐬\n\n"

        "🌍 Hindi • Gujarati • English\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )


# ============================================================
# 📖 EXPLANATION PROMPT
# ============================================================

def build_explanation_prompt(
    subject: str,
    topic: str,
    language: str = "Hindi",
    level: str = "Medium",
) -> str:

    return f"""
You are {BRAND} 🧑‍🎓

Act as a professional study teacher.

📚 Subject:
{subject}

📖 Topic:
{topic}

🌍 Language:
{language}

🎯 Student Level:
{level}

Explain the topic in a clear,
exam-oriented format.

Use:

• Simple explanation
• Important definitions
• Key points
• Examples
• Important facts
• Exam tips
• Quick revision
• 5 practice questions

Do not invent facts.

If information is uncertain,
clearly mention the uncertainty.
"""


# ============================================================
# 📝 MCQ PROMPT
# ============================================================

def build_mcq_prompt(
    subject: str,
    topic: str,
    language: str = "Hindi",
    count: int = 10,
    level: str = "Medium",
) -> str:

    return f"""
You are {BRAND} 🧠📝

Create {count} multiple-choice questions.

📚 Subject:
{subject}

📖 Topic:
{topic}

🌍 Language:
{language}

🎯 Difficulty:
{level}

For every question provide:

Q1. Question

A) Option
B) Option
C) Option
D) Option

Correct Answer:
Explanation:

Requirements:

• Only one correct answer.
• Keep options clear.
• Avoid ambiguous questions.
• Explanations should be concise.
• Focus on exam preparation.
"""


# ============================================================
# 🎯 QUIZ PROMPT
# ============================================================

def build_quiz_prompt(
    subject: str,
    topic: str,
    language: str = "Hindi",
    count: int = 10,
) -> str:

    return f"""
You are {BRAND} 🎯

Create a {count}-question quiz.

Subject:
{subject}

Topic:
{topic}

Language:
{language}

Rules:

1. Ask one question at a time.
2. Give four options.
3. Wait for the student's answer.
4. Tell whether the answer is correct.
5. Explain the answer.
6. Continue to the next question.
7. At the end calculate the score.
8. Give percentage and performance level.

Performance levels:

🏆 Excellent
🔥 Very Good
👍 Good
📚 Needs Revision
"""


# ============================================================
# ⚡ QUICK REVISION
# ============================================================

def build_revision_prompt(
    subject: str,
    topic: str,
    language: str = "Hindi",
) -> str:

    return f"""
You are {BRAND} ⚡📚

Create quick exam revision notes.

Subject:
{subject}

Topic:
{topic}

Language:
{language}

Format:

╭━━━━━━━━━━━━━━━━━━╮
⚡ QUICK REVISION
╰━━━━━━━━━━━━━━━━━━╯

📌 Definition

🔑 Important Points

🧠 Remember This

⚠️ Common Mistakes

🎯 Exam Focus

📝 5 Quick Questions

Keep the notes concise,
accurate and easy to revise.
"""


# ============================================================
# 📊 RECORD ANSWER
# ============================================================

def record_answer(
    user_id: int,
    question: str,
    user_answer: str,
    correct_answer: str,
) -> bool:

    session = get_session(
        user_id
    )

    if not session:
        return False

    is_correct = (
        user_answer.strip().lower()
        ==
        correct_answer.strip().lower()
    )

    session.answered += 1

    if is_correct:
        session.score += 1

    session.history.append(
        {
            "question": question,
            "user_answer": user_answer,
            "correct_answer":
                correct_answer,
            "correct": is_correct,
        }
    )

    return is_correct


# ============================================================
# 📈 SESSION RESULT
# ============================================================

def session_result(
    user_id: int
) -> str:

    session = get_session(
        user_id
    )

    if not session:
        return (
            "❌ No active study session."
        )

    total = session.answered

    score = session.score

    percentage = (
        (score / total) * 100
        if total
        else 0
    )

    if percentage >= 90:
        level = "🏆 Excellent"
    elif percentage >= 75:
        level = "🔥 Very Good"
    elif percentage >= 60:
        level = "👍 Good"
    else:
        level = "📚 Needs Revision"

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   📊 𝐒𝐓𝐔𝐃𝐘 𝐑𝐄𝐒𝐔𝐋𝐓\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"📚 Subject: {session.subject}\n"
        f"📖 Topic: {session.topic}\n\n"

        f"📝 Questions: {total}\n"
        f"✅ Correct: {score}\n"
        f"❌ Wrong: {total - score}\n"
        f"📈 Score: {percentage:.1f}%\n\n"

        f"🎯 Performance: {level}\n\n"

        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )


# ============================================================
# 🧪 MODULE TEST
# ============================================================

if __name__ == "__main__":

    session = create_session(
        user_id=12345,
        subject="Nursing",
        topic="Renal System",
        language="Hindi",
        level="Medium",
        questions=10,
    )

    print()
    print(
        "╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮"
    )
    print(
        f"   {BRAND}"
    )
    print(
        "   🧑‍🎓 STUDY MODE"
    )
    print(
        "╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯"
    )
    print()

    print(
        "✅ Study Mode module loaded."
    )

    print(
        f"📚 Subject: {session.subject}"
    )

    print(
        f"📖 Topic: {session.topic}"
    )

    print()
    print(
        "🔱 Created for Babadev AI"
    )
