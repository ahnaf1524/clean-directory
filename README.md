# A Handy Script for Competitive Programmers

Competitive programming often involves working with multiple files and directories. Cleaning up temporary files and directories manually can be time-consuming and tedious. This script automates the process, making it easier for you to keep your workspace clean and organized.

### Features:
- Removes `.vscode` and `.cph` directories.
- Deletes temporary files like `tempCodeRunnerFile.c` and `tempCodeRunnerFile.cpp`.
- Cleans up all `.exe` files from the specified directory.
- Provides a detailed summary of the cleanup process.

### How to Use:
1. **Input**: Provide the path to your directory when prompted.
2. **Cleanup**: The script will automatically identify and remove unwanted files and folders.
3. **Output**: Displays a detailed summary of the operation with a professional, color-coded message.

### Benefits:
- Saves time and effort by automating directory cleanup.
- Helps maintain an organized workspace, essential for efficient coding.
- Eliminates distractions caused by unnecessary files.

### Prerequisite:
Make sure you have Python installed and the `colorama` library set up. To install `colorama`, run:
```bash
pip install colorama
```

### Running the Script:
1. Save the script in a `.py` file (e.g., `cleanup.py`).
2. Open a terminal and execute the script:
```bash
python cleanup.py
```
3. Enter the folder path when prompted.

This tool is designed to enhance productivity and streamline your workflow as a competitive programmer. Happy coding!
