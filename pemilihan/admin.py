from django.contrib import admin
from pemilihan.models import JenisPemilihan,DaerahPemilihan

from  django.contrib.auth.admin import UserAdmin


class DaerahPemilihanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'no',
        'created_at',
        'updated_at',
    )



admin.site.register(JenisPemilihan)
admin.site.register(DaerahPemilihan,DaerahPemilihanAdmin)