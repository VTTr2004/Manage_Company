from collections import defaultdict
from types import SimpleNamespace

class CapNhanVien:
    @staticmethod
    def CongViec_DH(Table_list, id_nv):
        ThamGia = Table_list[0]
        DuAn = Table_list[1]
        CongViec = Table_list[2]
        thamgias = ThamGia.objects.filter(id_nv=id_nv)
        data = defaultdict(list)
        for tg in thamgias:
            ten_da = DuAn.objects.get(id_da=tg.id_da).ten_da
            ten_cv = CongViec.objects.get(id_cv=tg.id_cv).ten_cv
            data[ten_da].append(SimpleNamespace(id=tg.id,
                                                ten=ten_cv,
                                                thoi_han=tg.thoi_han,
                                                trang_thai=tg.trang_thai))
        return dict(data)
    
    @staticmethod
    def CongViec_BH(Table_list, id_nv):
        ThucHien = Table_list[0]
        KhachHang = Table_list[1]
        thuchiens = ThucHien.objects.filter(id_nv=id_nv)
        data = []
        for th in thuchiens:
            kh = KhachHang.objects.get(id_kh=th.id_kh)
            data.append(SimpleNamespace(id=th.id,
                                        ten=kh.ten,
                                        sdt=kh.sdt,
                                        loai=kh.loai,
                                        yeu_cau=th.yeu_cau,
                                        ghi_chu=th.ghi_chu))
        return data
    
    @staticmethod
    def CongViec_VH(Table_list, id_nv):
        pass

class CapTruong:
    @staticmethod
    def QLDA(Table_list, id_nv):
        QuanLy = Table_list[0]
        ThamGia = Table_list[1]
        DuAn = Table_list[2]
        CongViec = Table_list[3]
        id_nvs = [i.id_nv for i in QuanLy.objects.filter(id_trg=id_nv)]
        data = defaultdict(list)
        for id in id_nvs:
            thamgias = ThamGia.objects.filter(id_nv=id)
            for tg in thamgias:
                ten_da = DuAn.objects.get(id_da=tg.id_da).ten_da
                ten_cv = CongViec.objects.get(id_cv=tg.id_cv).ten_cv
                data[id].append(SimpleNamespace(id=tg.id,
                                                ten_da = ten_da,
                                                ten=ten_cv,
                                                thoi_han=tg.thoi_han,
                                                trang_thai=tg.trang_thai))
        return dict(data)