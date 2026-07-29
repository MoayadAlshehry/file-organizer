# File Organizer

A Python CLI tool that automatically organizes files in a directory by their file type into categorized folders.

## Features
- **Smart Categorization**: Organizes files into folders (Images, Documents, Videos, Music, Archives, Code, Other) based on their extension.
- **Duplicate Handling**: Automatically renames files with conflicting names (e.g., `file_1.txt`) to avoid overwriting.
- **Dry-Run Mode**: Preview what files will be moved without actually touching them.
- **Undo Functionality**: Made a mistake? Quickly restore files to their original locations.
- **Recursive Mode**: Optionally process files in all subdirectories.

## Installation
Clone the repository and run the script directly. No third-party dependencies are required.

```b```bash
git clone <your-repo-url>
cd file-organizer
```

## Usage
Run `main.py` passing the directory you want to organize. If no directory is passed, it uses the current directory.

```b```bash
python main.py /path/to/your/folder
```

### Examples
- **Dry Run** (preview changes):
  ```b```bash
  python main.py /path/to/your/folder --dry-run
  ```
- **Recursive Organize** (include subfolders):
  ```b```bash
  python main.py /path/to/your/folder -r
  ```
- **Undo Last Operation**:
  ```b```bash
  python main.py /path/to/your/folder --undo
  ```

## Supported File Types

| Category | Extensions |
|---|---|
| Images | `.jpg, .jpeg, .png, .gif, .bmp, .svg, .webp` |
| Documents | `.pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx, .csv` |
| Videos | `.mp4, .avi, .mkv, .mov, .wmv, .flv, .webm` |
| Music | `.mp3, .wav, .flac, .aac, .ogg, .wma` |
| Archives | `.zip, .rar, .7z, .tar, .gz, .bz2, .xz` |
| Code | `.py, .html, .css, .js, .java, .c, .cpp, .h, .cs, .php, .rb, .go, .json, .xml, .sh, .bat` |
| Other | Any file not listed above |

## Technologies
- Python 3
- Standard Libraries (`os`, `shutil`, `json`, `pathlib`, `argparse`)
