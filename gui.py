"""
gui.py
------
Version 3 Graphical User Interface (GUI): a simple Tkinter window featuring:
  - Folder selection button
  - Organize button
  - Progress bar

Tkinter is included in Python's standard library, so no additional
installation is required.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

from organizer import FileOrganizer


class OrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI File Organizer")
        self.root.geometry("480x260")
        self.root.resizable(False, False)

        self.selected_folder = tk.StringVar(value="No folder selected")

        self._build_widgets()

    def _build_widgets(self):
        padding = {"padx": 16, "pady": 8}

        title_label = tk.Label(self.root, text="AI File Organizer", font=("Segoe UI", 16, "bold"))
        title_label.pack(pady=(20, 4))

        subtitle = tk.Label(
            self.root,
            text="Select and organize your Downloads folder",
            fg="gray"
        )
        subtitle.pack()

        folder_frame = tk.Frame(self.root)
        folder_frame.pack(**padding, fill="x")

        self.folder_label = tk.Label(
            folder_frame,
            textvariable=self.selected_folder,
            wraplength=340,
            justify="right"
        )
        self.folder_label.pack(side="right", fill="x", expand=True)

        choose_btn = tk.Button(
            folder_frame,
            text="Choose Folder",
            command=self.choose_folder
        )
        choose_btn.pack(side="left")

        self.organize_btn = tk.Button(
            self.root,
            text="Organize",
            bg="#2e7d32",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=self.start_organize
        )
        self.organize_btn.pack(**padding)

        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=380,
            mode="determinate"
        )
        self.progress.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", fg="gray")
        self.status_label.pack()

    def choose_folder(self):
        folder = filedialog.askdirectory(title="Select a folder to organize")
        if folder:
            self.selected_folder.set(folder)

    def start_organize(self):
        folder = self.selected_folder.get()
        if folder == "No folder selected":
            messagebox.showwarning(
                "Warning",
                "Please select a folder first."
            )
            return

        self.organize_btn.config(state="disabled")
        self.progress["value"] = 0
        self.status_label.config(text="Scanning files...")

        # Run the operation in a separate thread to keep the GUI responsive.
        thread = threading.Thread(
            target=self._run_organize,
            args=(folder,),
            daemon=True
        )
        thread.start()

    def _run_organize(self, folder):
        try:
            organizer = FileOrganizer(folder)
            total_files = len(
                [f for f in organizer.target_folder.iterdir() if f.is_file()]
            )

            self._update_progress(30, "Organizing files...")
            report = organizer.organize()
            self._update_progress(100, "Done!")

            message = (
                f"{report['moved_files']} file(s) moved\n"
                f"{report['created_folders']} folder(s) created"
            )
            self.root.after(
                0,
                lambda: messagebox.showinfo("Organization Report", message)
            )

        except Exception as e:
            self.root.after(
                0,
                lambda: messagebox.showerror("Error", str(e))
            )
        finally:
            self.root.after(
                0,
                lambda: self.organize_btn.config(state="normal")
            )

    def _update_progress(self, value, status_text):
        self.progress["value"] = value
        self.status_label.config(text=status_text)
        self.root.update_idletasks()


def launch_gui():
    root = tk.Tk()
    OrganizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch_gui()