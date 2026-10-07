import SlotPicker from './pages/SlotPicker.jsx'

// แสดงหน้าจอ T-09 ใน App.jsx ตาม task สร้างหน้าเลือกแพ็กเกจและช่วงเวลา
export default function App() {
  return (
    <main className="min-h-screen bg-slate-100 p-6">
      <div className="mx-auto max-w-6xl">
        <header className="mb-6 text-center">
          <h1 className="text-3xl font-bold text-teal-800">ระบบจองคิวตรวจสุขภาพ</h1>
        </header>
        <SlotPicker />
      </div>
    </main>
  )
}
