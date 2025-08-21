from pymongo import MongoClient
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB client
mongo_client = None
mongo_db = None

def init_mongodb():
    """Initialize MongoDB connection"""
    global mongo_client, mongo_db
    
    try:
        mongo_client = MongoClient(settings.MONGODB_URL)
        mongo_db = mongo_client[settings.MONGODB_DATABASE]
        
        # Test connection
        mongo_client.admin.command('ping')
        logger.info("✅ MongoDB connection successful")
        return True
        
    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {str(e)}")
        return False

def get_mongo_db():
    """Get MongoDB database instance"""
    if mongo_db is None:
        init_mongodb()
    return mongo_db

def test_mongodb_connection():
    """Test MongoDB connection for milestone demo"""
    try:
        if init_mongodb():
            # Get database stats
            stats = mongo_db.command("dbstats")
            return {
                "status": "connected",
                "database": "MongoDB",
                "url": settings.MONGODB_URL,
                "database_name": settings.MONGODB_DATABASE,
                "collections": mongo_db.list_collection_names()
            }
    except Exception as e:
        return {
            "status": "error",
            "database": "MongoDB",
            "error": str(e)
        }