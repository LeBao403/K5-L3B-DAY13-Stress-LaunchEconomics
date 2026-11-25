# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm (hội đồng): 4NguoiDamDang 
- Nhóm được chấm: Stress (L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số của nhóm. Hồ sơ nêu các số bất lợi: xem lại 100% tốn 11.743 đ (0,98×) và 12.415 đ (1,03×), `quoc_te` 22.515 đ (1,88×), power khoảng 0,64, mở lại 4,25%. Mỗi số có cách xử lý: điều kiện 4 giảm xem lại theo bậc, điều kiện 2 ký chấp nhận mức chênh 6 điểm, loại `quoc_te` khỏi phạm vi, luật dừng an toàn |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Các số chi phí đều có nhãn `simulated` hoặc trạng thái Giả lập (mục 1, 2, 3, 7). Phạm vi chỉ `noi_dia` + `hang_nang` có lý do bằng số: 0,22× và 0,69× so với 12.000 đ, còn `quoc_te` 1,88× và `doi_tac` 0,85× bị loại. Ba chỉ số E1 lấy từ cột thật nên không gắn nhãn là đúng. Nhận xét nhỏ: con số 11.743 đ trong phần đề xuất chưa có nhãn ngay sau nó |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20 có đối chứng cùng tuần, bốc thăm ngẫu nhiên có seed ghi trước. Cỡ mẫu 859 mỗi nhóm, hệ số thiết kế 6,96, nhóm nêu rõ đánh đổi (power 0,64 nếu tác động thật là 5 điểm). Ba luật dừng đủ bốn vế, mỗi luật có ngưỡng (2 điểm hoặc 6%; 8.000 đ; 40%), thời hạn và người có quyền dừng. Ngày bắt đầu 2026-12-07, quyết định 2027-01-05 |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đề xuất khớp bằng chứng của nhóm: chi phí cả hệ thống 0,49× so với nhân viên tự làm trong phạm vi hẹp, các điều kiện có chức danh và ngày kiểm tra. Hội đồng đồng ý với bốn điều kiện nhóm đặt ra.

**Một câu hỏi cho đội trình:** Chỉ số chính cần 7 ngày mới biết khách có mở lại hay không, trong khi luật dừng an toàn xét theo "1 tuần đánh giá". Nhóm phát hiện ca mở lại xấu kịp thời bằng cách nào, và pilot nhỏ nhất (4 nhân viên ở bước đầu) có thể dừng trước khi đủ 7 ngày không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội thừa nhận khoảng trễ này: chỉ số mở lại phải chờ 7 ngày sau khi đóng ticket, nên ở bước 10% (4 nhân viên) tín hiệu mở lại của tuần 1 chỉ đầy đủ vào cuối tuần 2. Kế hoạch hiện có chặn việc sang bước 25% nếu tuần đánh giá vi phạm ngưỡng, và Giám đốc vận hành có thể tắt trợ lý trong 30 phút bất cứ lúc nào. Đội đề xuất bổ sung một luật dừng sớm dùng tín hiệu không bị trễ: nếu `refund_ledger_write` ghi hai lần cho cùng một đơn (cùng `idempotency_key`) thì tắt trợ lý ngay trong 30 phút. Chỉ số kiểm tra mẫu hằng tuần (`audit_sample_checked`, 100 đơn) cũng đã được liệt kê trong `chi_so.md` để bắt lỗi sai tiền sớm hơn.

