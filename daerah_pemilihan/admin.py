from django.contrib import admin

from daerah_pemilihan.models import DapilDprdKabKota


class DapilDprdKabKotaAdmin(admin.ModelAdmin):
    list_display = (
        "kabkota",
        "no",
        "jumlah_kursi",
    )
    ordering = ("kabkota",)


# Register your models here.

admin.site.register(DapilDprdKabKota, DapilDprdKabKotaAdmin)
