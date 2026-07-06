"""
config.py
---------
This file contains all project-wide configuration settings, including file
type categories, thresholds for large and old files, and keyword mappings
used for smart file classification (Version 4).

Keeping these settings in a separate file makes the project easier to
maintain. If you want to add a new file extension or adjust a threshold,
you can do so without modifying the application's core logic.
"""

# File categories based on file extensions (Version 1)
CATEGORIES = {
    "PDF": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Documents": [".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a"],
}

# Category used for files that do not match any known extension
UNKNOWN_CATEGORY = "Others"

# Threshold for considering a file "large" (Version 2), in gigabytes
LARGE_FILE_SIZE_GB = 1

# Threshold for considering a file "old" (Version 2), in days (approximately 6 months)
OLD_FILE_DAYS = 182

# Keywords used to classify files with unknown extensions based on their names (Version 4)
# This is not a true AI or machine learning model. Instead, it is a simple
# rule-based, keyword-driven classification system that provides basic
# smart file classification.
KEYWORD_HINTS = {
    "Documents": ["invoice", "report", "resume", "cv", "letter", "contract", "فاکتور", "گزارش", "رزومه"],
    "Images": ["photo", "img", "picture", "screenshot", "عکس", "تصویر"],
    "Videos": ["movie", "trailer", "clip", "video", "فیلم", "کلیپ"],
    "Audio": ["song", "music", "podcast", "آهنگ", "موزیک"],
    "Archives": ["backup", "setup", "install", "بکاپ", "نصب"],
}