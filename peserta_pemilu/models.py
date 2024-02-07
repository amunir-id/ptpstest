from django.db import models

from accounts.models import User
from daerah_pemilihan.models import DapilDprdKabKota
from wilayah.models import KabKota, Provinsi


# Create your models here.
class Parpol(models.Model):
    no_urut = models.IntegerField()
    name = models.CharField(max_length=255)
    akronim = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to="logo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.akronim


# class DprRi(models.Model):
#     name = models.CharField(max_length=255)
#     parpol = models.ForeignKey(Parpol, on_delete=models.CASCADE)
#     no_urut = models.IntegerField()
#     provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
#     dapil = models.IntegerField()
#     foto = models.ImageField(upload_to="foto-caleg", null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class DprdProv(models.Model):
#     name = models.CharField(max_length=255)
#     parpol = models.ForeignKey(Parpol, on_delete=models.CASCADE)
#     no_urut = models.IntegerField()
#     provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
#     dapil = models.IntegerField()
#     foto = models.ImageField(upload_to="foto-caleg", null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


class DprdKabKota(models.Model):
    name = models.CharField(max_length=255)
    parpol = models.ForeignKey(
        Parpol, on_delete=models.CASCADE, related_name="dprdkabkota"
    )
    no_urut = models.IntegerField()
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    kabkota = models.ForeignKey(KabKota, on_delete=models.CASCADE)
    dapil = models.ForeignKey(DapilDprdKabKota, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="foto-caleg", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
