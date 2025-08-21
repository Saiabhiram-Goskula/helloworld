# Customer Support Chatbot Backend

## 🎯 Milestone 4: Backend Foundation Setup

This is the backend API for a Customer Support Chatbot with Case Memory using Google Gemini AI.

### 🏗️ Architecture Overview

```
Frontend (React) → Backend API (FastAPI) → AI Services (Gemini)
                                        → Databases (PostgreSQL, MongoDB, Redis)
```

### 📁 Project Structure

```
app/
├── __init__.py
├── main.py              # FastAPI application entry point
├── core/
│   ├── __init__.py
│   └── config.py        # Application settings and configuration
├── db/
│   ├── __init__.py
│   ├── postgres.py      # PostgreSQL connection and models
│   ├── mongo.py         # MongoDB connection for case memory
│   └── redis.py         # Redis connection for caching
├── routes/
│   ├── __init__.py
│   ├── health.py        # Health check endpoints
│   └── chat.py          # Main chat API endpoints
└── services/
    ├── __init__.py
    └── gemini.py        # Google Gemini AI integration (placeholder)
```

### 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Run Development Server**
   ```bash
   python run_server.py
   ```

4. **Access API Documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### 🔗 API Endpoints

#### Core Endpoints
- `GET /` - Backend status check
- `GET /api/health` - Service health check
- `GET /api/health/databases` - Database connection status

#### Chat Endpoints
- `POST /api/chat/ask` - Main chat endpoint (with dummy AI responses)
- `GET /api/chat/demo` - Demo endpoint showing API structure

### 🗄️ Database Setup

#### PostgreSQL (Structured Data)
- Users, tickets, SLA tracking, FAQs
- Connection: `app/db/postgres.py`

#### MongoDB (Unstructured Data)
- Case memory, chat logs, embeddings
- Connection: `app/db/mongo.py`

#### Redis (Caching)
- Session management, frequent queries
- Connection: `app/db/redis.py`

### 🤖 AI Integration (Placeholder)

Currently using dummy responses for:
- Intent classification
- Sentiment analysis
- Response generation

**Next Milestone**: Replace with actual Google Gemini API integration.

### 📊 Milestone 4 Deliverables

✅ **Environment Setup**
- FastAPI backend with proper structure
- Virtual environment with all dependencies
- Configuration management with Pydantic

✅ **Server Configuration**
- Uvicorn ASGI server
- CORS middleware for frontend integration
- Proper routing and error handling

✅ **Database Integration**
- PostgreSQL connection setup
- MongoDB connection setup
- Redis connection setup
- Health check endpoints for all databases

✅ **API Foundation**
- RESTful API structure
- Request/Response validation
- Dummy chat endpoint with realistic flow

✅ **Demo Ready**
- Working `/api/chat/ask` endpoint
- Database connection verification
- Comprehensive API documentation

### 🔄 Example API Usage

```bash
# Test backend status
curl http://localhost:8000/

# Check database connections
curl http://localhost:8000/api/health/databases

# Send chat message (dummy response)
curl -X POST http://localhost:8000/api/chat/ask \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "query": "Why is my ATM card blocked?"
  }'
```

### 📈 Next Milestones

- **Milestone 5**: Google Gemini API integration
- **Milestone 6**: Real ML models for intent/sentiment
- **Milestone 7**: Case memory and context tracking
- **Milestone 8**: Frontend React application
- **Milestone 9**: Production deployment

### 🛠️ Development Notes

This is a foundation setup demonstrating:
- Clean architecture with separation of concerns
- Async/await patterns for scalability
- Proper error handling and logging
- Database abstraction layers
- API documentation and testing endpoints

Perfect for mentor review and milestone demonstration! 🎯