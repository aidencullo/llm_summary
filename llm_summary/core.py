import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get configuration from environment variables with defaults
MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))

def get_analysis(text: str) -> str:
    """
    Generate a summary of the input text using OpenAI's GPT-4.
    
    Args:
        text: The input text to summarize
        
    Returns:
        str: The generated summary
        
    Raises:
        Exception: If OPENAI_API_KEY is not set or API call fails
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides concise and accurate summaries."},
                {"role": "user", "content": f"Please provide a clear and concise summary of the following text:\n\n{text}"}
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Failed to generate summary: {str(e)}")
