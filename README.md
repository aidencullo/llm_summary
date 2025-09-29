# Text Analysis API

A FastAPI-based service for storing and retrieving text analyses.

## Endpoints

### 1. Analyze Text

**POST** `/analyze`

Submit new text for analysis.

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is some sample text about artificial intelligence."}' \
  -i  # Show response headers including status code
```

**Response:**
```http
HTTP/1.1 200 OK
content-type: application/json

{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "text": "This is some sample text about artificial intelligence.",
  "created_at": "2025-09-29T21:27:00.123456"
}
```
## Response Status Codes

- `200 OK`: Request was successful
- `422 Unprocessable Entity`: Invalid request format (e.g., missing required fields)
- `500 Internal Server Error`: Server encountered an error

1. Set up your OpenAI API key:
   ```bash
   # On macOS/Linux
   echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   
   # On Windows (PowerShell)
   [System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'your-api-key-here', 'User')
   ```

2. Install dependencies using `uv` (faster alternative to pip):
   ```bash
   uv pip install -e .
   ```

3. Run the server:
   ```bash
   uv run uvicorn app:app --reload
   ```


## Notes

- Data is stored in memory and will be lost when the server restarts
- CORS is enabled for all origins (`*`)
- You need a valid OpenAI API key with access to GPT-4
- Be aware of API rate limits and costs when using the OpenAI API
