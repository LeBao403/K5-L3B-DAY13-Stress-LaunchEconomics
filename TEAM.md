# Team

## Thông tin nhóm

- Tên nhóm: Stress
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Stress-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/LeBao403/K5-L3B-DAY13-Stress-LaunchEconomics · nhánh `main` · (điền commit chốt khi hoàn tất)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Thanh An       | 2A202603913     | 26ai.anpt3@vinuni.edu.vn      | thanhanbk02       | Người viết code, người kiểm số (Người 1) |
|   2 | Lê Quân Bảo | 2A202603888 | 26ai.baolq2@vinuni.edu.vn      | LeBao403 | Người gắn nhãn 1 (Người 2) |
|   3 | Nguyễn Văn Hậu | 2A202603932 | 26ai.haunv@vinuni.edu.vn | common-maker | Người gắn nhãn 2, kiêm giữ hồ sơ (Người 3) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Người 1 (HoVaTen-MSSV)

### Phần việc phụ trách

- Nhiệm vụ A (mô hình chi phí), B1 đến B3, E2 (rủi ro kinh tế), mục 1, 2, 3, 7 trong `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- (Người 1 điền sau khi hoàn thành)

### Bằng chứng

- (Người 1 điền sau khi hoàn thành)

## Người 2 (Lê Quân Bảo - 2A202603888)

### Phần việc phụ trách

- Nhiệm vụ D (`pilot_plan.yaml`), E1 (`chi_so.md`), gắn nhãn độc lập 20 ca lỗi, mục 4, 6 trong `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Viết `src/nhap_nguoi2.py` (cỡ mẫu hai tỉ lệ, hệ số thiết kế, cỡ mẫu hiệu dụng khi chia theo cụm, power) và đưa khối D1 vào `src/lab13.py`; điền `report/team/pilot_plan.yaml` (chia theo nhân viên 20 + 20, mức chênh 6 điểm, 3 luật dừng); tính ba chỉ số E1 và liệt kê 10 event có `trace_id` trong `report/team/chi_so.md`; gắn nhãn 20 ca lỗi trong `report/team/nhan_nguoi2.md`; điền dòng 4 và 6 của hồ sơ launch v0.

### Bằng chứng

- Commit `790cd1e`; file `src/nhap_nguoi2.py`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md` (mục E1), `report/team/nhan_nguoi2.md`, `report/team/2A202603888_LeQuanBao.md`.

## Người 3 (NguyenVanHau-2A202603932)

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: Nhiệm vụ B4 (tính từ dữ liệu thô), Nhiệm vụ C (gắn nhãn độc lập 20 ca lỗi và bảng khắc phục 5 ca), dựng khung và tổng hợp `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md`, `TEAM.md`.

### Đóng góp cụ thể

- Viết `src/nhap_nguoi3.py` tính chi phí kịch bản xem lại 100% phạm vi `noi_dia` + `hang_nang` (982 yêu cầu, 900 việc thành công) và độ nhạy theo `phut_lam_lai_simulated`, điền mục B4 trong `report/team/bang_chi_phi.md`.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR tại `report/team/nhan_nguoi3.md`; lập bảng khắc phục 5 ca đại diện (ca 9, 7, 18, 4, 17) với cách phát hiện đo được và chức danh phụ trách trong `report/team/bang_loi.md`.
- Dựng khung `TEAM.md`, `report/team/group_report.md`, điền mục 5 và khung đề xuất `Go có điều kiện` trong `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- File code nháp: `src/nhap_nguoi3.py`
- File nhãn độc lập: `report/team/nhan_nguoi3.md`
- Hồ sơ đã cập nhật: `report/team/bang_chi_phi.md` (mục B4), `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`.
