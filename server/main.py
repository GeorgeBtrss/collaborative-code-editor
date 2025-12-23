import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create Socket.IO server
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)

# Create FastAPI app
app = FastAPI()

# Enable CORS (frontend is on a different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Combine FastAPI + Socket.IO
socket_app = socketio.ASGIApp(sio, app)

@sio.event
async def connect(sid, environ):
    print("User connected:", sid)

@sio.event
async def disconnect(sid):
    print("User disconnected:", sid)

@sio.event
async def join_room(sid, room_id):
    await sio.enter_room(sid, room_id)
    print(f"{sid} joined room {room_id}")

@sio.event
async def code_change(sid, data):
    print("Code change received:", data)

    room_id = data["roomId"]
    code = data["code"]

    # Send update to everyone else in the room
    await sio.emit(
        "code_update",
        code,
        room=room_id,
        skip_sid=sid
    )

@app.get("/")
def root():
    return {"status": "backend running"}