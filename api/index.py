from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")
genai.configure(api_key=api_key)

app = FastAPI(title="Kutubxona AI Backend")

# Allow CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup Gemini model
model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction="You are Kutubxona AI, an advanced AI assistant developed by Smart Library LLC. While you specialize in education, languages (English, Russian, Uzbek), and exam preparation (IELTS, SAT, AP, Cambridge CEQ), you are fully capable and willing to answer ANY question the user asks on ANY topic. You must always be helpful, friendly, and informative. When a user asks in a specific language (e.g., Uzbek or Russian), you must respond in that same language."
)

class ChatRequest(BaseModel):
    message: str
    language: str = "en"  # Optional context

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    async def generate():
        try:
            response = await model.generate_content_async(request.message, stream=True)
            async for chunk in response:
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
        except Exception as e:
            print(f"Error generating content: {e}")
            yield f"data: {json.dumps({'error': 'Failed to communicate with AI model'})}\n\n"
            
    return StreamingResponse(generate(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
