# File & Folder Manager (CLI)

A simple command-line program written in Python that lets you create, read, update and delete files and folders from a menu. It uses only the Python standard library, so there is nothing extra to install.

## Features

**Folders**
- Create a new folder
- List all files and folders (including inside subfolders)
- Rename a folder
- Delete a folder (with everything inside it)

**Files**
- Create a file and write text into it
- Read a file's content
- Update a file: rename it, append text, or overwrite its content
- Delete a file

## Requirements

- Python 3.6 or higher

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## How to Use

When the program starts, it shows a menu:

```
Option:-
1.Create a folder
2.Read file and folders
3.Upadte the folders
4.Delete the folders
5.craete the file
6.read the file
7.update the file
8.delete the file
0.exist the program
```

Type the number of the action you want and press Enter, then follow the prompts.

**Example: create a file**
1. Enter `5`
2. Type a file name with extension, e.g. `notes.txt`
3. Type the text you want to save in it

## Project Structure

```
.
├── main.py      # the whole program
└── README.md
```

## Concepts Used

- `pathlib.Path` for working with files and folders
- `shutil.rmtree` for deleting folders
- `try / except` for error handling
- `while` loop and `if` conditions for the menu
- File handling with `open()` in read, write and append modes

## Warning

Deleting a folder or file is permanent and cannot be undone. Use the delete options carefully.

## Author

Rohit Tirmale
