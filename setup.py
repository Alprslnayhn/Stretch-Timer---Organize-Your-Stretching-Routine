import os
import subprocess
import urllib.request

# Paketlerin yüklü olup olmadığını kontrol et ve yükle
def install_packages():
    # Gerekli pip paketlerini kontrol et ve yükle
    try:
        import pygame  # pygame modülü yüklü mü kontrol et
    except ImportError:
        print("pygame modülü yüklü değil, yükleniyor...")
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "pygame"])

# Ses dosyasını indir
def download_sound():
    sound_url = "https://www.soundjay.com/buttons/beep-02.mp3"  # İndirilecek ses dosyasının URL'si
    sound_file = "beep.wav"

    # Dosya mevcutsa indirme işlemi yapma
    if not os.path.exists(sound_file):
        print(f"İndiriliyor: {sound_file}...")
        urllib.request.urlretrieve(sound_url, sound_file)
        print(f"Ses dosyası başarıyla indirildi: {sound_file}")
    else:
        print("Ses dosyası zaten mevcut.")

# Ana fonksiyon
def setup():
    install_packages()  # Paketleri yükle
    download_sound()  # Ses dosyasını indir

if __name__ == "__main__":
    setup()
