from django.db import models

from wilayah.models import Tps


# Create your models here.
class DaftarPemilih(models.Model):
    tps = models.ForeignKey(Tps, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    rt = models.CharField(max_length=3, blank=True, null=True)
    rw = models.CharField(max_length=3, blank=True, null=True)
    desa = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    kabupaten = models.CharField(max_length=50, blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
