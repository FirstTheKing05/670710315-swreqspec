# อ่านค่าตั้งระบบจากตัวแปรสภาพแวดล้อม (CON-TECH-01)
import os

# ระบบจริงต้องใช้ PostgreSQL ตาม CON-TECH-01
# ถ้าไม่มีค่า environment ให้ใช้ค่า PostgreSQL ที่เป็นมาตรฐานของโรงพยาบาล
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/checkup",
)
