import sys
import argparse
from organizer import FileOrganizer

def main():
    parser = argparse.ArgumentParser(description="Organize files by their extension into folders.")
    parser.add_argument("directory", nargs="?", default=".", help="Target directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    parser.add_argument("--undo", action="store_true", help="Undo the last organize operation")
    parser.add_argument("-r", "--recursive", action="store_true", help="Include subdirectories when organizing")
    
    args = parser.parse_args()
    target_dir = args.directory

    print(f"\033[96m File Organizer starting in {target_dir}...\033[0m")
    
    organizer = FileOrganizer(target_dir, args.dry_run, args.recursive)
    
    if args.undo:
        print(" Initiating undo...")
        restored = organizer.undo()
        print(f"\033[92m Successfully restored {restored} files!\033[0m")
    else:
        moved = organizer.organize()
        if args.dry_run:
            print(f"\033[93m Dry run complete. {moved} files would be moved.\033[0m")
        else:
            print(f"\033[92m Success! Moved {moved} files.\033[0m")

if __name__ == "__main__":
    main()
