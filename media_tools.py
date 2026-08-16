# ============================================================
# 🔱 BABADEV AI — MEDIA TOOLS
# ============================================================
# 🛠️ File handling
# 🖼️ Image information
# 📄 PDF information
# 🎤 Audio information
# 🎬 Video information
# 📦 Safe temporary files
# ============================================================

from pathlib import Path
import mimetypes
import shutil
import tempfile
import uuid


# ============================================================
# 🎨 BRAND
# ============================================================

BRAND = "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"


# ============================================================
# 📁 TEMP DIRECTORY
# ============================================================

BASE_TEMP_DIR = Path(
    tempfile.gettempdir()
) / "babadev_ai"


BASE_TEMP_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# 🆔 UNIQUE FILE NAME
# ============================================================

def unique_filename(
    original_name: str,
    prefix: str = "babadev"
) -> str:

    original = Path(
        original_name or "file"
    )

    extension = original.suffix

    return (
        f"{prefix}_"
        f"{uuid.uuid4().hex[:12]}"
        f"{extension}"
    )


# ============================================================
# 📥 CREATE USER DIRECTORY
# ============================================================

def user_directory(
    user_id: int
) -> Path:

    directory = (
        BASE_TEMP_DIR
        / str(user_id)
    )

    directory.mkdir(
        parents=True,
        exist_ok=True
    )

    return directory


# ============================================================
# 📄 CREATE TEMP FILE
# ============================================================

def create_temp_file(
    user_id: int,
    filename: str
) -> Path:

    directory = user_directory(
        user_id
    )

    safe_name = unique_filename(
        filename
    )

    path = directory / safe_name

    path.touch()

    return path


# ============================================================
# 📏 FILE SIZE
# ============================================================

def file_size(
    path
) -> int:

    return Path(path).stat().st_size


# ============================================================
# 📊 HUMAN READABLE SIZE
# ============================================================

def human_size(
    size: int
) -> str:

    size = float(size)

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
    ]

    for unit in units:

        if size < 1024:

            return (
                f"{size:.1f} {unit}"
            )

        size /= 1024

    return (
        f"{size:.1f} PB"
    )


# ============================================================
# 🔎 MIME TYPE
# ============================================================

def mime_type(
    path
) -> str:

    detected, _ = (
        mimetypes.guess_type(
            str(path)
        )
    )

    return (
        detected
        or "application/octet-stream"
    )


# ============================================================
# 🖼️ IS IMAGE
# ============================================================

def is_image(
    path
) -> bool:

    mime = mime_type(
        path
    )

    return mime.startswith(
        "image/"
    )


# ============================================================
# 🎤 IS AUDIO
# ============================================================

def is_audio(
    path
) -> bool:

    mime = mime_type(
        path
    )

    return mime.startswith(
        "audio/"
    )


# ============================================================
# 🎬 IS VIDEO
# ============================================================

def is_video(
    path
) -> bool:

    mime = mime_type(
        path
    )

    return mime.startswith(
        "video/"
    )


# ============================================================
# 📄 IS PDF
# ============================================================

def is_pdf(
    path
) -> bool:

    return (
        Path(path)
        .suffix
        .lower()
        == ".pdf"
    )


# ============================================================
# 🗂️ FILE TYPE
# ============================================================

def file_category(
    path
) -> str:

    path = Path(path)

    if is_pdf(path):
        return "pdf"

    if is_image(path):
        return "image"

    if is_audio(path):
        return "audio"

    if is_video(path):
        return "video"

    return "document"


# ============================================================
# 📋 FILE INFORMATION
# ============================================================

def file_info(
    path
) -> dict:

    path = Path(path)

    return {
        "name": path.name,
        "extension": path.suffix.lower(),
        "size": file_size(path),
        "size_text": human_size(
            file_size(path)
        ),
        "mime_type": mime_type(path),
        "category": file_category(
            path
        ),
        "exists": path.exists(),
    }


# ============================================================
# 📝 FILE INFO TEXT
# ============================================================

def file_info_text(
    path
) -> str:

    info = file_info(
        path
    )

    return (
        "╭━━━━━━━━━━━━━━━━━━━━━━╮\n"
        f"   {BRAND}\n"
        "   📁 𝐅𝐈𝐋𝐄 𝐈𝐍𝐅𝐎\n"
        "╰━━━━━━━━━━━━━━━━━━━━━━╯\n\n"

        f"📄 Name:\n"
        f"`{info['name']}`\n\n"

        f"🗂️ Type: "
        f"`{info['category']}`\n"

        f"📦 Size: "
        f"`{info['size_text']}`\n"

        f"🔤 MIME: "
        f"`{info['mime_type']}`\n\n"

        "🔱 𝐁𝐀𝐁𝐀𝐃𝐄𝐕 𝐀𝐈"
    )


# ============================================================
# 🛡️ SAFE EXTENSIONS
# ============================================================

ALLOWED_EXTENSIONS = {

    # Documents
    ".pdf",
    ".txt",
    ".doc",
    ".docx",

    # Images
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",

    # Audio
    ".mp3",
    ".wav",
    ".m4a",
    ".ogg",
    ".opus",

    # Video
    ".mp4",
    ".mkv",
    ".mov",
    ".webm",
}


# ============================================================
# 🔐 EXTENSION CHECK
# ============================================================

def is_allowed_extension(
    path
) -> bool:

    extension = (
        Path(path)
        .suffix
        .lower()
    )

    return (
        extension
        in ALLOWED_EXTENSIONS
    )


# ============================================================
# 🧹 CLEAN ONE FILE
# ============================================================

def delete_file(
    path
) -> bool:

    try:

        path = Path(path)

        if path.exists():

            path.unlink()

        return True

    except Exception:

        return False


# ============================================================
# 🧹 CLEAN USER FILES
# ============================================================

def cleanup_user_files(
    user_id: int
) -> int:

    directory = user_directory(
        user_id
    )

    removed = 0

    if not directory.exists():

        return removed

    for item in directory.iterdir():

        try:

            if item.is_file():

                item.unlink()

                removed += 1

            elif item.is_dir():

                shutil.rmtree(
                    item
                )

                removed += 1

        except Exception:

            pass

    return removed


# ============================================================
# 🧹 CLEAN ALL TEMP DATA
# ============================================================

def cleanup_all() -> int:

    removed = 0

    if not BASE_TEMP_DIR.exists():

        return removed

    for item in BASE_TEMP_DIR.iterdir():

        try:

            if item.is_file():

                item.unlink()

                removed += 1

            elif item.is_dir():

                shutil.rmtree(
                    item
                )

                removed += 1

        except Exception:

            pass

    return removed


# ============================================================
# 📦 COPY FILE
# ============================================================

def copy_file(
    source,
    destination
) -> Path:

    source = Path(source)

    destination = Path(
        destination
    )

    destination.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(
        source,
        destination
    )

    return destination


# ============================================================
# ✏️ SAFE FILE NAME
# ============================================================

def safe_filename(
    filename: str
) -> str:

    filename = (
        str(filename)
        .strip()
    )

    if not filename:

        return "babadev_file"

    unsafe = (
        "/",
        "\\",
        ":",
        "*",
        "?",
        '"',
        "<",
        ">",
        "|",
    )

    for character in unsafe:

        filename = filename.replace(
            character,
            "_"
        )

    return filename[:180]


# ============================================================
# 🧪 HEALTH CHECK
# ============================================================

def media_tools_status() -> dict:

    return {
        "status": "online",
        "temp_directory":
            str(BASE_TEMP_DIR),
        "supported_extensions":
            len(ALLOWED_EXTENSIONS),
    }


# ============================================================
# 🧪 TEST
# ============================================================

if __name__ == "__main__":

    print(
        "╔══════════════════════════╗"
    )

    print(
        "║   🔱 BABADEV AI          ║"
    )

    print(
        "║   🛠️ MEDIA TOOLS TEST    ║"
    )

    print(
        "╚══════════════════════════╝"
    )

    status = (
        media_tools_status()
    )

    print()

    print(
        f"🟢 Status: "
        f"{status['status']}"
    )

    print(
        f"📁 Temp: "
        f"{status['temp_directory']}"
    )

    print(
        f"📦 Supported extensions: "
        f"{status['supported_extensions']}"
)
