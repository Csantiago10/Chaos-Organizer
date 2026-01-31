# 📂 Chaos Organizer

> **"Stop the chaos. Reclaim your time."**

![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Built With](https://img.shields.io/badge/Built%20With-Python-yellow)

## 🧐 The Problem
Is your **Downloads folder a black hole**? 
We've all been there. You lose valuable time (approx. 20 mins/day) searching for important invoices, contracts, or images buried under hundreds of mixed files. It's frustrating, inefficient, and kills your productivity.

## 💡 The Solution
**Chaos Organizer** is an intelligent automation engine designed to detect, classify, and archive your documents instantly. It takes a messy directory and transforms it into a structured, navigable library with a single double-click.

### ✨ Key Features
* **Smart Classification:** Automatically identifies file extensions and routes them to logical subfolders (e.g., `.pdf` → `Documents/PDFs`, `.jpg` → `Media/Images`).
* **Safe Handling:** Uses robust path management (`os.path.join`) to ensure no data is lost or overwritten during the move.
* **Lightning Fast:** Process thousands of files in seconds.
* **Zero-Config:** No complex setup required. Just run and organize.

---

## 🚀 How to Use

### Option A: The Executable (No Coding Required)
1.  Download the `ChaosOrganizer.exe` file.
2.  **Run** the executable.
3.  **Paste** the full path of the folder you want to organize (e.g., `C:\Users\Santi\Downloads`).
4.  Press **Enter** and watch the magic happen! ✨

### Option B: Running from Source (For Developers)
If you want to inspect or modify the code:

```bash
# 1. Clone the repository
git clone https://github.com/Csantiago10/chaos-organizer.git

# 2. Navigate to the folder
cd Chaos_Organizer

# 3. Create virtual environment (Optional but recommended)
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash

# 4. Run the script
python main.py