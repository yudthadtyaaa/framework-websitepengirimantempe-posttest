from django.db import models
from django.contrib.auth.models import User

class Tempe(models.Model):
    nama_tempe = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_tempe

class PesananTempe(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    tempe = models.ForeignKey(Tempe, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal_pesanan = models.DateTimeField(auto_now_add=True)
    alamat_pengiriman = models.CharField(max_length=255)

    def __str__(self):
        return f"Pesanan oleh {self.pengguna.username} untuk {self.jumlah} {self.tempe.nama_tempe}"

class Pengiriman(models.Model):
    pesanan = models.OneToOneField(PesananTempe, on_delete=models.CASCADE)
    status_pengiriman = models.CharField(max_length=50)
    tanggal_pengiriman = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pengiriman pesanan {self.pesanan.id} - Status: {self.status_pengiriman}"
