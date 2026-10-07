# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:30 | test: 5 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ครบ |
| FR-BKG-02 | AC-BKG-02 | T-04 | ไม่พบโค้ดที่ตรวจกันจองซ้ำวันเดียวกัน | ไม่มี test ในโค้ด | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่พบโค้ดที่แจ้ง "ช่วงเวลาเต็ม" และเสนอ 3 ช่วงใกล้เคียง | ไม่มี test ในโค้ด | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/router.py: create_booking; backend/app/booking/service.py: create_booking, next_queue_no | backend/tests/test_AC_BKG_01.py: PASSED แต่ assert อ่อน | รอ Q-xx |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่พบคิวส่งข้อความซ้ำหรือการจัดการส่งซ้ำ | ไม่มี test ในโค้ด | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-10 | backend/app/slots/router.py: get_slots; backend/app/slots/service.py: list_available_slots (กรองตาม package_code) | ไม่มี test ที่ตรวจการเปลี่ยนแพ็กเกจเป็นการทดสอบ AC อย่างเป็นทางการ | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: PASSED | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี HTTPS/TLS หรือการเข้ารหัสในโค้ด | ไม่มี test | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มีคิวส่งซ้ำภายใน 5 นาที | ไม่มี test | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มีเกณฑ์เวลา/อาสาสมัคร 10 คน หรือ test ของ UX | ไม่มี test | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL default เป็น sqlite:///./dev.db | backend/tests/test_T01_schema.py ใช้ SQLite ในหน่วยความจำ | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | backend/app/db/models.py: AuditLog มีตาราง แต่ไม่มี middleware/record ที่เรียกจริงทุกครั้งที่เข้าถึงข้อมูล | ไม่มี test ของ audit log | ยังไม่ถึง |
| IF-IDP-01 | AC-BKG-01 | T-03 | backend/app/auth/idp.py: get_verified_hn | backend/tests/test_AC_BKG_01.py: PASSED ผ่าน Authentication header | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/db/models.py: Booking เก็บเฉพาะ hn; ไม่มี HIS client/lookup หรือการค้น HN จริง | ไม่มี test | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มีคิวส่งข้อความแบบ async หรือการส่งซ้ำภายใต้ ASM-03 | ไม่มี test | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: get_slots | FR-BKG-01 | ใช่ | คืนรายการ slot ที่ยังมีที่นั่งและกรอง package_code; ดำเนินการตรงตาม requirement อย่างพื้นฐาน |
| backend/app/booking/router.py: create_booking | FR-BKG-04, IF-IDP-01 | บางส่วน | บันทึกการจองและตรวจ Authorization ได้ แต่คำตอบยังผูกกับ `A001` โดยไม่รอคำตอบ Q-02 และไม่มีการแสดงผลบนหน้าจอจริง |
| backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | ไม่ | สร้างหมายเลขคิวแบบ `A001` โดยเดาเอง แม้ spec ระบุว่า Q-02 ยังไม่มีคำตอบ และต้องถามเจ้าหน้าที่เวชระเบียน |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ไม่ | ค่าเริ่มต้นเป็น SQLite ซึ่งไม่ตรงกับข้อบังคับ "ใช้ PostgreSQL ตามมาตรฐาน" หากไม่มี env var ตั้งค่า |
| backend/app/db/models.py: Booking, AuditLog | IF-HIS-01, DOM-PDPA-01 | บางส่วน | เก็บเฉพาะ `hn` ที่ถูกต้อง แต่ไม่มีการค้น HIS จริง และไม่มี log middleware ที่บันทึกทุกการเข้าถึง |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ใช่ | ตรวจ header เป็นแบบจำลองยืนยันตัวตนตาม spec ได้ชัดเจน |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | FR ไม่มี AC | spec.md, tasks.md | FR-BKG-06 | มี requirement ที่ต้องคำนวณช่วงว่างใหม่ตามแพ็กเกจแต่ไม่มี AC ที่ตรวจชัดเจน และ task T-10 ก็ไม่มี AC ให้ตรวจ | เพิ่ม Q-xx |
| F-02 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | FR-BKG-04, Q-02 | โค้ดออกหมายเลขคิวแบบ `A001` โดยไม่รอคำตอบจากเจ้าหน้าที่เวชระเบียน จึงเป็นการตัดสินใจแทนทีม | เพิ่ม Q-xx |
| F-03 | ละเมิด Constraint | backend/app/config.py: DATABASE_URL | CON-TECH-01 | ค่าเริ่มต้นเป็น SQLite แม้ spec บังคับ PostgreSQL และเป็นมาตรฐานของโรงพยาบาล | แก้โค้ด |
| F-04 | โค้ดไม่มี FR | backend/app/ | FR-BKG-05, IF-NOT-01, NFR-REL-02 | ไม่มีคิวส่งข้อความซ้ำ ไม่มี retry ภายใน 5 นาที และไม่มีการบันทึกงานส่งซ้ำแบบ ASM-03 | แก้โค้ด |
| F-05 | โค้ดไม่มี FR | backend/app/ | DOM-PDPA-01 | มีตาราง audit_logs แต่ไม่มี middleware หรือ endpoint ที่บันทึก audit log ทุกครั้งที่เข้าถึงข้อมูลการจอง | แก้โค้ด |
| F-06 | test อ่อน | backend/tests/test_AC_BKG_01.py | AC-BKG-01 | test ตรวจเพียง status_code 201 เท่านั้น ไม่ตรวจว่าการจองถูกบันทึกจริง remaining เป็น 0 และมีการแสดงหมายเลขคิวตาม AC | แก้ test |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | - | ยังไม่มีข้อค้นพบที่สามารถระบุว่าแก้แล้วได้จากการตรวจนี้ |
