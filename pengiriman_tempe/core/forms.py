from django import forms
from .models import Tempe, PesananTempe, Pengiriman, PengirimanProduk

class TempeForm(forms.ModelForm):
    class Meta:
        model = Tempe
        fields = ['nama_tempe', 'harga', 'deskripsi']

class PesananTempeForm(forms.ModelForm):
    class Meta:
        model = PesananTempe
        fields = ['pengguna', 'tempe', 'jumlah', 'alamat_pengiriman']

class PengirimanForm(forms.ModelForm):
    class Meta:
        model = Pengiriman
        fields = ['pesanan', 'status_pengiriman', 'tanggal_pengiriman']

class PengirimanProdukForm(forms.ModelForm):
    class Meta:
        model = PengirimanProduk
        fields = ['produk', 'alamat_pengiriman', 'tanggal_pengiriman', 'jumlah']
