# Python School Projects

A set of Python learning projects centered on a **Student Management System**, plus separate railway-record and stack exercises. The student application uses a Tkinter desktop interface, MySQL for student records, and Pandas/Matplotlib for data display and charts.

## Included projects

- `ana.py`, `m.py`, `mmmmm.py`, `IP project.py`, and `xyz.py` — different iterations of the student management GUI, with operations to add, view, modify, and delete student records and display marks.
- `KYF.py` — a command-line railway tracker that writes and edits railway records in `Railway.csv` and can visualize the records.
- `stack.py` — basic stack operations such as push, pop, peek, and display.

## Requirements

- Python 3
- MySQL Server and a local database/table matching the student app’s queries
- Python packages used by the student GUI: `mysql-connector-python`, `pandas`, and `matplotlib`

Install the Python dependencies with:

```bash
python -m pip install mysql-connector-python pandas matplotlib
```

## Run

Run an individual script from the repository directory, for example:

```bash
python "ana.py"
python KYF.py
python stack.py
```

The Tkinter student scripts expect a MySQL database and a `Student_Management_System` table to exist. Configure the database connection locally before running; do not commit credentials. `KYF.py` creates or updates its CSV data file as records are changed.

## Notes

The scripts are separate learning exercises rather than one packaged application. Several student-system files are alternate iterations of similar functionality.
