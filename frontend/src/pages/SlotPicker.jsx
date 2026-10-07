import { useEffect, useMemo, useState } from 'react'
import { api } from '../api/client.js'

// รองรับ FR-BKG-01, FR-BKG-06, CON-TECH-01
export default function SlotPicker() {
  const [packageCode, setPackageCode] = useState('basic')
  const [slots, setSlots] = useState([])
  const [loading, setLoading] = useState(true)

  const packageOptions = useMemo(
    () => [
      { code: 'basic', label: 'แพ็กเกจพื้นฐาน' },
      { code: 'full', label: 'แพ็กเกจเต็มรูปแบบ' },
    ],
    [],
  )

  useEffect(() => {
    let cancelled = false

    async function loadSlots() {
      setLoading(true)
      try {
        const payload = await api.getSlots({
          dateFrom: new Date().toISOString().slice(0, 10),
          packageCode,
        })

        const slotList = Array.isArray(payload) ? payload : payload.slots ?? []
        if (!cancelled) setSlots(slotList)
      } catch (error) {
        if (!cancelled) setSlots([])
      } finally {
        if (!cancelled) setLoading(false)
      }
    }

    loadSlots()
    return () => {
      cancelled = true
    }
  }, [packageCode])

  return (
    <section className="mx-auto max-w-4xl rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="mb-6 flex items-center justify-between gap-4">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-teal-700">Booking</p>
          <h2 className="mt-1 text-2xl font-bold text-slate-900">เลือกแพ็กเกจและช่วงเวลา</h2>
        </div>
      </div>

      <div className="mb-6">
        <p className="mb-2 text-sm font-medium text-slate-700">แพ็กเกจ</p>
        <div className="flex flex-wrap gap-3">
          {packageOptions.map((option) => {
            const active = option.code === packageCode
            return (
              <button
                key={option.code}
                type="button"
                onClick={() => setPackageCode(option.code)}
                className={[
                  'rounded-full border px-4 py-2 text-sm font-medium transition',
                  active
                    ? 'border-teal-600 bg-teal-600 text-white shadow-sm'
                    : 'border-slate-300 bg-white text-slate-700 hover:border-teal-500 hover:text-teal-700',
                ].join(' ')}
              >
                {option.label}
              </button>
            )
          })}
        </div>
      </div>

      <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
        {loading ? (
          <div className="rounded-xl border border-dashed border-slate-300 bg-slate-50 p-4 text-slate-500">
            กำลังโหลดช่วงเวลา...
          </div>
        ) : slots.length > 0 ? (
          slots.map((slot) => (
            <button
              key={`${slot.slot_date}-${slot.start_time}`}
              type="button"
              className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-left transition hover:border-teal-500 hover:bg-teal-50"
            >
              <div className="flex items-center justify-between gap-3">
                <p className="text-lg font-semibold text-slate-900">{slot.start_time}</p>
                <span className="rounded-full bg-emerald-100 px-2 py-1 text-xs font-semibold text-emerald-700">
                  {slot.remaining} ที่ว่าง
                </span>
              </div>
              <p className="mt-2 text-sm text-slate-600">{slot.slot_date}</p>
              <p className="mt-1 text-sm text-slate-500">แพ็กเกจ {slot.package_code}</p>
            </button>
          ))
        ) : (
          <div className="rounded-xl border border-dashed border-slate-300 bg-slate-50 p-4 text-slate-500">
            ไม่พบช่วงเวลาว่างในช่วงวันที่เลือก
          </div>
        )}
      </div>
    </section>
  )
}
