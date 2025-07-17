# Custom Backend for Phronetic AI Agent

This repository contains the source code for a Flask-based RESTful backend service built as part of the Phronetic AI Task 2 and Task 3 requirements.

It supports:
- Note CRUD operations with database persistence
- Weather API integration
- Simple API key authentication
- Logging and error handling

---

## Deployment

This backend is live and hosted on [Render](https://render.com/).

**Base URL:**  
```
https://phronetic-ai.onrender.com/notes
```

---

## Features

### CRUD for Notes

- `POST /notes` – Create a note  
- `GET /notes` – Retrieve all notes  
- `GET /notes/<note_id>` – Retrieve a single note  
- `PUT /notes/<note_id>` – Update a note  
- `DELETE /notes/<note_id>` – Delete a note  


### Auth (Simple API Key)

Pass this header with each request:

```http
Authorization: Bearer testkey
```

---

## 🛠️ Setup Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Percussor-hash/phronetic-ai.git
cd phronetic-ai
```

### 2. Create Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the App Locally
```bash
python app.py
```

Backend runs by default at:  
```
http://127.0.0.1:5000
```

---

## Database

- Uses **SQLite** for simplicity.
- A `notes.db` file will be created automatically on first run.

---

## API Usage Examples

### Create a Note
```bash
curl -X POST http://localhost:5000/notes \
  -H "Authorization: Bearer testkey" \
  -H "Content-Type: application/json" \
  -d '{"title": "Demo", "content": "This is a test note."}'
```


## Logging

All requests and errors are logged to `app.log`

---

## Environment Variables


```env
API_KEY=testkey
```

---

##  Used In: Phronetic AI Agent

This backend is integrated into a Phronetic AI agent with the following tools:

1. **Notes Tool** – CRUD functionality (via this backend)
---


