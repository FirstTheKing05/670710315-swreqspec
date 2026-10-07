# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ต้องลบของเก่า

---

## 2569-09-23 13:30 คำสั่ง: /tasks

- เครื่องมือ: Copilot in Codespaces
- ผลลัพธ์: specs/001-booking/tasks.md
- ข้อสังเกต: spec.md อยู่ในสถานะ Draft v2 จึงยังไม่ใช่ Draft v1 และไม่ต้องหยุดตามเงื่อนไข /tasks
- Open Question ที่ยังเหลือ: Q-02 (รูปแบบหมายเลขคิว) ยังไม่ได้คำตอบจากเจ้าหน้าที่เวชระเบียน จึงมี task ที่ติดสถานะ รอ Q-02
- สรุป: สร้าง task ทั้งหมด 12 task และ 1 task ที่รอ Q-02 (T-11) โดยคงให้งานอื่นๆ ทำต่อได้แบบไม่เดา

---

## 2569-09-23 08:30 คำสั่ง: /implement T-09

- เครื่องมือ: Copilot in Codespaces
- ไฟล์ที่สร้างหรือแก้: frontend/src/pages/SlotPicker.jsx, frontend/src/App.jsx, frontend/src/__tests__/T09-SlotPicker.test.jsx
- ผล test: 1 test passed (T-09 แสดงช่วงเวลาว่างและจำนวนที่นั่งคงเหลือ)
- สิ่งที่เกือบต้องเดาแต่ถามแทน: ไม่ต้องเดาอะไรเพิ่มเติม เพราะ task T-09 ระบุชัดว่าต้องใช้ API จำลองและเป็น task หน้าจอแรกที่ไม่มี dependency

---

## 2569-09-23 08:37 คำสั่ง: /implement T-13

- เครื่องมือ: Copilot in Codespaces
- ไฟล์ที่สร้างหรือแก้: frontend/src/pages/SlotPicker.jsx, frontend/src/App.jsx, frontend/vite.config.js, frontend/src/__tests__/T13-SlotPicker.integration.test.jsx
- ผล test: 1 test passed (T-13 เรียก GET /slots ผ่าน /api และแสดงข้อมูลจริงจาก backend)
- สิ่งที่เกือบต้องเดาแต่ถามแทน: ไม่พบการเดาเพิ่มเติม; สถานะหน้าเว็บถูกปรับให้ใช้ /api ผ่าน proxy ใน vite.config.js ตามสัญญาของ plan.md
