from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

# Create your models here.
# class CustomUser(AbstractUser):
#     user_type_data=((1, 'admin'), (2, 'nhanVien'), (3, 'giaoVien'))
#     user_type=models.CharField(default=1, choices=user_type_data, max_length=10)

class nguoiDung(AbstractUser):
    mand=models.AutoField(primary_key=True)
    hovaten=models.CharField(max_length=255)
    ngaysinh=models.DateField(default=datetime.date(1970, 1, 1))
    gioitinh=models.CharField(max_length=255)
    diachi=models.CharField(max_length=255)
    cccd=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    sdt=models.CharField(max_length=255)
    ngaybatdau=models.DateField(default=datetime.date(1970, 1, 1))
    user_type_data=((1, 'admin'), (2, 'nhanVien'), (3, 'giaoVien'))
    user_type=models.CharField(default=1, choices=user_type_data, max_length=10)

class admin(models.Model):
    admin=models.AutoField(primary_key=True)
    ten=models.CharField(max_length=255) #need delete
    email=models.CharField(max_length=255) #need delete
    password=models.CharField(max_length=255) #need delete
    admin=models.OneToOneField(nguoiDung,on_delete=models.CASCADE)
    objects=models.Manager()
     
class monHoc(models.Model):
    mamonhoc=models.AutoField(primary_key=True)
    tenmonhoc=models.CharField(max_length=255)
    sotiet=models.IntegerField()
    objects=models.Manager()
    
class nhanVien(models.Model):
    manv=models.AutoField(primary_key=True)
    vitri=models.CharField(max_length=255)
    admin=models.OneToOneField(nguoiDung,on_delete=models.CASCADE)
    objects=models.Manager()

class lop(models.Model):
    malop=models.AutoField(primary_key=True)
    tenlop=models.CharField(max_length=255)
    objects=models.Manager()

class giaoVien(models.Model):
    magv=models.AutoField(primary_key=True)
    mamonhoc=models.ForeignKey(monHoc, on_delete=models.CASCADE, default=1)
    malop=models.ForeignKey(lop, on_delete=models.CASCADE, default=1)
    admin=models.OneToOneField(nguoiDung,on_delete=models.CASCADE)
    objects=models.Manager()
    
class hocSinh(models.Model):
    mahs=models.AutoField(primary_key=True)
    hovaten=models.CharField(max_length=255)
    ngaysinh=models.DateField()
    gioitinh=models.CharField(max_length=255)
    diachi=models.CharField(max_length=255)
    malop=models.ForeignKey(lop, on_delete=models.CASCADE, default=1)
    tenbo=models.CharField(max_length=255)
    sdtbo=models.CharField(max_length=255)
    emailbo=models.CharField(max_length=255)
    tenme=models.CharField(max_length=255)
    sdtme=models.CharField(max_length=255)
    emailme=models.CharField(max_length=255)
    objects=models.Manager()
    
class diem(models.Model):
    maxulydiem=models.AutoField(primary_key=True)
    mahs=models.ForeignKey(hocSinh, on_delete=models.CASCADE, default=1)
    mamonhoc=models.ForeignKey(monHoc, on_delete=models.CASCADE, default=1)
    mucdatduoc=models.CharField(max_length=10)
    diem=models.FloatField()
    
@receiver(post_save,sender=nguoiDung)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            admin.objects.create(admin=instance)
        if instance.user_type==2:
            nhanVien.objects.create(admin=instance, vitri="")
        if instance.user_type==3:
            giaoVien.objects.create(admin=instance, malop=lop.objects.get(malop=1), mamonhoc=monHoc.objects.get(mamonhoc=1))

@receiver(post_save,sender=nguoiDung)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.nhanvien.save()
    if instance.user_type==3:
        instance.giaovien.save()
    