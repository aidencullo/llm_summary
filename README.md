# Text Analysis API

A FastAPI-based service for storing and retrieving text analyses by topic.

## Endpoints

### 1. Analyze Text

**POST** `/analyze`

Submit new text for analysis with a topic.

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is some sample text about artificial intelligence.", "topic": "AI"}'
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "text": "This is some sample text about artificial intelligence.",
  "topic": "AI",
  "created_at": "2025-09-29T21:27:00.123456"
}
```

### 2. Search Analyses

**GET** `/search?topic=your_topic_here`

Find all analyses matching a topic (case-insensitive).

```bash
curl "http://localhost:8000/search?topic=ai"
```

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "text": "This is some sample text about artificial intelligence.",
    "topic": "AI",
    "created_at": "2025-09-29T21:27:00.123456"
  }
]
```

## Setup

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

2. Run the server:
   ```bash
   uvicorn app:app --reload
   ```

3. The API will be available at `http://localhost:8000`

## Notes

- Data is stored in memory and will be lost when the server restarts
- CORS is enabled for all origins (`*`)
