import redis
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Redis client
redis_client = None

def init_redis():
    """Initialize Redis connection"""
    global redis_client
    
    try:
        redis_client = redis.from_url(
            settings.redis_url,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_timeout=5
        )
        
        # Test connection
        redis_client.ping()
        logger.info("✅ Redis connection successful")
        return True
        
    except Exception as e:
        logger.error(f"❌ Redis connection failed: {str(e)}")
        return False

def get_redis():
    """Get Redis client instance"""
    if redis_client is None:
        init_redis()
    return redis_client

def test_redis_connection():
    """Test Redis connection for milestone demo"""
    try:
        if init_redis():
            info = redis_client.info()
            return {
                "status": "connected",
                "database": "Redis",
                "host": settings.REDIS_HOST,
                "port": settings.REDIS_PORT,
                "version": info.get("redis_version", "unknown")
            }
    except Exception as e:
        return {
            "status": "error",
            "database": "Redis",
            "error": str(e)
        }