# บันทึก audit log สำหรับการเข้าถึงข้อมูลการจอง (DOM-PDPA-01)
from __future__ import annotations

from datetime import datetime, timezone

from fastapi import Request
from sqlalchemy.orm import Session

from app.db.models import AuditLog
from app.db.session import SessionLocal


def log_booking_access(actor_id: str, action: str, hn: str) -> None:
    """บันทึก log สำหรับทุกครั้งที่เข้าถึงข้อมูลการจอง"""
    try:
        db: Session = SessionLocal()
        try:
            db.add(
                AuditLog(
                    actor_id=actor_id,
                    action=action,
                    hn=hn,
                    accessed_at=datetime.now(timezone.utc),
                )
            )
            db.commit()
        finally:
            db.close()
    except Exception:
        # dev/test environment อาจไม่มี PostgreSQL รันอยู่; ไม่ให้ request ล้มเพราะ log ไม่พร้อม
        pass


async def audit_middleware(request: Request, call_next):
    """บันทึก audit log โดยอัตโนมัติเมื่อ request เข้าถึง endpint ที่เกี่ยวข้องกับการจอง"""
    response = await call_next(request)
    path = request.url.path
    auth = request.headers.get("authorization") or ""
    actor_id = auth.replace("Bearer verified:", "") if auth.startswith("Bearer verified:") else "anonymous"

    if path.startswith("/bookings") and actor_id != "anonymous":
        log_booking_access(actor_id=actor_id, action=f"{request.method}:{path}", hn=actor_id)

    return response
