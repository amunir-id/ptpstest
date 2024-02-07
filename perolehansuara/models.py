from django.db import models
from accounts.models import User, UserPengawasTps
from peserta_pemilu.models import DprdKabKota
from wilayah.models import Kecamatan, Tps
from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


class SuaraPeserta(models.Model):
    tps = models.ForeignKey(Tps, on_delete=models.SET_NULL, null=True)
    nama_caleg = models.ForeignKey(DprdKabKota, on_delete=models.SET_NULL, null=True)
    suara = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tps

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["tps"], name="unique_tps_constraint")
        ]


class SuaraTps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tps = models.ForeignKey(Tps, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    pemilih_dpt_lk = models.IntegerField(blank=True, null=True, default=0)
    pemilih_dpt_pm = models.IntegerField(blank=True, null=True, default=0)

    pengguna_dpt_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpt_pm = models.IntegerField(blank=True, null=True, default=0)

    pengguna_dptb_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dptb_pm = models.IntegerField(blank=True, null=True, default=0)

    pengguna_dpk_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpk_pm = models.IntegerField(blank=True, null=True, default=0)

    jml_terima = models.IntegerField(blank=True, null=True, default=0)
    jml_digunakan = models.IntegerField(blank=True, null=True, default=0)
    jml_dikembalikan = models.IntegerField(blank=True, null=True, default=0)
    jml_tidakdigunakan = models.IntegerField(blank=True, null=True, default=0)

    disabilitas_laki_laki = models.IntegerField(blank=True, null=True, default=0)
    disabilitas_wanita = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.tps.no}"


class HasilPpwp(models.Model):
    ptps = models.OneToOneField(UserPengawasTps, on_delete=models.CASCADE)
    paslon1 = models.IntegerField()
    paslon2 = models.IntegerField()
    paslon3 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"


class DataPemilihPenggunaHakPilihPpwp(models.Model):
    ptps = models.OneToOneField(UserPengawasTps, on_delete=models.CASCADE)
    datapemilih_lk = models.IntegerField(blank=True, null=True, default=0)
    datapemilih_pm = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpt_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpt_pm = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dptb_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dptb_pm = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpk_lk = models.IntegerField(blank=True, null=True, default=0)
    pengguna_dpk_pm = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tps.no}"


class DataPenggunaSuratSuaraPpwp(models.Model):
    ptps = models.OneToOneField(UserPengawasTps, on_delete=models.CASCADE)
    jumlah_terima = models.IntegerField(blank=True, null=True, default=0)
    jumlah_digunakan = models.IntegerField(blank=True, null=True, default=0)
    jumlah_dikembalikan = models.IntegerField(blank=True, null=True, default=0)
    jumlah_tidakdipakai = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tps.no}"


class DataDisabilitasPpwp(models.Model):
    ptps = models.OneToOneField(UserPengawasTps, on_delete=models.CASCADE)
    jml_lk = models.IntegerField(blank=True, null=True, default=0)
    jml_pm = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tps.no}"


class DataSuaraSahdanTidakSahPpwp(models.Model):
    ptps = models.OneToOneField(UserPengawasTps, on_delete=models.CASCADE)
    sah = models.IntegerField(blank=True, null=True, default=0)
    tidak = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tps.no}"


class PpwpMedia(models.Model):
    ptps = models.ForeignKey(
        UserPengawasTps, related_name="ppwp", default=None, on_delete=models.CASCADE
    )
    images = models.FileField(upload_to="ppwp/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.images)

        # Convert image to RGB mode if it's RGBA
        if im.mode == "RGBA":
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((945, 2048))

        # Save the modified image to the output
        im.save(output, format="JPEG", quality=300)
        output.seek(0)

        # Change the image field value to be the newly modified image value
        self.images = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.images.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

        super().save(*args, **kwargs)


class DprRiMedia(models.Model):
    ptps = models.ForeignKey(
        UserPengawasTps, related_name="dprri", default=None, on_delete=models.CASCADE
    )
    images = models.FileField(upload_to="dpr/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.images)

        # Convert image to RGB mode if it's RGBA
        if im.mode == "RGBA":
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((945, 2048))

        # Save the modified image to the output
        im.save(output, format="JPEG", quality=300)
        output.seek(0)

        # Change the image field value to be the newly modified image value
        self.images = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.images.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

        super().save(*args, **kwargs)


class DpdRiMedia(models.Model):
    ptps = models.ForeignKey(
        UserPengawasTps, related_name="dpdri", default=None, on_delete=models.CASCADE
    )
    images = models.FileField(upload_to="dpd/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.images)

        # Convert image to RGB mode if it's RGBA
        if im.mode == "RGBA":
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((945, 2048))

        # Save the modified image to the output
        im.save(output, format="JPEG", quality=300)
        output.seek(0)

        # Change the image field value to be the newly modified image value
        self.images = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.images.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

        super().save(*args, **kwargs)


class DprdProvMedia(models.Model):
    ptps = models.ForeignKey(
        UserPengawasTps, related_name="dprdprov", default=None, on_delete=models.CASCADE
    )
    images = models.FileField(upload_to="dprdprov/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.images)

        # Convert image to RGB mode if it's RGBA
        if im.mode == "RGBA":
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((1080, 1920))

        # Save the modified image to the output
        im.save(output, format="JPEG", quality=300)
        output.seek(0)

        # Change the image field value to be the newly modified image value
        self.images = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.images.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

        super().save(*args, **kwargs)


class DprdKabKotaMedia(models.Model):
    ptps = models.ForeignKey(
        UserPengawasTps,
        related_name="dprdkabkota",
        default=None,
        on_delete=models.CASCADE,
    )
    images = models.FileField(upload_to="dprdkab/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ptps.tps}"

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.images)

        # Convert image to RGB mode if it's RGBA
        if im.mode == "RGBA":
            im = im.convert("RGB")

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((945, 2048))

        # Save the modified image to the output
        im.save(output, format="JPEG", quality=300)
        output.seek(0)

        # Change the image field value to be the newly modified image value
        self.images = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % self.images.name.split(".")[0],
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

        super().save(*args, **kwargs)


class CekPpwp(models.Model):
    media = models.ForeignKey(PpwpMedia, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CekDprRi(models.Model):
    media = models.ForeignKey(DprRiMedia, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CekDpdRi(models.Model):
    media = models.ForeignKey(DpdRiMedia, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CekDprdProv(models.Model):
    media = models.ForeignKey(DprdProvMedia, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CekDprdKabKota(models.Model):
    media = models.ForeignKey(DprdKabKotaMedia, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
