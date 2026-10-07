import { render, screen, waitFor } from '@testing-library/react'
import SlotPicker from '../pages/SlotPicker.jsx'

const { mockApi } = vi.hoisted(() => ({
  mockApi: {
    getSlots: vi.fn(async () => [
      { slot_date: '2026-09-24', start_time: '09:00', package_code: 'basic', remaining: 1 },
      { slot_date: '2026-09-24', start_time: '10:00', package_code: 'basic', remaining: 3 },
    ]),
  },
}))

vi.mock('../api/client.js', () => ({
  api: mockApi,
}))

test('T-09 แสดงช่วงเวลาว่างและจำนวนที่นั่งคงเหลือ', async () => {
  render(<SlotPicker />)

  await waitFor(() => {
    expect(screen.getByText('เลือกแพ็กเกจและช่วงเวลา')).toBeTruthy()
    expect(screen.getByText('09:00')).toBeTruthy()
    expect(screen.getByText('1 ที่ว่าง')).toBeTruthy()
    expect(mockApi.getSlots).toHaveBeenCalled()
  })
})
