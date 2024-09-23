from django.shortcuts import render, redirect
from .forms import TempeForm, PesananTempeForm, PengirimanForm, PengirimanProdukForm

# Fungsi untuk halaman utama (index)
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
# View untuk input data Tempe
def input_tempe(request):
    if request.method == 'POST':
        form = TempeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_tempe')  # redirect ke halaman setelah submit
    else:
        form = TempeForm()
    return render(request, 'input_tempe.html', {'form': form})

# View untuk input data PesananTempe
def input_pesanan_tempe(request):
    if request.method == 'POST':
        form = PesananTempeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_pesanan_tempe')
    else:
        form = PesananTempeForm()
    return render(request, 'input_pesanan_tempe.html', {'form': form})

# View untuk input data Pengiriman
def input_pengiriman(request):
    if request.method == 'POST':
        form = PengirimanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_pengiriman')
    else:
        form = PengirimanForm()
    return render(request, 'input_pengiriman.html', {'form': form})

# View untuk input data Pengiriman Produk
def input_pengiriman_produk(request):
    if request.method == 'POST':
        form = PengirimanProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_pengiriman_produk')
    else:
        form = PengirimanProdukForm()
    return render(request, 'input_pengiriman_produk.html', {'form': form})
