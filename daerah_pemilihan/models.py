from django.db import models

from wilayah.models import KabKota, Kecamatan, Provinsi


class DapilDprdKabKota(models.Model):
    no = models.IntegerField()
    provinsi = models.ForeignKey(
        Provinsi,
        on_delete=models.SET_NULL,
        null=True,
        related_name="dapildprdkabkota_provinsi",
    )
    kabkota = models.ForeignKey(
        KabKota,
        on_delete=models.SET_NULL,
        null=True,
        related_name="dapildprdkabkota_kabkota",
    )
    jumlah_kursi = models.IntegerField()
    wilayah = models.ManyToManyField(
        Kecamatan, blank=True, related_name="dapildprdkabkota_wilayah"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.no)
