from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

app = FastAPI(title="InspireMe App")

# Set up static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# A small collection of motivational quotes
quotes = [
    "If it is to be, it is up to me.",
    "It’s not over until I win.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Push yourself, because no one else is going to do it for you.",
    "You are capable of amazing things.",
    "If you can imagine it, you can achieve it.",
]

@app.get("/", response_class=HTMLResponse)
def get_quote(request: Request):
    # Select a random quote
    quote = random.choice(quotes)
    return templates.TemplateResponse("index.html", {"request": request, "quote": quote})
