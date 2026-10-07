from __future__ import annotations

from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Slot


def seed_demo_slots(db: Session) -> None:
    today = date.today()
    sample_slots = [
        (today, '09:00', 'basic', 5, 5),
        (today, '10:00', 'basic', 4, 4),
        (today, '09:00', 'full', 3, 3),
        (today + timedelta(days=1), '11:00', 'basic', 2, 2),
    ]

    for slot_date, start_time, package_code, capacity, remaining in sample_slots:
        existing = db.execute(
            select(Slot).where(
                Slot.slot_date == slot_date,
                Slot.start_time == start_time,
                Slot.package_code == package_code,
            )
        ).scalar_one_or_none()
        if existing is None:
            db.add(
                Slot(
                    slot_date=slot_date,
                    start_time=start_time,
                    package_code=package_code,
                    capacity=capacity,
                    remaining=remaining,
                )
            )

    db.commit()


def get_slots(db: Session, date_from: str, package_code: str | None = None):
    from_date = date.fromisoformat(date_from)
    query = select(Slot).where(Slot.slot_date >= from_date)
    if package_code:
        query = query.where(Slot.package_code == package_code)
    query = query.order_by(Slot.slot_date.asc(), Slot.start_time.asc())

    rows = db.execute(query).scalars().all()
    return [
        {
            'slot_date': row.slot_date.isoformat() if hasattr(row.slot_date, 'isoformat') else str(row.slot_date),
            'start_time': row.start_time,
            'package_code': row.package_code,
            'capacity': row.capacity,
            'remaining': row.remaining,
        }
        for row in rows
    ]
