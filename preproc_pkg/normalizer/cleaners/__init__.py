from importlib import import_module

html = import_module(".html", __name__)
url = import_module(".url", __name__)
nonbmp = import_module(".nonbmp", __name__)
collapse_spaces = import_module(".collapse_spaces", __name__)

email = import_module(".email", __name__)
mention = import_module(".mention", __name__)
hashtag = import_module(".hashtag", __name__)
phone = import_module(".phone", __name__)
quotes_dashes = import_module(".quotes_dashes", __name__)

__all__ = [
    "html",
    "url",
    "nonbmp",
    "collapse_spaces",
    "email",
    "mention",
    "hashtag",
    "phone",
    "quotes_dashes",
]
