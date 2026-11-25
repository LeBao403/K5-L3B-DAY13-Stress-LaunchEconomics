# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Stress · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | ... | ... | ... |
| 2 · Ba yếu tố nhạy nhất | ... | ... | ... |
| 3 · So với nhân viên tự làm | ... | ... | ... |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | ... | ... | ... |
| 5 · Bảng lỗi và cách khắc phục | 20 ca phân theo 5 loại PAIR (Do người dùng: 4, Hệ thống: 5, Ngữ cảnh: 4, Giới hạn hệ thống: 4, Ngầm: 3 — chờ đối chiếu nhãn Người 2); 5 ca khắc phục đo được (ca 9, 7, 18, 4, 17) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | ... | ... | ... |
| 7 · Rủi ro kinh tế | ... | ... | ... |

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (khung dự thảo của Người giữ hồ sơ; đối chiếu lại sau khi Người 1 và Người 2 điền đủ số mục 1–4, 6–7). Các con số bất lợi cần kiểm soát: xem lại 100% tốn 11.743 đ = 0,98× của 12.000 đ với 9 phút làm lại, hoặc 12.415 đ = 1,03× (TB toàn mẫu 15,30 phút/ca) và 12.516 đ = 1,04× (16,25 phút/ca thực tế phạm vi) [simulated]; loại `quoc_te` đắt hơn nhân viên tự làm nên loại khỏi pilot; power chỉ khoảng 0,64 nếu tác động thật +5 điểm khi thiết kế MDE +6 điểm; tỉ lệ mở lại 7 ngày hiện tại là 4,25% toàn mẫu (3,97% trong phạm vi).

- Điều kiện 1 (lỗi hệ thống nghiêm trọng): Vá khoá chống trùng lệnh hoàn và đối soát API sổ cái trước khi bật pilot (ca 7, 20) — **Kỹ sư trưởng agent** — kiểm tra trước `2027-01-05`.
- Điều kiện 2 (cỡ mẫu & đánh đổi power): Ký duyệt phương án 20 + 20 nhân viên, MDE +6 điểm (chấp nhận power ~0,64 nếu tác động thật +5 điểm) — **Giám đốc vận hành LogiX-VN** — kiểm tra trước `2027-01-05`.
- Điều kiện 3 (đo lường thật): Bật đủ tối thiểu 6 event có `trace_id`, thay thời gian `_simulated` bằng thời gian đo thật sau tuần 1 — **PM trợ lý hoàn phí** — kiểm tra `2027-01-12`.
- Điều kiện 4 (giảm xem lại có kiểm soát): Áp dụng lộ trình giảm tỉ lệ xem lại theo bậc và rút thời gian xem lại xuống ≤ 4,80 phút/lần [simulated] vì xem lại 100% không tiết kiệm chi phí (B4) — **Trưởng nhóm CSKH** — kiểm tra `2027-01-12`.
