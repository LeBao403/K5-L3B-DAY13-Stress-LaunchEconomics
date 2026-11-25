# Báo cáo cá nhân — NguyenVanHau-2A202603932

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Hậu
- MSSV: 2A202603932
- Email: nguyenhau230303@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (Người 3)

## 2. Phần việc phụ trách

- **Nhiệm vụ B4 (xem lại 100% phạm vi `noi_dia` + `hang_nang`):** Viết `src/nhap_nguoi3.py` tính từ dữ liệu thô (`logix_runs.csv`, `logix_requests.csv`) và điền mục B4 trong `report/team/bang_chi_phi.md`.
- **Nhiệm vụ C (Bảng lỗi và cách khắc phục):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR tại `report/team/nhan_nguoi3.md`, đối chiếu đồng thuận với Người gắn nhãn 1 (`nhan_nguoi2.md`) và lập bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`.
- **Giữ hồ sơ & tổng hợp:** Dựng khung `TEAM.md`, `report/team/group_report.md`, điền Mục 5, đề xuất `Go có điều kiện` và kiểm tra tổng thể `report/team/ho_so_launch_v0.md`, chuẩn bị cho phiên duyệt chéo Gate 2a (`report/team/phieu_cham.md`).

## 3. Đóng góp cụ thể

- Viết `src/nhap_nguoi3.py` tính kịch bản B4 trên 982 yêu cầu (`noi_dia` + `hang_nang`), 900 việc thành công, 948 yêu cầu có `status == 'ok'`, 48 ca `lam_lai`, `224.513 đ` tiền token + tool:
  - Kịch bản chuẩn (9 phút làm lại): **11.743 đ = 0,98×** của 12.000 đ (`simulated`), mức xem lại hoà vốn **≤ 5,12 phút/lần** (`simulated`).
  - Độ nhạy theo `phut_lam_lai_simulated`: **12.415 đ = 1,03×** (TB toàn mẫu 15,30 phút/ca, hoà vốn **≤ 4,80 phút/lần**) và **12.516 đ = 1,04×** (thực tế phạm vi 16,25 phút/ca, hoà vốn **≤ 4,76 phút/lần**, `simulated`).
- Gắn nhãn độc lập 20 ca lỗi tại `report/team/nhan_nguoi3.md` (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm) và so nhãn với `nhan_nguoi2.md` (Lê Quân Bảo) đạt **đồng thuận 20/20 = 100%** trong `report/team/bang_loi.md`.
- Hoàn thiện bảng khắc phục 5 ca đại diện (ca 9, 7, 18, 4, 17) với event gắn `trace_id`, ngưỡng định lượng, tần suất theo dõi và chức danh phụ trách.
- Tổng hợp hồ sơ `report/team/ho_so_launch_v0.md` (7/7 mục, đề xuất `Go có điều kiện` kèm 4 điều kiện có chức danh và hạn kiểm tra) và `report/team/group_report.md`.

## 4. Bằng chứng

- Commit trên `main`: `7811cc8` (PR #1) và các file đã cập nhật:
  - `src/nhap_nguoi3.py`
  - `report/team/nhan_nguoi3.md`
  - `report/team/bang_chi_phi.md` (mục B4)
  - `report/team/bang_loi.md`
  - `report/team/ho_so_launch_v0.md`
  - `report/team/group_report.md`
  - `TEAM.md`

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Antigravity / Gemini) để hỗ trợ viết script `src/nhap_nguoi3.py`, rà soát công thức B4, kiểm tra đối chiếu nhãn và kiểm tra quy tắc hồ sơ.
- **Cách tự kiểm tra kết quả:**
  - Chạy trực tiếp `python src/nhap_nguoi3.py` và `cd src && python lab13.py` để xác nhận toàn bộ số liệu B4 và mô hình chi phí khớp dữ liệu thô trong `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`).
  - Kiểm tra `yaml.safe_load` cho `report/team/pilot_plan.yaml` và kiểm tra không có từ cấm theo quy tắc 5 của lab trong 6 file hồ sơ tại `report/team/`.
  - Tự đối chiếu từng ca trong 20 ca lỗi theo quy tắc nguyên nhân gốc trước khi so với `nhan_nguoi2.md`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc độc lập và phần tổng hợp của Người 3 đúng tiến độ, không làm ảnh hưởng đến file của Người 1 và Người 2.
- Đạt đồng thuận 100% (20/20) khi so nhãn độc lập và phát hiện rõ rủi ro chi phí ở kịch bản xem lại 100% khi dùng `phut_lam_lai_simulated` thực tế (1,03×–1,04×) để đưa vào điều kiện Go của hồ sơ Gate 2a.
