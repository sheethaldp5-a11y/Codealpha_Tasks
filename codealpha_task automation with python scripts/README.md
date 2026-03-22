# Task Automation with Python Scripts

A collection of Python automation scripts for file organization and management tasks, featuring both command-line and GUI-based photo organizers.

## Features

- **File Organizer (CLI)**: Automatically organize files by extension type
- **Smart Photo Organizer (GUI)**: Advanced photo organization with multiple sorting options
- **Flexible Configuration**: JSON-based configuration for file types and settings
- **Logging System**: Track all file operations with timestamped logs
- **Recursive Processing**: Process files in subdirectories
- **Preview Mode**: Test organization without actually moving files

## Components

### 1. File Organizer (CLI)
A command-line script that organizes files from a source directory into categorized folders based on file extensions.

### 2. Smart Photo Organizer (GUI)
A graphical user interface application for organizing photos with advanced options:
- Sort by file extension (JPG, PNG, etc.)
- Sort by date (Year-Month format)
- Recursive folder processing
- Preview mode for testing
- Real-time progress tracking

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd "task automation with python scripts"
   ```
3. Install required dependencies (if any):
   ```bash
   pip install tk  # For GUI components (usually pre-installed with Python)
   ```

## Usage

### Command-Line File Organizer

1. Configure the file types in `config.json`:
   ```json
   {
     "allowed_types": ["jpg", "png", "jpeg", "gif"]
   }
   ```

2. Run the organizer:
   ```bash
   python main.py
   ```

3. Files from `source_folder` will be organized into `organized_files` by extension.

### GUI Photo Organizer

1. Run the GUI application:
   ```bash
   python organize_photos.py
   ```

2. Select source and destination folders
3. Choose sorting method (Extension or Date)
4. Configure options (recursive, preview mode)
5. Click "Organize Files" to start

## Configuration

### config.json
```json
{
  "allowed_types": ["jpg", "png", "jpeg"]
}
```
- `allowed_types`: Array of file extensions to process (without dots)

## Project Structure

```
task-automation-python-scripts/
├── main.py                    # CLI file organizer entry point
├── organizer.py               # Core file organization logic
├── organize_photos.py         # GUI photo organizer application
├── logger.py                  # Logging functionality
├── config.json               # Configuration file
├── log.txt                   # Log output file
├── source_folder/            # Source directory for files to organize
│   ├── document.txt
│   ├── readme.md
│   └── vacation/
├── organized_files/          # Destination directory for organized files
│   ├── JPEG/
│   │   └── sunset.jpeg
│   └── PNG/
│       └── beach.png
├── jpg_folder/               # Additional test folder
└── README.md                 # This file
```

## Logging

The system maintains detailed logs of all file operations in `log.txt` with JSON format entries containing:
- Timestamp of operation
- Filename
- Destination path

## Supported File Types

Currently configured to handle:
- JPG/JPEG
- PNG

Additional file types can be added to `config.json`.

## Requirements

- Python 3.x
- tkinter (usually included with Python installation)

## Future Enhancements

- Support for additional file types
- Custom sorting criteria
- Duplicate file detection
- Undo functionality
- Batch processing options
- Integration with cloud storage services