# uvicorn main:app
# uvicorn main:app --reload

# main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom function imports
from functions.database import store_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response


# Initiate our application
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:5174",
    "http://localhost:3000",
]

# CORS - Middleware

app.add_middleware (
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = {"*"}
    
)

# Check Health
@app.get("/health")
async def check_health():
    return {"message": "Hello From EastAfrica Uganda"}

# Get Audio
@app.get("/post-audio-get/")
async def get_audio():
    print('you uploaded file')
    
    # Get Saved audio
    audio_input = open("emiru.mp3", "rb")
    
    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)
    
    # Guard to ensure message has decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to Decode Message")
    
    #Get Chat Response
    chat_response = get_chat_response(message_decoded)
    
    # Store Chat Response
    store_messages(message_decoded, chat_response)
    
    #print(chat_response)
    
    return "Conversion Completed"


# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print('you uploaded file')
