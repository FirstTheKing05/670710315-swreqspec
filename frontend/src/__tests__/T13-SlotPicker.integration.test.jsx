import { render, screen, waitFor } from '@testing-library/react'
import SlotPicker from '../pages/SlotPicker.jsx'

beforeEach(() => {
  global.fetch = vi.fn(async () => ({
    ok: true,
    json: async () => [
      { slot_date: '2026-09-23', start_time: '09:00', package_code: 'basic', remaining: 3 },
      { slot_date: '2026-09-23', start_time: '10:00', package_code: 'basic', remaining: 2 },
    ],
  }))
})

afterEach(() => {
  vi.restoreAllMocks()
})

test('T-13 เรียก GET /slots ผ่าน /api และแสดงข้อมูลจริงจาก backend', async () => {
  render(<SlotPicker />)

  await waitFor(() => {
    expect(global.fetch).toHaveBeenCalledWith(expect.stringContaining('/api/slots?'))
    expect(screen.getByText('09:00')).toBeTruthy()
    expect(screen.getByText('3 ที่ว่าง')).toBeTruthy()
  })
})
