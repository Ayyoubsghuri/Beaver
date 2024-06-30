Beaver

Beaver is a Python application designed to automate the process of taking language tests on the website Altesia. The script includes a graphical user interface (GUI) built with tkinter to provide a seamless user experience.

Features
- Graphical User Interface: Utilizes tkinter for a user-friendly interface.
- Automated Test Taking: Runs a bot script (run()) to navigate through tests on Altesia and provide answers.
- Password Protection: Requires a password to start the bot script.
- File Management: Includes options to clear temporary files and open an answears.txt file.

Requirements
- Python 3.x
- tkinter (usually included with Python)
- Additional modules as per your script structure (pyautogui, fetch, etc.)

Installation
1. Clone the repository:
git clone https://github.com/yourusername/Beaver.git
cd Beaver

2. Install the required libraries:
pip install pyautogui opencv-python pytesseract keyboard

3. Ensure additional dependencies (fetch, etc.) are properly installed. You may need to download or install them separately.

Usage
1. Place all necessary images (imgPC, imgAn) and scripts (fetch.py, etc.) in your project directory.
2. Run the GUI application using the command:
py run.py
3. Follow the on-screen instructions to enter the password and start automating test-taking on Altesia.

Script Details
run.py
This script handles the GUI setup and integration with the bot script (run() function):
- Imports necessary modules and dependencies.
- Defines GUI elements (labels, buttons, progress bar).
- Implements functions for password validation, running the bot script, clearing files, and handling GUI events.

run()
This function, imported from fetch.py, contains the core automation logic to interact with the Altesia website and provide answers to language tests.

Code Snippet
from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox
import tkinter
import pyautogui
from fetch import run
import os
import sys
import glob
import os.path
import urllib.request

File Structure
- run.py: Main script for the graphical user interface.
- requirements.txt: List of required Python libraries.
- imgPC/: Directory containing reference images for screen locations.
- imgAn/: Directory for storing and processing answer images.
- fetch.py, Locate.py, saveAnswears.py, anQu.py, saAn.py: Additional modules and scripts.
- temp/: Temporary directory for processing images.
- answears.txt: File to store answers.

Contributing
Contributions are welcome! Fork the repository, create a pull request, or suggest improvements via issues.

Disclaimer
This project is for educational and experimental purposes. Use it responsibly and respect the terms of service of Altesia or any website you interact with.

License
This project is licensed under the MIT License. See the LICENSE file for details.
