# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Stress
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Đánh giá tính khả thi kinh tế, phân loại lỗi và thiết kế kế hoạch chạy thử nghiệm (pilot Gate 2a) cho trợ lý hoàn phí LogiX-VN từ dữ liệu mẫu 1.200 yêu cầu và 1.624 lần chạy (`logix_requests.csv`, `logix_runs.csv`). Nhóm chia 3 người phối hợp song song các phần độc lập trước khi ghép vào hồ sơ launch v0: Người 1 xây dựng mô hình chi phí (A, B1–B3, E2), Người 2 thiết kế pilot và bộ chỉ số/event (D, E1, gắn nhãn 1), Người 3 tính toán kịch bản B4, gắn nhãn độc lập 20 ca lỗi (C), lập bảng khắc phục và giữ hồ sơ tổng hợp.

## 3. Giải pháp

- **Nhiệm vụ A & B1–B3 (Mô hình chi phí & độ nhạy):** Xem `src/lab13.py` và `report/team/bang_chi_phi.md` (Người 1 hoàn thiện).
- **Nhiệm vụ B4 (Xem lại 100% phạm vi `noi_dia` + `hang_nang`):** Viết `src/nhap_nguoi3.py` tính từ dữ liệu thô trên 982 yêu cầu (900 việc thành công, 948 yêu cầu có `ok`, 48 ca `lam_lai`), đối chiếu giả định 9 phút làm lại với cột `phut_lam_lai_simulated` và tính ngưỡng xem lại hoà vốn (`report/team/bang_chi_phi.md`).
- **Nhiệm vụ C (Bảng lỗi & cách khắc phục):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (`report/team/nhan_nguoi3.md`, chờ so với `nhan_nguoi2.md`), xây dựng bảng khắc phục đo được cho 5 ca đại diện (ca 9, 7, 18, 4, 17) trong `report/team/bang_loi.md`.
- **Nhiệm vụ D & E1–E2 (Pilot plan, chỉ số & rủi ro):** Xem `report/team/pilot_plan.yaml` và `report/team/chi_so.md` (Người 2 và Người 1 hoàn thiện).
- **Nhiệm vụ E3 & duyệt chéo:** Tổng hợp tại `report/team/ho_so_launch_v0.md` và `report/team/phieu_cham.md`.

## 4. Kết quả

- **Kết quả A & B1–B3 (`bang_chi_phi.md`, `simulated`):** Chi phí mỗi việc thành công là **4.472 đ** (`simulated`, gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu; 978 việc thành công); chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (`simulated`). Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%). Giới hạn chạy lại 2 lần rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`). Phạm vi `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×) khả thi, còn `quoc_te` (22.515 đ = 1,88×, `simulated`) không đáng xử lý.
- **Kết quả B4 (`noi_dia` + `hang_nang`, `simulated`):** Chi phí mỗi việc thành công khi xem lại 100% là **11.743 đ = 0,98×** của 12.000 đ (giả định 9 phút làm lại, `simulated`); tăng lên **12.415 đ = 1,03×** theo trung bình toàn mẫu 15,30 phút/ca hoặc **12.516 đ = 1,04×** theo thực tế trong phạm vi 16,25 phút/ca (`simulated`). Ngưỡng xem lại hoà vốn là **≤ 5,12 phút/lần** (hoặc **≤ 4,80 phút/lần** với 15,30 phút làm lại, `simulated`).
- **Kết quả C (`bang_loi.md`):** Hai bộ nhãn độc lập (`nhan_nguoi2.md` của Lê Quân Bảo và `nhan_nguoi3.md` của Người 3) đạt **đồng thuận 20/20 = 100%** (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm); 5 ca khắc phục đại diện (ca 9, 7, 18, 4, 17) có đầy đủ event gắn `trace_id`, ngưỡng định lượng và chức danh phụ trách.
- **Kết quả D & E1–E2 (`pilot_plan.yaml`, `chi_so.md`):** Pilot chia theo nhân viên `20 + 20`, MDE +6 điểm (859 yêu cầu/nhóm, DE = 6,96; power ~0,64 nếu tác động thật +5 điểm), 3 luật dừng đủ 4 vế. Đợt chạy thử ghi nhận chỉ số chính **82,83%**, bỏ qua gợi ý **27,12%**, mở lại 7 ngày **4,25%** (3,97% trong phạm vi).
- **Đề xuất (`ho_so_launch_v0.md`):** **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` với 4 điều kiện có chức danh và hạn kiểm tra rõ ràng. *(Kết quả duyệt chéo Gate 2a sẽ cập nhật sau phiên 17:00.)*

## 5. Khó khăn và cách xử lý

- **Rủi ro thiên lệch từ dữ liệu giả lập:** Hai cột `phut_xem_lai_simulated` và `phut_lam_lai_simulated` là số giả lập; đặc biệt thời gian làm lại thực tế trong dữ liệu (`15,30 phút/ca` toàn mẫu, `16,25 phút/ca` trong phạm vi `noi_dia` + `hang_nang`) cao hơn mức giả định 9 phút của đề bài, làm thay đổi kết luận B4 từ 0,98× sang 1,03×–1,04×. **Cách xử lý:** Gắn nhãn `simulated` ở mọi số suy ra, báo cáo cả hai kịch bản và đưa yêu cầu đo thời gian thật sau tuần 1 vào điều kiện Go.
- **Phối hợp song song 3 thành viên tránh xung đột git:** Phân tách file sở hữu và file nháp riêng (`src/nhap_nguoi3.py`, `report/team/nhan_nguoi3.md`), giữ nguyên các mục của Người 1 và Người 2, tuân thủ `git pull --rebase` trước khi đẩy bài.
- **Hai bộ nhãn lỗi chưa hoàn toàn độc lập:** trước khi gắn nhãn, Người 2 đã nhìn thấy số ca theo từng loại trong bản nháp hồ sơ của Người 3. **Cách xử lý:** ghi rõ điều này trong `bang_loi.md` và báo cho giảng viên.
- **Dữ liệu thiếu hoặc sai định dạng khi đọc CSV:** Đọc `logix_requests.csv` với `keep_default_na=False` để ô trống ở `quyet_dinh_xem_lai` không bị chuyển thành `NaN`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện tại vẫn là dữ liệu `simulated`; cần thu thập đầy đủ sự kiện đo thật (`staff_review_decision`, `staff_rework_completed`) gắn `trace_id` trong tuần 1 của pilot.
- Cần sớm triển khai kiểm tra mẫu định kỳ (`audit_sample_checked`) để phát hiện các lỗi ngầm như sai bảng giá trong bộ nhớ đệm hoặc lỗi thừa chi phí token theo depot.
- Mẫu 1.200 yêu cầu chỉ đến từ 20 nhân viên ở 6 depot, trong khi pilot dùng cả 40 nhân viên (20 + 20) và không còn người dự phòng; nếu một người nghỉ thì chỉ còn 19 cụm ở một nhóm.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn buổi chiều Lab 13 (`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
- Tài liệu dữ liệu và công thức chuẩn (`docs/du_lieu_va_cong_thuc.md`).
- Quy định và thang chấm (`RULES.md`, `RUBRIC.md`).
