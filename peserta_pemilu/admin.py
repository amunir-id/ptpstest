from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from peserta_pemilu.models import Parpol, DprdKabKota


class ParpolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "no_urut",
        "name",
        "akronim",
    )
    ordering = ("no_urut",)


class DprdKabKotaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "no_urut",
        "name",
        "parpol",
        "dapil",
    )
    ordering = ("no_urut",)


admin.site.register(Parpol, ParpolAdmin)
admin.site.register(DprdKabKota, DprdKabKotaAdmin)
