# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (4.472 / 274,7).
- Khoản lớn nhất là làm lại: 2.264.000 đ, chiếm 51,8% tổng chi phí (simulated). Xem lại đứng thứ hai, 40,7% (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 (simulated) | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 (simulated) | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 (simulated) | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 (simulated) | 0,85× |

- `quoc_te` không đáng để trợ lý xử lý: 22.515 đ/việc thành công = 1,88× mức 12.000 đ, tỉ lệ thành công chỉ 27,3% (simulated).
- Chạy lại tới 3 lần không giúp loại này: tỉ lệ `ok` lần 1 là 30,0%, lần 2 còn 11,4%, lần 3 còn 2,2%.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 (simulated) | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 (simulated) | 0,48× |

- Ở 45.000 yêu cầu/tháng, cộng 1.185 đ cố định vẫn còn 4.599 đ = 0,38× mức 12.000 đ, kết luận không đổi (simulated).
- Một nửa khối lượng thì cố định thành 2.370 đ/việc, tổng 5.784 đ = 0,48×, vẫn rẻ hơn nhân viên tự làm nhưng đắt hơn rõ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ/việc thành công, +46,3% so với 4.472 đ (simulated). Bằng 5,6% + 40,7% vì mô hình cộng từng khoản.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn 2 lần rẻ nhất cho công ty: chi phí cả hệ thống 6.901.220 đ (simulated). Không trùng với giới hạn làm chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ).
- Giới hạn 1 lần đẩy thêm 85 yêu cầu sang nhân viên (319 so với 234), nên cả hệ thống đắt hơn dù chi phí mỗi việc thành công thấp hơn.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 948/982 yêu cầu chạy `ok` (xem lại 5 phút = 9.480.000 đ `simulated`), 48 ca `lam_lai` (9 phút = 864.000 đ `simulated`) và 224.513 đ token + tool chia cho 900 việc thành công, chi phí đạt **11.743 đ = 0,98×** của 12.000 đ (`simulated`). Nếu tính theo `phut_lam_lai_simulated` (TB toàn mẫu 15,30 phút/ca → **12.415 đ = 1,03×**; thực tế trong phạm vi 16,25 phút/ca → **12.516 đ = 1,04×**, `simulated`), xem lại 100% đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% triệt tiêu lợi thế chi phí do tiền xem lại chiếm tới ~90% tổng chi phí (`simulated`), và mức xem lại hoà vốn chỉ là **≤ 5,12 phút/lần** (với 9 phút làm lại) hoặc **≤ 4,80 phút/lần** (với 15,30 phút làm lại, `simulated`). Pilot phải đo thời gian xem lại thật và kiểm chứng tỉ lệ xem lại tối thiểu có thể hạ xuống một cách an toàn mà vẫn giữ được chất lượng.
