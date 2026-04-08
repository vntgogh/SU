
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# API
movies = [
    {"title": "Inception", "image": "inception.png"},
    {"title": "Interstellar", "image": "interstellar.png"},
    {"title": "The Matrix", "image": "matrix.png"},
]

@app.get("/movies")
async def get_movies():
    return movies

# Page principale
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html") as f:
        return f.read()

# Servir les fichiers statiques (CSS, JS, imagesâ€¦)
app.mount("/static", StaticFiles(directory="static"), name="static")
