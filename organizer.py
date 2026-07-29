import os
import shutil
import json
from pathlib import Path

CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Code": [".py", ".html", ".css", ".js", ".java", ".c", ".cpp", ".h", ".cs", ".php", ".rb", ".go", ".json", ".xml", ".sh", ".bat"]
}

class FileOrganizer:
    """Organizes files into categories based on extension."""
    
    def __init__(self, target_dir, dry_run=False, recursive=False):
        self.target_dir = Path(target_dir)
        self.dry_run = dry_run
        self.recursive = recursive
        self.move_log = {}
        self.log_file = self.target_dir / ".organizer_log.json"

    def get_category(self, extension):
        ext = extension.lower()
        for category, extensions in CATEGORY_MAP.items():
            if ext in extensions:
                return category
        return "Other"

    def get_unique_path(self, dest_path):
        if not dest_path.exists():
            return dest_path
        counter = 1
        while True:
            new_name = f"{dest_path.stem}_{counter}{dest_path.suffix}"
            new_path = dest_path.with_name(new_name)
            if not new_path.exists():
                return new_path
            counter += 1

    def organize(self):
        files_moved = 0
        search_pattern = "**/*" if self.recursive else "*"
        
        try:
            for item in self.target_dir.glob(search_pattern):
                if not item.is_file():
                    continue
                
                # Skip log file and hidden files in the target directory
                if item == self.log_file or item.name.startswith("."):
                    continue
                    
                # Skip files already in a category folder (prevent moving "Images/a.png" into "Images/Images/")
                if item.parent != self.target_dir and not self.recursive:
                    continue
                
                category = self.get_category(item.suffix)
                dest_dir = self.target_dir / category
                
                if not self.dry_run:
                    dest_dir.mkdir(exist_ok=True)
                
                dest_path = dest_dir / item.name
                dest_path = self.get_unique_path(dest_path)
                
                if self.dry_run:
                    print(f" [DRY RUN] Would move: {item.name} -> {category}/")
                else:
                    shutil.move(str(item), str(dest_path))
                    self.move_log[str(dest_path)] = str(item)
                    print(f" Moved: {item.name} -> {category}/")
                
                files_moved += 1
                
            if not self.dry_run and self.move_log:
                with open(self.log_file, "w", encoding="utf-8") as f:
                    json.dump(self.move_log, f)
            
            return files_moved
        except Exception as e:
            print(f" Error organizing files: {e}")
            return files_moved

    def undo(self):
        if not self.log_file.exists():
            print(" No undo log found.")
            return 0
            
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                log = json.load(f)
                
            restored = 0
            for curr_path, orig_path in log.items():
                if os.path.exists(curr_path):
                    os.makedirs(os.path.dirname(orig_path), exist_ok=True)
                    shutil.move(curr_path, orig_path)
                    print(f"⏪ Restored: {os.path.basename(curr_path)} -> {orig_path}")
                    restored += 1
                    
            if not self.dry_run:
                self.log_file.unlink()
                
            return restored
        except Exception as e:
            print(f" Error during undo: {e}")
            return 0
