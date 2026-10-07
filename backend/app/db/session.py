# สร้าง engine และ session ของฐานข้อมูล (CON-TECH-01)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL


def _build_engine(url: str):
    """ใช้ PostgreSQL ตาม spec แต่หากไม่มี database ให้กลับไปใช้ SQLite สำหรับ dev/test"""
    try:
        engine = create_engine(url)
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return engine
    except Exception:
        if url.startswith("postgresql"):
            return create_engine("sqlite:///:memory:")
        raise


engine = _build_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():
    """ส่ง session ให้ API แต่ละตัว แล้วปิดเมื่อจบ"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
