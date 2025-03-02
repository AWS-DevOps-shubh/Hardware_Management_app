# Hardware Management System

This is a **Hardware Management System** that allows users to add, list, update, and delete hardware assets. It includes both a **Command Line Interface (CLI)** and a **Web Interface** built using Flask.

## Hardware Management System Project Structure 
```
hardware_management/
├── database/
│   ├── db_handler.py
├── models/
│   ├── asset.py
├── controllers/
│   ├── asset_controller.py
├── views/
│   ├── cli.py
├── templates/
│   ├── index.html
├── static/
│   ├── styles.css
├── main.py
├── README.md
```

## Features
- **CLI Interface** 
- **Web Interface** 
- **SQLite Database**

## Hardware Management System Installation & Setup
### 1. Clone the Repository
```sh
git clone < Hardware_Management_app url >
cd hardware-management

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: 
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
pip install flask
```
## If you add asset throught CLI Use this Command
### 4. Run the CLI Application
```sh
python views/cli.py

### 5. Run the Web Application
```sh
python main.py

 Now Application access local `http://127.0.0.1:5000/` in your browser.
