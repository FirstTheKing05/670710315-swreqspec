# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 09:35 | test: 4 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | backend/app/booking/service.py: create_booking (ไม่มีการปฏิเสธเมื่อมีคิวเดิมในวันเดียวกัน) | ไม่มี test ในโค้ด | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่พบโค้ดที่แจ้ง "ช่วงเวลาเต็ม" และเสนอ 3 ช่วงใกล้เคียง | ไม่มี test ในโค้ด | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/router.py: create_booking; backend/app/booking/service.py: create_booking | backend/tests/test_AC_BKG_01.py: PASSED แต่ยังไม่ตรวจหมายเลขคิวตาม AC และยังคงมี Q-02 ที่ยังไม่ได้ตอบ | รอ Q-xx |
| FR-BKG-05 | AC-BKG-04 | T-07 | backend/app/booking/service.py: create_booking; backend/app/notify/queue.py: enqueue_retry | ไม่มี test ที่ตรวจฉบับจริงว่าการจองยังถูกบันทึกและมีงานส่งซ้ำภายใน 5 นาที | ช่องโหว่ |
| FR-BKG-06 | ไม่มี AC | T-10 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots (กรอง package_code) | ไม่มี test ที่ตรวจการเปลี่ยนแพ็กเกจเป็นการทดสอบ AC อย่างเป็นทางการ | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี HTTPS/TLS หรือการเข้ารหัสในโค้ด | ไม่มี test | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | backend/app/notify/queue.py: enqueue_retry, get_pending_retry_jobs | ไม่มี test ที่ตรวจเวลา 5 นาทีและจำนวน retry | ช่องโหว่ |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มีเกณฑ์เวลา/อาสาสมัคร 10 คน หรือ test ของ UX | ไม่มี test | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL; backend/app/db/session.py: _build_engine | backend/tests/test_T01_schema.py ใช้ SQLite ในหน่วยความจำ | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | backend/app/audit/middleware.py: audit_middleware; backend/app/db/models.py: AuditLog | ไม่มี test ของ audit log จริง | ช่องโหว่ |
| IF-IDP-01 | AC-BKG-01 | T-03 | backend/app/auth/idp.py: get_verified_hn | backend/tests/test_AC_BKG_01.py: PASSED ผ่าน Authorization header | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/db/models.py: Booking เก็บเฉพาะ hn; ไม่มี client หรือ lookup HIS จริง | ไม่มี test | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | backend/app/notify/queue.py: enqueue_retry | ไม่มี test ที่ตรวจส่งข้อความแบบ async และไม่มี retry ตาม ASM-03 ที่ความจริง | ช่องโหว่ |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: get_slots | FR-BKG-01 | บางส่วน | คืนรายการช่วงเวลาว่างและ filter ตาม package_code แต่ตัวเลข 14 วันยังไม่ตรงกับ "ภายใน 30 วันข้างหน้า" ตาม FR-BKG-01 |
| backend/app/booking/router.py: create_booking | FR-BKG-04, IF-IDP-01 | บางส่วน | ใช้ Authorization header ตรวจตัวตนแล้ว แต่ยังไม่ได้แสดงหมายเลขคิวที่เป็นจริงและยังไม่มีการบังคับเรื่อง Q-02 |
| backend/app/booking/service.py: create_booking | FR-BKG-04, FR-BKG-02 | บางส่วน | ตัดที่นั่งและบันทึกได้ แต่ไม่ตรวจว่ามีคิวในวันเดียวกันยังไม่ได้ใช้ หรือปฏิเสธการจองซ้ำตาม FR-BKG-02 |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ไม่ | ค่าจาก env เกิด default เป็น PostgreSQL แต่โค้ด fallback แบบ SQLite ใน dev/test จึงไม่ใช่ "ใช้ PostgreSQL ตลอด" ตาม constraint |
| backend/app/audit/middleware.py: audit_middleware | DOM-PDPA-01 | บางส่วน | มี middleware แต่ยังไม่ได้พิสูจน์ว่า log ถูกเก็บทุก access และไม่มีข้อกำหนดว่าต้องปกป้องเลขบัตรประชาชนใน log |
| backend/app/notify/queue.py: enqueue_retry | IF-NOT-01, NFR-REL-02 | บางส่วน | มีคิว retry แต่ยังไม่มีการตรวจว่าส่งซ้ำทุก 5 นาทีและจำกัด 3 ครั้งตาม ASM-03 |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | FR ไม่มี AC | spec.md, tasks.md | FR-BKG-06 | ยังไม่มี AC ที่ตรวจว่าต้องแสดงช่วงเวลาว่างใหม่เมื่อเปลี่ยนแพ็กเกจ และ task ที่เกี่ยวข้องยังไม่ได้ตรวจจริง | เพิ่ม Q-xx |
| F-02 | เดา Q-xx | backend/app/booking/service.py: create_booking | FR-BKG-04, Q-02 | โค้ดยังไม่มีการกำหนดรูปแบบเวลาและเลขคิวอย่างเป็นทางการ จึงยังไม่สามารถยืนยันว่าการแสดงเลขคิวตรงตาม spec | เพิ่ม Q-xx |
| F-03 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | โค้ดกำหนดแสดง 14 วัน แต่ spec ระบุภายใน 30 วันข้างหน้า จึงผิดกับ requirement | แก้โค้ด |
| F-04 | ละเมิด Constraint | backend/app/db/session.py: _build_engine | CON-TECH-01 | มี fallback SQLite ใน dev/test จึงไม่ยืนยันว่าระบบใช้ PostgreSQL แบบบังคับตลอดไป | แก้โค้ด |
| F-05 | โค้ดไม่มี FR | backend/app/notify/queue.py; backend/app/booking/service.py | FR-BKG-05, IF-NOT-01, NFR-REL-02 | ยังไม่มีการจัดการ retry ที่ครบตาม ASM-03 เช่น ส่งซ้ำสูงสุด 3 ครั้ง และรอ 5 นาที อย่างเป็นทางการ | แก้โค้ด |
| F-06 | โค้ดไม่มี FR | backend/app/audit/middleware.py | DOM-PDPA-01 | ยังไม่มีหลักฐานว่ามี log สำหรับทุกการเข้าถึงข้อมูลสุขภาพ และยังไม่มีความชัดเจนว่าต้องไม่เก็บเลขบัตรประชาชนใน log | แก้โค้ด |
| F-07 | test อ่อน | backend/tests/test_AC_BKG_01.py | AC-BKG-01 | test ตรวจเพียง status 201 และไม่มี assert ของหมายเลขคิว/remaining ตาม Then จริง ๆ | แก้ test |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | - | ยังไม่มีข้อค้นพบที่ผ่านการยืนยันแล้วว่าจะแก้แล้วต่อเนื่องจากรอบนี้ |
