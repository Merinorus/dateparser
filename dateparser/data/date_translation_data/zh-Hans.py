"""
This is the translation data for Simplified Chinese (zh-Hans).
Simplified Chinese is the default script for Chinese (zh) according to CLDR,
so zh-Hans.py directly inherits from zh.py to avoid duplication.

See: https://st.unicode.org/cldr-apps/v#/zh_Hans
"""
from .zh import info as zh_info

info = zh_info.copy()
info.update(
    {
        "name": "zh-Hans",
        "locale_specific": {
            "zh-Hans-HK": {"name": "zh-Hans-HK", "date_order": "DMY"},
            "zh-Hans-MO": {"name": "zh-Hans-MO", "date_order": "DMY"},
            "zh-Hans-SG": {"name": "zh-Hans-SG", "date_order": "DMY"},
        }
    }
)
