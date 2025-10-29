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

2. Create a Python virtual environment (recommended):

   - On Windows (VSCode Terminal (or any IDE you're using)/cmd.exe):

     ```cmd
     python -m venv .venv
     ```

   - On macOS / Linux:

     ```bash
     python3 -m venv .venv
     ```

3. Activate the virtual environment before installing dependencies:

   - On Windows (cmd.exe):

     ```cmd
     .venv\Scripts\activate
     ```

   - On PowerShell:

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

   - On macOS / Linux:

     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install fastapi uvicorn jinja2
   ```

   (Optional) To freeze the exact dependencies for later use:

   ```bash
   pip freeze > requirements.txt
   ```

5. Run the app:

   ```bash
   uvicorn main:app --reload --port 8080
   ```

6. Open in your browser:

   ```txt
   http://127.0.0.1:8080
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
├── main.py                 # FastAPI app entry point(our backend logic — our server & routes)
├── templates/              # HTML templates that form the frontend
│   └── index.html
├── static/                 # Static assets like CSS, JS, images
│   └── style.css
├── README.md               # Documentation for developers
└── .gitignore
```

**Created by:** Solomon Eshun | [LinkedIn](https://www.linkedin.com/in/solomon-eshun-788568177/) | [Medium](https://soloshun.medium.com/) <br/>
**Workshop:** Tech & Beyond Expo Ghana 2025 <br/>
**Topic:** _Software Engineering in the Age of AI_
