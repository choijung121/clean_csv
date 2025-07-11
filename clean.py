import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog

exclude_phrases = [
    "Online Payment",
    "AMEX Dining Credit",
    "AMEX DUNKIN' CREDIT"
]   

def should_remove(description):
    for phrase in exclude_phrases:
        if phrase.lower() in description.lower():
            return True
    return False

def browse_file():
    path = filedialog.askopenfilename(
        filetypes = [("CSV files", "*.csv")],
        title = "Select a CSV file"
    )
    if path: 
        file_path_var.set(path)
        file_label.config(text=f"File: 📂 {os.path.basename(path)}")

def clean_csv():
    file_path = file_path_var.get()
    custom_filename = output_name_var.get()

    if not file_path:
        messagebox.showerror("Error", "Please drop a CSV file before cleaning.")
        return

    try: 
        df = pd.read_csv(file_path)
        print("Dropped file:", file_path)

    except Exception as e:
        print(f"Error reading the file: {str(e)}")
        messagebox.showerror("Error", f"Could not read file: {e}")
        return

    try:
        # Remove unwanted columns
        df_clean = df.drop(columns=["Card Member", "Account #"], errors='ignore')

        # Remove unwanted descriptions
        df_clean = df_clean[~df_clean["Description"].apply(should_remove)]
        
        # Convert and sort dates
        df_clean["Date"] = pd.to_datetime(df_clean["Date"])
        df_clean = df_clean.sort_values(by="Date")

        # Shorten descriptions
        df_clean["Description"] = df_clean["Description"].apply(
            lambda x: x if len(x) <= 15 else x[:12] + "..."
        )

        folder = os.path.dirname(file_path)
        original_file = os.path.splitext(os.path.basename(file_path))[0]
        file_to_use = custom_filename.strip() or f"CLEANED_{original_file}"
        cleaned_file = os.path.join(folder, file_to_use + ".csv")

        df_clean.to_csv(cleaned_file, index=False)

        messagebox.showinfo("Success", f"✅ Cleaned CSV saved as {cleaned_file}")

        # Reset GUI after success
        file_path_var.set("")
        file_label.config(text="No file selected")
        output_name_var.set("")

    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred while processing the file: {e}")
        
def on_drop(event): 
    file_path = event.data.strip().replace("{", "").replace("}", "")
    if file_path.endswith(".csv"):
        # clean_csv(file_path)
        file_path_var.set(file_path)
        file_label.config(text=f"File: 📂 {os.path.basename(file_path)}")

    else: 
        messagebox.showerror("Error", "Please drop a valid CSV file.")

# Set up the GUI
root = TkinterDnD.Tk()
root.title("CSV Cleaner")
root.geometry("420x350")

output_name_label = tk.Label(root, text="Save File as... (no .CSV): ").pack(pady=(10, 5))
output_name_var = tk.StringVar()
output_name_entry = tk.Entry(root, textvariable=output_name_var, width=30)
output_name_entry.pack()

drop_area = tk.Label(root, text="\n⬇ Drop CSV file here ⬇\n", relief="ridge", width=40, height=6)
drop_area.pack(pady=20)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

browse_button = tk.Button(root, text="📂 Browse File", command=browse_file)
browse_button.pack(pady=5)

file_path_var = tk.StringVar()
file_label = tk.Label(root, text="No file selected")
file_label.pack()

clean_button = tk.Button(root, text="🧼 Clean CSV", command=clean_csv, bg="#4CAF50", fg="black")
clean_button.pack(pady=10)

root.mainloop()