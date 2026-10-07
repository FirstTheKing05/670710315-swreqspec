# คิวส่งข้อความแบบ asynchronous ตาม IF-NOT-01 และ ASM-03
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


@dataclass
class RetryJob:
    booking_id: int
    hn: str
    scheduled_for: datetime
    retries: int = 0
    status: str = "queued"


RETRY_QUEUE: list[RetryJob] = []


def enqueue_retry(booking_id: int, hn: str, *, delay_seconds: int = 300) -> RetryJob:
    """เพิ่มงานส่งข้อความซ้ำไว้ในคิว; ส่งภายใน 5 นาที ตาม NFR-REL-02"""
    job = RetryJob(
        booking_id=booking_id,
        hn=hn,
        scheduled_for=datetime.now(timezone.utc) + timedelta(seconds=delay_seconds),
    )
    RETRY_QUEUE.append(job)
    return job


def get_pending_retry_jobs(now: datetime | None = None) -> list[RetryJob]:
    """คืนงานที่ยังค้างและถึงเวลาส่งซ้ำ"""
    current = now or datetime.now(timezone.utc)
    return [job for job in RETRY_QUEUE if job.status == "queued" and job.scheduled_for <= current]


def mark_retry_sent(job: RetryJob) -> None:
    """ทำเครื่องหมายว่าจัดส่งซ้ำสำเร็จแล้ว"""
    job.status = "sent"
