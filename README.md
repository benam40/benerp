# Berp ERP App

A simple, modular ERP web application inspired by Odoo, built with FastAPI.

## Features
- Modular architecture: user, crm, inventory, pos
- Easily extensible for more modules

## Getting Started

### 1. Create and activate a virtual environment (recommended)
For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
uvicorn main:app --reload
```

### 3. API Endpoints
- `/user` - User management
- `/crm` - Customer Relationship Management
- `/inventory` - Inventory management
- `/pos` - Point of Sale

## Development
- Add more modules by creating new `*.py` files and registering routers in `main.py`.
- Contributions welcome!

## Version Control
Initialize git and connect to your remote repository to start tracking changes.
