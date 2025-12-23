# Real-Time Collaborative Code Editor

A real-time collaborative code editor built with React, FastAPI, and Socket.IO.

## Features
- Live multi-user code editing
- Room-based collaboration
- WebSocket-powered real-time sync

## Tech Stack
- Frontend: React, socket.io-client
- Backend: FastAPI, python-socketio
- Real-time: WebSockets

## Getting Started

### Backend
```bash
cd server
venv\Scripts\activate
uvicorn main:socket_app --port 5000