# Bộ nhãn độc lập 20 ca lỗi · Người gắn nhãn 2 (Người 3)

- **Vai trò:** Người gắn nhãn 2, kiêm giữ hồ sơ (Nhiệm vụ C).
- **Phương pháp:** Gắn độc lập trong 8 phút theo **nguyên nhân gốc** thuộc 5 loại của Google PAIR (`Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`), không theo chỗ cần sửa.

| Ca | Nhãn độc lập (Người 3) | Lý do ngắn (nguyên nhân gốc) |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. |
| 2 | Hệ thống | Trợ lý gọi tool tra bảng giá sai tham số (hàng thường thay vì hàng nặng), hoàn thiếu 45.000 đ. |
| 3 | Ngữ cảnh | Hệ thống hoàn về ví LogiX đúng thiết kế, nhưng giả định không khớp kỳ vọng hoàn về ngân hàng của khách. |
| 4 | Giới hạn hệ thống | Hệ thống không có dữ liệu chặng do hãng nước ngoài giao nên không thể xác định trạng thái. |
| 5 | Ngầm | Hoàn thừa 14 đơn có mã giảm giá theo giá trước giảm; không khách nào báo và không cảnh báo nào kích hoạt, chỉ phát hiện khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn nhầm mục "Hoàn phí giao trễ" dù nội dung mô tả là hàng bị vỡ. |
| 7 | Hệ thống | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền nhưng trợ lý vẫn báo "đã hoàn tiền thành công" sai chính sách. |
| 8 | Hệ thống | Trợ lý bịa "Điều 7.2 chính sách hoàn phí" không tồn tại trong chính sách hiện hành (lỗi hiển thị lộ ra ngoài). |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. |
| 10 | Ngữ cảnh | Trợ lý từ chối đúng điều khoản bất khả kháng do bão, nhưng giao diện vẫn hiện "cam kết giao 24 giờ" gây xung đột nhận thức cho khách. |
| 11 | Giới hạn hệ thống | Đầu vào là tin nhắn thoại 40 giây, ngoài khả năng xử lý của trợ lý chỉ nhận văn bản. |
| 12 | Ngầm | Tool depot D05 trả thiếu trường khiến trợ lý gọi nhiều lần, đẩy tiền token D05 gấp 3 lần suốt 3 tuần mà không ai nhận ra. |
| 13 | Giới hạn hệ thống | Bảo hiểm hàng hóa của đối tác nằm ngoài phạm vi xử lý của trợ lý hoàn phí. |
| 14 | Do người dùng | Khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận khiến yêu cầu bị đóng. |
| 15 | Hệ thống | Trợ lý tính hoàn 100% trái với chính sách trễ 24–48 giờ hoàn 50%; nhân viên xem lại bắt được lỗi trước khi gửi. |
| 16 | Ngữ cảnh | Trợ lý gửi thông báo đúng thiết kế "gửi ngay khi xong" nhưng thực hiện lúc 2:14 sáng gây làm phiền khách. |
| 17 | Ngầm | Trợ lý dùng bảng giá cũ trong bộ nhớ đệm lệch 1.000–2.000 đ/đơn trên 212 đơn suốt 9 ngày mà không ai mở lại. |
| 18 | Ngữ cảnh | Trợ lý tính đúng 50% (15.000 đ) nhưng thông báo không kèm cách tính làm khách tưởng hoàn thiếu và mở lại. |
| 19 | Giới hạn hệ thống | Đơn từ 14 tháng trước vượt giới hạn truy cập dữ liệu 12 tháng của hệ thống. |
| 20 | Hệ thống | Trợ lý hoàn tiền 2 lần cho cùng một đơn do thiết kế thiếu khoá chống trùng khi khách gửi lại yêu cầu. |

## Thống kê sơ bộ của Người 3

- `Do người dùng`: 4 ca (1, 6, 9, 14)
- `Hệ thống`: 5 ca (2, 7, 8, 15, 20)
- `Ngữ cảnh`: 4 ca (3, 10, 16, 18)
- `Giới hạn hệ thống`: 4 ca (4, 11, 13, 19)
- `Ngầm`: 3 ca (5, 12, 17)
