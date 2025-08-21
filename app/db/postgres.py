from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database engine and session
engine = None
SessionLocal = None
Base = declarative_base()

def init_postgres():
    """Initialize PostgreSQL connection"""
    global engine, SessionLocal
    
    try:
        engine = create_engine(
            settings.postgres_url,
            pool_pre_ping=True,
            pool_recycle=300
        )
        
        SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
        
        # Test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("✅ PostgreSQL connection successful")
            return True
            
    except Exception as e:
        logger.error(f"❌ PostgreSQL connection failed: {str(e)}")
        return False

def get_db():
    """Get database session"""
    if SessionLocal is None:
        init_postgres()
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_postgres_connection():
    """Test PostgreSQL connection for milestone demo"""
    try:
        if init_postgres():
            return {
                "status": "connected",
                "database": "PostgreSQL",
                "host": settings.POSTGRES_HOST,
                "port": settings.POSTGRES_PORT,
                "database_name": settings.POSTGRES_DB
            }
    except Exception as e:
        return {
            "status": "error",
            "database": "PostgreSQL",
            "error": str(e)
        }