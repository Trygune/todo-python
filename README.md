# 📝 To-Do List (CLI)

A simple **command-line To-Do List application in Python** that lets you manage tasks with titles, descriptions, and priorities.  
Tasks are saved to a CSV file so they survive between runs—because memory is overrated.

---

## 🚀 Features

- Add tasks with:
  - Title
  - Description
  - Priority (low / medium / high — freeform but polite)
- Remove tasks by title
- View all tasks in a numbered list
- Save tasks to a CSV file
- Load saved tasks automatically on startup

---

## 📂 Project Structure

.
├── my_menu.py # Core logic (Task & ToDoList classes)
├── To_Do_List.py # CLI interface (user interaction)
└── data.csv # Stored tasks (created after saving)

yaml
Copy code

---

## ▶️ How to Run

Make sure you have **Python 3.10+** installed.

```bash
python To_Do_List.py
On launch, saved tasks are automatically loaded.

🧠 How It Works
Task class
Represents a single task with:

title
description
priority

Supports saving to and loading from CSV format.

ToDoList class
Manages:

Adding tasks
Removing tasks
Displaying tasks

Saving/loading tasks to/from data.csv

💾 Data Storage
Tasks are saved as CSV using Python’s built-in csv module.

File path used:

bash
Copy code
./Projects/Final/data.csv
⚠️ Make sure this directory exists before saving, or update the path in save_file().

🛠 Example Usage
yaml
Copy code
Welcome
*Add
*Remove
*See All Tasks
*Save

Choose your Action: add
Title: Learn Python
Description: Practice OOP and file handling
Priority: high

🧪 Known Limitations
No input validation for priority values

Removing tasks is title-based (duplicate titles = chaos)

No edit/update feature yet

These are features waiting patiently to be born.

📌 Future Improvements
Edit existing tasks

Priority validation

Better file path handling

Sorting tasks by priority

Colored CLI output (because aesthetics matter)

👤 Author
Farbod
GitHub: Trygune

📜 License
This project is open-source and free to use for learning and experimentation.
