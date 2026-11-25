"""Nháp của Người 2: D1 (cỡ mẫu), tỉ lệ mở lại, E1 (ba chỉ số), số liệu để chọn phạm vi pilot.
Chạy trong src/: python nhap_nguoi2.py
Hàm in_bang_d1() sẽ được dán vào lab13.py tại TODO CP4 sau khi Người 1 xong.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

BASELINE = 0.70
ALPHA = 0.05
POWER = 0.80
ICC = 0.02
SO_NHAN_VIEN = 40


def co_mau(p1, p2, alpha=ALPHA, power=POWER):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (chia theo yêu cầu)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu = za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(tu ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    return 1 + (m - 1) * icc


def mau_hieu_dung(c, m, icc=ICC):
    """Cỡ mẫu hiệu dụng khi chia theo cụm: c cụm, mỗi cụm m yêu cầu."""
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(c, n_can, icc=ICC):
    """Số yêu cầu tối thiểu mỗi cụm để c cụm đạt cỡ mẫu hiệu dụng n_can.
    Giải c*m / (1 + (m-1)*icc) >= n_can."""
    if c / icc <= n_can:
        return None
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def in_bang_d1():
    # a) chia theo yêu cầu
    n5 = co_mau(BASELINE, BASELINE + 0.05)
    print(f'D1a  chia theo yêu cầu, +5 điểm: {n5:,} yêu cầu mỗi nhóm')
    # b) chia theo nhân viên, m = 75
    m = 75
    de = he_so_thiet_ke(m)
    n_cum = math.ceil(n5 * de)
    so_nv = math.ceil(n_cum / m)
    print(f'D1b  theo nhân viên, m={m}: DE={de:.2f}, {n_cum:,} yêu cầu mỗi nhóm '
          f'= {so_nv} người mỗi nhóm, tổng {2 * so_nv} (có {SO_NHAN_VIEN} nhân viên)')
    # c) 20 nhân viên mỗi nhóm
    print(f'D1c  20 nhân viên mỗi nhóm: hiệu dụng tối đa c/ICC = {20 / ICC:,.0f} '
          f'(cần {n5:,}) -> {"đạt" if 20 / ICC >= n5 else "không đạt"}')
    # d) 6 depot mỗi nhóm
    print(f'D1d  6 depot mỗi nhóm: hiệu dụng tối đa = {6 / ICC:,.0f}')
    # e) mức chênh 6 điểm, 20 nhân viên mỗi nhóm
    n6 = co_mau(BASELINE, BASELINE + 0.06)
    me = m_toi_thieu(20, n6)
    print(f'D1e  mức chênh 6 điểm: {n6:,} mỗi nhóm; 20 nhân viên cần m >= {me} yêu cầu mỗi người '
          f'(DE={he_so_thiet_ke(me):.2f}, hiệu dụng={mau_hieu_dung(20, me):,.0f})')
    # power nếu tác động thật chỉ 5 điểm mà thiết kế theo 6 điểm
    es = proportion_effectsize(BASELINE + 0.05, BASELINE)
    pw = NormalIndPower().power(effect_size=es, nobs1=n6, alpha=ALPHA, ratio=1.0)
    print(f'     power thật nếu tác động chỉ 5 điểm, n={n6}: {pw:.2f}')
    return dict(n5=n5, de_b=de, n_cum=n_cum, so_nv=so_nv, n6=n6, m_e=me, power5=pw)


def phan_tich_du_lieu(runs, reqs):
    print('\n--- Tỉ lệ mở lại trong 7 ngày (chỉ số an toàn hiện tại) ---')
    tl = reqs.mo_lai_trong_7_ngay.mean()
    pham_vi = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    print(f'toàn mẫu: {tl:.2%} ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})')
    print(f'noi_dia + hang_nang: {pham_vi.mo_lai_trong_7_ngay.mean():.2%} '
          f'({pham_vi.mo_lai_trong_7_ngay.sum()}/{len(pham_vi)})')
    print(reqs.groupby('loai').mo_lai_trong_7_ngay.mean().map('{:.2%}'.format).to_string())

    print('\n--- E1: ba chỉ số tính thử ---')
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0))
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'chính: {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})')
    print(f'dùng (bỏ qua gợi ý): {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})')
    print(f'an toàn: {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)})')
    print('quyết định xem lại:', xem.quyet_dinh_xem_lai.value_counts().to_dict())
    pv_chinh = ((pham_vi.dong_trong_24h == 1) & (pham_vi.mo_lai_trong_7_ngay == 0))
    print(f'chính trong phạm vi noi_dia + hang_nang: {pv_chinh.mean():.2%}')

    print('\n--- Tỉ lệ làm lại trong phạm vi (cho luật dừng/rủi ro) ---')
    print(f'lam_lai toàn mẫu: {(reqs.ket_qua == "lam_lai").mean():.2%}; '
          f'trong phạm vi: {(pham_vi.ket_qua == "lam_lai").mean():.2%}')
    print(f'tỉ lệ được xem lại toàn mẫu: {reqs.duoc_xem_lai.mean():.2%}')

    print('\n--- Phân bố theo nhân viên và depot (cho cách chia) ---')
    print(f'số nhân viên: {reqs.staff_id.nunique()}, số depot: {reqs.depot.nunique()}')
    print(f'yêu cầu/nhân viên: trung bình {len(reqs) / reqs.staff_id.nunique():.1f}')

    print('\n--- Chọn phạm vi: số liệu theo loại (chi phí là bản tính nhanh của Người 2, '
          'đối chiếu với A3 của Người 1) ---')
    r = runs[runs.request_id.isin(reqs.request_id)]
    tien_run = (r.tokens_in / 1000 * 26 + r.tokens_out / 1000 * 130 + r.tool_calls * 15)
    chi_run = tien_run.groupby(r.request_id).sum()
    rq = reqs.set_index('request_id')
    rq['chi_run'] = chi_run
    rq['chi_nv'] = (rq.phut_xem_lai_simulated + rq.phut_lam_lai_simulated) * 2000
    rows = []
    for loai, g in rq.groupby('loai'):
        tc = (g.ket_qua == 'thanh_cong').sum()
        cps = (g.chi_run.sum() + g.chi_nv.sum()) / tc
        rows.append((loai, len(g), tc / len(g), cps, cps / 12000))
    out = pd.DataFrame(rows, columns=['loai', 'n', 'ti_le_tc', 'cps_sim', 'so_voi_12000'])
    print(out.to_string(index=False, formatters={
        'ti_le_tc': '{:.1%}'.format, 'cps_sim': '{:,.0f}'.format, 'so_voi_12000': '{:.2f}x'.format}))
    tc_all = (rq.ket_qua == 'thanh_cong').sum()
    print(f'cps toàn mẫu (simulated): {(rq.chi_run.sum() + rq.chi_nv.sum()) / tc_all:,.0f}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    in_bang_d1()
    phan_tich_du_lieu(runs, reqs)
