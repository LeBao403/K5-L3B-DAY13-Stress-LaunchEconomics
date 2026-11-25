# Báo cáo cá nhân — Phạm Thanh An — 2A202603913

## 1. Thông tin thành viên

- Họ tên: Phạm Thanh An
- MSSV: 2A202603913
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code, người kiểm số

## 2. Phần việc phụ trách

- Nhiệm vụ A: ba hàm A1, hàm `mo_hinh`, bảng A2, A3, A4.
- Nhiệm vụ B1 đến B3: độ nhạy từng yếu tố, một cặp yếu tố, giới hạn 1, 2, 3 lần chạy.
- Mục E2 rủi ro kinh tế trong `chi_so.md`.
- Dòng 1, 2, 3, 7 trong `ho_so_launch_v0.md`. Cả bốn dòng trạng thái Giả lập.

## 3. Đóng góp cụ thể

- Viết `src/lab13.py`: `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `mo_hinh`, rồi gọi lại cho từng loại yêu cầu, chi phí cố định và các kịch bản B1–B3.
- Điền số vào `report/team/bang_chi_phi.md` (trừ mục B4).
- Điền ba dòng rủi ro và bốn dòng hồ sơ thuộc Người 1.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, mục E2 của `report/team/chi_so.md`, dòng 1, 2, 3, 7 của `report/team/ho_so_launch_v0.md`.
- `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- Chi phí mỗi việc thành công 4.472 đ (simulated), gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu. Làm lại chiếm 51,8% (simulated).
- Ba yếu tố nhạy nhất: số ca làm lại +51,8%, tỉ lệ xem lại +40,7%, lương nhân viên +23,1%.
- Giới hạn 2 lần rẻ nhất cho công ty: chi phí cả hệ thống 6.901.220 đ (simulated).

Số tính tay để đối chiếu, không lấy từ bảng đã điền:

- Đếm cột `ket_qua` của 1.200 dòng trong `logix_requests.csv`: `thanh_cong` 978, `chuyen_nhan_vien` 148, `lam_lai` 74. Tổng 978 + 148 + 74 = 1.200. Mẫu số của `mo_hinh` cũng là 978.
- Cộng token trên 1.624 lần chạy trong `logix_runs.csv`: `tokens_in` = 5.771.712, `tokens_out` = 734.774. Tiền token = 5.771.712 / 1.000 × 26 + 734.774 / 1.000 × 130 = 245.585,132 đ, làm tròn 245.585 đ. Khớp dòng token của bảng A2.
- 5.600 lần gọi tool × 15 đ = 84.000 đ. Khớp dòng tool của bảng A2.

## 5. Công cụ AI đã dùng

Dùng Cursor (trợ lý trong editor) để viết các hàm trong `src/lab13.py`, chạy `python lab13.py`, và điền bảng A, B1–B3 cùng mục rủi ro và bốn dòng hồ sơ.

Tự kiểm tra: ba phép thử A1 phải in ĐẠT trước khi dùng số phía sau. Đối chiếu tiền token và số việc thành công bằng phép đếm và phép cộng ở mục 4, tách khỏi hàm `mo_hinh`. Mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" (5,6% và 2,8%; 40,7% và 20,3%; 51,8% và 25,9%).

## 6. Tự đánh giá

Phần A và B1–B3 chạy ra số và đã điền bảng. Mục B4, chỉ số E1, event và dòng 4, 5, 6 của hồ sơ thuộc Người 2 và Người 3.

Câu hội đồng có thể hỏi: tử số cộng token, tool, xem lại và làm lại trên mọi lần chạy, kể cả lần lỗi, vì những lần đó vẫn tốn tiền. Mẫu số chỉ đếm `ket_qua == thanh_cong` (978), nên chi phí của lần hỏng được gánh lên mỗi việc làm xong. Vì vậy 4.472 đ/việc thành công khác với chi phí cả hệ thống 5.865 đ/yêu cầu: số sau cộng thêm 222 yêu cầu không thành công × 12.000 đ rồi chia cho 1.200.
