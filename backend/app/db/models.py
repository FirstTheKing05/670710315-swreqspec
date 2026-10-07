from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import Date, ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Slot(Base):
    # รองรับ FR-BKG-01, FR-BKG-06, CON-TECH-01
    __tablename__ = 'slots'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    slot_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    start_time: Mapped[str] = mapped_column(String(5), nullable=False)
    package_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    remaining: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)

    bookings: Mapped[list['Booking']] = relationship(back_populates='slot')


class Booking(Base):
    # รองรับ FR-BKG-02, FR-BKG-04, IF-HIS-01
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    hn: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    slot_id: Mapped[int] = mapped_column(ForeignKey('slots.id'), nullable=False, index=True)
    booking_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    queue_no: Mapped[str | None] = mapped_column(String(20), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default='confirmed', nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)

    slot: Mapped['Slot'] = relationship(back_populates='bookings')


class AuditLog(Base):
    # รองรับ DOM-PDPA-01
    __tablename__ = 'audit_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    actor_id: Mapped[str] = mapped_column(String(100), nullable=False)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    hn: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    accessed_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)
