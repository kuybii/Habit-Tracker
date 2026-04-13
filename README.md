📘 Habit Tracker (Python)

A simple command-line Habit Tracker built in Python that allows users to create habits, log daily progress, and track performance over time.

🚀 Features
➕ Add new habits with weekly targets
📅 Log daily habit completion
📋 View all habits
📊 See progress summary with completion percentage
💾 Save data using JSON (persistent storage)
🔁 Interactive menu system
🧠 How It Works

The program stores habits as a list of dictionaries and saves them to a JSON file.

Example structure:

{
    "name": "Gym",
    "target_per_week": 4,
    "total": 2,
    "log": [1, 1]
}

name → Habit name
target_per_week → Weekly goal
total → Number of times completed
log → History of completions

Data is automatically loaded on startup and saved when exiting.

🖥️ How to Run
1. Clone the repository
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
2. Run the program
python Habit_Tracker_Fin.py

(Make sure you have Python installed)

📌 Menu Options

When running the program, you’ll see:

1. Add habit
2. Log today
3. Show habits
4. Show summary
5. Save and Exit
💾 File Storage
Data is stored in: habits.json
Uses Python’s built-in json module
Automatically loads on start using load_habits()
Saves on exit using save_habits()

This ensures your progress is not lost.

🧪 Example Usage
--- HABIT TRACKER ---
1. Add habit
2. Log today
3. Show habits
4. Show summary
5. Save and Exit

Choose (1-5): 1
Habit name: Reading
Target per week: 5
Habit added.
⚠️ Limitations
Terminal-based (no graphical interface)
No input validation for all cases (e.g. text instead of numbers may crash)
No date tracking for logs
Single-user only
Basic summary (no graphs or analytics)
🔮 Future Improvements
✅ Add input validation (try/except)
📊 Add graphs for habit progress
🖼️ Build a GUI (Tkinter or web app)
📅 Add timestamps for each log
✏️ Edit/delete habits
👥 Multi-user support
🛠️ Technologies Used
Python
JSON (for data storage)
📂 Project Structure
habit-tracker/
│
├── Habit_Tracker_Fin.py
├── habits.json
└── README.md
📖 Code Reference

Main program file:

Includes:

load_habits() → loads JSON data
save_habits() → saves data
add_habit() → creates habits
log_today() → logs progress
show_habits() → displays habits
show_summary() → shows progress
🤖 Use of AI

AI was used to:

improve code structure and readability
assist with documentation (this README)
explain programming concepts

All core logic and implementation were written and understood independently.

📌 Author

Willber Lima M00945712
Middlesex University CST0400

