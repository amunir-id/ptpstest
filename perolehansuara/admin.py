from django.contrib import admin

from perolehansuara.models import (
    CekPpwp,
    CekDpdRi,
    CekDprRi,
    CekDprdKabKota,
    CekDprdProv,
    HasilPpwp,
    DataPemilihPenggunaHakPilihPpwp,
    DataPenggunaSuratSuaraPpwp,
    DataDisabilitasPpwp,
    DataSuaraSahdanTidakSahPpwp,
    PpwpMedia,
    DprRiMedia,
    DpdRiMedia,
    DprdProvMedia,
    DprdKabKotaMedia,
)


@admin.register(HasilPpwp)
class HasilPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CekPpwp)
class CekPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CekDpdRi)
class CekDpdRiAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CekDprRi)
class CekDprRiAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CekDprdProv)
class CekDprdProvAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(CekDprdKabKota)
class CekDprdKabKotaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(PpwpMedia)
class PpwpMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DataPemilihPenggunaHakPilihPpwp)
class DataPemilihPenggunaHakPilihPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DataPenggunaSuratSuaraPpwp)
class DataPenggunaSuratSuaraPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DataDisabilitasPpwp)
class DataDisabilitasPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DataSuaraSahdanTidakSahPpwp)
class DataSuaraSahdanTidakSahPpwpAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DprRiMedia)
class DprRiMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DpdRiMedia)
class DpdRiMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DprdProvMedia)
class DprdProvMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


@admin.register(DprdKabKotaMedia)
class DprdKabKotaMediaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
