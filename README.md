# Pentax Photo Transfer Tool

*A simple Python utility to organize RAW photos from your Pentax camera.*

## What It Does
- Automatically creates a designated folder in your Pictures folder (e.g., `Something_RAW`).
- Checks if folder has already been transfered.
- If there are multiple folders to transfer it will ask you to name them separately.
- Moves all `.PEF` (Pentax RAW) and `.xmp` (Metadata) files from the current directory into a subdirectory in that folder"
- Case-insensitive handling (works with `.pef`, `.PEF`, etc.).

## Getting Started
1. **Prerequisites**:  
   - Python 3.6+ (tested on 3.10)
   - Your Pentax camera’s SD card (or directory with `.PEF` files)

2. **Usage**:
   Place python file onto root of SD Card
   ```bash
   python name_file.py
