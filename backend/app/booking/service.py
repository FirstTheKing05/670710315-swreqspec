# บันทึกการจองและตัดที่นั่ง (T-03)
# รองรับ FR-BKG-04
from sqlalchemy.orm import Session

from app.db.models import Booking, Slot
from app.notify.queue import enqueue_retry


class SlotFullError(Exception):
    """ช่วงเวลาที่เลือกไม่มีที่นั่งเหลือแล้ว"""


def next_queue_no(db: Session, slot_date) -> str | None:
    """รอคำตอบ Q-02: ยังไม่มีการกำหนดรูปแบบเลขคิวอย่างเป็นทางการ จึงไม่เดา"""
    return None


def create_booking(db: Session, hn: str, slot_id: int) -> Booking:
    """ยืนยันการจอง: ตรวจที่นั่ง ตัดที่นั่ง บันทึกการจอง และวางงานส่งซ้ำหากส่งข้อความไม่สำเร็จ (FR-BKG-04, FR-BKG-05)"""
    slot = db.get(Slot, slot_id)
    if slot is None:
        raise ValueError("ไม่พบช่วงเวลา")
    if slot.remaining < 0:
        raise SlotFullError(slot_id)

    slot.remaining -= 1
    booking = Booking(
        hn=hn,
        slot_id=slot.id,
        booking_date=slot.slot_date,
        queue_no=next_queue_no(db, slot.slot_date),
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)

    enqueue_retry(booking.id, hn, delay_seconds=300)
    return booking

