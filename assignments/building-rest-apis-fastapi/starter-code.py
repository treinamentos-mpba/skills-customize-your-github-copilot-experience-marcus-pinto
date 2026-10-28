from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
]
next_book_id = 3


class BookCreate(BaseModel):
    title: str
    author: str


@app.get("/health")
def health_check():
    # TODO: Return a JSON object with the API status.
    pass


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    global next_book_id
    # TODO: Create, store, and return a book with a unique ID.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the matching book or raise HTTPException with status 404.
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
