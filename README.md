# 🌍 Futurisys POC

This project is a **POC** 

---

## 🚀 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) – Backend API services
- [Supabase](https://supabase.com/) – Cloud-based database and authentication (PostgreSQL)

---

## 🔍 Features

### 📊 Tab 1: ****

-

### ⚙️ Filters

- 
---

## 🚧 Project Structure

```
.
├── README.md
├── __pycache__
│   └── start.cpython-312.pyc
├── requirements.txt
├── src
│   ├── __pycache__
│   ├── app_config_system.py
│   ├── db
│   │   ├── __pycache__
│   │   │   ├── models.cpython-312.pyc
│   │   │   └── session.cpython-312.pyc
│   │   ├── commands.py
│   │   ├── create_db.sql
│   │   ├── models.py
│   │   └── session.py
│   └── model
│       ├── __pycache__
│       │   └── load_model.cpython-312.pyc
│       ├── export_model.py
│       ├── load_model.py
│       └── model.joblib
├── start.py
├── test
│   ├── __pycache__
│   │   ├── test_predict.cpython-312-pytest-9.0.1.pyc
│   │   └── test_predict.cpython-313-pytest-8.3.4.pyc
│   └── test_predict.py
└── tree.bash

```

---

## 🚫 Requirements

- Python 3.10+
- Free account on [Supabase](https://supabase.com/)

---

## 📚 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone #############
cd ###########
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash

```

### 4. Create the `.env` file

```env

```

### 5. Run the API (FastAPI)

```bash
cd api
uvicorn main:app --reload --port 8000
```

---

## 🏙️ Deployment

### ✨ Suggested Platforms:

- **Render.com**: Ideal for running FastAPI (backend)
- **Streamlit Community Cloud**: Free frontend hosting

---

## 💼 Author

**Raphael Montico**\
Data Analyst | Python 
[LinkedIn](https://www.linkedin.com/in/raphaelmontico/)

---

## ✨ Future To-Do

- User authentication
- Report export functionality

---

Made with ❤️ by a data enthusiast!
