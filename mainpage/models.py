from django.db import models

class Account(models.Model):
    id_staf = models.CharField(max_length=5)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    access_token = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.tk} - {self.id_nv}"
    
class Role(models.Model):
    id_r = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    describe = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.id_chucvu} - {self.ten}"

class Role_Permission(models.Model):
    id_r = models.CharField(max_length=5)
    code_permis = models.CharField(max_length=5)

class Staff_Permission(models.Model):
    id_staf = models.CharField(max_length=5)
    code_permis = models.CharField(max_length=5)

class Staff(models.Model):
    id_staf = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    year_born = models.CharField(max_length=4)
    date_bg_work = models.DateField(blank=True)
    email = models.CharField(max_length=50, unique=True)
    id_r = models.CharField(max_length=5)
    spec = models.CharField(max_length=30) # specializations
    status = models.CharField(max_length=30)
    # anh_dai_dien = models.ImageField(upload_to='avatars/', null=True, blank=True)
    def __str__(self):
        return f"{self.name} - {self.spec}"

class Manage_Staf(models.Model):
    id_mana = models.CharField(max_length=5)
    id_staf = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.id_trg} - {self.id_nv}"
    
class Project(models.Model):
    id_pr = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    begin = models.DateField(blank=True, null=True)
    describe = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.ten_da} - {self.id_phong}"
    
class Manage_Proj(models.Model):
    id_staf = models.CharField(max_length=5)
    id_pr = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.id_staf} - {self.id_pr}"

class Job(models.Model):
    id_job = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    describe = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class Join(models.Model):
    id_staf = models.CharField(max_length=5)
    id_pr = models.CharField(max_length=5)
    id_job = models.CharField(max_length=5)
    status = models.CharField(max_length=30)
    duration = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True)
    def __str__(self):
        return f"NV:{self.id_staf} - CV:{self.id_job}"
    
# class PhongBan(models.Model):
#     id_ph = models.CharField(max_length=5)
#     ten_ph = models.CharField(max_length=50)
#     id_trg = models.CharField(max_length=5)
#     mo_ta = models.TextField(null=True, blank=True)
#     def __str__(self):
#         return self.ten_ph
    
# class Thuoc(models.Model):
#     id_nv = models.CharField(max_length=5)
#     id_ph = models.CharField(max_length=5)
#     def __str__(self):
#         return f"{self.id_nv} - {self.id_ph}"

# class KhachHang(models.Model):
#     id_kh = models.CharField(max_length=5)
#     ten = models.CharField(max_length=50)
#     sdt = models.CharField(max_length=11)
#     loai = models.CharField(max_length=1)
#     ghi_chu = models.TextField(blank=True)
#     def __str__(self):
#         return f"{self.ten} - {self.loai}"
    
# class ThucHien(models.Model):
#     id_nv = models.CharField(max_length=5)
#     id_kh = models.CharField(max_length=5)
#     yeu_cau = models.CharField(max_length=50, blank=False)
#     ghi_chu = models.TextField(blank=True)
#     def __str__(self):
#         return f"{self.id_nv} - {self.id_kh}"
    
# class GiaoHang(models.Model):
#     id_nv = models.CharField(max_length=5)
#     id_dh = models.IntegerField()
#     ghi_chu = models.TextField(blank=True)