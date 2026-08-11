# Rahi Fitness Centre Management System

Console-based Python + MySQL project (cleaned-up version of the original
class project — same features, working code).

## Setup (VS Code)

1. **Open the folder** `fitness_centre_project` in VS Code.

2. **Create a virtual environment** (Terminal in VS Code):
   ```
   python -m venv venv
   venv\Scripts\activate        (Windows)
   source venv/bin/activate     (Linux/Mac)
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database.** Open MySQL (Workbench, CLI, or the MySQL
   extension in VS Code) and run the contents of `schema.sql`. That
   creates the `fit_project` database and three tables.

5. **Set your MySQL password.** Open `db_config.py` and replace
   `"your_mysql_password"` with your actual root password — or set an
   environment variable instead so it's not hardcoded:
   ```
   set FIT_DB_PASSWORD=yourpassword     (Windows)
   export FIT_DB_PASSWORD=yourpassword  (Linux/Mac)
   ```

6. **Run it:**
   ```
   python main.py
   ```

## What changed from the original report

The original had several bugs that would crash or misbehave — this
version fixes them while keeping the same features:

- Menu now loops (`while True`) instead of running once and exiting.
- Login checks `user_id`/`password` together in one SQL query, instead
  of the broken `if user_id in row and passwd in row` logic.
- All SQL uses parameterized queries (`%s` placeholders) instead of
  string concatenation — avoids SQL injection and quote-related crashes.
- Missing `:` after `if`/`elif` statements fixed.
- Add customer / add item use `INSERT ... ON DUPLICATE KEY UPDATE` so
  re-entering the same ID updates instead of erroring.
- Input validation added for numeric fields (ID, amount, count).
- Code split into functions across a clean structure instead of one
  flat script.

## Files

- `main.py` — the program (menus + logic)
- `db_config.py` — MySQL connection settings
- `schema.sql` — creates the database and tables
- `requirements.txt` — Python dependencies
