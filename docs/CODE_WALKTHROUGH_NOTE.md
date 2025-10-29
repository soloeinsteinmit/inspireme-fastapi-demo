## 🧠 Software Engineering in Action: Code walkthrough note

> “Software engineering is not just about writing code — it’s about designing _systems_ that are structured, maintainable, and scalable. Even this simple ‘InspireMe’ app follows the same principles used in real-world systems — it has structure, logic, and separation of concerns.”

Our **InspireMe** project demonstrates these key software engineering ideas:

1. **Modularity** – different parts (backend, frontend, assets) are separated.
2. **Maintainability** – if something breaks, we know exactly where to look.
3. **Scalability** – it’s easy to add features like new quotes, colors, or even AI.

---

## 🗂️ FOLDER STRUCTURE EXPLAINED

```
inspireme-fastapi-demo/
│
├── main.py                 # Backend logic — our server & routes
├── templates/              # HTML templates that form the frontend
│   └── index.html
├── static/                 # Static assets like CSS, JS, images
│   └── style.css
└── README.md               # Documentation for developers
```

Here’s what each part means:

| Folder/File    | Purpose                                                                                                                       | Explanation                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **main.py**    | The **brain** of the app. It tells FastAPI how to handle requests, what data to process, and what page to show.               | “When you visit the website, `main.py` decides what to display and passes information to the HTML page.” |
| **templates/** | The **face** of the app — the web pages users see. It uses **Jinja2 templates**, which let us mix Python variables into HTML. | “The templates are dynamic — they can display changing data from Python, like random quotes.”            |
| **static/**    | The **clothes and design** of the app — contains CSS, images, or scripts that make things look good.                          | “This is where we put styles, logos, or icons — things that don’t change often.”                         |
| **README.md**  | The **manual** for developers who want to understand or contribute.                                                           | “Good software engineers document their work so others can understand or build on it.”                   |

---

## ⚙️ HOW FASTAPI + JINJA2 WORK TOGETHER

> **💡TIP:** Split screen to show `main.py` and `index.html` side by side.

---

### 🧩 Step 1: FastAPI App Setup

```python
app = FastAPI(title="InspireMe App")
```

✅ This line _creates our web application_.
Think of it as starting an empty restaurant — the restaurant is ready, but you need to add **menus (routes)** and **chefs (functions)** to serve visitors.

---

### 🧩 Step 2: Mounting Static Files

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

✅ This tells FastAPI where to find images, CSS, or JavaScript files.

> “When the browser asks for `/static/style.css`, FastAPI knows to look inside our static folder.”

---

### 🧩 Step 3: Setting Up Jinja2 Templates

```python
templates = Jinja2Templates(directory="templates")
```

✅ This connects FastAPI to **Jinja2**, a templating engine that lets you insert Python variables directly into HTML pages.

> “Jinja allows us to send data from Python to HTML dynamically — like sending a new quote each time someone reloads.”

---

### 🧩 Step 4: The Quote Logic

```python
quotes = [
    "If it is to be, it is up to me.",
    "It’s not over until I win.",
    ...
]
```

✅ This is our simple **data layer** — a list of quotes.

> “In real systems, this could be a database or even an AI model generating text.”

Then we pick one randomly:

```python
quote = random.choice(quotes)
```

---

### 🧩 Step 5: The Route

```python
@app.get("/", response_class=HTMLResponse)
def get_quote(request: Request):
    quote = random.choice(quotes)
    return templates.TemplateResponse("index.html", {"request": request, "quote": quote})
```

✅ This function does 3 things:

1. **Listens** for people visiting `/` (the homepage).
2. **Selects** a random quote.
3. **Sends** that quote to the HTML file called `index.html`.

> “Every time someone visits our page, the backend chooses one random quote and sends it to the frontend — like a new message of inspiration.”

---

## 🧱 HOW JINJA2 WORKS IN THE HTML

```html
<p class="quote">"{{ quote }}"</p>
```

✅ The double curly braces `{{ ... }}` are placeholders where Jinja injects data from Python.
Here, `{{ quote }}` will be replaced with whatever string Python sends (our random quote).

You can say:

> “Jinja acts as a bridge — it allows data from our Python backend to appear inside our HTML. It’s like filling blanks in a sentence template.”

---

### Example of Jinja in Action

If Python sends:

```python
{"quote": "Keep pushing forward!"}
```

Then in the browser, the user will see:

```html
<p class="quote">"Keep pushing forward!"</p>
```

---

## 🧩 HOW SOFTWARE ENGINEERING IS SHOWN HERE

| Concept            | How It Appears in Our Project                                              |
| ------------------ | -------------------------------------------------------------------------- |
| **Requirements**   | “Build an app that shows motivational quotes.”                             |
| **Design**         | We decided to use FastAPI for backend, HTML for frontend, CSS for styling. |
| **Implementation** | We wrote `main.py` and `index.html`.                                       |
| **Testing**        | We run the app and verify it loads new quotes correctly.                   |
| **Deployment**     | In real life, we’d push it to GitHub and deploy it on Render or Vercel.    |

> Encourage creativity: “Software engineering is about turning ideas into reality. Even a small project can evolve into something powerful when you keep improving it.”
