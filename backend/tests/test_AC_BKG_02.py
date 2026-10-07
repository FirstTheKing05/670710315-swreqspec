# AC-BKG-02: ปฏิเสธการจองซ้ำวันเดียวกัน
# รองรับ FR-BKG-02
from app.db.models import Booking
from tests.conftest import AUTH


def test_AC_BKG_02_reject_duplicate_same_day_booking(client, db, make_slot):
    """Given ผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน When จองคิวใหม่ในวันเดียวกัน Then ระบบปฏิเสธและคืนคิวเดิม"""
    slot = make_slot(start="09:00", remaining=1)
    existing = Booking(
        hn="0001234",
        slot_id=slot.id,
        booking_date=slot.slot_date,
        queue_no=None,
        status="BOOKED",
    )
    db.add(existing)
    db.commit()
    db.refresh(existing)

    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    assert res.status_code == 409
    payload = res.json()["detail"]
    assert payload["existing_booking_id"] == existing.id
    assert payload["existing_queue_no"] == existing.queue_no
    assert db.query(Booking).count() == 1
    db.refresh(slot)
    assert slot.remaining == 1
