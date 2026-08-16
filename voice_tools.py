# ============================================================
# 🔱 BABADEV AI
# 🎤 VOICE → TEXT ENGINE
# ============================================================

import os
import subprocess
from pathlib import Path

import speech_recognition as sr


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# 📁 TEMP AUDIO DIRECTORY
# ============================================================

AUDIO_DIR = Path("data/voice")

AUDIO_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 🎧 CONVERT AUDIO → WAV
# ============================================================

def convert_to_wav(
    input_file: str
) -> str:

    source = Path(input_file)

    if not source.exists():
        raise FileNotFoundError(
            "❌ Audio file not found."
        )

    output = (
        AUDIO_DIR /
        f"{source.stem}_converted.wav"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(source),
        "-ar",
        "16000",
        "-ac",
        "1",
        str(output)
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            "❌ Audio conversion failed."
        )

    return str(output)


# ============================================================
# 🧠 SPEECH → TEXT
# ============================================================

def transcribe_audio(
    audio_file: str,
    language: str = "en-IN"
) -> str:

    wav_file = convert_to_wav(
        audio_file
    )

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(
            wav_file
        ) as source:

            audio = recognizer.record(
                source
            )

        text = recognizer.recognize_google(
            audio,
            language=language
        )

        return text.strip()

    except sr.UnknownValueError:

        return ""

    except sr.RequestError as error:

        raise RuntimeError(
            f"Speech recognition service error: {error}"
        )

    finally:

        try:
            Path(wav_file).unlink(
                missing_ok=True
            )
        except Exception:
            pass


# ============================================================
# 🌍 LANGUAGE MAP
# ============================================================

VOICE_LANGUAGES = {

    "english":
        "en-IN",

    "hindi":
        "hi-IN",

    "gujarati":
        "gu-IN",

    "marathi":
        "mr-IN",

    "bengali":
        "bn-IN",

    "punjabi":
        "pa-IN",

    "tamil":
        "ta-IN",

    "telugu":
        "te-IN",

    "kannada":
        "kn-IN",

}


def get_voice_language(
    language: str
) -> str:

    language = (
        language
        .strip()
        .lower()
    )

    return VOICE_LANGUAGES.get(
        language,
        "en-IN"
    )


# ============================================================
# 📊 TEXT STATISTICS
# ============================================================

def voice_statistics(
    text: str
) -> dict:

    text = text or ""

    return {

        "characters":
            len(text),

        "words":
            len(text.split()),

        "lines":
            len(text.splitlines()),

    }


# ============================================================
# 🎨 FORMAT RESULT
# ============================================================

def format_voice_result(
    text: str,
    language: str = "English"
) -> str:

    if not text:

        return (
            "╭━━━━━━━━━━━━━━━━━━━━╮\n"
            f"   {BRAND}\n"
            "   🎤 𝐕𝐎𝐈𝐂𝐄 → 𝐓𝐄𝐗𝐓\n"
            "╰━━━━━━━━━━━━━━━━━━━━╯\n\n"

            "❌ 𝐍𝐨 𝐯𝐨𝐢𝐜𝐞 𝐰𝐚𝐬 𝐝𝐞𝐭𝐞𝐜𝐭𝐞𝐝.\n\n"

            "🎤 Please send a clearer voice message."
        )

    stats = voice_statistics(
        text
    )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   🎤 𝐕𝐎𝐈𝐂𝐄 → 𝐓𝐄𝐗𝐓\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"🌍 Language: {language}\n"
        f"🔤 Characters: {stats['characters']}\n"
        f"📝 Words: {stats['words']}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📜 𝐓𝐑𝐀𝐍𝐒𝐂𝐑𝐈𝐏𝐓\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"

        f"{text}\n\n"

        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🔱 𝐉𝐀𝐈 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 🔱"
    )


# ============================================================
# 🧹 CLEANUP
# ============================================================

def cleanup_audio(
    file_path: str
):

    try:

        Path(file_path).unlink(
            missing_ok=True
        )

    except Exception:
        pass


# ============================================================
# 🧪 ENGINE STATUS
# ============================================================

def engine_status() -> dict:

    ffmpeg_ready = (
        subprocess.run(
            ["which", "ffmpeg"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).returncode == 0
    )

    return {

        "voice_engine": True,

        "ffmpeg": ffmpeg_ready,

        "languages":
            len(VOICE_LANGUAGES),

    }


# ============================================================
# 🚀 TEST
# ============================================================

if __name__ == "__main__":

    status = engine_status()

    print()
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈")
    print("   🎤 𝐕𝐎𝐈𝐂𝐄 𝐄𝐍𝐆𝐈𝐍𝐄")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    print()

    print(
        f"🎤 Voice Engine : "
        f"{'READY' if status['voice_engine'] else 'ERROR'}"
    )

    print(
        f"🎧 FFmpeg       : "
        f"{'READY' if status['ffmpeg'] else 'MISSING'}"
    )

    print(
        f"🌍 Languages     : "
        f"{status['languages']}"
    )

    print()
    print(
        "✅ Voice → Text module loaded."
    )
    print(
        "🔱 Created for Babadev AI"
  )
