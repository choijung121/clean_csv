# 🧼 CSV Cleaner (Drag & Drop GUI for macOS)
A simple macOS-friendly GUI app to clean up .csv credit card statements:
- 🧹 Removes unnecessary columns
- 🧾 Filters out unwanted description rows (e.g. "Online Payment")
- 🗃 Sorts rows by date
- ✂️ Shortens long descriptions
- 🖱 Drag-and-drop or browse for CSV files
- 🛠 Built with Tkinter, tkinterDnD2, and pandas

# ✅ Features
- Drag & drop your .csv file or browse manually
- Optional custom output filename
- Press a button to clean — your file is saved instantly
- No command line needed after building the app

<img width="415" height="377" alt="Screenshot 2025-07-10 at 11 17 42 PM" src="https://github.com/user-attachments/assets/f4e5f055-4487-4a70-aaae-f29fa8e86f11" />


# 📁 Folder Structure
```
csv-cleaner/
├── csv_cleaner.py          # Your main Python GUI app
├── setup.py                # For building .app using py2app
├── icon.icns               # Optional app icon
├── dist/                   # Folder where macOS app gets built
├── build/                  # Temp build files (can delete after build)
└── README.md
```

# 🚀 Run Locally (during development)
```
python3 clean.py
```
Make sure you have pandas and tkinterdnd2 installed:
```
pip install pandas tkinterdnd2
```

# 🍎 Build a Standalone macOS App (.app)
macOS users only — no Python needed after build
✅ 1. Set up a clean virtual environment
```
python3 -m venv csvenv
source csvenv/bin/activate
pip install pandas tkinterdnd2 py2app
```
✅ 2. Build the app
```
python3 setup.py py2app
```
Your .app will be in the dist/ folder
You can now double-click to launch the app like a native macOS app
