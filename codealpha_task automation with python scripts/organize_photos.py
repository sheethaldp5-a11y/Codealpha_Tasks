import os
import shutil
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class PhotoOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Photo Organizer & Automation")
        self.root.geometry("600x650")

        # Variables
        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.sort_by = tk.StringVar(value="Extension")  # Default: Extension
        self.date_format = tk.StringVar(value="Year-Month")
        self.preview_mode = tk.BooleanVar(value=False)
        self.recursive_mode = tk.BooleanVar(value=True)
        self.moved_count = 0
        self.total_size = 0

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="Smart Photo Organizer", font=("Helvetica", 16, "bold"))
        header.pack(pady=10)

        # Folder Selection Frame
        folder_frame = tk.LabelFrame(self.root, text="Folder Selection", padx=10, pady=10)
        folder_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(folder_frame, text="Source Folder:").grid(row=0, column=0, sticky="w")
        tk.Entry(folder_frame, textvariable=self.source_path, width=50).grid(row=0, column=1, padx=5)
        tk.Button(folder_frame, text="Browse", command=self.browse_source).grid(row=0, column=2)

        tk.Label(folder_frame, text="Dest Folder:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(folder_frame, textvariable=self.dest_path, width=50).grid(row=1, column=1, padx=5)
        tk.Button(folder_frame, text="Browse", command=self.browse_dest).grid(row=1, column=2)

        # Options Frame
        options_frame = tk.LabelFrame(self.root, text="Organization Options", padx=10, pady=10)
        options_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(options_frame, text="Sort Files By:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(options_frame, text="Extension (JPG, PNG, etc.)", variable=self.sort_by, value="Extension").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(options_frame, text="Date (Year-Month)", variable=self.sort_by, value="Date").grid(row=0, column=2, sticky="w")

        tk.Checkbutton(options_frame, text="Recursive Scanning", variable=self.recursive_mode).grid(row=1, column=1, sticky="w")
        tk.Checkbutton(options_frame, text="Preview Mode (No Moving)", variable=self.preview_mode).grid(row=1, column=2, sticky="w")

        # Statistics Dashboard
        stats_frame = tk.LabelFrame(self.root, text="Statistics Dashboard", padx=10, pady=10)
        stats_frame.pack(fill="x", padx=20, pady=5)

        self.stats_label = tk.Label(stats_frame, text="Files Moved: 0 | Total Size: 0 MB", font=("Helvetica", 10))
        self.stats_label.pack()

        # Log Display
        tk.Label(self.root, text="Activity Log:").pack(pady=(10, 0))
        self.log_area = scrolledtext.ScrolledText(self.root, height=12, width=70, font=("Consolas", 9))
        self.log_area.pack(padx=20, pady=5)

        # Control Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="START ORGANIZING", command=self.run_organizer, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=20, pady=10)
        self.start_btn.pack(side="left", padx=10)

        tk.Button(btn_frame, text="Clear Log", command=self.clear_log, padx=20, pady=10).pack(side="left")

    def browse_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_path.set(path)

    def browse_dest(self):
        path = filedialog.askdirectory()
        if path:
            self.dest_path.set(path)

    def log(self, message):
        self.log_area.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.log_area.see(tk.END)
        self.root.update_idletasks()

        # Also write to log.txt
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

    def clear_log(self):
        self.log_area.delete(1.0, tk.END)

    def run_organizer(self):
        src = self.source_path.get()
        dst = self.dest_path.get()

        if not src or not dst:
            messagebox.showerror("Error", "Please select both source and destination folders.")
            return

        if not os.path.exists(src):
            messagebox.showerror("Error", "Source folder does not exist.")
            return

        self.moved_count = 0
        self.total_size = 0
        self.start_btn.config(state="disabled")
        self.log(f"Starting organization from '{src}' to '{dst}'...")

        try:
            if self.recursive_mode.get():
                for root, _, files in os.walk(src):
                    self.process_files(root, files, dst)
            else:
                files = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]
                self.process_files(src, files, dst)

            self.update_stats()
            self.log("===== SUCCESS: Organization Complete =====")
            messagebox.showinfo("Done", f"Task completed!\nFiles Moved: {self.moved_count}")
        except Exception as e:
            self.log(f"ERROR: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.start_btn.config(state="normal")

    def process_files(self, current_root, files, base_dst):
        for filename in files:
            # Check for images
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                src_file = os.path.join(current_root, filename)
                file_size = os.path.getsize(src_file)

                # Determine destination folder
                if self.sort_by.get() == "Extension":
                    subfolder = filename.split('.')[-1].upper()
                else:  # Date sorting
                    mtime = os.path.getmtime(src_file)
                    dt_obj = datetime.fromtimestamp(mtime)
                    subfolder = dt_obj.strftime("%Y-%m")

                target_dir = os.path.join(base_dst, subfolder)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Duplicate Handling
                dest_file = os.path.join(target_dir, filename)
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(dest_file):
                        dest_file = os.path.join(target_dir, f"{base}_{counter}{ext}")
                        counter += 1

                # Move or Preview
                if self.preview_mode.get():
                    self.log(f"[PREVIEW] {filename} -> {os.path.basename(dest_file)}")
                else:
                    shutil.move(src_file, dest_file)
                    self.moved_count += 1
                    self.total_size += file_size
                    self.log(f"Moved: {filename} to {subfolder}/")
                    self.update_stats()

    def update_stats(self):
        size_mb = self.total_size / (1024 * 1024)
        self.stats_label.config(text=f"Files Moved: {self.moved_count} | Total Size: {size_mb:.2f} MB")
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoOrganizerApp(root)
    root.mainloop()
