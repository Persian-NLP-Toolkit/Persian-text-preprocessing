from __future__ import annotations
import os, io, zipfile, pathlib, urllib.request

_PARSIVAR_SPELL_URL = "https://www.dropbox.com/s/tlyvnzv1ha9y1kl/spell.zip?dl=1"


def ensure_parsivar_spell_data(
    url: str = _PARSIVAR_SPELL_URL, timeout: int = 60
) -> str:
    """Ensure Parsivar spell resources exist; download once if missing. Returns dst dir."""
    import parsivar

    dst = os.path.join(os.path.dirname(parsivar.__file__), "resource", "spell")
    if os.path.isdir(dst) and any(os.scandir(dst)):
        return dst
    pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=timeout) as r:
        data = r.read()
    zipfile.ZipFile(io.BytesIO(data)).extractall(dst)
    return dst
