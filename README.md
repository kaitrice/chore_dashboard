# chore_dashboard

A simple Python-based dashboard for tracking and rotating household chores among roommates. Built using **SQLite** for storage and designed for small households.

---

## Features

* Track chores assigned to each roommate
* Check off completed chores
* Automatically rotate chores every Sunday
* Track incomplete chores for accountability
* Simple command-line interface (CLI)
* Lightweight SQLite database (file-based, no server required)

---

## Project Structure

```
chore_dashboard/
│
├── main.py            # Entry point, CLI dashboard
├── db.py              # SQLite connection and table setup
├── chores.py          # Chore logic (add, list, rotate, complete)
├── roommates.py       # Roommate logic (add, list)
├── utils.py           # Helper functions (week calculation, Sunday check)
└── data/
    └── chores.db      # SQLite database file
```

---

## Setup Instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/kaitrice/chore_dashboard.git
    cd chore_dashboard
    ```

2. **Install dependencies**

    ```bash
    pip install pytz
    ```

    *(`pytz` is optional if you plan to handle timezones for rotation)*

3. **Initialize the database**

    ```bash
    py main.py
    ```

    This will create the SQLite database (`data/chores.db`) and tables.

4. **Add roommates and chores**

    Uncomment the examples in `main.py` or use the functions from `roommates.py` and `chores.py`.

---

## Usage

* **Run the dashboard**

    ```bash
    python main.py
    ```

* **Mark a chore as complete**
  Use the `complete_chore(chore_id)` function from `chores.py`.

* **Chores rotate automatically every Sunday** based on the system date.

---

## Future Enhancements

* CLI menu for interactive marking and adding chores
* Web-based or mobile dashboard
* Points or reward system for completing chores
* Monthly or 3–6 month task scheduling
* Display roommate names instead of IDs in the dashboard

---

## Dependencies

* Python 3.8+
* SQLite3 (built into Python)
* `pytz` (optional, for timezone handling)

---

## License

MIT License – free to use and modify.
