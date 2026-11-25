# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý mà nhân viên mở gợi ý của trợ lý | số `agent_suggestion_shown` có `arm` = trợ lý, chia số `refund_request_created` có `arm` = trợ lý, tính theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm mà khách và hệ thống chưa nhận ra) | số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm, mẫu 100 đơn mỗi tuần | Không cần tính |

Cả ba số tính thử lấy từ cột thật của mẫu 1.200 yêu cầu, không dùng hai cột `_simulated`. Trong phạm vi `noi_dia` + `hang_nang` (982 yêu cầu), chỉ số chính là 92,26% và tỉ lệ mở lại là 3,97% (39/982).

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng, nên 82,83% không so được với mức nền 0,70.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, arm, staff_id, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| staff_review_decision | Nhân viên | staff_id, quyet_dinh (giu, sua, bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| staff_rework_completed | Nhân viên | staff_id, phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển cho nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng ticket |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại ticket |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (giờ gửi), `ticket_closed` (`closed_at`, đối chiếu trong 24 giờ) và `ticket_reopened` (không có bản ghi nào trong 7 ngày sau khi đóng). Nối với nhau qua `trace_id`.
- Chỉ số dùng (tỉ lệ bỏ qua gợi ý): `staff_review_decision` (đếm `sua` và `bo` chia tổng số quyết định). Chỉ số dùng nhóm đề xuất: `agent_suggestion_shown` chia `refund_request_created` theo `arm`.
- Chỉ số an toàn (lỗi lọt đến khách): `ticket_reopened` chia số `ticket_closed`. Chỉ số an toàn nhóm đề xuất: `audit_sample_checked`.
- Các luật dừng cũng cần event: luật chi phí dùng `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho cột simulated); luật an toàn có thêm `refund_ledger_write` (phát hiện ca hoàn trùng qua `idempotency_key`).
- Chưa có event nào ghi phần việc nhân viên làm thay ở các ca `handoff_to_staff`. Cần thêm trường phút xử lý vào `handoff_to_staff` hoặc `staff_rework_completed`, nếu không chi phí cả hệ thống chưa đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc thành công (simulated, B1) | Tỉ lệ làm lại theo tuần trên 7% (đợt chạy thử trong phạm vi `noi_dia` + `hang_nang`: 4,9%, 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× mức 12.000 đ; 12.414 đ = 1,03× nếu làm lại 15,3 phút/ca (simulated, B4) | Tỉ lệ yêu cầu được xem lại còn trên 50% cuối bước 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (simulated, A4) | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
