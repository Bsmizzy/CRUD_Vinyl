# Vinyl Collection CRUD App

A Flask app for managing vinyl records with full CRUD functionality.

## Features

- Add, view, edit, and delete vinyl records
- Input validation
- SQLite database

## Model

The `Vinyl` model has 7 fields:
- id (primary key)
- title (required)
- artist (required)
- year (required, 1900-2025)
- genre (optional)
- condition (optional)
- date_added (auto-generated)

## Installation

1. Create and activate virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Run the app:
```powershell
python app.py
```

4. Open http://127.0.0.1:5000

## Routes

- `GET/POST /` - List all records and add new ones
- `GET/POST /update/<id>` - Edit a record
- `GET /delete/<id>` - Delete a record

## Project Structure

```
CRUD_Vinyl/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── update.html
└── vinyl_collection.db
```

## Stack

- Flask
- Flask-SQLAlchemy
- SQLite
