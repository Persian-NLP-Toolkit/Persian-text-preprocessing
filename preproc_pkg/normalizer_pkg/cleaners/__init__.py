from importlib import import_module

html = import_module(".html", __name__)
url = import_module(".url", __name__)
nonbmp = import_module(".nonbmp", __name__)
collapse_spaces = import_module(".collapse_spaces", __name__)

__all__ = [
    "html",
    "url",
    "nonbmp",
    "collapse_spaces",
]
