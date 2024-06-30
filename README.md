## Beaver: Your Altesia Test-Taking Buddy

**Beaver** is a Python application with a graphical user interface (GUI) that automates test-taking on the Altesia website.

### Features

* **Automated Test Taking:** Runs a bot script (`run()`) to navigate through Altesia tests and provide answers based on your configuration.
* **User-Friendly GUI:** Built with `tkinter` for an intuitive and easy-to-use interface.
* **Password Protection:** Requires a password to activate the bot script, ensuring unauthorized use prevention.
* **File Management:** Offers options to clear temporary files generated during test automation and open an `answers.txt` file to review potential answers.

### Requirements

* Python 3.x (pre-installed on most systems)
* `tkinter` (included with Python)
* Additional modules based on your script's functionality (e.g., `pyautogui`, `fetch`)

### Installation

1. **Clone the Repository:**

Use code with caution.
content_copy
git clone https://github.com/yourusername/Beaver.git
cd Beaver


2. **Install Libraries:**

pip install pyautogui opencv-python pytesseract keyboard


**Note:** Install any additional dependencies (like `fetch`) following their specific instructions.

### Usage

1. **Place Necessary Files:**

Move all required images (e.g., `imgPC`, `imgAn`) and scripts (e.g., `fetch.py`) into the project directory.

2. **Run the GUI:**

py run.py


3. **Follow On-Screen Instructions:**

Enter the password and initiate the test automation process on Altesia.

### Script Details

**run.py**

* Handles GUI setup and integration with the bot script (`run()` function).
* Imports necessary modules.
* Defines GUI elements (labels, buttons, progress bar).

**Additional Notes:**

* Feel free to expand on this structure to include details about specific functionalities or configuration options.
* Remember to replace `yourusername` with your actual GitHub username.

**You can select and copy the instructions above for your reference.**
