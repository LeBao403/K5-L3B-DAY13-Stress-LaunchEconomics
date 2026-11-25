"""File nháp Người 3 (Người gắn nhãn 2, giữ hồ sơ) — Lab 13.
Tính toán Nhiệm vụ B4 (xem lại 100% cho phạm vi noi_dia + hang_nang) từ dữ liệu thô.
Chạy từ thư mục gốc hoặc src/: python src/nhap_nguoi3.py
"""
from pathlib import Path
import pandas as pd

GIA_VAO = 26        # đồng / 1.000 token đầu vào
GIA_RA = 130        # đồng / 1.000 token đầu ra
GIA_TOOL = 15       # đồng / 1 lần gọi tool
LUONG_PHUT = 2000   # đồng / phút nhân viên
BASELINE = 12000    # đồng / yêu cầu nhân viên tự làm (6 phút)

PHUT_XEM_LAI_B4 = 5
PHUT_LAM_LAI_B4 = 9


def main():
    src_dir = Path(__file__).resolve().parent
    runs = pd.read_csv(src_dir / 'logix_runs.csv')
    reqs = pd.read_csv(src_dir / 'logix_requests.csv', keep_default_na=False)

    # Lọc phạm vi noi_dia + hang_nang
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    scope_runs = runs[runs['request_id'].isin(scope_reqs['request_id'])].copy()

    tong_yeu_cau = len(scope_reqs)
    thanh_cong = int((scope_reqs['ket_qua'] == 'thanh_cong').sum())

    # 1. Số yêu cầu có ít nhất một lần chạy status == 'ok'
    yc_co_ok = int(scope_runs[scope_runs['status'] == 'ok']['request_id'].nunique())
    tien_xem_lai = yc_co_ok * PHUT_XEM_LAI_B4 * LUONG_PHUT

    # 2. Số ca ket_qua == 'lam_lai'
    ca_lam_lai = scope_reqs[scope_reqs['ket_qua'] == 'lam_lai']
    so_ca_lam_lai = len(ca_lam_lai)
    tien_lam_lai_9p = so_ca_lam_lai * PHUT_LAM_LAI_B4 * LUONG_PHUT

    # 3. Cộng token + tool của mọi lần chạy thuộc phạm vi
    tien_token = (
        scope_runs['tokens_in'] / 1000 * GIA_VAO
        + scope_runs['tokens_out'] / 1000 * GIA_RA
    ).sum()
    tien_tool = (scope_runs['tool_calls'] * GIA_TOOL).sum()
    tien_token_tool = tien_token + tien_tool

    # 4. Tổng chi phí và chi phí mỗi việc thành công (giả định 9 phút làm lại)
    tong_9p = tien_token_tool + tien_xem_lai + tien_lam_lai_9p
    cps_9p = tong_9p / thanh_cong
    ty_so_9p = cps_9p / BASELINE

    # 5. Độ nhạy theo phut_lam_lai_simulated
    tb_lam_lai_toan_mau = reqs[reqs['ket_qua'] == 'lam_lai']['phut_lam_lai_simulated'].mean()
    tien_lam_lai_toan_mau = so_ca_lam_lai * tb_lam_lai_toan_mau * LUONG_PHUT
    tong_toan_mau = tien_token_tool + tien_xem_lai + tien_lam_lai_toan_mau
    cps_toan_mau = tong_toan_mau / thanh_cong
    ty_so_toan_mau = cps_toan_mau / BASELINE

    tong_phut_lam_lai_scope = ca_lam_lai['phut_lam_lai_simulated'].sum()
    tb_lam_lai_scope = ca_lam_lai['phut_lam_lai_simulated'].mean()
    tien_lam_lai_scope = tong_phut_lam_lai_scope * LUONG_PHUT
    tong_scope = tien_token_tool + tien_xem_lai + tien_lam_lai_scope
    cps_scope = tong_scope / thanh_cong
    ty_so_scope = cps_scope / BASELINE

    # 6. Mức xem lại hoà vốn (cps <= 12.000 đ <=> tổng chi phí <= thanh_cong * 12.000)
    ngan_sach_hoa_von = thanh_cong * BASELINE
    hoa_von_9p = (ngan_sach_hoa_von - tien_token_tool - tien_lam_lai_9p) / (yc_co_ok * LUONG_PHUT)
    hoa_von_toan_mau = (ngan_sach_hoa_von - tien_token_tool - tien_lam_lai_toan_mau) / (yc_co_ok * LUONG_PHUT)
    hoa_von_scope = (ngan_sach_hoa_von - tien_token_tool - tien_lam_lai_scope) / (yc_co_ok * LUONG_PHUT)

    print('=== NHIỆM VỤ B4: XEM LẠI 100% (noi_dia + hang_nang) ===')
    print(f'Số yêu cầu trong phạm vi       : {tong_yeu_cau}')
    print(f'Số việc thành công             : {thanh_cong}')
    print(f'Yêu cầu có >= 1 lần status=ok  : {yc_co_ok}')
    print(f'Số ca lam_lai                  : {so_ca_lam_lai}')
    print(f'Tiền token + tool              : {tien_token_tool:,.0f} đ (token: {tien_token:,.0f} đ, tool: {tien_tool:,.0f} đ)')
    print(f'Tiền xem lại (5 phút/yc) [sim] : {tien_xem_lai:,.0f} đ')
    print('--- Trường hợp chuẩn (9 phút/ca làm lại) ---')
    print(f'Tiền làm lại (9 phút) [sim]    : {tien_lam_lai_9p:,.0f} đ')
    print(f'Tổng chi phí [sim]             : {tong_9p:,.0f} đ')
    print(f'Chi phí / việc thành công [sim]: {cps_9p:,.0f} đ ({ty_so_9p:.2f}x của 12.000 đ)')
    print(f'Mức xem lại hoà vốn [sim]      : <= {hoa_von_9p:.2f} phút/lần')
    print('--- Độ nhạy theo phut_lam_lai_simulated (trung bình toàn mẫu) ---')
    print(f'TB toàn mẫu phut_lam_lai [sim] : {tb_lam_lai_toan_mau:.2f} phút/ca')
    print(f'Tổng chi phí [sim]             : {tong_toan_mau:,.0f} đ')
    print(f'Chi phí / việc thành công [sim]: {cps_toan_mau:,.0f} đ ({ty_so_toan_mau:.2f}x của 12.000 đ)')
    print(f'Mức xem lại hoà vốn [sim]      : <= {hoa_von_toan_mau:.2f} phút/lần')
    print('--- Độ nhạy theo phut_lam_lai_simulated (thực tế trong phạm vi) ---')
    print(f'Tổng phút làm lại phạm vi [sim]: {tong_phut_lam_lai_scope:.0f} phút (TB {tb_lam_lai_scope:.2f} phút/ca)')
    print(f'Tổng chi phí [sim]             : {tong_scope:,.0f} đ')
    print(f'Chi phí / việc thành công [sim]: {cps_scope:,.0f} đ ({ty_so_scope:.2f}x của 12.000 đ)')
    print(f'Mức xem lại hoà vốn [sim]      : <= {hoa_von_scope:.2f} phút/lần')


if __name__ == '__main__':
    main()
