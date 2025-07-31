from mainpage.models import Account, Staff, Manage_Staf, Job, Join, Manage_Proj, Project

from collections import defaultdict
from types import SimpleNamespace

class Job_Page:
    @staticmethod
    def Get_Data_Coder(id_staf, non_comp = False, for_lead = False):
        joins = Join.objects.filter(id_staf=id_staf)
        staf_content = None
        if non_comp:
            joins = joins.exclude(status='hoan thanh')
        if for_lead:
            staf_content = defaultdict(list)
            for j in joins:
                staf_content[j.id_pr].append(SimpleNamespace(
                    id=j.id,
                    id_staf=id_staf,
                    id_job=j.id_job,
                    dura=j.duration,
                    status=j.status
                ))
            return staf_content
        staf_content = []
        jobs = Job.objects.in_bulk(field_name='id_job')
        for j in joins:
            name_job = jobs.get(j.id_job)
            staf_content.append(SimpleNamespace(
                name_job=name_job if name_job else None,
                dura=j.duration,
                status=j.status
            ))
        return staf_content
    
    @staticmethod
    def Get_Data_Coder_Lead(id_staf):
        id_stafs = [staf.id_staf for staf in Manage_Staf.objects.filter(id_mana=id_staf)]
        staf_content = defaultdict(list)
        for id_st in id_stafs:
            temp = Job_Page.Get_Data_Coder(id_st, non_comp=True, for_lead=True)
            for i_pr, joins in temp.items():
                staf_content[i_pr].extend([j for j in joins])
        return dict(staf_content)

    @staticmethod
    def Get_Data_Saler(id_staf):
        return
    
    @staticmethod
    def Get_Data_Saler_Lead(id_staf):
        return

    @staticmethod
    def Get_Data_Shipper(id_staf):
        return
    
    @staticmethod
    def Get_Data_Shipper_Lead(id_staf):
        return
    
    @staticmethod
    def Get_Data_Mana_Proj(id_staf):
        projs = [mana.id_pr for mana in Manage_Proj.objects.filter(id_staf=id_staf)]
        staf_content = defaultdict(list)
        for id_pr in projs:
            temp = defaultdict(list)
            joins = Join.objects.filter(id_pr=id_pr)
            for j in joins:
                id_mana = Manage_Staf.objects.get(id_staf=j.id_staf).id_mana
                temp[id_mana].append(j.status)
            for id_mana, data in temp.items():
                staf_content[id_pr].append(SimpleNamespace(
                    id_mana=id_mana,
                    progress=round(data.count('hoan thanh')/len(data), 2) * 100
                ))
        return dict(staf_content)

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
    def Get_Data(access_token, leader = False):
        id_staf = Account.objects.get(access_token=access_token).id_staf
        id_r = Staff.objects.get(id_staf=id_staf).id_r
        addr = "staff_page/func_page/job/"
        if 'CD' in id_r or id_r in ['AD001', 'AD002', 'AD003']:
            if leader:
                addr += "leader_it.html"
                staf_content = Job_Page.Get_Data_Coder_Lead(id_staf)
            else:
                addr += "coder.html"
                staf_content = Job_Page.Get_Data_Coder(id_staf)
        elif 'SL' in id_r:
            if leader:
                staf_content = Job_Page.Get_Data_Saler_Lead(id_staf)
            else:
                staf_content = Job_Page.Get_Data_Saler(id_staf)
        elif 'SP' in id_r:
            if leader:
                staf_content = Job_Page.Get_Data_Shipper_Lead(id_staf)
            else:
                staf_content = Job_Page.Get_Data_Shipper(id_staf)
        elif 'PR' in id_r:
            addr += "proj.html"
            staf_content = Job_Page.Get_Data_Mana_Proj(id_staf)
        elif 'ST' in id_r:
            staf_content = Job_Page.Get_Data_Mana_Staf(id_staf)
        elif 'BR' in id_r:
            staf_content = Job_Page.Get_Data_Mana_Bran(id_staf)
        elif 'CU' in id_r:
            staf_content = Job_Page.Get_Data_Mana_Cust(id_staf)

        return addr, staf_content