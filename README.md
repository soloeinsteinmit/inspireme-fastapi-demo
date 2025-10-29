# ✨ InspireMe — FastAPI Demo App

This project was built during the **Tech & Beyond Expo Ghana** workshop on Software Engineering.  
It introduces students to software engineering by building a motivational quotes web app using **FastAPI**.

## 🧠 What You'll Learn

- What software engineering is and why it matters
- How to build a simple backend using FastAPI
- How HTML templates interact with backend logic
- How to add new features and maintain clean, modular code

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML + CSS (Jinja templates)
- **Data:** List of quotes (hardcoded for simplicity)

## 🚀 Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/soloeinsteinmit/inspireme-fastapi-demo.git
   cd inspireme-fastapi-demo

   ```

2. Install dependencies:

   ```bash
   pip install fastapi uvicorn jinja2
   ```

3. Run the app:

   ```bash
   uvicorn main:app --reload --port 8080
   ```

4. Open in your browser:

   ```
   http://127.0.0.1:8000
   ```

## 💡 Future Improvements

- Add an AI model to generate new quotes
- Store quotes in a database
- Create a REST API endpoint `/api/quote` for mobile apps

---

## 🧩 2. Project Structure

```
inspireme-fastapi-demo/
│
├── main.py                 # FastAPI app entry point
├── templates/
│   └── index.html          # Main HTML template
├── static/
│   └── style.css           # CSS styling
├── README.md
└── .gitignore
```
