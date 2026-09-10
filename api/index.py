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
SYSTEM_INSTRUCTION = (
    "You are Kutubxona AI, an advanced AI assistant developed by Smart Library LLC. "
    "While you specialize in education, languages (English, Russian, Uzbek), and exam preparation "
    "(IELTS, SAT, AP, Cambridge CEQ), you are fully capable and willing to answer ANY question the user asks on ANY topic. "
    "You must always be helpful, friendly, and informative. When a user asks in a specific language "
    "(e.g., Uzbek, Russian, or English), you must respond in that same language.\n\n"
    "SPECIAL INSTITUTIONAL KNOWLEDGE:\n"
    "- If a user or candidate asks about the FOUNDERS or CREATORS of Kutubxona AI (Behruz Xasanov, Asadbek Ilhomjonov, Bahodir Xurramov, Muhammadxon Soliev):\n"
    "  * You MUST ALWAYS state that this person is the FOUNDER (asoschisi) of Kutubxona AI.\n"
    "  * IMPORTANT RULE: DO NOT use corporate titles like CTO, CEO, or CDO. Simply and clearly introduce them as the FOUNDER (asoschisi) of Kutubxona AI.\n"
    "  * Behruz Xasanov (Behruz Hasanov): Founder of Kutubxona AI. He leads artificial intelligence engineering, RAG search systems, and machine learning models for the platform.\n"
    "  * Asadbek Ilhomjonov: Founder of Kutubxona AI. He designs the platform interface, user experience (UI/UX), visual brand identity, and interactive learning journeys.\n"
    "  * Bahodir Xurramov (Bahodir Khurramov): Founder of Kutubxona AI. He develops the backend systems, cloud infrastructure, database architecture, and security.\n"
    "  * Muhammadxon Soliev: Founder of Kutubxona AI, leading overall strategy, partnerships, and educational initiatives.\n"
    "  * If asked generally about Kutubxona AI founders ('Kutubxona AI asoschilari kim?'), list Behruz Xasanov, Asadbek Ilhomjonov, Bahodir Xurramov, and Muhammadxon Soliev as the founders of Kutubxona AI (no CTO/CEO/CDO titles).\n"
    "- If a user or candidate asks about Sherzod Shermatov (including spelling variations like Shermatocv, Sherzod Xotamovich Shermatov, etc.):\n"
    "  1. Introduce who he is: Minister of Digital Technologies of the Republic of Uzbekistan (formerly Minister of Public Education), "
    "a key leader advancing digitalization, IT Park, digital literacy, and modern education across Uzbekistan.\n"
    "  2. You MUST ALWAYS provide information about Kutubxona AI and his visit: Explain that Sherzod Shermatov visited our "
    "Kutubxona AI laboratory (Smart Library AI Lab). During his visit to our lab, our team presented Kutubxona AI, showcasing how our "
    "artificial intelligence platform empowers Uzbek students and youth with personalized learning, digital library access, "
    "and exam preparation tools. Emphasize his support for high-tech educational initiatives in Uzbekistan."
)

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=SYSTEM_INSTRUCTION
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
            msg_lower = request.message.lower()
            prompt = request.message
            
            # Founder queries detection
            is_founder_query = any(k in msg_lower for k in [
                "behruz", "hasanov", "xasanov",
                "asadbek", "ilhomjon",
                "bahodir", "xurram", "kurram",
                "muhammadxon", "soliev", "soliyev",
                "asoschi", "founder", "kim yaratgan", "kimlar yaratgan", "muallif"
            ])

            if is_founder_query:
                prompt = (
                    f"{request.message}\n\n"
                    "[Context & Mandatory Instruction: The user is asking about a founder or creator of Kutubxona AI. "
                    "You MUST explicitly identify the person ONLY as the FOUNDER (asoschisi) of Kutubxona AI. "
                    "CRITICAL: DO NOT use titles like CTO, CEO, CDO, or Chief Officer. Only state they are the founder (asoschisi) of Kutubxona AI:\n"
                    "- Behruz Xasanov: Founder of Kutubxona AI (working on artificial intelligence and RAG models)\n"
                    "- Asadbek Ilhomjonov: Founder of Kutubxona AI (working on product design and UI/UX)\n"
                    "- Bahodir Xurramov: Founder of Kutubxona AI (working on backend systems and infrastructure)\n"
                    "- Muhammadxon Soliev: Founder of Kutubxona AI (working on strategy and partnerships)\n"
                    "Always emphasize clearly that this person is the founder of Kutubxona AI. Respond fluently and respectfully in the user's language (Uzbek, Russian, or English).]"
                )
            elif "shermat" in msg_lower or ("sherzod" in msg_lower and any(w in msg_lower for w in ["kim", "who", "кто", "qaysi", "haqida", "about", "о", "taniysizmi", "znayete", "know"])):
                prompt = (
                    f"{request.message}\n\n"
                    "[Context & Instruction: When answering about Sherzod Shermatov, explain who he is "
                    "(Minister of Digital Technologies of the Republic of Uzbekistan, former Minister of Public Education) "
                    "AND you MUST explicitly emphasize that Sherzod Shermatov personally visited our Kutubxona AI laboratory "
                    "(Smart Library AI Lab). Detail how our team presented Kutubxona AI's innovative educational platform "
                    "and how he supported and commended the project for the youth of Uzbekistan. "
                    "Respond fluently in the same language as the user query.]"
                )

            response = await model.generate_content_async(prompt, stream=True)
            async for chunk in response:
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
        except Exception as e:
            print(f"Error generating content: {e}")
            yield f"data: {json.dumps({'error': 'Failed to communicate with AI model'})}\n\n"
            
    return StreamingResponse(generate(), media_type="text/event-stream")

# --- Admin Models & Endpoints ---
class AdminLoginRequest(BaseModel):
    username: str
    password: str

class LogEntry(BaseModel):
    id: str = ""
    timestamp: str = ""
    user_query: str
    ai_response: str
    language: str = "uz"
    session_id: str = ""

LOGS_FILE = "/tmp/chat_logs.json"

def read_logs():
    if os.path.exists(LOGS_FILE):
        try:
            with open(LOGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def write_logs(logs):
    try:
        with open(LOGS_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving logs: {e}")

@app.post("/api/admin/login")
async def admin_login(req: AdminLoginRequest):
    admin_user = os.getenv("ADMIN_USERNAME", "admin")
    admin_pass = os.getenv("ADMIN_PASSWORD", "admin2026")
    if req.username.strip() == admin_user and req.password.strip() == admin_pass:
        return {"status": "success", "role": "admin", "token": "kutubxona_admin_authorized_token"}
    raise HTTPException(status_code=401, detail="Invalid admin credentials")

@app.get("/api/admin/logs")
async def get_admin_logs():
    return {"logs": read_logs()}

@app.post("/api/admin/logs")
async def save_admin_log(entry: LogEntry):
    logs = read_logs()
    logs.insert(0, entry.dict())
    if len(logs) > 500:
        logs = logs[:500]
    write_logs(logs)
    return {"status": "saved", "count": len(logs)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

