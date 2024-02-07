from django import forms
from accounts.models import User, UserSaksiTps
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

# from perolehansuara.models import (
#     PerolehanTps,
# )
from wilayah.admin import KabKota

from wilayah.models import Kecamatan, KelDesa, Provinsi, Tps


class CekTPSForm(forms.ModelForm):
    keldesa = forms.ModelChoiceField(
        required=True,
        queryset=KelDesa.objects.all(),
        empty_label="Pilih Kelurahan/Desa",
        widget=forms.Select(
            attrs={
                "id": "id_keldesa",
                "class": "form-control ",
            }
        ),
    )
    tps = forms.ModelChoiceField(
        required=True,
        queryset=Tps.objects.none(),
        empty_label="Pilih Nomor TPS",
        widget=forms.Select(
            attrs={
                "id": "id_tps",
                "class": "form-control ",
            }
        ),
    )

    class Meta:
        model = UserSaksiTps
        fields = ["keldesa", "tps"]

    def __init__(self, *args, **kwargs):
        super(CekTPSForm, self).__init__(*args, **kwargs)

        # Handling the 'tps' field queryset
        if "keldesa" in self.data:
            try:
                keldesa_id = int(self.data.get("keldesa"))
                self.fields["tps"].queryset = Tps.objects.filter(keldesa_id=keldesa_id)
            except (ValueError, TypeError):
                pass
        # If the form is bound to an instance (for editing an existing record)
        elif self.instance.pk:
            self.fields["tps"].queryset = self.instance.keldesa.tps_set.all()


# class PerolehanSuaraForm(forms.ModelForm):
#     pemilih_dpt_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pemilih_dpt_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pemilih_dpt_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pemilih_dpt_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dpt_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpt_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dpt_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpt_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dptb_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dptb_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dptb_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dptb_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dpk_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpk_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dpk_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpk_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     jml_terima = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_terima",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_digunakan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_digunakan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_dikembalikan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_dikembalikan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_tidakdigunakan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_tidakdigunakan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     disabilitas_laki_laki = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "disabilitas_laki_laki",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     disabilitas_wanita = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "disabilitas_wanita",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     class Meta:
#         model = PerolehanTps
#         fields = [
#             "pemilih_dpt_lk",
#             "pemilih_dpt_pm",
#             "pengguna_dpt_lk",
#             "pengguna_dpt_pm",
#             "pengguna_dptb_lk",
#             "pengguna_dptb_pm",
#             "pengguna_dpk_lk",
#             "pengguna_dpk_pm",
#             "jml_terima",
#             "jml_digunakan",
#             "jml_dikembalikan",
#             "jml_tidakdigunakan",
#             "disabilitas_laki_laki",
#             "disabilitas_wanita",
#         ]


# class PerolehanSuaraStep1Form(forms.ModelForm):
#     pemilih_dpt_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pemilih_dpt_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pemilih_dpt_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pemilih_dpt_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dpt_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpt_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dpt_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpt_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dptb_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dptb_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dptb_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dptb_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     pengguna_dpk_lk = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpk_lk",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     pengguna_dpk_pm = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "pengguna_dpk_pm",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     jml_terima = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_terima",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_digunakan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_digunakan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_dikembalikan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_dikembalikan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     jml_tidakdigunakan = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "jml_tidakdigunakan",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     disabilitas_laki_laki = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "disabilitas_laki_laki",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )
#     disabilitas_wanita = forms.CharField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "input-perolehan form-input w-full !bg-transparent font-bold text-success dark:!bg-transparent",
#                 "placeholder": "isi disini",
#                 "type": "number",
#                 "id": "disabilitas_wanita",
#                 "oninput": "updateResult()",
#             },
#         ),
#     )

#     class Meta:
#         model = PerolehanTps
#         fields = [
#             "pemilih_dpt_lk",
#             "pemilih_dpt_pm",
#             "pengguna_dpt_lk",
#             "pengguna_dpt_pm",
#             "pengguna_dptb_lk",
#             "pengguna_dptb_pm",
#             "pengguna_dpk_lk",
#             "pengguna_dpk_pm",
#             "jml_terima",
#             "jml_digunakan",
#             "jml_dikembalikan",
#             "jml_tidakdigunakan",
#             "disabilitas_laki_laki",
#             "disabilitas_wanita",
#         ]
