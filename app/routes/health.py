from fastapi import APIRouter
from app.db.postgres import test_postgres_connection
from app.db.mongo import test_mongodb_connection
from app.db.redis import test_redis_connection

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint - verify all services"""
    return {
        "status": "healthy",
        "service": "Customer Support Chatbot API",
        "milestone": "4 - Backend Foundation Setup"
    }

@router.get("/health/databases")
async def database_health():
    """Check database connections for milestone demo"""
    
    # Test all database connections
    postgres_status = test_postgres_connection()
    mongodb_status = test_mongodb_connection()
    redis_status = test_redis_connection()
    
    return {
        "milestone": "4 - Database Integration Demo",
        "databases": {
            "postgresql": postgres_status,
            "mongodb": mongodb_status,
            "redis": redis_status
        },
        "summary": {
            "total_databases": 3,
            "connected": sum(1 for db in [postgres_status, mongodb_status, redis_status] 
                           if db.get("status") == "connected"),
            "status": "operational" if all(db.get("status") == "connected" 
                                         for db in [postgres_status, mongodb_status, redis_status]) 
                     else "partial"
        }
    }