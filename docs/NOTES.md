# 🧠 InspireMe Workshop Notes

_Tech & Beyond Expo — Software Engineering in the Age of AI_

---

## 🌍 What Is Software Engineering?

Software engineering is the **systematic and disciplined process** of designing, building, testing, and maintaining software systems.

It’s not just about coding — it’s about **planning, structure, teamwork, and continuous improvement**.

---

## 🧩 What Is Software?

Software is a set of **instructions** that tells a computer what to do.  
Examples include:

- Mobile apps (e.g., WhatsApp)
- Websites (e.g., YouTube)
- Games
- AI systems

---

## ⚙️ What Is Engineering?

Engineering means **applying science and creativity to solve problems** using structure and design.  
So, _Software Engineering_ = **using engineering principles to create reliable software systems.**

---

## 💡 Why Software Engineering Matters

Good software engineering ensures that programs are:

- ✅ Reliable (they work correctly)
- 🔧 Maintainable (easy to fix or update)
- ⚡ Scalable (can handle growth)
- 🔒 Secure (protect user data)

Without these, even great code can fail.

---

## 🏗️ The InspireMe App Overview

This simple app demonstrates how software engineers structure a project.

When you visit the app, it:

1. Randomly selects a motivational quote.
2. Sends it to the frontend (HTML page).
3. Displays it with nice styling.

It’s simple — but follows **real-world engineering principles**.

---

## 📁 Folder Structure Explained

```
inspireme-fastapi-demo/
│
├── main.py # The brain (backend logic)
├── templates/ # The face (HTML templates)
│ └── index.html
├── static/ # The clothes (CSS, images, scripts)
│ └── style.css
└── README.md # The manual (project documentation)
```

| File / Folder | Description                                                                            |
| ------------- | -------------------------------------------------------------------------------------- |
| `main.py`     | Contains our FastAPI backend code. It decides what data to send and what page to show. |
| `templates/`  | Contains HTML files that display content to the user.                                  |
| `static/`     | Contains CSS, images, and JavaScript for styling and visuals.                          |
| `README.md`   | Explains how the app works and how to set it up.                                       |

---

## 🧠 How FastAPI Works

FastAPI is a **Python web framework** that helps us build web apps quickly and efficiently.

In `main.py`, we:

1. Create an app using `FastAPI()`
2. Define routes (pages)
3. Use **Jinja2 templates** to send data from Python to HTML

### Example:

```python
@app.get("/")
def get_quote(request: Request):
    quote = random.choice(quotes)
    return templates.TemplateResponse("index.html", {"request": request, "quote": quote})
```

🗣️ When a user visits the home page (`/`):

- Python picks a random quote.
- It sends the quote to our HTML page using a Jinja2 template.

---

## 🖥️ How Jinja2 Templates Work

Jinja2 allows us to insert Python variables into HTML files.

In our HTML, we write:

```html
<p class="quote">"{{ quote }}"</p>
```

Here, `{{ quote }}` is replaced by the actual quote chosen in Python.
It’s like saying:

> “Fill this blank space with data from the backend.”

---

## 🔄 How the App Works (Step-by-Step)

1. You open the app → Browser sends a request to FastAPI.
2. FastAPI runs `get_quote()` and picks a random quote.
3. The quote is inserted into the HTML template.
4. The browser displays the web page with that quote.
5. Clicking “Show Another Quote” reloads the page to display a new one.

---

## 🧩 Software Engineering Principles in Action

| Step | Concept        | Example in InspireMe                                    |
| ---- | -------------- | ------------------------------------------------------- |
| 1️⃣   | Requirements   | “Build an app that shows random motivational quotes.”   |
| 2️⃣   | Design         | Use FastAPI + HTML + CSS.                               |
| 3️⃣   | Implementation | Write the Python, HTML, and CSS code.                   |
| 4️⃣   | Testing        | Run the app to check if it works correctly.             |
| 5️⃣   | Deployment     | (Optional) Upload to GitHub / Render for others to use. |

---

## 💡 Try These Features Yourself!

Here are some fun ideas to improve your version of **InspireMe**:

1. 🎨 Add a “Change Background Color” button that switches between 3 color themes.
2. 🗂️ Add categories (e.g., Motivation, Focus, Discipline).
3. 💬 Allow users to submit their own quotes.
4. 🔊 Add sound or animations when the quote changes.
5. 🧠 Connect to an AI model to generate new quotes automatically.

> “Small ideas grow into great software — that’s how every engineer starts.”

---

## 🧭 Final Thoughts

Software Engineering = **Turning ideas into real, reliable systems.**

Even this simple app shows how:

- You analyze requirements,
- Design a structure,
- Implement it cleanly,
- And think about how to extend it later.

> _"If it is to be, it is up to me."_
> — Remember, the power to build the future is in your hands.

---

**Created by:** Solomon Eshun | [LinkedIn](https://www.linkedin.com/in/solomon-eshun-788568177/) | [Medium](https://soloshun.medium.com/) <br/>
**Workshop:** Tech & Beyond Expo Ghana 2025 <br/>
**Topic:** _Software Engineering in the Age of AI_
