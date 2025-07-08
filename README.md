# 🔍 Bing Search Automation for Microsoft Rewards (Edge + Selenium)

This Python script automates searches on Bing using Microsoft Edge browser to help you earn **Microsoft Rewards points** quickly and effortlessly.

---

## 📂 Project Overview

The script:
- Launches Microsoft Edge using Selenium.
- Performs a list of predefined searches.
- Waits between each search to simulate natural activity.
- Helps you reach your daily search quota for Microsoft Rewards.

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- Microsoft Edge browser
- Internet connection

---

## 🧪 Virtual Environment Setup (Recommended)

### 1. Create a virtual environment:
```bash
python -m venv bing_env
```

### 2. Activate the virtual environment:

#### On Windows:
```bash
bing_env\Scripts\activate
```

#### On macOS/Linux:
```bash
source bing_env/bin/activate
```

---

## 📦 Install Dependencies

### Using `requirements.txt`:
First, create a file named `requirements.txt` and add:

```text
selenium
webdriver-manager
```

Then run:
```bash
pip install -r requirements.txt
```

### Or install manually:
```bash
pip install selenium webdriver-manager
```

---

## 🚀 How to Run the Script

```bash
python bing_search_rewards.py
```

Make sure your Microsoft Edge browser is installed and up to date.

---

## 🧠 What the Script Does

- Uses `webdriver-manager` to automatically download the right Edge WebDriver version.
- Opens Bing homepage.
- Inputs predefined search queries one by one.
- Waits 5 seconds between each search to mimic natural behavior.
- Closes the browser after completing all searches.

---

## ⚠️ Disclaimer

- This script is for **educational purposes only**.
- Excessive or unnatural usage might violate Microsoft's terms of service.
- Use responsibly on your personal account.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Feel free to contribute or suggest improvements.
