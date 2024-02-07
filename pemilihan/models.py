from django.db import models

from wilayah.models import Provinsi


# Create your models here.
class JenisPemilihan(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DaerahPemilihan(models.Model):
    jenis_pemilihan = models.ForeignKey(
        JenisPemilihan, on_delete=models.SET_NULL, null=True
    )
    provinsi = models.ForeignKey(
        Provinsi, on_delete=models.SET_NULL, null=True, related_name="daerah_pemilihan"
    )
    no = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PesertaPemiluPartai(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
