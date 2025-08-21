#!/usr/bin/env python3
"""
Customer Support Chatbot Backend Server
Milestone 4: Backend Foundation Setup

Run this script to start the development server:
python run_server.py
"""

import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print("🚀 Starting Customer Support Chatbot Backend")
    print(f"📍 Milestone 4: Backend Foundation Setup")
    print(f"🌐 Server: http://{settings.HOST}:{settings.PORT}")
    print(f"📚 API Docs: http://{settings.HOST}:{settings.PORT}/docs")
    print(f"🔧 Debug Mode: {settings.DEBUG}")
    print("-" * 50)
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )