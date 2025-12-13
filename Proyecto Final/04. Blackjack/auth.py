import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "usuarios.json"


def cargar_usuarios():
    """Carga el diccionario de usuarios desde usuarios.json."""
    if not USERS_FILE.exists():
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def guardar_usuarios(usuarios: dict):
    """Guarda el diccionario de usuarios en usuarios.json."""
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=2)
