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

### 💰 Tab 2: ****

- 

### ⚙️ Filters

- 
---

## 🚧 Project Structure

```
.
├── api/                    # FastAPI - Data endpoints
│   ├── main.py             # Main API file
├── frontend/               # Streamlit app
│   ├── app.py              # Main entry point
├── poetry.lock             # Dependencies lock file
├── pyproject.toml          # Project metadata and dependencies
├── README.md
```

---

## 🚫 Requirements

- Python 3.10+
- Free account on [Supabase](https://supabase.com/)

---

## 📚 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/JoaoEscorcio/Streamlit_case.git
cd Streamlit_case
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies with Poetry

```bash
poetry install
```

### 4. Create the `.env` file

```env
SUPABASE_URL=https://<your-project>.supabase.co
SUPABASE_KEY=eyJhbGciOi...   # Your API Key
```

### 5. Run the API (FastAPI)

```bash
cd api
uvicorn main:app --reload --port 8000
```

### 6. Run the Frontend (Streamlit)

Open another terminal:

```bash
cd frontend
streamlit run app.py
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
- Price prediction using Machine Learning

---

Made with ❤️ by a data enthusiast!
