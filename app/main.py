from fastapi import FastAPI
from pydantic import BaseModel
from app.core import get_chat_response
from fastapi.middleware.cors import CORSMiddleware # NEW IMPORT

# Initialize the FastAPI application
app = FastAPI(
    title="Eco-Anxiety AI Counselor",
    description="An API for the AI-powered eco-anxiety counseling chatbot.",
    version="1.0.0"
)

# --- NEW: Set up CORS Middleware ---
origins = [
    "http://localhost:3000", # The origin of our React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)
# --- END of CORS section ---


# --- SAFETY LAYER (No changes here) ---
EMERGENCY_KEYWORDS = [
    "suicide", "kill myself", "hopeless", "can't go on",
    "end my life", "self-harm", "panic attack", "i want to die"
]
EMERGENCY_RESPONSE = (
    "It sounds like you are going through a lot right now. "
    "It's important to talk to a person who can support you. "
    "Please reach out to a crisis hotline or mental health professional. "
    "You can connect with people who can support you by calling or texting 988 anytime in the US and Canada. In the UK, you can call 111."
)

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Eco-Anxiety AI Counselor API"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    user_query_lower = request.query.lower()
    if any(keyword in user_query_lower for keyword in EMERGENCY_KEYWORDS):
        return {"response": EMERGENCY_RESPONSE}
    response = get_chat_response(request.query)
    return {"response": response}