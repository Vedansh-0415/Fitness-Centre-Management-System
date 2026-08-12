# 🏋️ Rahi Fitness Centre Management System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql)
![CLI](https://img.shields.io/badge/Interface-Console-000000)

</p>

A console-based **fitness centre management system** built with **Python** and **MySQL**, developed as a Computer Science project (Code: 083). Handles member accounts, customer records, and gym equipment inventory through a simple menu-driven interface backed by a relational database.

---

## 📌 Project Highlights

* Built a full **CRUD workflow** (Create, Read, Update) against a live MySQL backend
* Menu-driven console app with **persistent login sessions** and account creation
* All queries use **parameterized SQL** — no string-concatenated queries, no injection risk
* **Upsert logic** (`INSERT ... ON DUPLICATE KEY UPDATE`) for customer and inventory records
* Input validation on all numeric fields (IDs, amounts, counts)
* Clean separation between connection handling (`db_config.py`) and application logic (`main.py`)

---

## 🧩 Why This Project?

Small fitness centres often track members and equipment on paper or in spreadsheets, which gets error-prone as the member base grows. This project models the core of a real gym-management workflow — member accounts, customer billing records, and equipment tracking — as a relational database driven by a simple, dependency-light console app.

---

## 📂 Database Schema

| Table                 | Purpose                                     | Key Columns                                                                 |
| ---------------------- | -------------------------------------------- | ----------------------------------------------------------------------------- |
| `user_fitness_rahi1`   | Staff/admin login accounts                   | `user_id` (PK), `password`, `name`                                            |
| `custmer`               | Gym customer records                        | `custmer_id` (PK), `custmer_name`, `custmer_address`, `joined_date`, `amt_paid` |
| `jim_items`             | Gym equipment inventory                     | `object_id` (PK), `object_name`, `date_of_parchase`, `repairing_data`, `total_people_using` |

---

## ⚙️ Application Workflow

```text
                Rahi Fitness Centre — Program Flow

                     ┌─────────────────────┐
                     │   Connect to MySQL  │
                     └─────────┬───────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │    Main Menu        │
                     │ 1. Login             │
                     │ 2. Create Account    │
                     │ 3. Exit              │
                     └─────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
      ┌───────────────────┐      ┌───────────────────┐
      │   Login (auth)     │      │  Create Account    │
      └─────────┬─────────┘      └─────────┬─────────┘
                │                          │
                ▼                          │
      ┌─────────────────────┐              │
      │   Logged-in Menu     │◀────────────┘
      │ 1. View Customers     │
      │ 2. Add/Update Customer│
      │ 3. View Gym Items     │
      │ 4. Add/Update Item    │
      │ 5. Logout              │
      └─────────┬─────────────┘
                │
                ▼
      ┌─────────────────────┐
      │  MySQL (fit_project) │
      │  Parameterized CRUD  │
      └─────────────────────┘
```

---

## 🖥️ Running the App

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up the database (run once in MySQL Workbench / CLI)
#    Executes schema.sql, creating fit_project and its 3 tables

# 3. Set your MySQL password for this session
$env:FIT_DB_PASSWORD="yourpassword"     # PowerShell
export FIT_DB_PASSWORD="yourpassword"   # Linux / Mac

# 4. Run it
python main.py
```

The app runs entirely in the terminal — no server or browser needed.

---

## 🛠️ Technologies Used

* Python
* MySQL
* mysql-connector-python

---

## 📁 Repository Structure

```text
fitness_centre_project/
│
├── main.py           # Program entry point — menus and CRUD logic
├── db_config.py       # MySQL connection handling
├── schema.sql          # Database + table definitions
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## 👨‍💻 Author

- **Vedansh** — Class 10th student, Khelgaon Public School

⭐ If you found this project useful, consider giving it a star!
