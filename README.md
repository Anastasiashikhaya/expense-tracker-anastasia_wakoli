# Personal Expense Tracker CLI
A command-line application for tracking personal expenses with SQLite database storage.

## Features

- 💰 Add expenses with date, category, amount, and description
- 📋 List expenses with filtering options
- 📊 View spending summaries by category/time period
- 💻 Both interactive menu and direct command-line modes
- 🗄️ SQLite database storage with SQLAlchemy ORM

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-tracker-firstname-lastname.git
   cd expense-tracker-firstname-lastname

2. * Install dependencies:
    pip install pipenv
    pipenv install

3. * Initialize the database:
    pipenv run init-db

4. * Usage
 - Interactive Mode
   pipenv run tracker
 - Example workflow:
   1) Select "1. Add Expense"
   2) Enter date (YYYY-MM-DD)
   3) Enter category (e.g., "food", "gaming")
   4) Enter amount
   5) Optional description

5. Command Mode
   Add an expense:
   pipenv run add-expense --date 2024-07-08 --category food --amount 80.25 --description "Lunch with friends"

6. List expenses:
   # List all expenses
    pipenv run list-expenses

# Filter by category
  pipenv run list-expenses --category food

# Filter by date range
  pipenv run list-expenses --start-date 2024-07-10 --end-date 2024-07-06

7) View summary:
   # Monthly summary
   pipenv run summary --month 07 --year 2024

   # Yearly summary
   pipenv run summary --year 2024 

8) Project Structure 
   expense-tracker/
├── Pipfile
├── Pipfile.lock
├── README.md
├── init_db.py
├── tracker.py
├── db/
│   └── database.py
├── models/
│   └── expense.py
├── commands/
│   ├── add.py
│   ├── list.py
│   ├── summary.py
│   └── utils.py
└── tests/
    ├── test_add.py
    ├── test_list.py
    └── test_summary.py

9) Troubleshooting
   Database issues:
   # If you get "no such table" errors:
   rm expenses.db
   pipenv run init-db

10) Dependency issues:
    # Recreate virtual environment
    pipenv --rm
    pipenv install

11) Contributing
    1) Fork the project

    2) Create your feature branch (git checkout -b feature/AmazingFeature)

    3) Commit your changes (git commit -m 'Add some AmazingFeature')

    4) Push to the branch (git push origin feature/AmazingFeature)

   
 

