from django.db import models
from django.contrib.auth.models import User

# Model Tempe
class Tempe(models.Model):
    nama_tempe = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_tempe

# Model PesananTempe
class PesananTempe(models.Model):
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    tempe = models.ForeignKey(Tempe, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal_pesanan = models.DateTimeField(auto_now_add=True)
    alamat_pengiriman = models.CharField(max_length=255)

    def __str__(self):
        return f"Pesanan oleh {self.pengguna.username} untuk {self.jumlah} {self.tempe.nama_tempe}"

# Model Pengiriman
class Pengiriman(models.Model):
    pesanan = models.OneToOneField(PesananTempe, on_delete=models.CASCADE)
    status_pengiriman = models.CharField(max_length=50)
    tanggal_pengiriman = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pengiriman pesanan {self.pesanan.id} - Status: {self.status_pengiriman}"

# Model Produk (Posttest 2)
class Produk(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_produk

# Model Pengiriman untuk Produk (Posttest 2)
class PengirimanProduk(models.Model):
    alamat_pengiriman = models.CharField(max_length=255)
    tanggal_pengiriman = models.DateField()
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    def __str__(self):
        return f'{self.produk} - {self.alamat_pengiriman}'
