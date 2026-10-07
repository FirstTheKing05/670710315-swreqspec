# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from tests.conftest import AUTH


def test_AC_BKG_01(client, make_slot, db):
    """AC-BKG-01: บันทึกสำเร็จ และห้องว่างลดลงถึง 0"""
    slot = make_slot(start="09:00", remaining=1)

    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    assert res.status_code == 201
    assert res.json()["booking_id"] is not None
    assert res.json()["queue_no"] is None
    db.refresh(slot)
    assert slot.remaining == 0
