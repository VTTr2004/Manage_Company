from mainpage.models import Account, Staff, Manage_Staf, Job, Join, Manage_Proj, Project
from types import SimpleNamespace

class Infor:
    @staticmethod
    def Get_Personal_Infor(id_staf):
        return Staff.objects.get(id_staf=id_staf)
    
    @staticmethod
    def Get_Data_Leader(id_staf):
        id_stafs = [staf.id_staf for staf in Manage_Staf.objects.filter(id_mana=id_staf)]
        staf_content = []
        for id in id_stafs:
            staf = Staff.objects.get(id_staf=id)
            staf_content.append(SimpleNamespace(
                id_staf=staf.id_staf,
                name=staf.name,
                spec=staf.spec,
                email=staf.email,
                status=staf.status
            ))
        return staf_content

    @staticmethod
    def Get_Data_Coder(id_staf, leader = False):
        if leader:
            return Infor.Get_Data_Leader(id_staf)
        num_comp = len(Join.objects.filter(id_staf=id_staf, status='hoan thanh'))
        num_non_comp = len(Join.objects.filter(id_staf=id_staf, status='chua'))
        num_late_comp = len(Join.objects.filter(id_staf=id_staf, status='hoan thanh cham'))
        num_over = len(Join.objects.filter(id_staf=id_staf, status='qua han'))
        staf_content = SimpleNamespace(
            comp=str(num_comp),
            non_comp=str(num_non_comp),
            late_copm=str(num_late_comp),
            over=str(num_over)
        )
        return staf_content

    @staticmethod
    def Get_Data_Saler(id_staf):
        return

    @staticmethod
    def Get_Data_Shipper(id_staf):
        return

    @staticmethod
    def Get_Data_Mana_Proj(id_staf):
        projs = Manage_Proj.objects.filter(id_staf=id_staf)
        return

    @staticmethod
    def Get_Data_Mana_Staf(id_staf):
        return

    @staticmethod
    def Get_Data_Mana_Bran(id_staf):
        return

    @staticmethod
    def Get_Data_Mana_Cust(id_staf):
        return

    @staticmethod
    def Get_Data(access_token, inf_only = False, leader = False):
        id_staf = Account.objects.get(access_token=access_token).id_staf
        staf_inf = Infor.Get_Personal_Infor(id_staf)
        if inf_only:
            return staf_inf
        id_r = staf_inf.id_r
        addr = "staff_page/func_page/infor/"
        staf_content = None
        if leader:
            addr += 'staf_lv2.html'
            staf_content = Infor.Get_Data_Leader(id_staf)
        elif 'CD' in id_r or id_r in ['AD002', 'AD003']:
            addr += "coder.html"
            staf_content = Infor.Get_Data_Coder(id_staf)
        elif 'SL' in id_r:
            staf_content = Infor.Get_Data_Saler(id_staf)
        elif 'SP' in id_r:
            staf_content = Infor.Get_Data_Shipper(id_staf)
        elif 'PR' in id_r:
            addr += 'staf_lv3.html'
            staf_content = Infor.Get_Data_Mana_Proj(id_staf)
        elif 'ST' in id_r:
            staf_content = Infor.Get_Data_Mana_Staf(id_staf)
        elif 'BR' in id_r:
            staf_content = Infor.Get_Data_Mana_Bran(id_staf)
        elif 'CU' in id_r:
            staf_content = Infor.Get_Data_Mana_Cust(id_staf)

        return addr, staf_content, staf_inf