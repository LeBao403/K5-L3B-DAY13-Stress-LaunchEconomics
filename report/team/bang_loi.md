# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: (chờ Người 2 từ `nhan_nguoi2.md`) · Người gắn nhãn 2: Người 3 (`nhan_nguoi3.md`) (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | Do người dùng | ... | ... |
| 2 | ... | Hệ thống | ... | ... |
| 3 | ... | Ngữ cảnh | ... | ... |
| 4 | ... | Giới hạn hệ thống | ... | ... |
| 5 | ... | Ngầm | ... | ... |
| 6 | ... | Do người dùng | ... | ... |
| 7 | ... | Hệ thống | ... | ... |
| 8 | ... | Hệ thống | ... | ... |
| 9 | ... | Do người dùng | ... | ... |
| 10 | ... | Ngữ cảnh | ... | ... |
| 11 | ... | Giới hạn hệ thống | ... | ... |
| 12 | ... | Ngầm | ... | ... |
| 13 | ... | Giới hạn hệ thống | ... | ... |
| 14 | ... | Do người dùng | ... | ... |
| 15 | ... | Hệ thống | ... | ... |
| 16 | ... | Ngữ cảnh | ... | ... |
| 17 | ... | Ngầm | ... | ... |
| 18 | ... | Ngữ cảnh | ... | ... |
| 19 | ... | Giới hạn hệ thống | ... | ... |
| 20 | ... | Hệ thống | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...% (chờ đối chiếu với bộ nhãn độc lập của Người 2)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại. (Cập nhật sau khi so nhãn với Người 2; lưu ý phân biệt theo nguyên nhân gốc cho các ca dễ lẫn: ca 6, 9 gốc do người dùng nhập/chọn sai chứ không phải lỗi hệ thống; ca 13 ngoài phạm vi nên là giới hạn hệ thống; ca 8, 15 lỗi đã lộ ra nên là hệ thống chứ không phải ngầm; ca 18 là ngữ cảnh do thiếu giải thích cách tính; ca 12 là ngầm vì tốn token gấp 3 lần nhiều tuần không ai thấy.)

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo hằng ngày khi tỉ lệ vượt quá **2%** tổng yêu cầu | Tự động nhận diện mã đơn sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn nhập đúng mã kèm ảnh ví dụ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng giờ giữa event `agent_run_completed` và `refund_ledger_write` theo `trace_id`: tin nhắn báo "đã hoàn" nhưng không có bản ghi sổ cái `ok`; ngưỡng cảnh báo **≥ 1 ca** (mục tiêu **0 ca**) | Chỉ cho phép gửi thông báo "đã hoàn" khi sổ cái trả `ok`; sau 3 lần lỗi 503 thì trả trạng thái "đang xử lý" và kích hoạt `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` có lý do thắc mắc số tiền nhưng kiểm tra sổ cái đúng chính sách; ngưỡng cảnh báo **> 1%** số yêu cầu đã đóng | Chuẩn hoá mẫu tin nhắn hoàn tiền luôn kèm công thức tính cụ thể (ví dụ: 30.000 đ × 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` theo `loai` và `trace_id`, tổng hợp hằng tuần; ngưỡng cảnh báo khi tỉ lệ chuyển tiếp **> 15%** trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt ngữ cảnh; loại nhóm `quoc_te` khỏi phạm vi pilot do thiếu dữ liệu hãng nước ngoài | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` gắn `trace_id` kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; ngưỡng cảnh báo khi **> 1%** đơn lệch giá | Vô hiệu hoá/xoá bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi bắt buộc `pricing_version` vào mọi trace | Kế toán trưởng |
