# 📖 Book API - Filtering, Searching, and Ordering

## 🔍 Filtering
You can filter books by title, author ID, or publication year.

| Parameter          | Example Usage |
|-------------------|--------------|
| `title`          | `/api/books/?title=Harry%20Potter` |
| `author`         | `/api/books/?author=1` |
| `publication_year` | `/api/books/?publication_year=2020` |

## 🔎 Searching
You can search for books by **title** or **author name**.

| Parameter  | Example Usage |
|-----------|--------------|
| `search`  | `/api/books/?search=Potter` |
| `search`  | `/api/books/?search=Rowling` |

## 📌 Ordering
You can sort books by **title** or **publication year**.

| Parameter  | Example Usage |
|-----------|--------------|
| `ordering=title` | `/api/books/?ordering=title` (A–Z) |
| `ordering=-title` | `/api/books/?ordering=-title` (Z–A) |
| `ordering=publication_year` | `/api/books/?ordering=publication_year` (Oldest to Newest) |
| `ordering=-publication_year` | `/api/books/?ordering=-publication_year` (Newest to Oldest) |

# ✅ Unit Testing for Book API

## 🔹 Running Tests
