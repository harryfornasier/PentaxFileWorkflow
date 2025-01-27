# Pentax Photo Transfer Tool

*A simple Python utility to organize RAW photos from your Pentax camera (work in progress).*

## What It Does (Currently)
- Automatically creates a designated folder (e.g., `Something_RAW`).
- Moves all `.PEF` (Pentax RAW) and `.xmp` (Metadata) files from the current directory into this folder.
- Case-insensitive handling (works with `.pef`, `.PEF`, etc.).

## Planned Features
- [ ] Automate movement from SD Card to photos folder
- [ ] Add support for `.DNG`/other formats
- [ ] Move OOC Jpegs to sub directory if they exist in the folder
- [ ] Name the parent folder

## Getting Started
1. **Prerequisites**:  
   - Python 3.6+ (tested on 3.10)
   - Your Pentax camera’s SD card (or directory with `.PEF` files)

2. **Usage**:  
   ```bash
   python name_file.py
