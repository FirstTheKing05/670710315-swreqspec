# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:35 | test: 5 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ครบ |
| FR-BKG-02 | AC-BKG-02 | T-04 | backend/app/booking/service.py: create_booking; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_02.py: PASSED | ครบ |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มี implementation ใน backend/app/ และ frontend/src/ ที่แสดง "ช่วงเวลาเต็ม" พร้อม 3 ตัวเลือก | ไม่มี test ที่ผ่านในโค้ดจริง | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/router.py: create_booking; backend/app/booking/service.py: create_booking | backend/tests/test_AC_BKG_01.py: PASSED | รอ Q-xx |
| FR-BKG-05 | AC-BKG-04 | T-07 | backend/app/booking/service.py: create_booking; backend/app/notify/queue.py: enqueue_retry | ไม่มี test ที่ตรวจว่ามีคิวส่งซ้ำและส่งภายใน 5 นาที | ช่องโหว่ |
| FR-BKG-06 | ไม่มี AC | T-10 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots | frontend/src/__tests__/setup.test.jsx: PASSED แต่ไม่ใช่ AC; ไม่มี test สำหรับเปลี่ยนแพ็กเกจจริง | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี TLS/HTTPS หรือการเข้ารหัสในโค้ด | ไม่มี test | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | backend/app/notify/queue.py: enqueue_retry, get_pending_retry_jobs | ไม่มี test ที่ตรวจจำนวน retry และเวลา 5 นาที | ช่องโหว่ |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี UX flow ที่วัดค่า 3 นาที หรือ 8/10 คน | ไม่มี test | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL; backend/app/db/session.py: _build_engine | backend/tests/test_T01_schema.py: PASSED แต่ใช้ SQLite fallback ใน dev/test | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | backend/app/db/models.py: AuditLog; backend/app/audit/middleware.py | ไม่มี test ของ audit log จริง | ช่องโหว่ |
| IF-IDP-01 | AC-BKG-01 | T-03 | backend/app/auth/idp.py: get_verified_hn | backend/tests/test_AC_BKG_01.py: PASSED | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/db/models.py: Booking เก็บเฉพาะ hn; ไม่มี client HIS จริง | ไม่มี test | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | backend/app/notify/queue.py: enqueue_retry | ไม่มี test ที่ตรวจการส่ง asynchronous และ retry ตาม ASM-03 | ช่องโหว่ |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/booking/router.py: create_booking | FR-BKG-02, FR-BKG-04, IF-IDP-01 | ใช่ | ปฏิเสธซ้ำวันเดียวกันและตรวจ Authorization header ตาม spec ได้ |
| backend/app/booking/service.py: create_booking | FR-BKG-02, FR-BKG-04 | ใช่ | มีป้องกัน duplicate same-day และตัดที่นั่ง แต่ queue_no ยังเป็น `None` เพราะรอ Q-02 |
| backend/app/slots/service.py: list_available_slots | FR-BKG-01 | บางส่วน | คืนช่วงเวลาว่างแบบ 14 วัน และ filter package_code แต่ไม่ถึง 30 วัน ตาม requirement |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ไม่ | ค่าเริ่มต้นเป็น PostgreSQL แต่มี fallback SQLite ใน dev/test จึงยังละเมิดเงื่อนไข "ใช้ PostgreSQL ตามมาตรฐาน" แม้รัน test ผ่าน |
| backend/app/notify/queue.py: enqueue_retry | IF-NOT-01, NFR-REL-02 | บางส่วน | มีคิว retry แต่ยังไม่มีการส่งซ้ำจริงตาม 5 นาที / 3 ครั้ง และยังไม่มี test ที่พิสูจน์ |
| frontend/src/App.jsx | FR-BKG-01, FR-BKG-06 | ไม่ | โครงหน้าเริ่มต้นเท่านั้น ยังไม่มีหน้าจอเลือกแพ็กเกจหรือช่วงเวลาอย่างเป็นจริง |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | คำสั่งนี้ยังเก็บ `queue_no = None` เพราะยังไม่มีคำตอบว่าเลขคิวจะเริ่มที่เท่าไรหรือรีเซ็ตวันไหน | เพิ่ม Q-xx |
| F-02 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | Spec ระบุภายใน 30 วันข้างหน้า แต่โค้ดกำหนด 14 วัน | แก้โค้ด |
| F-03 | ละเมิด Constraint | backend/app/db/session.py: _build_engine | CON-TECH-01 | มี fallback SQLite ใน dev/test ทำให้ระบบอาจไม่ใช้ PostgreSQL ตามมาตรฐานโรงพยาบาลอย่างต่อเนื่อง | แก้โค้ด |
| F-04 | โค้ดไม่มี FR | backend/app/notify/queue.py; backend/app/booking/service.py | FR-BKG-05, IF-NOT-01, NFR-REL-02 | ยังไม่มีการคืนกลับหรือยืนยันว่า retry ส่งซ้ำสูงสุด 3 ครั้ง ภายใน 5 นาที ตาม ASM-03 | แก้โค้ด |
| F-05 | FR ไม่มี AC | spec.md, tasks.md | FR-BKG-06 | FR บอกว่าเปลี่ยนแพ็กเกจต้องคำนวณช่วงว่างใหม่ แต่ไม่มี AC ที่กำหนดเกณฑ์ยอมรับชัดเจน | เพิ่ม Q-xx |
| F-06 | โค้ดไม่มี FR | backend/app/audit/middleware.py; backend/app/db/models.py | DOM-PDPA-01 | ยังไม่มี audit middleware ที่พิสูจน์ว่า log ถูกบันทึกทุกการเข้าถึงและมี actor_id, accessed_at, hn อย่างจริง | แก้โค้ด |
| F-07 | AC ไม่มี test | backend/tests | AC-BKG-06 | มี AC แต่ไม่มี test ที่ตรวจ audit log จริง | แก้ test |
| F-08 | test อ่อน | backend/tests/test_AC_BKG_01.py | AC-BKG-01 | test ยังไม่ตรวจว่า queue_no เป็นค่าที่ถูกต้องและยังไม่ได้ตรวจว่าจองจริงตาม AC ทั้งฉบับ | แก้ test |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| F-02 | เพิ่มการปฏิเสธการจองซ้ำวันเดียวกันใน backend/app/booking/service.py และ backend/app/booking/router.py | รู้ได้จาก backend/tests/test_AC_BKG_02.py: PASSED และ `cd backend && pytest -v` ผล 5 passed |
