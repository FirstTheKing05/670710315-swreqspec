from fastapi import APIRouter, Depends, Query

from app.db.models import Slot
from app.db.session import SessionLocal, init_db
from app.slots.service import get_slots, seed_demo_slots

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/slots')
# รองรับ FR-BKG-01, FR-BKG-06
async def list_slots(
    date_from: str = Query(..., alias='date_from'),
    package_code: str | None = Query(None, alias='package_code'),
    db=Depends(get_db),
):
    init_db(db.bind)
    if db.query(Slot).count() == 0:
        seed_demo_slots(db)
    return get_slots(db, date_from=date_from, package_code=package_code)
