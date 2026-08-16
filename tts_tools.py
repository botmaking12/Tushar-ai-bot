# ============================================================
# 🔱 BABADEV AI
# 🔊 AI TEXT → VOICE ENGINE
# ============================================================

import asyncio
from pathlib import Path

import edge_tts


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"

VOICE_DIR = Path("data/tts")
VOICE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 🌍 VOICE MAP
# ============================================================

VOICE_MAP = {

    "english":
        "en-US-AriaNeural",

    "hindi":
        "hi-IN-SwaraNeural",

    "gujarati":
        "gu-IN-DhwaniNeural",

    "marathi":
        "mr-IN-AarohiNeural",

    "bengali":
        "bn-IN-TanishaaNeural",

}


# ============================================================
# 🔤 GET VOICE
# ============================================================

def get_voice(
    language: str
) -> str:

    language = (
        language
        .strip()
        .lower()
    )

    return VOICE_MAP.get(
        language,
        VOICE_MAP["english"]
    )


# ============================================================
# 🔊 GENERATE VOICE
# ============================================================

async def generate_voice(
    text: str,
    language: str = "English",
    filename: str = "babadev_voice.mp3",
    rate: str = "+0%",
    pitch: str = "+0Hz"
) -> str:

    text = text.strip()

    if not text:
        raise ValueError(
            "❌ Text cannot be empty."
        )

    voice = get_voice(
        language
    )

    output = (
        VOICE_DIR /
        Path(filename).name
    )

    if output.suffix.lower() != ".mp3":
        output = output.with_suffix(".mp3")

    communicator = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch
    )

    await communicator.save(
        str(output)
    )

    if not output.exists():
        raise RuntimeError(
            "❌ Voice generation failed."
        )

    if output.stat().st_size == 0:
        raise RuntimeError(
            "❌ Generated audio is empty."
        )

    return str(output)


# ============================================================
# ⚡ SIMPLE SYNC WRAPPER
# ============================================================

def text_to_voice(
    text: str,
    language: str = "English",
    filename: str = "babadev_voice.mp3"
) -> str:

    return asyncio.run(
        generate_voice(
            text=text,
            language=language,
            filename=filename
        )
    )


# ============================================================
# 🎛️ VOICE STYLES
# ============================================================

VOICE_STYLES = {

    "normal": {
        "rate": "+0%",
        "pitch": "+0Hz"
    },

    "slow": {
        "rate": "-20%",
        "pitch": "+0Hz"
    },

    "fast": {
        "rate": "+20%",
        "pitch": "+0Hz"
    },

    "soft": {
        "rate": "-5%",
        "pitch": "-2Hz"
    },

    "energetic": {
        "rate": "+10%",
        "pitch": "+3Hz"
    },

}


# ============================================================
# 🎚️ GENERATE WITH STYLE
# ============================================================

async def generate_voice_style(
    text: str,
    language: str = "English",
    style: str = "normal",
    filename: str = "babadev_voice.mp3"
) -> str:

    selected = VOICE_STYLES.get(
        style.lower(),
        VOICE_STYLES["normal"]
    )

    return await generate_voice(
        text=text,
        language=language,
        filename=filename,
        rate=selected["rate"],
        pitch=selected["pitch"]
    )


# ============================================================
# 🧹 CLEANUP
# ============================================================

def cleanup_voice(
    file_path: str
):

    try:

        Path(file_path).unlink(
            missing_ok=True
        )

    except Exception:
        pass


# ============================================================
# 📊 VOICE INFO
# ============================================================

def voice_info(
    language: str
) -> dict:

    voice = get_voice(
        language
    )

    return {

        "language":
            language,

        "voice":
            voice,

        "engine":
            "Microsoft Edge TTS",

        "format":
            "MP3",

    }


# ============================================================
# 🧪 TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("╭━━━━━━━━━━━━━━━━━━━━━━━━━━╮")
    print("   🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈")
    print("   🔊 𝐓𝐄𝐗𝐓 → 𝐕𝐎𝐈𝐂𝐄")
    print("╰━━━━━━━━━━━━━━━━━━━━━━━━━━╯")
    print()

    print("🗣️ English  : READY")
    print("🇮🇳 Hindi    : READY")
    print("🪷 Gujarati : READY")
    print("🌸 Marathi  : READY")
    print("🌺 Bengali  : READY")
    print()
    print("🎙️ Voice Styles : READY")
    print("🎧 MP3 Output   : READY")
    print()
    print("✅ TTS module loaded.")
    print("🔱 Created for Babadev AI")
