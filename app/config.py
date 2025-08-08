import os
from dotenv import load_dotenv

load_dotenv()

# Load the Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")