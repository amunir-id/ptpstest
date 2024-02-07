from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.forms import RegisterUserForm
from accounts.models import User, UserSaksiTps
from django.contrib import messages
import random
from django.db.models import ProtectedError
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from perolehansuara.forms import (
    CekTPSForm,
    # PerolehanSuaraForm,
    # PerolehanSuaraStep1Form,
)
from perolehansuara.models import SuaraTps
from django.core.exceptions import PermissionDenied

# from perolehansuara.models import PerolehanTps
from peserta_pemilu.models import DprdKabKota, Parpol
from wilayah.forms import (
    WilayahKabKotaForm,
    WilayahKecamatanForm,
    WilayahKelDesaForm,
    WilayahProvinsiForm,
)
from django.db.models import Prefetch
from wilayah.models import KabKota, Kecamatan, KelDesa, Provinsi, Tps
from django.db.models import Count
import json
from django.views import View

# Create your views here.


# @login_required(login_url="Login")
# def UserSaksiTPS(request):
#     title_page = "User Saksi TPS"
#     users = User.objects.filter(role=2)
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         s_form = RegisterSaksiTPSForm(request.POST)
#         if form.is_valid() and s_form.is_valid:
#             random_number = str(random.randint(1, 9000))
#             fullname = form.cleaned_data["fullname"]
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#             user = User.objects.create_user(
#                 fullname=fullname, email=email, password=password
#             )
#             user.username = (
#                 user.email.split("@")[0].replace(".", "").replace("-", "")
#                 + random_number
#             )
#             user.role = User.SAKSI_TPS
#             user.save()
#             saksi = s_form.save(commit=False)
#             saksi.user = user
#             caleg = User.objects.get(user=request.user)
#             saksi.caleg = caleg
#             saksi.save()
#             return redirect("caleg:UserSaksiTPS")
#         else:
#             print("invalid form")
#             print(form.errors)
#     else:
#         form = RegisterUserForm()
#         s_form = RegisterSaksiTPSForm()

#     context = {
#         "title_page": title_page,
#         "users": users,
#         "form": form,
#         "s_form": s_form,
#     }
#     return render(request, "caleg/user_saksi_tps.html", context)


@login_required(login_url="Login")
def UserSaksiTPSDelete(request, pk=None):
    try:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        messages.success(request, f"User  {user.fullname} berhasil di hapus!")
        return redirect("caleg:UserSaksiTPS")
    except User.DoesNotExist:
        messages.error(request, f"Maaf user tidak ada!")
        return redirect("caleg:UserSaksiTPS")
    except ProtectedError:
        messages.error(
            request,
            f"Maaf divisi {user.fullname} tidak dapat dihapus, jika ingin menghapus pastikan tidak ada user yang terhubung dengan user ini!",
        )
        return redirect("caleg:UserSaksiTPS")


@login_required(login_url="Login")
def WilayahProvinsi(request):
    title_page = "Provinsi Indonesia"
    paginator = Paginator(
        Provinsi.objects.annotate(
            jumlah_kabkota=Count("kabkota", distinct=True),
            jumlah_kecamatan=Count("kabkota__kecamatan", distinct=True),
            jumlah_keldesa=Count("kabkota__kecamatan__keldesa", distinct=True),
            jumlah_tps=Count("kabkota__kecamatan__keldesa__tps", distinct=True),
        ),
        100,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        provinsi_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        provinsi_list = paginator.page(1)
    index = provinsi_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    if request.method == "POST":
        form = WilayahProvinsiForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            add = Provinsi(name=name)
            add.save()
            messages.success(request, f"Provinsi {name} telah ditambahkan")
            return redirect("caleg:WilayahProvinsi")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = WilayahProvinsiForm()
    context = {
        "provinsi_list": provinsi_list,
        "page_range": page_range,
        "title_page": title_page,
        "form": form,
    }

    return render(request, "caleg/wilayah_provinsi.html", context)


@login_required(login_url="Login")
def WilayahProvinsiDelete(request, pk=None):
    try:
        provinsi = get_object_or_404(Provinsi, pk=pk)
        provinsi.delete()
        messages.success(request, f"Provinsi  {provinsi.name} berhasil di hapus!")
        return redirect("caleg:WilayahProvinsi")
    except Provinsi.DoesNotExist:
        messages.error(request, f"Maaf provinsi tidak ada!")
        return redirect("caleg:WilayahProvinsi")
    except ProtectedError:
        messages.error(
            request,
            f"Maaf Provinsi {provinsi.name} tidak dapat dihapus, jika ingin menghapus pastikan tidak ada yang terhubung dengan provinsi ini!",
        )
        return redirect("caleg:WilayahProvinsi")


def WilayahKabKota(request):
    title_page = "Kabupaten Kota Indonesia"
    paginator = Paginator(
        KabKota.objects.annotate(
            jumlah_kecamatan=Count("kecamatan", distinct=True),
            jumlah_keldesa=Count("kecamatan__keldesa", distinct=True),
            jumlah_tps=Count("kecamatan__keldesa__tps", distinct=True),
        ),
        100,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        kabkota_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        kabkota_list = paginator.page(1)
    index = kabkota_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    if request.method == "POST":
        form = WilayahKabKotaForm(request.POST)
        if form.is_valid():
            provinsi = form.cleaned_data["provinsi"]
            name = form.cleaned_data["name"]
            add = KabKota(name=name, provinsi=provinsi)
            add.save()
            messages.success(request, f"Kabupaten {name} telah ditambahkan")
            return redirect("caleg:WilayahKabKota")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = WilayahKabKotaForm()
    context = {
        "kabkota_list": kabkota_list,
        "page_range": page_range,
        "title_page": title_page,
        "form": form,
    }

    return render(request, "caleg/wilayah_kabkota.html", context)


@login_required(login_url="Login")
def WilayahKabKotaDelete(request, pk=None):
    try:
        kabkota = get_object_or_404(KabKota, pk=pk)
        kabkota.delete()
        messages.success(request, f"Provinsi  {kabkota.name} berhasil di hapus!")
        return redirect("caleg:WilayahKabKota")
    except Provinsi.DoesNotExist:
        messages.error(request, f"Maaf kabupaten tidak ada!")
        return redirect("caleg:WilayahKabKota")
    except ProtectedError:
        messages.error(
            request,
            f"Maaf Kabupaten {kabkota.name} tidak dapat dihapus, jika ingin menghapus pastikan tidak ada yang terhubung dengan kabupaten ini!",
        )
        return redirect("caleg:WilayahKabKota")


@login_required(login_url="Login")
def WilayahKecamatan(request):
    title_page = "Kecamatan Indonesia"
    paginator = Paginator(
        Kecamatan.objects.annotate(
            jumlah_keldesa=Count("keldesa", distinct=True),
            jumlah_tps=Count("keldesa__tps", distinct=True),
        ),
        100,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        kecamatan_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        kecamatan_list = paginator.page(1)
    index = kecamatan_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    if request.method == "POST":
        form = WilayahKecamatanForm(request.POST)
        if form.is_valid():
            provinsi = form.cleaned_data["provinsi"]
            kabkota = form.cleaned_data["kabkota"]
            name = form.cleaned_data["name"]
            add = Kecamatan(name=name, provinsi=provinsi, kabkota=kabkota)
            add.save()
            messages.success(request, f"Kecamatan {name} telah ditambahkan")
            return redirect("caleg:WilayahKecamatan")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = WilayahKecamatanForm()
    context = {
        "kecamatan_list": kecamatan_list,
        "page_range": page_range,
        "title_page": title_page,
        "form": form,
    }

    return render(request, "caleg/wilayah_kecamatan.html", context)


@login_required(login_url="Login")
def WilayahKecamatanDelete(request, pk=None):
    try:
        kecamatan = get_object_or_404(Kecamatan, pk=pk)
        kecamatan.delete()
        messages.success(request, f"Kecamatan  {kecamatan.name} berhasil di hapus!")
        return redirect("caleg:WilayahKecamatan")
    except Kecamatan.DoesNotExist:
        messages.error(request, f"Maaf kecamatan tidak ada!")
        return redirect("caleg:WilayahKecamatan")
    except ProtectedError:
        messages.error(
            request,
            f"Maaf Kecamatan {kecamatan.name} tidak dapat dihapus, jika ingin menghapus pastikan tidak ada yang terhubung dengan kabupaten ini!",
        )
        return redirect("caleg:WilayahKecamatan")


@login_required(login_url="Login")
def WilayahKelDesa(request):
    title_page = "Desa Indonesia"
    paginator = Paginator(
        KelDesa.objects.annotate(
            jumlah_tps=Count("tps", distinct=True),
        ),
        100,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        keldesa_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        keldesa_list = paginator.page(1)
    index = keldesa_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    if request.method == "POST":
        form = WilayahKelDesaForm(request.POST)
        if form.is_valid():
            provinsi = form.cleaned_data["provinsi"]
            kabkota = form.cleaned_data["kabkota"]
            kecamatan = form.cleaned_data["kecamatan"]
            name = form.cleaned_data["name"]
            add = KelDesa(
                name=name, provinsi=provinsi, kabkota=kabkota, kecamatan=kecamatan
            )
            add.save()
            messages.success(request, f"Kelurahan/Desa {name} telah ditambahkan")
            return redirect("caleg:WilayahKelDesa")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = WilayahKelDesaForm()
    context = {
        "keldesa_list": keldesa_list,
        "page_range": page_range,
        "title_page": title_page,
        "form": form,
    }

    return render(request, "caleg/wilayah_keldesa.html", context)


@login_required(login_url="Login")
def WilayahKelDesaDelete(request, pk=None):
    try:
        keldesa = get_object_or_404(KelDesa, pk=pk)
        keldesa.delete()
        messages.success(request, f"Kelurahan Desa  {keldesa.name} berhasil di hapus!")
        return redirect("caleg:WilayahKelDesa")
    except KelDesa.DoesNotExist:
        messages.error(request, f"Maaf Kelurahan Desa tidak ada!")
        return redirect("caleg:WilayahKelDesa")
    except ProtectedError:
        messages.error(
            request,
            f"Maaf Kelurahan Desa {keldesa.name} tidak dapat dihapus, jika ingin menghapus pastikan tidak ada yang terhubung dengan kabupaten ini!",
        )
        return redirect("caleg:WilayahKelDesa")


@login_required(login_url="Login")
def WilayahTps(request):
    title_page = "TPS Indonesia"
    paginator = Paginator(
        Tps.objects.all(),
        100,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        tps_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        tps_list = paginator.page(1)
    index = tps_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        "tps_list": tps_list,
        "page_range": page_range,
        "title_page": title_page,
    }

    return render(request, "caleg/wilayah_tps.html", context)


def AkunMe(request):
    title_page = "Akun Saya"

    context = {
        "title_page": title_page,
    }
    return render(request, "caleg/akun_me.html", context)


def PerolehanSuaraTpsList(request):
    template_name = "caleg/perolehan_suara2.html"
    return render(request, template_name)


# def PerolehanSuaraTpsView(request):
#     perolehan = [
#         {
#             "id": peroleh.id,
#             "tps": peroleh.tps,
#         }
#         for peroleh in PerolehanTps.objects.all()
#     ]
#     return JsonResponse(status=200, data=perolehan, safe=False)


def PerolehanSuaraList(request):
    title_page = "Perolehan Suara"
    wilayah_dapil_list = Kecamatan.objects.all()
    paginator = Paginator(SuaraTps.objects.all(), 20)
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        tps_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        tps_list = paginator.page(1)
    index = tps_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]

    if request.method == "POST":
        form = CekTPSForm(request.POST)
        if form.is_valid():
            tps = form.cleaned_data["tps"]

            add = SuaraTps(tps=tps)
            add.user = request.user
            if SuaraTps.objects.filter(tps=tps).exists():
                messages.success(request, f"Perolehan Suara {tps.no} sudah ada")
                return redirect("caleg:PerolehanSuara")
            add.save()
            messages.success(request, f"Perolehan Suara {tps.no} telah ditambahkan")
            return redirect("caleg:PerolehanSuaraList")
        else:
            print("invalid form")
            print(form.errors)
    else:
        form = CekTPSForm()

    context = {
        "title_page": title_page,
        "form": form,
        "tps_list": tps_list,
        "wilayah_dapil_list": wilayah_dapil_list,
        "page_range": page_range,
    }
    return render(request, "caleg/perolehan_suara.html", context)


# def PerolehanSuaraEdit(request, pk=None):
#     title_page = "Perbaharui Data TPS"
#     perolehan = get_object_or_404(PerolehanTps, pk=pk)

#     pemilih_dpt_lk = perolehan.pemilih_dpt_lk
#     pemilih_dpt_pm = perolehan.pemilih_dpt_pm
#     pengguna_dpt_lk = perolehan.pengguna_dpt_lk
#     pengguna_dpt_pm = perolehan.pengguna_dpt_pm
#     pengguna_dptb_lk = perolehan.pengguna_dptb_lk
#     pengguna_dptb_pm = perolehan.pengguna_dptb_pm
#     pengguna_dpk_lk = perolehan.pengguna_dpk_lk
#     pengguna_dpk_pm = perolehan.pengguna_dpk_pm
#     disabilitas_laki_laki = perolehan.disabilitas_laki_laki
#     disabilitas_wanita = perolehan.disabilitas_wanita

#     if pemilih_dpt_lk is None:
#         pemilih_dpt_lk = 0
#     if pemilih_dpt_pm is None:
#         pemilih_dpt_pm = 0
#     if pengguna_dpt_lk is None:
#         pengguna_dpt_lk = 0
#     if pengguna_dpt_pm is None:
#         pengguna_dpt_pm = 0
#     if pengguna_dptb_lk is None:
#         pengguna_dptb_lk = 0
#     if pengguna_dptb_pm is None:
#         pengguna_dptb_pm = 0
#     if pengguna_dpk_lk is None:
#         pengguna_dpk_lk = 0
#     if pengguna_dpk_pm is None:
#         pengguna_dpk_pm = 0
#     if pengguna_dpk_pm is None:
#         pengguna_dpk_pm = 0
#     if disabilitas_laki_laki is None:
#         disabilitas_laki_laki = 0
#     if disabilitas_wanita is None:
#         disabilitas_wanita = 0

#     jml_pemilih = pemilih_dpt_lk + pemilih_dpt_pm
#     jml_pengguna_dpt = pengguna_dpt_lk + pengguna_dpt_pm
#     jml_pengguna_dptb = pengguna_dptb_lk + pengguna_dptb_pm
#     jml_pengguna_dpk = pengguna_dpk_lk + pengguna_dpk_pm
#     jml_pengguna_lk = pengguna_dpt_lk + pengguna_dptb_lk + pengguna_dpk_lk
#     jml_pengguna_pm = pengguna_dpt_pm + pengguna_dptb_pm + pengguna_dpk_pm
#     jml_pengguna = jml_pengguna_lk + jml_pengguna_pm
#     jml_disabilitas = disabilitas_laki_laki + disabilitas_wanita

#     if request.method == "POST":
#         perolehan_form = PerolehanSuaraForm(request.POST, instance=perolehan)
#         if perolehan_form.is_valid():
#             perolehan_form.save()

#             messages.success(request, f"Perolehan Suara  telah ditambahkan")
#             return redirect("caleg:PerolehanSuara")
#         else:
#             print("invalid form")
#             print(perolehan_form.errors)
#             messages.success(request, "Ada kesalahan input, ulangi")
#         return redirect("caleg:PerolehanSuara")
#     else:
#         perolehan_form = PerolehanSuaraForm(instance=perolehan)
#     paginator = Paginator(
#         Parpol.objects.all()
#         .prefetch_related(
#             Prefetch(
#                 "dprdkabkota",
#                 queryset=DprdKabKota.objects.all(),
#             )
#         )
#         .order_by("no_urut")
#         .annotate(num_caleg=Count("dprdkabkota__parpol") + 1),
#         100,
#     )
#     try:
#         page_number = int(request.GET.get("page", "1"))
#     except:
#         page_number = 1
#     try:
#         parpol_list = paginator.page(page_number)
#     except (EmptyPage, InvalidPage):
#         parpol_list = paginator.page(1)
#     index = parpol_list.number - 1
#     max_index = len(paginator.page_range)
#     start_index = index - 3 if index >= 3 else 0
#     end_index = index + 3 if index <= max_index - 3 else max_index
#     page_range = list(paginator.page_range)[start_index:end_index]
#     context = {
#
#         "title_page": title_page,
#         "perolehan": perolehan,
#         "jml_pemilih": jml_pemilih,
#         "jml_pengguna_dpt": jml_pengguna_dpt,
#         "jml_pengguna_dptb": jml_pengguna_dptb,
#         "jml_pengguna_dpk": jml_pengguna_dpk,
#         "jml_pengguna_lk": jml_pengguna_lk,
#         "jml_pengguna_pm": jml_pengguna_pm,
#         "jml_pengguna": jml_pengguna,
#         "jml_disabilitas": jml_disabilitas,
#         "perolehan_form": perolehan_form,
#         "parpol_list": parpol_list,
#     }
#     return render(request, "caleg/perolehan_suara_edit.html", context)


def PerolehanSuaraCaleg(request):
    return render(request, "caleg/perolehan_suara_caleg.html")


def SuaraCaleg(request):
    title_page = "Perolehan Suara"

    paginator = Paginator(
        Parpol.objects.all()
        .prefetch_related(
            Prefetch(
                "dprdkabkota",
                queryset=DprdKabKota.objects.all(),
            )
        )
        .order_by("no_urut"),
        4,
    )
    try:
        page_number = int(request.GET.get("page", "1"))
    except:
        page_number = 1
    try:
        parpol_list = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        parpol_list = paginator.page(1)
    index = parpol_list.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        "title_page": title_page,
        "parpol_list": parpol_list,
    }
    return render(request, "caleg/suara_caleg.html", context)


# def PerolehanSuaraView(request):
#     step1_form = PerolehanSuaraStep1Form()

#     context = {
#         "step1_form": step1_form,
#     }
#     return render(request, "caleg/perolehan_suara_test.html", context)
