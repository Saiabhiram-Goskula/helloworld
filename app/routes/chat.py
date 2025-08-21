from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

router = APIRouter()

# Request/Response Models
class ChatRequest(BaseModel):
    user_id: str
    query: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    user_id: str
    query: str
    intent: str
    sentiment: str
    response: str
    session_id: str
    timestamp: datetime
    milestone_note: str

@router.post("/ask", response_model=ChatResponse)
async def chat_ask(request: ChatRequest):
    """
    Main chat endpoint - Milestone 4 Demo
    
    This is a dummy implementation to demonstrate the backend foundation.
    In future milestones, this will integrate:
    - Intent classification
    - Sentiment analysis
    - Google Gemini API
    - Case memory retrieval
    """
    
    # Generate session ID if not provided
    session_id = request.session_id or str(uuid.uuid4())
    
    # Dummy intent classification (will be replaced with ML model)
    intent = classify_intent_dummy(request.query)
    
    # Dummy sentiment analysis (will be replaced with ML model)
    sentiment = analyze_sentiment_dummy(request.query)
    
    # Dummy response generation (will be replaced with Gemini API)
    response = generate_response_dummy(request.query, intent)
    
    return ChatResponse(
        user_id=request.user_id,
        query=request.query,
        intent=intent,
        sentiment=sentiment,
        response=response,
        session_id=session_id,
        timestamp=datetime.now(),
        milestone_note="Milestone 4: Backend foundation with dummy responses"
    )

def classify_intent_dummy(query: str) -> str:
    """Dummy intent classifier - will be replaced with ML model"""
    query_lower = query.lower()
    
    if any(word in query_lower for word in ["atm", "card", "blocked", "pin", "account"]):
        return "banking"
    elif any(word in query_lower for word in ["bill", "payment", "charge", "refund"]):
        return "billing"
    elif any(word in query_lower for word in ["password", "login", "access", "forgot"]):
        return "account_access"
    elif any(word in query_lower for word in ["order", "delivery", "shipping", "product"]):
        return "order_support"
    else:
        return "general"

def analyze_sentiment_dummy(query: str) -> str:
    """Dummy sentiment analyzer - will be replaced with ML model"""
    query_lower = query.lower()
    
    negative_words = ["angry", "frustrated", "terrible", "awful", "hate", "worst"]
    positive_words = ["great", "excellent", "love", "amazing", "perfect", "wonderful"]
    
    if any(word in query_lower for word in negative_words):
        return "negative"
    elif any(word in query_lower for word in positive_words):
        return "positive"
    else:
        return "neutral"

def generate_response_dummy(query: str, intent: str) -> str:
    """Dummy response generator - will be replaced with Gemini API"""
    
    responses = {
        "banking": "I understand you're having issues with your banking services. Let me help you resolve this. For security reasons, I'll need to verify your account details first.",
        "billing": "I can help you with billing inquiries. Let me check your account and recent transactions to provide accurate information.",
        "account_access": "I'll assist you with account access issues. For security, I'll guide you through the proper verification process.",
        "order_support": "I'm here to help with your order. Let me check the status and provide you with detailed information.",
        "general": "Thank you for contacting our support. I'm here to help you with any questions or concerns you may have."
    }
    
    return responses.get(intent, "I'm here to help you. Could you please provide more details about your inquiry?")

@router.get("/demo")
async def demo_endpoint():
    """Demo endpoint to show API structure for milestone presentation"""
    return {
        "milestone": "4 - Backend Foundation Demo",
        "endpoints": {
            "POST /api/chat/ask": "Main chat endpoint with dummy AI responses",
            "GET /api/chat/demo": "This demo endpoint",
            "GET /api/health": "Service health check",
            "GET /api/health/databases": "Database connection status"
        },
        "features_implemented": [
            "FastAPI backend structure",
            "Database connections (PostgreSQL, MongoDB, Redis)",
            "Request/Response validation with Pydantic",
            "CORS configuration for frontend integration",
            "Dummy AI services (intent, sentiment, response generation)"
        ],
        "next_milestones": [
            "Integrate Google Gemini API",
            "Implement real ML models for intent/sentiment",
            "Add case memory and context tracking",
            "Build frontend React application"
        ]
    }