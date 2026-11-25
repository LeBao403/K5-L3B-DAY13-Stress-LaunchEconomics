# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Thanh An | 2A202603913 |       |        | Người viết code, người kiểm số |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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

## Phạm Thanh An — 2A202603913

Báo cáo cá nhân: `report/team/2A202603913_PhamThanhAn.md`.

### Phần việc phụ trách

- Nhiệm vụ A: ba hàm A1, `mo_hinh`, bảng A2, A3, A4.
- Nhiệm vụ B1 đến B3: chín kịch bản, một cặp yếu tố, ba giới hạn chạy lại.
- Mục rủi ro kinh tế trong `report/team/chi_so.md` và dòng 1, 2, 3, 7 trong `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Viết và chạy `src/lab13.py`. Ba phép thử in ĐẠT: 1,20 · 1,25 · 1,25.
- Điền A2–A4 và B1–B3 vào `report/team/bang_chi_phi.md`. Mục B4 để Người 3 điền.
- Tính tay số việc thành công và tiền token để đối chiếu với `mo_hinh` (cách tính ở báo cáo cá nhân).

### Bằng chứng

- `python lab13.py` trong `src/`: chi phí mỗi việc thành công 4.472 đ (simulated), 978 việc thành công, hoá đơn token + tool 274,7 đ/yêu cầu.
- Giới hạn rẻ nhất cho cả hệ thống là 2 lần: 6.901.220 đ (simulated).
- Chi phí cả hệ thống trên mỗi yêu cầu: 5.865 đ = 0,49× mức 12.000 đ (simulated).
