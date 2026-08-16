# ============================================================
# 🔱 BABADEV AI — QUIZ ENGINE
# 📝 Professional MCQ / Quiz System
# ============================================================

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import random


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# 📝 QUESTION MODEL
# ============================================================

@dataclass
class Question:

    question: str

    options: List[str]

    answer: int

    explanation: str = ""

    subject: str = ""

    topic: str = ""

    difficulty: str = "Medium"


# ============================================================
# 🎯 QUIZ SESSION
# ============================================================

@dataclass
class QuizSession:

    user_id: int

    questions: List[Question] = field(
        default_factory=list
    )

    current: int = 0

    score: int = 0

    answered: int = 0

    started: bool = True


# ============================================================
# 💾 ACTIVE QUIZZES
# ============================================================

active_quizzes: Dict[
    int,
    QuizSession
] = {}


# ============================================================
# 🚀 CREATE QUIZ
# ============================================================

def create_quiz(
    user_id: int,
    questions: List[Question],
    shuffle: bool = True,
) -> QuizSession:

    question_list = list(
        questions
    )

    if shuffle:
        random.shuffle(
            question_list
        )

    session = QuizSession(
        user_id=user_id,
        questions=question_list,
    )

    active_quizzes[user_id] = session

    return session


# ============================================================
# 🔎 GET QUIZ
# ============================================================

def get_quiz(
    user_id: int
) -> Optional[QuizSession]:

    return active_quizzes.get(
        user_id
    )


# ============================================================
# 🗑️ DELETE QUIZ
# ============================================================

def delete_quiz(
    user_id: int
):

    active_quizzes.pop(
        user_id,
        None
    )


# ============================================================
# 📌 CURRENT QUESTION
# ============================================================

def current_question(
    user_id: int
) -> Optional[Question]:

    quiz = get_quiz(
        user_id
    )

    if not quiz:
        return None

    if quiz.current >= len(
        quiz.questions
    ):
        return None

    return quiz.questions[
        quiz.current
    ]


# ============================================================
# 🖥️ QUESTION DISPLAY
# ============================================================

def question_text(
    user_id: int
) -> str:

    quiz = get_quiz(
        user_id
    )

    if not quiz:
        return (
            "❌ 𝐍𝐨 𝐚𝐜𝐭𝐢𝐯𝐞 𝐪𝐮𝐢𝐳."
        )

    question = current_question(
        user_id
    )

    if not question:
        return result_text(
            user_id
        )

    number = quiz.current + 1

    total = len(
        quiz.questions
    )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   📝 𝐐𝐔𝐈𝐙 𝐌𝐎𝐃𝐄\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"📍 Question {number}/{total}\n\n"

        f"❓ {question.question}\n\n"

        f"📌 A) {question.options[0]}\n"
        f"📌 B) {question.options[1]}\n"
        f"📌 C) {question.options[2]}\n"
        f"📌 D) {question.options[3]}\n\n"

        "👇 Select your answer"
    )


# ============================================================
# 🎯 CHECK ANSWER
# ============================================================

def answer_question(
    user_id: int,
    selected: int,
) -> dict:

    quiz = get_quiz(
        user_id
    )

    if not quiz:

        return {
            "success": False,
            "message":
                "❌ Quiz session not found."
        }

    question = current_question(
        user_id
    )

    if not question:

        return {
            "success": False,
            "message":
                "🏁 Quiz already completed."
        }

    if selected not in range(
        4
    ):

        return {
            "success": False,
            "message":
                "❌ Invalid option."
        }

    correct = (
        selected == question.answer
    )

    quiz.answered += 1

    if correct:
        quiz.score += 1

    result = {
        "success": True,
        "correct": correct,
        "selected": selected,
        "answer": question.answer,
        "explanation":
            question.explanation,
        "question":
            question.question,
        "score":
            quiz.score,
        "answered":
            quiz.answered,
    }

    quiz.current += 1

    return result


# ============================================================
# 📊 RESULT MESSAGE
# ============================================================

def result_text(
    user_id: int
) -> str:

    quiz = get_quiz(
        user_id
    )

    if not quiz:
        return (
            "❌ Quiz session not found."
        )

    total = len(
        quiz.questions
    )

    score = quiz.score

    percentage = (
        score / total * 100
        if total
        else 0
    )

    if percentage >= 90:
        performance = (
            "🏆 𝐄𝐱𝐜𝐞𝐥𝐥𝐞𝐧𝐭"
        )

    elif percentage >= 75:
        performance = (
            "🔥 𝐕𝐞𝐫𝐲 𝐆𝐨𝐨𝐝"
        )

    elif percentage >= 60:
        performance = (
            "👍 𝐆𝐨𝐨𝐝"
        )

    elif percentage >= 40:
        performance = (
            "📚 𝐍𝐞𝐞𝐝𝐬 𝐑𝐞𝐯𝐢𝐬𝐢𝐨𝐧"
        )

    else:
        performance = (
            "🔄 𝐏𝐫𝐚𝐜𝐭𝐢𝐜𝐞 𝐌𝐨𝐫𝐞"
        )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   🏆 𝐐𝐔𝐈𝐙 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"📊 Total Questions: {total}\n"
        f"✅ Correct: {score}\n"
        f"❌ Wrong: {total - score}\n"
        f"📈 Score: {percentage:.1f}%\n\n"

        f"🎯 Performance:\n"
        f"{performance}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )


# ============================================================
# 💡 ANSWER FEEDBACK
# ============================================================

def answer_feedback(
    result: dict
) -> str:

    if not result.get(
        "success"
    ):

        return result.get(
            "message",
            "❌ Error"
        )

    if result["correct"]:

        status = (
            "╭━━━━━━━━━━━━━━━━━━╮\n"
            "   🎉 𝐂𝐎𝐑𝐑𝐄𝐂𝐓!\n"
            "╰━━━━━━━━━━━━━━━━━━╯"
        )

    else:

        status = (
            "╭━━━━━━━━━━━━━━━━━━╮\n"
            "   ❌ 𝐖𝐑𝐎𝐍𝐆!\n"
            "╰━━━━━━━━━━━━━━━━━━╯"
        )

    letters = [
        "A",
        "B",
        "C",
        "D"
    ]

    correct_letter = letters[
        result["answer"]
    ]

    explanation = (
        result.get(
            "explanation"
        )
        or
        "No explanation available."
    )

    return (
        f"{status}\n\n"

        f"🎯 Correct Answer: "
        f"**{correct_letter}**\n\n"

        f"💡 Explanation:\n"
        f"{explanation}"
    )


# ============================================================
# 🧪 SAMPLE QUESTIONS
# ============================================================

def sample_questions() -> List[Question]:

    return [

        Question(
            question=(
                "Normal human body temperature "
                "is approximately?"
            ),
            options=[
                "95°F",
                "97°F",
                "98.6°F",
                "101°F",
            ],
            answer=2,
            explanation=(
                "Normal average body temperature "
                "is approximately 98.6°F."
            ),
            subject="Nursing",
            topic="Fundamentals",
        ),

        Question(
            question=(
                "Which organ primarily filters "
                "blood and forms urine?"
            ),
            options=[
                "Heart",
                "Kidney",
                "Liver",
                "Lung",
            ],
            answer=1,
            explanation=(
                "The kidneys filter blood and "
                "produce urine."
            ),
            subject="Nursing",
            topic="Renal System",
        ),

    ]


# ============================================================
# 🧪 TEST
# ============================================================

if __name__ == "__main__":

    questions = sample_questions()

    quiz = create_quiz(
        user_id=12345,
        questions=questions,
    )

    print(
        question_text(12345)
    )

    print()

    result = answer_question(
        12345,
        2,
    )

    print(
        answer_feedback(result)
    )

    print()

    print(
        question_text(12345)
    )

    print()

    result = answer_question(
        12345,
        1,
    )

    print(
        answer_feedback(result)
    )

    print()

    print(
        result_text(12345)
  )
