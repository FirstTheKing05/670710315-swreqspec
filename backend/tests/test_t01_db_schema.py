from sqlalchemy import inspect

from app.db.models import AuditLog, Booking, Slot
from app.db.session import get_engine, init_db


def test_t01_creates_expected_booking_schema():
    engine = get_engine("sqlite:///:memory:")
    init_db(engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert {"slots", "bookings", "audit_logs"}.issubset(set(tables))

    slot_columns = {column["name"] for column in inspector.get_columns("slots")}
    booking_columns = {column["name"] for column in inspector.get_columns("bookings")}
    audit_columns = {column["name"] for column in inspector.get_columns("audit_logs")}

    assert {"slot_date", "start_time", "package_code", "capacity", "remaining"}.issubset(slot_columns)
    assert {"hn", "slot_id", "booking_date", "queue_no", "status"}.issubset(booking_columns)
    assert {"actor_id", "action", "hn", "accessed_at"}.issubset(audit_columns)
    assert "national_id" not in booking_columns

    assert Slot.__tablename__ == "slots"
    assert Booking.__tablename__ == "bookings"
    assert AuditLog.__tablename__ == "audit_logs"
