# 🚀 T-Bomb by Rayhan

![T-Bomb Logo](https://via.placeholder.com/150?text=T-Bomb) <!-- Replace with your logo -->

**T-Bomb** is an advanced **SMS, Call, and Email bombing tool** created for **educational purposes**. Designed and maintained by **Rayhan**, it allows users to test the resilience of APIs and understand how high-volume requests are handled by modern systems.

> ⚠️ **Disclaimer**: This tool is intended strictly for **educational and ethical testing**. Any misuse for illegal activities is strictly prohibited. The developer is not responsible for any misuse of this project.

---

## ✨ Features

- **Multi-Mode Support** — SMS, Call, and Mail bombing
- **Global Country Code Integration** — Supports multiple countries via `isdcodes.json`
- **Threaded Requests** — Efficient, fast, and customizable
- **Colorful UI** — Clean CLI interface with `colorama`
- **Easy Setup** — Bash script for automatic installation
- **Modular API System** — Configure APIs in `apidata.json` easily
- **Termux Support** — Run directly from Android with Termux

---

## ⚙️ Installation

### For Linux
```bash
git clone https://github.com/rayhankhan4u/T-Bomb.git
cd T-Bomb
chmod +x tbomb.sh
./tbomb.sh
```


For Termux (Android)
```bash
pkg install python git figlet toilet -y
git clone https://github.com/rayhankhan4u/T-Bomb.git
cd T-Bomb
chmod +x tbomb.sh
./tbomb.sh
```

---

▶️ Usage

Run via Bash script (Recommended):
```bash
./tbomb.sh
```
Run via Python directly:
```bash
python tbomb.py
```
Example Workflow
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

> 💡 Tip: For safe testing, use lower message count (1–2) and higher delay (≥ 5 seconds).




---

📁 Project Structure

T-Bomb/
├── tbomb.py             # Main Python script
├── tbomb.sh             # Bash setup/launcher script
├── apidata.json         # API config (ignored by .gitignore)
├── isdcodes.json        # Country codes data
├── requirements.txt     # Python dependencies
├── .version             # Version info (e.g., 3.0.0-rayhan)
├── .notify              # Notice & credits
├── utils/
│   ├── decorators.py    # Colorful output formatting
├── provider.py          # API handler logic
└── .gitignore           # Ignore sensitive/cache files


---

📦 Requirements

Python

Python 3.8 or higher

Install dependencies:

```bash
pip install -r requirements.txt
```
Termux (Android)
```bash
pkg install python git figlet toilet -y
pip install -r requirements.txt
```
Python Libraries Used:

certifi>=2020.6.20
chardet>=3.0.4
colorama>=0.4.3
idna>=2.10
requests>=2.24.0


---

🔖 Version

Current version: 3.0.0-rayhan
Version details available in .version and .notify files.


---

👨‍💻 Developer

Rayhan Khan

GitHub: @rayhankhan4u

Contact: Open an issue for questions or feedback.


This is a personal learning project focused on API testing and ethical research. Not affiliated with any third-party group.


---

📄 License

Licensed under the MIT License.
See the LICENSE file for full details.


---

© 2025 Rayhan Khan | T-Bomb Project
