from django.urls import path, include
from . import views
from . import views as perolehan_views


urlpatterns = [
    path(
        "user-saksi-tps/delete/<int:pk>/",
        views.UserSaksiTPSDelete,
        name="UserSaksiTPSDelete",
    ),
    path("wilayah/provinsi", views.WilayahProvinsi, name="WilayahProvinsi"),
    path(
        "wilayah/provinsi/<int:pk>/",
        views.WilayahProvinsiDelete,
        name="WilayahProvinsiDelete",
    ),
    path("wilayah/kabkota", views.WilayahKabKota, name="WilayahKabKota"),
    path(
        "wilayah/kabkota/<int:pk>/",
        views.WilayahKabKotaDelete,
        name="WilayahKabKotaDelete",
    ),
    path("wilayah/kecamatan", views.WilayahKecamatan, name="WilayahKecamatan"),
    path(
        "wilayah/kecamatan/<int:pk>/",
        views.WilayahKecamatanDelete,
        name="WilayahKecamatanDelete",
    ),
    path("wilayah/keldesa", views.WilayahKelDesa, name="WilayahKelDesa"),
    path(
        "wilayah/keldesa/<int:pk>/",
        views.WilayahKelDesaDelete,
        name="WilayahKelDesaDelete",
    ),
    path("wilayah/tps", views.WilayahTps, name="WilayahTps"),
    path("pengaturan/akun", views.AkunMe, name="AkunMe"),
    path("perolehansuara/", views.PerolehanSuaraList, name="PerolehanSuaraList"),
    # path(
    #     "perolehansuara/<int:pk>",
    #     views.PerolehanSuaraEdit,
    #     name="PerolehanSuaraEdit",
    # ),
    path("perolehancaleg/", views.SuaraCaleg, name="SuaraCaleg"),
    # path("perolehantest/", views.PerolehanSuaraView, name="PerolehanSuaraView"),
    path("perolehan/", views.PerolehanSuaraTpsList, name="PerolehanSuaraTpsList"),
    # path(
    #     "perolehan/v1/",
    #     perolehan_views.PerolehanSuaraTpsView,
    #     name="PerolehanSuaraTpsView",
    # ),
]
