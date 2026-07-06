
AI File Organizer

A simple yet professional tool for automatically organizing your Downloads folder (or any other folder).

This project is built step by step, making it ideal for learning Python while also serving as a portfolio-worthy project.

✨ Features

Version 1 – Basic Organization

Move PDF files to the PDF/ folder

Move images to Images/

Move videos to Videos/

Move ZIP files and other archives to Archives/

Automatically create destination folders if they do not exist

Generate a summary report showing:

Number of files moved

Number of folders created



Version 2 – Folder Analysis

Detect duplicate files based on file content hashes, not just filenames

List files larger than 1 GB

List files older than 6 months


Version 3 – Graphical User Interface

Simple GUI built with Tkinter

Folder selection button

Organize button

Progress bar


Version 4 – Smart Classification

If a file has an unknown extension, the program attempts to classify it based on its filename.

For example, a file named invoice_2024 will be moved to the Documents folder.

This feature uses a rule-based, keyword-driven classification system rather than a real machine learning model, making it an excellent starting point before exploring NLP and AI-based document classification.

📁 Project Structure
AI-File-Organizer/
│
├── main.py          # Entry point + Command-Line Interface (CLI)
├── organizer.py     # Main FileOrganizer class (core logic for Versions 1–4)
├── gui.py           # Tkinter graphical user interface (Version 3)
├── utils.py         # Utility functions (file hashing, human-readable file sizes, file age, etc.)
├── config.py        # Configuration: file type mappings, thresholds, and keywords
├── README.md
├── requirements.txt
└── screenshots/
## 🚀 Installation & Usage

No external packages are required. Simply install **Python 3.10 or later**, and you're ready to go.، 
git clone https://github.com/<username>/AI-File-Organizer.git
cd AI-File-Organizer
## Command-Line Usage (CLI)

```bash
# Organize the Downloads folder
python main.py organize ~/Downloads

# Organize the folder without enabling the Version 4 smart classification
python main.py organize ~/Downloads --no-ai

# Find duplicate files
python main.py duplicates ~/Downloads

# List files larger than 2 GB
python main.py large ~/Downloads --min-size 2

# List files older than 90 days
python main.py old ~/Downloads --days 90

## Graphical User Interface (GUI)

```bash
python gui.py
```python main.py gui

```