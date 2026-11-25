# Nhãn của Người 2 · 20 ca lỗi (nhiệm vụ C)

Người gắn: Lê Quân Bảo

| Ca | Nhãn | Lý do |
| ---: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số số tài khoản. Đầu vào sai ngay từ khách, trợ lý làm đúng theo dữ liệu được nhập |
| 2 | Hệ thống | Trợ lý gọi tool với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Sai so với thiết kế và đã lộ ra vì khách mở lại sau 2 ngày |
| 3 | Ngữ cảnh | Trợ lý hoàn về ví LogiX trong 5 phút đúng thiết kế. Khách chờ tiền về ngân hàng nên thấy "chưa được hoàn", chỉ là giả định không khớp |
| 4 | Giới hạn hệ thống | LogiX không có dữ liệu chặng do hãng nước ngoài giao nên trợ lý không thể xác định, đã chuyển cho nhân viên |
| 5 | Ngầm | 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích, chỉ thấy khi kiểm tra mẫu cuối tuần |
| 6 | Do người dùng | Khách chọn mục "Hoàn phí giao trễ" nhưng mô tả hàng bị vỡ. Gốc là khách chọn sai mục, trợ lý xử lý đúng luồng đã chọn |
| 7 | Hệ thống | API sổ cái lỗi 503, trợ lý thử lại 3 lần rồi vẫn báo "đã hoàn tiền thành công". Trợ lý báo sai sự thật so với thiết kế, và lỗi này nhìn thấy được |
| 8 | Hệ thống | Trợ lý dẫn "Điều 7.2" không có trong chính sách hiện hành. Dẫn sai chính sách, sai đã lộ ra (trích dẫn nhìn thấy được) dù số tiền đúng |
| 9 | Do người dùng | Khách nhập mã đơn sàn thương mại điện tử thay vì mã vận đơn. Đầu vào sai ngay từ khách |
| 10 | Ngữ cảnh | Từ chối hoàn theo điều khoản bất khả kháng là đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ", chỉ là giả định không khớp hoàn cảnh |
| 11 | Giới hạn hệ thống | Trợ lý không xử lý được âm thanh, đầu vào thuộc loại không xử lý được và trợ lý nói rõ yêu cầu nhập chữ |
| 12 | Ngầm | Tool depot D05 thiếu một trường, kết quả vẫn đúng nhưng token gấp 3 lần suốt 3 tuần mà không ai thấy. Sai về chi phí, không lộ ra ở câu trả lời |
| 13 | Giới hạn hệ thống | Bảo hiểm hàng hoá nằm ngoài phạm vi trợ lý. Ngoài phạm vi là giới hạn, kể cả khi trợ lý trả lời chung chung |
| 14 | Do người dùng | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Gốc là thao tác sai của khách |
| 15 | Hệ thống | Đơn trễ 26 giờ, chính sách hoàn 50% nhưng trợ lý tính 100%. Sai so với chính sách, đã bị nhân viên xem lại bắt được trước khi gửi |
| 16 | Ngữ cảnh | Trợ lý gửi thông báo lúc 2:14 sáng đúng thiết kế "gửi ngay khi xong". Khách thấy bị làm phiền vì hoàn cảnh không khớp thiết kế |
| 17 | Ngầm | Bảng giá đổi từ 01/11 nhưng bộ nhớ đệm vẫn dùng bản cũ, lệch 212 đơn trong 9 ngày mà không ai mở lại. Không ai nhận ra |
| 18 | Ngữ cảnh | Số tiền hoàn 15.000 đ đúng chính sách (30.000 đ × 50%). Khách mở lại vì tin nhắn không kèm cách tính, chỉ là giả định khách hiểu cách tính |
| 19 | Giới hạn hệ thống | Đơn từ 14 tháng trước nhưng trợ lý chỉ truy cập được 12 tháng dữ liệu. Thiếu dữ liệu, trợ lý đã nói rõ và chuyển nhân viên |
| 20 | Hệ thống | Hoàn hai lần cho cùng một đơn vì lệnh thứ hai thiếu khoá chống trùng. Lỗi so với thiết kế |

Tổng: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3.
