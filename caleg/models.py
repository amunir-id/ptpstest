from django.db import models

from accounts.models import User

# Create your models here.
# class Caleg(models.Model):
#     DPR = 1
#     DPRD_PROVINSI = 2
#     DPRD_KABKOTA = 3

#     JENISPEMILIHAN_CHOICES = [
#         (DPR, 'DPR'),
#         (DPRD_PROVINSI, 'DPRD Provinsi'),
#         (DPRD_KABKOTA, 'DPRD Kabupaten Kota'),
#     ]
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'role': 1})

#     jenis_pemilihan = models.IntegerField(choices=JENISPEMILIHAN_CHOICES, default=DPRD_KABKOTA)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)