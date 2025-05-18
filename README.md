# T-Bomb by Rayhan

![T-Bomb Logo](https://via.placeholder.com/150?text=T-Bomb) <!-- Replace with actual logo if available -->

**T-Bomb by Rayhan** is a Python-based tool designed for **educational purposes** to test API functionalities and spam detection systems. It supports SMS, call, and email bombing modes, allowing users to understand how APIs handle high-volume requests. This project is maintained by Rayhan and is intended for research and learning only.

> **⚠️ Disclaimer**: This tool is strictly for **educational and research purposes**. Misuse of this tool, such as unauthorized spamming or harassment, is illegal and unethical. The developer (Rayhan) is not responsible for any misuse or consequences arising from improper use.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Version](#version)
- [Contributing](#contributing)
- [Developer](#developer)
- [License](#license)

## Features
- **Multi-Mode Support**: Send SMS, call, or email requests for testing purposes.
- **Country Code Integration**: Supports multiple country codes via `isdcodes.json`.
- **Threaded Requests**: Efficiently handles concurrent API requests with customizable delays and threads.
- **Colorful Console Output**: Uses `colorama` for visually appealing and formatted messages.
- **PIP Installation**: Recommends PIP-based dependency installation for stability (see `.notify`).
- **Customizable APIs**: Configure API providers using `apidata.json` (template provided).

## Installation

Follow these steps to set up **T-Bomb by Rayhan** on your system:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rayhankhan4u/T-Bomb.git
   cd T-Bomb
   ```
Make the Bash Script Executable:
  ```bash
chmod +x tbomb.sh
  ```
Run the Setup Script:
```bash
./tbomb.sh
```
## Usage
You can run T-Bomb in two ways:
Using the Bash Script (Recommended):
```bash
./tbomb.sh
```
The script displays a menu to select modes (SMS, Call, or Mail).
Follow the prompts to input:
➤Country Code (e.g., 91 for India)
➤Target Number/Email (e.g., 1234567890 or example@email.com)
➤Message/Call Count (e.g., 10)
➤Delay (e.g., 2 seconds)
➤Thread Count (e.g., 5)

Using the Python Script Directly:
```bash
python tbomb.py
```
Similar prompts as above will guide you through the process.

Example: 
```bash
./tbomb.sh
```
[ # ] Welcome to T-Bomb by Rayhan
[ → ] Select Mode:
1. SMS Bomber
2. Call Bomber
3. Mail Bomber
Enter choice: 1
Enter country code (e.g., 91): 91
Enter target number: 1234567890
Enter message count: 10
Enter delay (seconds): 2
Enter thread count: 5
[ ✔ ] Starting SMS Bomber...

Tip: For testing, use a low message count (e.g., 1-2) and a higher delay (e.g., 5 seconds) to avoid overwhelming APIs.

## Project Structure
The repository is organized as follows:
tbomb.py: Main Python script that orchestrates the bombing process and user interaction.
tbomb.sh: Bash script for easy setup, dependency installation, and launching the tool.
apidata.json: Configuration file for API providers (ignored by .gitignore for security).
isdcodes.json: Contains country codes for phone number validation.
requirements.txt: Lists Python dependencies for PIP installation.
.version: Specifies the project version (3.0.0-rayhan).
.notify: Displays a message recommending the PIP version and credits Rayhan.
.gitignore: Ensures sensitive files (e.g., apidata.json, __pycache__/) are not uploaded.
utils/:decorators.py: Formats console output with colored icons and status messages using colorama.
provider.py: Manages API providers and sends HTTP requests based on apidata.json.

## Requirements
Python 3.x (tested with Python 3.8+)Bash (for running tbomb.sh)
Termux (optional, for Android users)
Dependencies (listed in requirements.txt):
```
certifi>=2020.6.20
chardet>=3.0.4
colorama>=0.4.3
idna>=2.10
requests>=2.24.0
```
Termux Packages (for Termux users):
```bash
pkg install python git figlet toilet
```

## Version
Current version: 3.0.0-rayhan (see .version and apidata.json)

## Developer
Developed by Rayhan
➤GitHub: rayhankhan4u
➤Contact: For queries, open an issue on the repository.
This project is a personal endeavor by Rayhan to explore API testing and Python scripting. It is not affiliated with any other projects or developers.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

