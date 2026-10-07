# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 00.00 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: ร่าง
- TC ID ที่เสนอ: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- ผลลัพธ์: ไม่เขียนโค้ด test เนื่องจากยังไม่มีแถวในตาราง test-cases.md ที่มีสถานะ "ใช้ได้" และโหมดนี้ต้องหยุดก่อน
- รายงาน: เสนอ 3 แถวสำหรับ AC-BKG-01 รวมทางปกติ / ขอบ / ทางผิด แล้วระบุให้ทีมตรวจ
- ข้อ Open Question: ส่วน "แสดงหมายเลขคิว" ยังติด Q-02 จึงเขียนว่า (รอ Q-02) และกรณี "ยังไม่ได้ยืนยันตัวตน" ยังไม่มีผลลัพธ์ที่ระบุชัดใน spec จึงให้เป็น "spec ไม่ได้บอก"
- ข้อสรุป: ตรวจแถวในตาราง แก้ได้ตามต้องการ แล้วเปลี่ยนสถานะเป็น "ใช้ได้" ก่อน จากนั้นสั่ง /testcases อีกครั้ง

---

## 2569-10-07 08:30 คำสั่ง: /verify specs/001-booking/

- โหมด: ตรวจ requirement (ไม่แก้โค้ด)
- ผล test: backend: 4 passed จาก 4; frontend: 1 passed จาก 1
- จำนวนแถวในตารางไปข้างหน้า: ครบ 3, ยังไม่ถึง 9, รอ Q-xx 1, ช่องโหว่ 2
- ข้อค้นพบใหม่: F-01, F-02, F-03, F-04, F-05, F-06
- ข้อสรุป: ระบบมีการทำงานพื้นฐานของ FR-BKG-01 และ IF-IDP-01 ที่ผ่าน test แต่ยังมี gap หลักใน FR-BKG-02, FR-BKG-03, FR-BKG-05, DOM-PDPA-01, IF-HIS-01, IF-NOT-01 และมีความเสี่ยงจาก default SQLite กับ CON-TECH-01 และการเดา Q-02 โดยไม่รอคำตอบจากทีม
- รายงานที่ยืนยัน: "ข้อค้นพบทั้งหมด AI เป็นคนตรวจ และอาจหาไม่ครบ ทีมต้องเปิดโค้ดและ spec ยืนยันทีละข้อ แล้วเขียนช่อง 'ทีมตัดสิน' เอง"

---

## 2569-10-07 09:20 คำสั่ง: /fix F-02 F-03 F-04 F-05 F-06 specs/001-booking/

- แก้เฉพาะไฟล์ที่เกี่ยวข้อง: backend/app/config.py, backend/app/db/session.py, backend/app/booking/service.py, backend/app/main.py, backend/app/audit/middleware.py, backend/app/notify/queue.py, backend/tests/test_AC_BKG_01.py
- ห้ามแก้ test ที่ขึ้นต้นด้วย test_TC_ และไม่มีการแก้ไข test_TC_* ใด ๆ
- ปรับตามข้อค้นพบ: ยกเลิกการเดาเลขคิว (Q-02 ยังไม่ตอบ), ตั้งค่า PostgreSQL เป็นค่าเริ่มต้นแต่รองรับ fallback SQLite ใน dev/test เมื่อ DB จริงไม่พร้อม, เพิ่มคิว retry สำหรับข้อความส่งซ้ำ, เพิ่ม audit log เมื่อเข้าถึงข้อมูลการจอง และทำ test AC-BKG-01 ให้ตรวจผลจริงว่า remaining ลดเป็น 0
- ผล test: `cd backend && pytest -v` -> 4 passed ใน 0.77s

---

## 2569-10-07 09:30 คำสั่ง: /question Q-03 Q-04 specs/001-booking/

- เพิ่ม Open Question ใหม่ใน spec.md: Q-03 และ Q-04
- Q-03: log ของระบบเก็บเลขบัตรประชาชนได้ไหม หรือ IF-HIS-01 ต้องครอบคลุม log ด้วย?
- Q-04: FR-BKG-01 (แสดง 30 วัน) และ FR-BKG-06 (เปลี่ยนแพ็กเกจ) ควรมีเกณฑ์ยอมรับอย่างไร?
- สถานะ: รอคำตอบจากฝ่าย IT ของโรงพยาบาลและพยาบาลคัดกรอง จนกว่าจะได้รับคำตอบ

---

## 2569-10-07 09:35 คำสั่ง: /verify specs/001-booking/

- ผล test: backend: 4 passed จาก 4; frontend: 1 passed จาก 1 (setup-only UI smoke test)
- จำนวนแถวในตารางไปข้างหน้า: ครบ 2, ยังไม่ถึง 4, รอ Q-xx 1, ช่องโหว่ 7
- ข้อค้นพบใหม่: F-01, F-02, F-03, F-04, F-05, F-06, F-07
- สรุป: จากการตรวจจริง ระบบยังไม่ “ครบ” สำหรับ requirement หลักของ booking ทั้ง FR-BKG-01, FR-BKG-02, FR-BKG-03, FR-BKG-05, DOM-PDPA-01, IF-HIS-01 และ IF-NOT-01 และยังมีความเสี่ยงจากตัวเลข 14 วัน, Q-02, และกรณี log/notification ที่ยังไม่ได้มีคำตอบจากทีม
- ข้อสรุป: "ข้อค้นพบทั้งหมด AI เป็นคนตรวจ และอาจหาไม่ครบ ทีมต้องเปิดโค้ดและ spec ยืนยันทีละข้อ แล้วเขียนช่อง 'ทีมตัดสิน' เอง"

---

## 2569-10-07 10:05 คำสั่ง: /testcases AC-BKG-02 specs/001-booking/

- โหมด: ร่าง
- TC ID ที่เสนอ: TC-BKG-02-1, TC-BKG-02-2, TC-BKG-02-3
- ผลลัพธ์: ไม่เขียนโค้ด test เนื่องจากไม่มีแถวใดใน test-cases.md ที่มีสถานะ "ใช้ได้" สำหรับ AC-BKG-02 และตามเงื่อนไขต้องหยุดในโหมดร่าง
- รายงาน: เสนอ 3 แถวสำหรับ AC-BKG-02 รวมทางปกติ / ขอบ / ทางผิด; ส่วน "แสดงหมายเลขคิวเดิม" ยังติด Q-02 จึงเขียนเป็น (รอ Q-02) และกรณี "คิวเดิมถูกใช้แล้วหรือไม่ใช่คิวที่ยังไม่ได้ใช้" ยังไม่มีคำสั่งที่ชัดเจนใน spec จึงให้เป็น "spec ไม่ได้บอก"
- ข้อสรุป: ตรวจแถวในตาราง แก้ได้ตามต้องการ แล้วเปลี่ยนสถานะเป็น "ใช้ได้" ก่อน จากนั้นสั่ง /testcases อีกครั้ง

---

## 2569-10-07 10:20 คำสั่ง: /implement T-04 specs/001-booking/tasks.md

- โหมด: ทำ task เดียวตาม tasks.md
- ไฟล์ที่แก้: backend/app/booking/service.py, backend/app/booking/router.py, backend/tests/test_AC_BKG_02.py
- รายละเอียด: เพิ่มตรวจการจองซ้ำวันเดียวกันใน `create_booking` ก่อนตัดที่นั่ง หากมี booking เดิมที่ `hn` และ `booking_date` ตรงและ `status = BOOKED` จะยก exception `DuplicateBookingError` และ router ส่ง 409 พร้อม `existing_booking_id` และ `existing_queue_no`
- Constraint ที่ทำจริง: FR-BKG-02 ถูกบังคับใน code; ไม่เก็บเลขบัตรประชาชนไม่ได้แตะ; ไม่มีการเดาเลขคิวต่อเนื่องเพราะ Q-02 ยังไม่ได้ตอบและยังคงปล่อย `queue_no` เป็น `None` จนกว่าจะได้รับคำตอบ
- ผล test: `cd /workspaces/670710315-swreqspec/backend && pytest -v` -> 5 passed, 0 failed
- สิ่งที่เกือบต้องเดา: ไม่มี เพราะมี spec ระบุชัดว่าต้องปฏิเสธเมื่อมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน และ Q-02 ยังไม่ปิดให้ใช้ `existing_queue_no` จาก booking เดิมแทนการสร้างเลขคิวใหม่
